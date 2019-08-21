import requests
import json

import toolsForAPICalls
from operator import itemgetter
#Functions to make:
#                   - Get Event Names and Keys from Year - /events/{year}/simple
#                   - Get Distrct Names from Year - /districts/{year}                   (optional atm)
#                   - Get Districts' Event Names and Keys from Year
#                   - Get Team Numbers from Event Code - /event/{event_key}/teams/simple
#                   - Get Team Names from Event Code - /event/{event_key}/teams/simple
#                   - Get Team Numbers and Team Names from Event Code - /event/{event_key}/teams/simple


#Returns dictonary of all District Name from a given year
#Parameter:
#       1. year - int
#=====================================================================================================================





#Returns JSON object of list of dictionaris of Districts with lists of all Event Names and Event Keys of all events in a District
#Dictionaries in aphanumeric order
#Event lists in Region dictionaries in alphanumeric order
#ex:
#    {
#    [
#           district1: {
#                            [event_code1, event_name1],
#                            [event_code2, event_name2],
#                      },
#           district2: {
#                            [event_code1, event_name1],
#                            [event_code2, event_name2],
#                      }
#    ]
#    }
#Parameter:
#           1. year - int
def getDistrictEventNamesAndKeysFromYear(year):
    api_call = toolsForAPICalls.APICall("/events/"+ str(year) + "/simple")
    api_to_json_obj = toolsForAPICalls.APICalltoJSON(api_call)
    print(api_to_json_obj)
    extractedData= list()

    for i in api_to_json_obj:
        temp = {
                str("name"):str(i["name"]),
                str("event_key"):str(i["key"])
                }
        extractedData.append(temp)
    print("extracted DATA: " + str(extractedData))
    newlist = sorted(extractedData, key=itemgetter("name"))
    print(newlist)
    jsonList =json.dumps(newlist)
    print(jsonList)

    return jsonList



def getTeamNumbersFromEventCode(eventCode):
    api_call = toolsForAPICalls.APICall("/event/" + str(eventCode) + "/teams/simple")
    api_to_json_obj = toolsForAPICalls.APICalltoJSON(api_call)
    extractedData = list()
    print(api_to_json_obj)
    for i in api_to_json_obj:
        temp = {
            "team_number" : int(i["team_number"]),
            "nickname" : str(i["nickname"])

        }
        extractedData.append(temp)
    newList = sorted(extractedData, key=itemgetter("team_number"))
    print("TEAMS EXTRACTED: " + str(extractedData))

    jsonList = json.dumps(newList)
    return jsonList

def getTeamNamesFromEventCode(eventCode):
    pass


def getTeamNamesAndNumbersFromEventCode(eventCode):
    pass


def generateEventsFromYear(year):
    pass

print(getTeamNumbersFromEventCode('2019arc'))

#getDistrictEventNamesAndKeysFromYEar(2019)