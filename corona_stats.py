import requests
import json
import datetime

def getStats():

    response = requests.get('https://covidtracking.com/api/states/daily')

    headers_json = json.loads(response.text)

    today = datetime.datetime.today().strftime('%Y%m%d')

    string = f"Results for {datetime.datetime.today().strftime('%Y-%m-%d')}\n"

    for item in headers_json:

        if str(item['date']) == today:

            pos_cases = item['positive']
            if str(item['hospitalized']) == "None":
                hosp_cases = 0
            else:
                hosp_cases = item['hospitalized']
            if str(item['death']) == "None":
                deaths = 0
            else:
                deaths = item['death']
            death_increase = item['deathIncrease']

            string += f"-----{item['state']}-----\npositive cases: {pos_cases}\nhospitalizations: {hosp_cases}\ndeaths: {deaths}\n\n"

    return string
