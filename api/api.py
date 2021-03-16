import time
from flask import Flask, jsonify, request, session
from flask_cors import CORS
import requests
import json
import re
import ast

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

@app.route('/')
def domain_api():
    react_json = session.get("react_json", None)
    print(react_json['surround'])
    if react_json['surround'] == '' or react_json['surroundingsuburbs'] == 'False':
        react_json['surround'] = 1
        print(react_json['surround'])
    response = requests.post('https://auth.domain.com.au/v1/connect/token',
                                data = {'client_id':'client_a33fefb8c17ba7a3275a86f4a42d8c95',
                                        "client_secret":'secret_c9ca393f79c3fcac90de4e584d8e9dc0',
                                        "grant_type":"client_credentials",
                                        "scope":"api_listings_read",
                                        "Content-Type":"text/json"})
    token=response.json()
    access_token=token["access_token"]
    post_fields = {
    "listingType": react_json['level'],
    "locations": [
        {
            # "state": "VIC",
            # "suburb": "Richmond",     
            # "postCode": 3121,
            "state": react_json['state'],
            "suburb": react_json['suburb'],     
            "postCode": react_json['postcode'],
            "includeSurroundingSuburbs": react_json['surroundingsuburbs'],
            "surroundingRadiusInMeters": react_json['surround'],
        }
    ],
    "pageSize": 200,
    "minBedrooms": react_json['minBed'],
    "maxBedrooms": react_json['maxBed'],
    "minBathrooms": react_json['minBath'],
    "maxBathrooms": react_json['maxBath'],
    "minCarspaces": react_json['minParks'],
    "maxCarspaces": react_json['maxParks'],
    "minPrice": react_json['minPrice'],
    "maxPrice": react_json['maxPrice'],
    }
    url = "https://api.domain.com.au/v1/listings/residential/_search"
    auth = {"Authorization":"Bearer "+access_token}
    request = requests.post(url, headers=auth, json=post_fields)
    details=request.json()
    print(len(details))
    # react_json = session.get("react_json", None)
    # print(react_json['level'])
    # print(details[0]['listing']['propertyDetails']['postcode'])
    # print(details[0]['listing']['priceDetails']['displayPrice'])
    return jsonify(details)

# @app.route('/time')
# def get_current_time():
#     return {'time': time.time()}

@app.route('/result', methods = ['POST'])
def result():
    if not request.json:
        return "unsuccessful"
    react_json = request.json
    print(react_json)
    session["react_json"]=react_json
    # print(react_json['level'])
    return "success"