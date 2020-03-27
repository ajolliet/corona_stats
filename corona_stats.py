import requests
import json
import datetime

def getStats():

    response = requests.get('https://covidtracking.com/api/states/daily')

    headers_json = json.loads(response.text)

    today = datetime.datetime.today().strftime('%Y%m%d')
    today_format = datetime.datetime.today().strftime('%Y-%m-%d')
    yesterday = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%Y%m%d')
    yesterday_format = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

    string = f""

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

            string += f"Today's results ({today_format})\n-----{item['state']}-----\npositive cases: {pos_cases}\nhospitalizations: {hosp_cases}\ndeaths: {deaths}\n\n"

            if str(item['state']) == "WY":
                break

        else:

            if str(item['date']) == yesterday:

                pos_cases = item['positive']
                if str(item['death']) == "None":
                    deaths = 0
                else:
                    deaths = item['death']

                string += f"Yesterday's results ({yesterday_format}):\n-----{item['state']}-----\npositive cases: {pos_cases}\ndeaths: {deaths}\n\n"

                if str(item['state']) == "WY":
                    break

    return string

print(getStats())
