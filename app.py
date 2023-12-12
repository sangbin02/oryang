from flask import Flask, render_template
import requests
import json
from datetime import datetime

app = Flask(__name__)

def get_lunch_info():
    today = datetime.now()

    url = "https://open.neis.go.kr/hub/mealServiceDietInfo"
    service_key = "b1834f9eba344dc0ad96644054eb6d38"
    params = {
        'KEY': service_key,
        'Type': 'json',
        'pIndex': '1',
        'pSize': '100',
        'ATPT_OFCDC_SC_CODE': 'G10',
        'SD_SCHUL_CODE': '7430048',
        'MLSV_YMD': today.strftime('%Y%m%d')
    }

    response = requests.get(url, params=params)
    data = json.loads(response.text)

    ddish_nm_breakfast = []
    ddish_nm_lunch = []
    ddish_nm_dinner = []

    for row in data["mealServiceDietInfo"][1]["row"]:
        meal_type = row["MMEAL_SC_NM"]
        ddish_nm = row["DDISH_NM"]

        if meal_type == "조식":
            ddish_nm_breakfast.extend(ddish_nm.split("<br/>"))
        elif meal_type == "중식":
            ddish_nm_lunch.extend(ddish_nm.split("<br/>"))
        elif meal_type == "석식":
            ddish_nm_dinner.extend(ddish_nm.split("<br/>"))

    return ddish_nm_breakfast, ddish_nm_lunch, ddish_nm_dinner, today

@app.route('/')
def index():
    ddish_nm_breakfast, ddish_nm_lunch, ddish_nm_dinner, today = get_lunch_info()
    return render_template('page1.html', 
                           ddish_nm_breakfast=ddish_nm_breakfast, 
                           ddish_nm_lunch=ddish_nm_lunch, 
                           ddish_nm_dinner=ddish_nm_dinner,
                           today=today)

if __name__ == '__main__':
    app.run(debug=True)

