#! -*- coding:utf8 -*-

import sys
import json
import requests

reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append("..")

from models import WeatherInfo


def get_weather_info(lat, lng):
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    params = {
        "showapi_appid": "399577",
        "showapi_sign": "0b09677f94c445ce8049edf471424ef9",
        "from": "5",
        "lng": str(lng),
        "lat": str(lat),
        "needMoreDay": "0",
        "needIndex": "1",
        "needHourData": "0",
        "need3HourForcast": "0",
        "needAlarm": "0"
    }
    response = requests.post(url="http://route.showapi.com/9-5", headers=header, data=params)
    resp_json = response.json()
    print json.dumps(resp_json)

    showapi_res_body = resp_json.get("showapi_res_body")
    f1 = showapi_res_body.get("f1")
    f1_index = f1.get("index")
    city_info = showapi_res_body.get("cityInfo")

    weather_info = WeatherInfo()
    weather_info.city_name = city_info.get("c3"),
    weather_info.day_weather = f1.get("day_weather"),
    weather_info.night_weather = f1.get("night_weather"),
    weather_info.day_air_temperature = f1.get("day_air_temperature"),
    weather_info.night_air_temperature = f1.get("night_air_temperature"),
    weather_info.day_wind_power = f1.get("day_wind_power"),
    weather_info.night_wind_direction = f1.get("night_wind_direction"),
    weather_info.uv_title = f1_index.get("uv").get("title"),
    weather_info.uv_desc = f1_index.get("uv").get("desc"),
    weather_info.clothes_title = f1_index.get("clothes").get("title"),
    weather_info.clothes_desc = f1_index.get("clothes").get("desc")

    return weather_info


if __name__ == '__main__':
    weather_info = get_weather_info("31.214744", "121.409526")
    print json.dumps(weather_info.weather_print())
