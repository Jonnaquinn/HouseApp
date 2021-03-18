import time
from flask import Flask, jsonify, request, session, render_template, send_file, redirect, url_for
from flask_cors import CORS
import requests
import json
import re
import ast
import folium
import branca 
import pandas as pd

app =  Flask(__name__)
CORS(app, supports_credentials=True)
app.secret_key = 'dljsaklqk24e21cjn!Ew@@dsa5'
#Define Foursquare Credentials and Version

CLIENT_ID = 'XX2RK0KHBAX412Q053MRATKP3QPOXPJXNC2OXXQFFXKPCOTM' # Foursquare ID
CLIENT_SECRET = 'GW1HUCQ4GYM5PMXUQPZBZTBYDUP5AGIVLRDO04VENXKOXYF4' # Foursquare Secret
VERSION = '20181206' # Foursquare API version

print('Your credentails:')
print('CLIENT_ID: ' + CLIENT_ID)
print('CLIENT_SECRET:' + CLIENT_SECRET)

    # print(details[0]['listing']['propertyDetails']['postcode'])
    # print(details[0]['listing']['priceDetails']['displayPrice'])
    # print(details[0]['listing']['propertyDetails']['latitude'])
    # print(details[0]['listing']['propertyDetails']['latitude'])
    
def getNearbyVenues(json_all_pages, radius=1000, LIMIT=100):
    names = []
    lat1 = []
    lng1 = []
    # names = [json_all_pages[0]['listing']['propertyDetails']['displayableAddress']]
    # lat1 = [json_all_pages[0]['listing']['propertyDetails']['latitude']]
    # lng1 = [json_all_pages[0]['listing']['propertyDetails']['latitude']]
    try:
        for i in range(1000):
            names.append(json_all_pages[i]['listing']['propertyDetails']['displayableAddress'])
            lat1.append(json_all_pages[i]['listing']['propertyDetails']['latitude'])
            lng1.append(json_all_pages[i]['listing']['propertyDetails']['latitude'])
    except:
        pass
    # print(names, lat1, lng1)
    # print(name, lat, lng)
    #radius 1000 LIMIT 100   
    venues_list=[]
    for name, lat, lng in zip(names, lat1, lng1):
        # print(name, lat, lng)
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
        # results = requests.get(url).json()["response"]['groups'][0]['items']
        results = requests.get(url).json()["response"]["venues"]
        venues_list.append([(
                name, 
                lat, 
                lng, 
                v['name'], 
                v['location']['lat'], 
                v['location']['lng']) for v in results])

        nearby_venues = pd.DataFrame([item for venue_list in venues_list for item in venue_list])
        return(nearby_venues)
        
    #     # return only relevant information for each nearby venue
    #     venues_list.append([(
    #         name, 
    #         lat, 
    #         lng,
    #         aurl,
    #         v['venue']['name'], 
    #         v['venue']['location']['lat'], 
    #         v['venue']['location']['lng'],  
    #         v['venue']['categories'][0]['name']) for v in results])
    # nearby_venues = pd.DataFrame([item for venue_list in venues_list for item in venue_list])
    # nearby_venues.columns = ['Address', 
    #               'Address Latitude', 
    #               'Address Longitude',
    #               'Address URL',
    #               'Venue', 
    #               'Venue Latitude', 
    #               'Venue Longitude', 
    #               'Venue Category']                                  
    # return(nearby_venues)

# client_id = 'client_a33fefb8c17ba7a3275a86f4a42d8c95'
# client_secret = 'secret_c9ca393f79c3fcac90de4e584d8e9dc0'
# scopes = ['api_properties_read']
# auth_url = 'https://auth.domain.com.au/v1/connect/token'
# url_endpoint = 'https://api.domain.com.au/v1/properties/'
# property_id = 'RF-8884-AK'

# @app.route('/')
# def get_property_info():
#     response = requests.post(auth_url, data = {
#                         'client_id':client_id,
#                         'client_secret':client_secret,
#                         'grant_type':'client_credentials',
#                         'scope':scopes,
#                         'Content-Type':'text/json'
#                         })
#     json_res = response.json()
#     access_token=json_res['access_token']
#     print(access_token)
#     auth = {'Authorization':'Bearer ' + access_token}
#     url = url_endpoint + property_id
#     res1 = requests.get(url, headers=auth)    
#     r = res1.json()
#     # print(r)
#     return r

