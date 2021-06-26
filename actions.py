# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Tracker
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import json
import re
import gc
from rasa_sdk.forms import FormAction
from requests.models import Response
import feedparser
import random
import pathlib
import os

def load_faq():
    q_list = []
    a_list = []

    filepath = str(pathlib.Path().absolute()) + '/data/timviec.txt'.replace('/', os.sep)
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            # Process
            print("Process line ", line)
            q_list.append( line.split("|")[0].replace("\n",""))
            a_list.append( line.split("|")[1].replace("\n",""))
            line = fp.readline()
            cnt += 1
    return q_list,a_list

q_list,a_list=load_faq()
# print("Loaded", len(q_list))

def get_faq():
    idx =random.randint(0,len(q_list)-1)
    ret_text = "🎁Một số vấn đề bạn có thể quan tâm:\n"
    ret_text += "🔸Hỏi: " + q_list[idx] + "\n"
    ret_text += "🔸Đáp:️ " + a_list[idx] + "\n"

    return ret_text
class ActionLookUpWordDictionary(Action):
    def name(self) -> Text:
        return 'action_lookUp_en'

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        word = str(tracker.get_slot('enword')).lower()
        print(word)
        if not word:
            dispatcher.utter_message("Đôi lúc sự thông thái của tôi cũng có giới hạn!")
            return []
        if word =='none':
            dispatcher.utter_message("Mình chưa hiểu ý của bạn")
            return []

        return []

class act_unknown(Action):
    
    def name(self) -> Text:
        return "act_unknown"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        button = {
            "title": "Địa chỉ của công ty?"   
        }
        button1 = {
            "title": "Gặp nhân viên tư vấn.",
            "payload": "gọi hotline",
        }
       
        dispatcher.utter_message(
            text="Xin lỗi bạn vì hiện tại tôi chưa hiểu bạn muốn gì! Bạn có thể chọn một trong những yêu cầu sau\n"
            , buttons=[button, button1])

        del button, button1
        gc.collect()
        
        return []

class act_help(Action):
    
    def name(self) -> Text:
        return "act_help"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        gift_cnt = get_faq()
        dispatcher.utter_message(
            text=gift_cnt)
        return []


# Ham lay ket qua so xo va tra ve. Ten ham la action_get_lottery
class action_get_lottery(Action):
	def name(self):
            # Doan nay khai bao giong het ten ham ben tren la okie
		    return 'action_get_lottery'
	def run(self, dispatcher, tracker, domain):
            # Khai bao dia chi luu tru ket qua so xo. O day lam vi du nen minh lay ket qua SX Mien Bac
            url = 'https://xskt.com.vn/rss-feed/mien-bac-xsmb.rss'
            # Tien hanh lay thong tin tu URL
            feed_cnt = feedparser.parse(url)
            # Lay ket qua so xo moi nhat
            first_node = feed_cnt['entries']
            # Lay thong tin ve ngay va chi tiet cac giai
            return_msg = first_node[0]['title'] + "\n" + first_node[0]['description']
            # Tra ve cho nguoi dung
            dispatcher.utter_message(return_msg)
            gift_cnt = get_faq()
            dispatcher.utter_message(
                text=gift_cnt)
            return []

