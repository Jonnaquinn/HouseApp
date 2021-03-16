import time
from flask import Flask
import sys
import os
import json
from pandastable import Table, TableModel
#import all libraries ill be using
from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import itertools
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from geopy.extra.rate_limiter import RateLimiter
# Matplotlib and associated plotting modules
import matplotlib.cm as cm
import matplotlib.colors as colors
from IPython.display import HTML, display
# import k-means from clustering stage
from sklearn.cluster import KMeans
import folium # map rendering library
from io import StringIO
import json
import requests # library to handle requests

app =  Flask(__name__)
global df

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/api-scrape', methods=['GET'])
def apiScrape():
    response_json = scrape()
    return response_json
@app.route('/api-plot', methods=['GET'])
def apiPlot():
    response_json = scrape()
    response_plot = plot()
    return response_plot
@app.route('/api-venues', methods=['GET'])
def apiVenues():
    response_venues = getNearbyVenues()
    return response_venues

# @app.route('/scrape')
def scrape():
    global df
    headers = ({'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
    #Create a bunch of list's to handle the data
    prices = []
    addresses = []
    suburbs = []
    states = []
    postcodes = []
    bedss = []
    bathrooms = []
    parkings = []
    urls = []
    n_pages = 0 # set the page
    for page in range(1,50): #domain restricts queries to 50 pages
        n_pages += 1 # make the page iterate through the FOR loop
        #Define the base URL to be used when querying the website. Limited to *Eastern Suburbs && $350k-700k
        houses_url = 'https://www.domain.com.au/sale/eastern-suburbs-vic/?ptype=duplex,free-standing,new-home-designs,new-house-land,semi-detached,terrace,town-house,villa&price=250000-450000&sort=price-asc'+ '&page='+str(page)
        r = get(houses_url, headers=headers)
        #Use BeautifulSoup to pull data out of HTML tags within the website
        page_html = BeautifulSoup(r.text, 'html.parser')
        #Houses on the website sit within a HTML class "css-1gkcyyc"
        #We use beautifulsoup to parse through the class and grab all related info
        house_containers = page_html.find_all('div', class_="css-1gkcyyc")
        if house_containers != []:
            for container in house_containers:
                # x = container.find_all('span')
                # if x is not None and len(x) > 0:
                #Grab all neccessary info sitting within tags and apply data manipulation
                #Store these values
                #Price
                try: 
                    price = container.find_all('p')[0].text[0:9]
                    price = price.replace(',','')
                    price = price.replace('$','')
                    price = price.replace(' ','')
                    prices.append(price)
                except:
                    prices.append('N/A')
                #Address
                try: 
                    address = container.find_all('span')[0].text
                    address = address.replace(',\xa0','')
                    addresses.append(address)
                except: 
                    addresses.append('N/A')
                #Suburb
                try: 
                    suburb = container.find_all('span')[2].text
                    suburbs.append(suburb)
                except: 
                    suburbs.append('N/A')
                #State
                try:
                    state = container.find_all('span')[3].text
                    states.append(state)
                except:
                    states.append('N/A')
                #Postcode
                try: 
                    postcode = container.find_all('span')[4].text
                    postcodes.append(postcode)
                except: 
                    postcodes.append('N/A')
                #Beds
                try:
                    beds = container.find_all('span')[5].text
                    beds = beds.replace(' Beds', '')
                    beds = beds.replace(' Bed', '')
                    beds = beds.replace('âˆ’', '')
                    bedss.append(beds)
                except:
                    bedss.append('N/A')
                
                #Bathrooms
                try:
                    bathroom = container.find_all('span')[8].text
                    bathroom = bathroom.replace(' Bath', '')
                    bathroom = bathroom.replace('s', '')
                    bathroom = bathroom.replace('âˆ’', '')
                    bathrooms.append(bathroom)
                except:
                    bathrooms.append("N/A")
                
                #Parking Spots
                try:
                    parking = container.find_all('span')[11].text
                    parking = parking.replace(' Parking', '')
                    parking = parking.replace('âˆ’', '')
                    parkings.append(parking)
                except: 
                    parkings.append("N/A")
                #Url
                url = container.find_all('a')[0].get('href')
                urls.append(url)
                
        else:
            break
    #Print how many properties we scapred 
    print('You scraped {} pages containing {} properties.'.format(n_pages, len(addresses)))
    #Save all scraped variables into a single dataframe
    # global df
    df = pd.DataFrame({'Price':prices, 
                   'Address': addresses, 
                   'Suburb': suburbs, 
                   'State': states, 
                   'Postcode': postcodes, 
                   'Beds': bedss, 
                   'Bathrooms': bathrooms, 
                   'Parking_Spots': parkings, 'URL': urls})
    df = df.drop_duplicates(subset='Address', keep='first')
    df = df[df.Price.apply(lambda x: x.isnumeric())]
    df = df[df.State == 'VIC']
    df = df[df.Parking_Spots <= '5']
    df['Full_Address'] = df['Address'] +' '+ df['Suburb'] + ' ' + df['Postcode'] + ' ' + df['State']
    json_df = df.to_json(orient = 'records')
    # print(json)
    return json_df

# @app.route('/plot')
def plot():
    global df
    #Using geopy to locate the coordinates of these addresses
    geolocator = Nominatim(user_agent="my-app")
    #Add in a 1 second delay to handle error responses
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    #Apply geopy to the Full_Address column and make a new column City_Coordinates with the return values
    df['city_coord']  = df['Full_Address'].apply(geocode)
    #We remove any rows geopy couldnt discover
    df = df.dropna(how='any',axis=0) ## removes any rows geocode couldnt discover 
    #Make 2 new columns "Latitude" & "Longitude" and apply geopy to get these values from the "City_Coordinates" column
    df['Latitude'] = df['city_coord'].apply(lambda x: (x.latitude))
    df['Longitude'] = df['city_coord'].apply(lambda x: (x.longitude))
    #Use geopy to find the coordinates of melbourne
    melbourne = 'Melbourne, City of Melbourne'
    location = geolocator.geocode(melbourne)
    latitude = location.latitude
    longitude = location.longitude
    # print('The geograpical coordinate of Melbourne is {}, {}.'.format(latitude, longitude))
    # print('Interactive Folium map mymap.html made in local DIR')
    #print('Created interactive Folium map mymap.html in C:\Users\joquinn\Showcase')
    # create map of melbourne using latitude and longitude values
    map_melbourne = folium.Map(location=[latitude, longitude], zoom_start=11)
    print(df)
    # add markers to map
    for lat, lng, city_coord, house_url in zip(df['Latitude'], df['Longitude'], df['Full_Address'], df['URL']):
        label = '{}, {}'.format(city_coord, house_url)
        label = folium.Popup(label, parse_html=True)
        folium.CircleMarker(
            [lat, lng],
            radius=5,
            popup=label,
            color='blue',
            fill=True,
            fill_color='#3186cc',
            fill_opacity=0.7,
            parse_html=False).add_to(map_melbourne)  
    # map_melbourne.save("C:/Users/joquinn/Showcase/mymap.html")
    return map_melbourne._repr_html_()

#Apply FourSquare API to grab all venue's/locations within 1KM of each data point & limit it to the first 100 values.
@app.route('/venues')
def getNearbyVenues(radius=1000, LIMIT=100):
    CLIENT_ID = 'XX2RK0KHBAX412Q053MRATKP3QPOXPJXNC2OXXQFFXKPCOTM' # Foursquare ID
    CLIENT_SECRET = 'GW1HUCQ4GYM5PMXUQPZBZTBYDUP5AGIVLRDO04VENXKOXYF4' # Foursquare Secret
    VERSION = '20181206' # Foursquare API version
    #radius 1000 LIMIT 100   
    venues_list=[]
    for name, lat, lng, aurl in zip(df['Full_Address'], df['Latitude'], df['Longitude'], df['URL']):
        print(name)
            
        # create the API request URL
        url = 'https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}&limit={}'.format(           
            CLIENT_ID, 
            CLIENT_SECRET, 
            VERSION, 
            lat, 
            lng, 
            radius, 
            LIMIT)
            
       # make the GET request
        results = requests.get(url).json()["response"]['groups'][0]['items']
        
        # return only relevant information for each nearby venue
        venues_list.append([(
            name, 
            lat, 
            lng,
            aurl,
            v['venue']['name'], 
            v['venue']['location']['lat'], 
            v['venue']['location']['lng'],  
            v['venue']['categories'][0]['name']) for v in results])
    global nearby_venues
    nearby_venues = pd.DataFrame([item for venue_list in venues_list for item in venue_list])
    nearby_venues.columns = ['Address', 
                  'Address Latitude', 
                  'Address Longitude',
                  'Address URL',
                  'Venue', 
                  'Venue Latitude', 
                  'Venue Longitude', 
                  'Venue Category']
    # json_nearby_venues = nearby_venues.to_json(orient = 'records')
    # my_venues = nearby_venues[nearby_venues['Venue Category'].isin(criteria.get().split('-'))]
    my_venues = nearby_venues[nearby_venues['Venue Category'].isin(['Supermarket', 'Gym'])]
    #Group the addresses together
    my_venues.groupby(['Address', 'Address Latitude', 'Address Longitude'])['Venue Category'].apply(list).reset_index()
    #Groups Dataframe by Address and puts Venue Category's into a list
    my_venues_final = my_venues.groupby(['Address', 'Address Latitude', 'Address Longitude', 'Address URL'])['Venue Category'].apply(list).reset_index
    #Removes duplicates within the list
    my_venues_final = my_venues.groupby(['Address', 'Address Latitude', 'Address Longitude', 'Address URL'])['Venue Category'].apply(set).reset_index()
    #Only show grouped Addresses that contain all 4 Categorys
    my_venues_final = my_venues_final[my_venues_final['Venue Category'].map(set(['Supermarket', 'Gym']).issubset)]
    return ''