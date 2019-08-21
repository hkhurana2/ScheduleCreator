
import json
import requests
from operator import itemgetter
import creds


#Using /event/{event_key}/matches/simple GET call
#Get back a JSON Object
#  Example
# {
#     "actual_time": 1556371933,
#     "alliances": {
#       "blue": {
#         "dq_team_keys": [],
#         "score": 85,
#         "surrogate_team_keys": [],
#         "team_keys": [
#           "frc3015",
#           "frc1640",
#           "frc271"
#         ]
#       },
#       "red": {
#         "dq_team_keys": [],
#         "score": 95,
#         "surrogate_team_keys": [],
#         "team_keys": [
#           "frc2481",
#           "frc4976",
#           "frc5460"
#         ]
#       }
#     },
#     "comp_level": "qf",                                         IMPORTANT - can tell match type [qm,ef,qf,sf,f]
#     "event_key": "2019arc",
#     "key": "2019arc_qf1m1",                                     IMPORTANT - can tell year,event_code,
#     "match_number": 1,
#     "predicted_time": 1556371927,
#     "set_number": 1,
#     "time": 1556371800,
#     "winning_alliance": "red"
#   }
#                                                                 IMPORTANT - match type definitions:
#                                                                                                         qm - Qualification Match
#                                                                                                         qf - Quarter Final
#                                                                                                         sf - Semi Final
#                                                                                                         f -  Final
#                                                                                                         ef - ????
# Want the following output:
# {
#    "matchNum": 1,
#    "red1": 5860,
#    "red2": 4956,
#    "red3": 3184,
#    "blue1": 6032,
#    "blue2": 188,
#    "blue3": 7650
#  }
#  Basically a Dictionary of matchNum, red1, red2, red3, blue1, blue2, blue3



token =  creds.token

url_base = 'https://www.thebluealliance.com/api/v3'

headers  = {
    'accept': 'application/json',
           'If-Modified-Since': '',
    'X-TBA-Auth-Key' : str(token)
}


# Makes call for /event/{event_key}/matches/simple
# Returns JSON object from Blualliance API
def getMatchesCall(event_key):

    url  = url_base + "/event/"+ event_key +"/matches/simple"
    return requests.get(url,headers=headers)


# Extracts a list of all matches, as dictionaries
# Parameter: Json Obj from /event/{event_key}/matches/simple
# Returns List of dictionaries
# sortedMatchList= [match1,match2....matchn]
# Structure of each index of lisst
#    {
#         "matchNum": "",
#         "red1" : "",
#         "red2" : "",
#         "red3" : "",
#         "blue1": "",
#         "blue2": "",
#         "blue3": ""
#     }
#
def extractMatches(json_obj):
    matchesJSON = list(json_obj)
    matchDict = dict()
    matchesList = list()
    #initialize temp match dictionary object
    match = {
        "matchNum": "",
        "red1" : "",
        "red2" : "",
        "red3" : "",
        "blue1": "",
        "blue2": "",
        "blue3": ""
    }
    #loops through each JSON match object of list
    for i in matchesJSON:
        #matchDict = dict(i)
    # Extracts matchNum, red1,red2,red3.blue1.blue2.blue3 from each match object. Only used for qualifications matches
        if(i['comp_level'] == 'qm'):
            matchNum = i['match_number']

            blue1= int(i['alliances']['blue']['team_keys'][0][3:])
            blue2= int(i['alliances']['blue']['team_keys'][1][3:])
            blue3= int(i['alliances']['blue']['team_keys'][2][3:])

            red1 = int(i['alliances']['red']['team_keys'][0][3:])
            red2 = int(i['alliances']['red']['team_keys'][1][3:])
            red3 = int(i['alliances']['red']['team_keys'][2][3:])
            # print("Match Num: " + str(matchNum))
            # print("BlueL " + str([blue1,blue2,blue3]))
            # print("Red: " + str([red1,red2,red3]))


            #Values are inserted into the match dictionary object
            match= {
                "matchNum" : int(matchNum),
                "red1": red1,
                "red2": red2,
                "red3": red3,
                "blue1": blue1,
                "blue2": blue2,
                "blue3": blue3

            }
            #match dictionary object is added to the matchesList list
            matchesList.append(match)
            #print("MATCH: " + str(match))

    #print("***MATCH LIST: " + str(matchesList))


    #sorts the matchList in accending order using the matchNum key
    sortedMatchesList = sorted(matchesList, key=itemgetter('matchNum'))

    print("***MATCH LIST SORTED: " + str(sortedMatchesList))
        # for j in i['alliances']:
        #     #print("i['alliances']: "+ str(i['alliances']))
        #     #print("*******i['alliances']['blue']*****: " +str(i['alliances']['blue']))
        #     alliances = j
        #     print("ALLIANCE: "+ alliances)

        #matchesList.append(match)
    #print(match)

    #Returns sorted list of match dictionaries
    return sortedMatchesList


def createJSONScheduleFile(match_schedule_dict):
    match_schedule = {
        'matchArrayList':match_schedule_dict
    }
    print(match_schedule)


#
def getscheduleJSON(event_key):
    #gets list of JSON objects for each match
    resp = getMatchesCall(event_key)
    data = 1
    # If the call goes through,  a list of dictionaries is returned, sorted by match number
    if resp.status_code == 200:
        print("Call working. Status code:" + str(resp.status_code))
        data = resp.json()
        matchList = extractMatches(data)
        return matchList

    else:
        print("Call failed. Status: " + str(resp.status_code))

def getScheduleJSONForApp(event_key):
    resp = getMatchesCall(event_key)
    data = 1
    if resp.status_code == 200:
        print("Call working. Status code:" + str(resp.status_code))
        data = resp.json()
        matchList = extractMatches(data)
        appSchedule = createJSONScheduleFile(matchList)
        return appSchedule

    else:
        print("Call failed. Status: " + str(resp.status_code))