# @app.before_request
# def before_request_func():
#     return session.pop("react_json", None)

@app.route('/', methods = ['POST'])
def result():
    print('-----------------FIRST--------------')
    if not request.json:
        return "unsuccessful"
    react_json = request.json
    # print(react_json)
    session["react_json"] = react_json
    print('----FROM REACT-----', session["react_json"])
    # print(react_json['level'])
    return "success"

@app.route('/domain_api')
def domain_api():
    # if session.get("react_json_new") is not None:
    #     session.pop("react_json_new", None)
    # if 'react_json_new' in locals():
    #     print('--------hello world----------')
    # react_json_new = []
    react_json_new = session.get("react_json", None)
    print('-----------------SECOND--------------')
    # react_json_new = session.get("react_json", None)
    print("---------FROM DOMAIN_API--------", react_json_new)
    # print(react_json_new['surround'])
    if react_json_new['surround'] == '' or react_json_new['surroundingsuburbs'] == 'False':
        react_json_new['surround'] = 1
        # print(react_json_new['surround'])
    response = requests.post('https://auth.domain.com.au/v1/connect/token',
                                # data = {'client_id':'client_a33fefb8c17ba7a3275a86f4a42d8c95',
                                #         "client_secret":'secret_c9ca393f79c3fcac90de4e584d8e9dc0',
                                #         "grant_type":"client_credentials",
                                #         "scope":"api_listings_read",
                                #         "Content-Type":"text/json"})
                                #  data = {'client_id':'client_aa2d07ab3594787d1048a019237d774d',
                                #         "client_secret":'secret_162a98b8fe40d235324bda115668022b',
                                #         "grant_type":"client_credentials",
                                #         "scope":"api_listings_read",
                                #         "Content-Type":"text/json"})
                                data = {'client_id':'client_e25959d1af3757d782dade5906a90862',
                                        "client_secret":'secret_c54620807a9b965de8b317300ea237e1',
                                        "grant_type":"client_credentials",
                                        "scope":"api_listings_read",
                                        "Content-Type":"text/json"})
    token=response.json()
    access_token=token["access_token"]
    # json_all_pages = []
    # post_fields = {
    #     "pageNumber": 1,
    #     "listingType": react_json_new['level'],
    #     "locations": [
    #         {
    #             # "state": "VIC",
    #             # "suburb": "Richmond",     
    #             # "postCode": 3121,
    #             "state": react_json_new['state'],
    #             "suburb": react_json_new['suburb'],     
    #             "postCode": react_json_new['postcode'],
    #             "includeSurroundingSuburbs": react_json_new['surroundingsuburbs'],
    #             "surroundingRadiusInMeters": react_json_new['surround'],
    #         }
    #     ],
    #     "pageSize": 200,
    #     "minBedrooms": react_json_new['minBed'],
    #     "maxBedrooms": react_json_new['maxBed'],
    #     "minBathrooms": react_json_new['minBath'],
    #     "maxBathrooms": react_json_new['maxBath'],
    #     "minCarspaces": react_json_new['minParks'],
    #     "maxCarspaces": react_json_new['maxParks'],
    #     "minPrice": react_json_new['minPrice'],
    #     "maxPrice": react_json_new['maxPrice'],
    # }
    # url = "https://api.domain.com.au/v1/listings/residential/_search"
    # auth = {"Authorization":"Bearer "+access_token}
    # request = requests.post(url, headers=auth, json=post_fields)
    # details=request.json()
    # print('length of json', len(details))
    # json_all_pages = details + json_all_pages
    # if (len(json_all_pages) == 200):
    #     print('-------------doing for loop to get 5 pages---------------')
        # for loop till HERE
    try:
        json_all_pages = []
        for i in range(5):
            i = i + 1
            print(i)
            post_fields = {
                "pageNumber": i,
                "listingType": react_json_new['level'],
                "locations": [
                    {
                        # "state": "VIC",
                        # "suburb": "Richmond",     
                        # "postCode": 3121,
                        "state": react_json_new['state'],
                        "suburb": react_json_new['suburb'],     
                        "postCode": react_json_new['postcode'],
                        "includeSurroundingSuburbs": react_json_new['surroundingsuburbs'],
                        "surroundingRadiusInMeters": react_json_new['surround'],
                    }
                ],
                "pageSize": 200,
                "minBedrooms": react_json_new['minBed'],
                "maxBedrooms": react_json_new['maxBed'],
                "minBathrooms": react_json_new['minBath'],
                "maxBathrooms": react_json_new['maxBath'],
                "minCarspaces": react_json_new['minParks'],
                "maxCarspaces": react_json_new['maxParks'],
                "minPrice": react_json_new['minPrice'],
                "maxPrice": react_json_new['maxPrice'],
            }
            url = "https://api.domain.com.au/v1/listings/residential/_search"
            auth = {"Authorization":"Bearer "+access_token}
            request = requests.post(url, headers=auth, json=post_fields)
            details=request.json()
            print('length of json', len(details))
            json_all_pages = details + json_all_pages
            # print('length of json', len(json_all_pages))
            # for loop till HERE
            if (len(details) < 200):
                print('reading page numbers')
                break
    except:
        pass

    print('length of END JSON', len(json_all_pages))
    # session["details"] = details
    # print(session["details"])
    # print('length of json', len(details))
    # react_json = session.get("react_json", None)
    # print(react_json['level'])
    # print(details[0]['listing']['propertyDetails']['postcode'])
    # print(details[0]['listing']['priceDetails']['displayPrice'])
    # print(details[0]['listing']['propertyDetails']['latitude'])
    # print(details[0]['listing']['propertyDetails']['longitude'])
    start_coords = (json_all_pages[0]['listing']['propertyDetails']['latitude'], json_all_pages[0]['listing']['propertyDetails']['longitude'])
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    # print(json_all_pages[0]['listing']['propertyDetails']['latitude'])
    # print(json_all_pages[7])
    for element in json_all_pages:
        # print(len(element['listing']))
        # print('------------------ghsfdsfsdfsd-----------------', element)
        try:
            url ='https://www.domain.com.au/' + element['listing']['listingSlug']
            url_link = folium.Html('<a href="'+ url +'"target="_blank">' + element['listing']['propertyDetails']['displayableAddress'] + '</a>' + '<br />' + element['listing']['priceDetails']['displayPrice'], script=True)
            iframe = branca.element.IFrame(html=url_link, width=260, height=60)
            # iframe = branca.element.IFrame(html=url_link, width=500, height=300)    
            # print(element['listing']['propertyDetails']['latitude'])
            # label = '{}, {}, {}'.format(element['listing']['propertyDetails']['displayableAddress'], element['listing']['priceDetails']['displayPrice'], url_link)
            # label = folium.Popup(label, parse_html=True)
            # html = folium.Html(label)
            folium.CircleMarker(
                [element['listing']['propertyDetails']['latitude'], element['listing']['propertyDetails']['longitude']],
                radius=5,
                popup=folium.Popup(iframe, parse_html=True),
                # tooltip=element['listing']['propertyDetails']['displayableAddress'],
                color='blue',
                fill=True,
                fill_color='#3186cc',
                fill_opacity=0.7,
                parse_html=False).add_to(folium_map)
        except:
            print('skipping listing due to bad data')
    # print('----------being passed through domain api--------------', details[0]['listing']['propertyDetails']['postcode'])
    # session.clear()
    # getNearbyVenues(json_all_pages)
    return folium_map._repr_html_()
    # return jsonify(details)
    # return jsonify(json_all_pages)
def hello(whatever):
    print(whatever)
# @app.route('/time')
# def get_current_time():
#     return {'time': time.time()}

    
@app.route('/map')
def show_map():
    # details = session.get("details", None)
    # print(details)
    start_coords = (46.9540700, 142.7360300)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    return folium_map._repr_html_()