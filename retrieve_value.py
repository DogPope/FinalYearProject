# This script contains a function to retrieve a value from a JSON Object.
import requests
import json

# Works
#def easy_practice_run(num):
#    url = 'http://localhost:5000/api/composers/' + str(num)
#    response = requests.get(url)
#    response_as_json = response.json()
#    json_str = json.dumps(response_as_json)
#    resp = json.loads(json_str)
#    print(resp['lastName'])

#easy_practice_run(1)

#def med_practice_run(num): # 5786b3f1149f34b06fac9b3e0900102e  - ID number for sampleElevation.json sent to couchDB.
#    url = 'http://admin:mtu12345@localhost:5984/project/' + str(num)
#    response = requests.get(url)
#    response_as_json = response.json()
#    json_str = json.dumps(response_as_json)
#    resp = json.loads(json_str)
#    print(resp['results'][0]['elevation']) # The answer should be 994.4034423828125

#med_practice_run('5786b3f1149f34b06fac9b3e0900102e')

# https://maps.googleapis.com/maps/api/elevation/json?locations=51.999445%2C-9.742693&key=apikey

def return_elevation(lat, long):
    url = "https://maps.googleapis.com/maps/api/elevation/json?locations=" + str(lat) + "%2C" + str(long) + "&key=apikey"
    response = requests.get(url)
    response_as_json = response.json()
    json_str = json.dumps(response_as_json)
    resp = json.loads(json_str)
    print(resp['results'][0]['elevation'])

return_elevation(51.999445, -9.742693)
# This should give back the elevation of the point with Longitude and Latitude inserted into the method definition.