#! -*- coding:utf8 -*-

import sys
import json
import requests

reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append("..")


class WeatherInfo(object):
    city_name = ""  # 城市名
    day_weather = ""  # 白天天气
    night_weather = ""  # 晚上天气
    day_air_temperature = ""  # 白天温度
    night_air_temperature = ""  # 晚上温度
    day_wind_power = ""  # 白天风力
    night_wind_direction = ""  # 夜晚风力
    uv_title = ""  # 紫外线
    uv_desc = ""  # 紫外线描述
    clothes_title = ""  # 穿衣
    clothes_desc = ""  # 穿衣

    def weather_print(self):
        return "今天%s白天天气%s, 温度%s, 风力%s, 紫外线%s, %s%s" % (
            self.city_name[0], self.day_weather[0], self.day_air_temperature[0], self.day_wind_power[0],
            self.uv_title[0],
            self.uv_desc[0], self.clothes_desc)
