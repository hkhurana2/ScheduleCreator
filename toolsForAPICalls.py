import requests
import creds
import json
token = creds.token

url_base = 'https://www.thebluealliance.com/api/v3'

headers  = {
    'accept': 'application/json',
           'If-Modified-Since': '',
    'X-TBA-Auth-Key' : str(token)
}


def APICall(urlAPIExtention):
    url = url_base+ urlAPIExtention
    print("USING: " +  url)
    return requests.get(url,headers= headers)


def APICalltoJSON(APIReturn):
    return APIReturn.json()
