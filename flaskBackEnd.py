import requests
from flask import Flask, render_template
import backendAPIFunctions


app = Flask(__name__)


@app.route('/getEventsFromYear/<year>', methods= ['GET'])
def getEventsFromYear(year):
   #return "TEST"
    return (backendAPIFunctions.getDistrictEventNamesAndKeysFromYear(int(year)))

@app.route('/')
def main():

    return render_template("index2.html")

@app.route('/getTeamsFromEventKey/<event_key>', methods = ['GET'])
def getTeamsFromEventCode(event_key):
    return (backendAPIFunctions.getTeamNumbersFromEventCode(event_key))

if __name__== "__main__":
    app.run(debug=True)