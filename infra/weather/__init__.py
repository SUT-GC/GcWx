#! -*- coding:utf8 -*-

import sys
import json

reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append("..")

from wan_yi import (
    get_weather_info
)


class WeatherService(object):
    def __init__(self):
        super(WeatherService, self).__init__()

    def get_info(self, lat, lng):
        return get_weather_info(lat, lng)


if __name__ == '__main__':
    service = WeatherService()
    print service.get_info("31.214744", "121.409526")
