#! -*- coding:utf8 -*-

import itchat
import sys
import json

reload(sys)
sys.setdefaultencoding("utf-8")

#
# @itchat.msg_register(itchat.content.TEXT)
# def print_content_and_return(msg):
#     print json.dumps(msg)
#
#     if msg.get("FromUserName") == "@174d05a47c96727082002b216d946184f1588f2a4d45530f89dbc9ac498078c1":
#         return
#
#     msg.user.send('%s: %s' % (msg.type, msg.text))
#
#
# @itchat.msg_register(itchat.content.FRIENDS)
# def add_friend(msg):
#     msg.user.verify()
#     msg.user.send('Nice to meet you!')
#
#
# @itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
# def text_reply(msg):
#     if msg.isAt:
#         msg.user.send(u'@%s\u2005I received: %s' % (
#             msg.actualNickName, msg.text))
#
#
# def login_call_back():
#     print 'Login OK'
#
#
# def exit_call_back():
#     print 'Exit OK'
#

if __name__ == "__main__":
    itchat.auto_login(hotReload=True, enableCmdQR=False, loginCallback=login_call_back, exitCallback=exit_call_back)
    itchat.run()
