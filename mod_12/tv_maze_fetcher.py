import json
import requests

keyword = input("Enter keyword: ")

# Request template: https://api.tvmaze.com/search/shows?q=girls
request_url = "https://api.tvmaze.com/search/shows?q=" + keyword

try:
    response = requests.get(request_url)
    if response.status_code==200:
        json_response = response.json()
        # print(json.dumps(json_response, indent=2))
        for a in json_response:
            print(a["show"]["name"], a["show"]["type"])
            print(a["show"]["rating"]["average"])
            print(a["show"]["language"])
            #for day in a["show"]["schdule"]["days"]:
                #print(f"Days, {day}")
except requests.exceptions.RequestException as e:
    print ("Request could not be completed.")
