#! -*- coding:utf8 -*-

import sys
import json
import time
import itchat

reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append("..")

from infra.weather import WeatherService
from infra.weather.models import WeatherInfo

weather_service = WeatherService()

send = False
send_hour = 23
send_min = 28
send_sec = 00


def send(itchat, msg):
    itchat.send(msg, "@d6289ba22f9a03a8d5f8d43e7da94557")


def test():
    while True:
        local_time = time.localtime(time.time())
        hour = local_time[3]
        min = local_time[4]
        sec = local_time[5]

        if hour == send_hour and min == send_min and sec == send_sec:
            info = weather_service.get_info("31.214744", "121.409526")
            print info

        time.sleep(1)
        print hour, min, sec


if __name__ == '__main__':
    # test()
    itchat.auto_login(hotReload=True, enableCmdQR=False)
    send(itchat, "你好")
    print itchat.search_friends(userName="@502c9eb83ead29ad58cbf00d6daa3cf45ecaed3e0ef58cb44889804318bc20e9")
