import time
from flask import Flask, jsonify, request, session, render_template, send_file, redirect, url_for
from flask_cors import CORS
import requests
import json
import re
import ast
import folium

app =  Flask(__name__)
app.secret_key = 'dljsaklqk24e21cjn!Ew@@dsa5'

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


# get_property_info()
@app.route('/result', methods = ['POST'])
def result():
    print('-----------------FIRST--------------')
    if not request.json:
        return "unsuccessful"
    react_json = request.json
    # print(react_json)
    session["react_json"]=react_json
    print('----FROM REACT-----', session["react_json"])
    # print(react_json['level'])
    return "success"

@app.route('/')
def domain_api():
    print('-----------------SECOND--------------')
    react_json_new = session.get("react_json", None)
    print("---------FROM DOMAIN_API--------", react_json_new)
    # print(react_json_new['surround'])
    if react_json_new['surround'] == '' or react_json_new['surroundingsuburbs'] == 'False':
        react_json_new['surround'] = 1
        # print(react_json_new['surround'])
    response = requests.post('https://auth.domain.com.au/v1/connect/token',
                                data = {'client_id':'client_a33fefb8c17ba7a3275a86f4a42d8c95',
                                        "client_secret":'secret_c9ca393f79c3fcac90de4e584d8e9dc0',
                                        "grant_type":"client_credentials",
                                        "scope":"api_listings_read",
                                        "Content-Type":"text/json"})
    token=response.json()
    access_token=token["access_token"]
    post_fields = {
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
    # session["details"] = details
    # print(session["details"])
    print('length of json', len(details))
    # react_json = session.get("react_json", None)
    # print(react_json['level'])
    # print(details[0]['listing']['propertyDetails']['postcode'])
    # print(details[0]['listing']['priceDetails']['displayPrice'])
    # print(details[0]['listing']['propertyDetails']['latitude'])
    # print(details[0]['listing']['propertyDetails']['longitude'])
    start_coords = (details[0]['listing']['propertyDetails']['latitude'], details[0]['listing']['propertyDetails']['longitude'])
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    for element in details:
        # print(element['listing']['propertyDetails']['latitude'])
        label = '{}'.format(element['listing']['propertyDetails']['displayableAddress'])
        label = folium.Popup(label, parse_html=True)
        # html = folium.Html(label)
        folium.CircleMarker(
            [element['listing']['propertyDetails']['latitude'], element['listing']['propertyDetails']['longitude']],
            radius=5,
            popup=label,
            color='blue',
            fill=True,
            fill_color='#3186cc',
            fill_opacity=0.7,
            parse_html=False).add_to(folium_map)
    # print('----------being passed through domain api--------------', details[0]['listing']['propertyDetails']['postcode'])
    # session.clear()
    return folium_map._repr_html_()
    # return jsonify(details)

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