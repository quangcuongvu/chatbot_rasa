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

    filepath = str(pathlib.Path().absolute()) + '/data/timviec365/cauhoithuonggap.txt'.replace('/', os.sep)
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            # Process
            # print("Process line ", line)
            q_list.append( line.split("|")[0].replace("\n",""))
            a_list.append( line.split("|")[1].replace("\n",""))
            line = fp.readline()
            cnt += 1
    return q_list,a_list

q_list,a_list=load_faq()
# print("Loaded", len(q_list))
hotline='Ngoài ra bạn có thể gọi trực tiếp cho nhân viên timviec365 vào số 1900633682 - phím 1 để được phục vụ.'
def get_faq():
    idx =random.randint(0,len(q_list)-1)
    ret_text = "\nDưới đây là một vài thông tin hữu ích hay gặp:"
    ret_text += "\n🔸Hỏi: " + q_list[idx]
    ret_text += "\n🔸Đáp:️ " + a_list[idx] 
    ret_text += "\n🔸Ngoài ra, bạn có thể gọi hotline số  1900633682 - phím 1 để được tư vấn thêm." 

    return ret_text

class act_unknown(Action):
    
    def name(self) -> Text:
        return "act_unknown"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        text="Xin lỗi bạn vì hiện tại tôi chưa hiểu bạn muốn gì! Bạn có thể chọn một trong những yêu cầu sau:\n1. Gặp nhân viên tư vấn.\n2. Tìm việc làm quanh đây \n3. Tìm ứng viên phù hợp \n4. Cách tạo Cv online "
        dispatcher.utter_message(text=text)
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
            text="Hi, Chào bạn.\nMình có thể giúp bạn giải đáp những vấn đề về tìm việc làm, tìm ứng viên, tạo cv và rất nhiều thứ khác..."+gift_cnt +"\nBạn có yêu cầu cụ thể gì không ạ?")
        
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

# những vấn đề về cv
def load_cv():
    q_list = []
    a_list = []

    filepath = str(pathlib.Path().absolute()) + '/data/timviec365/cv.txt'.replace('/', os.sep)
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            # Process
            # print("Process line ", line)
            q_list.append( line.split("|")[0].replace("\n",""))
            a_list.append( line.split("|")[1].replace("\n",""))
            line = fp.readline()
            cnt += 1
    return q_list,a_list
q_listcv,a_listcv=load_cv()
def get_cv():
    idx =random.randint(0,len(q_listcv)-1)
    ret_text = "\nMột số vấn đề bạn có thể quan tâm khác:"
    ret_text += "\n🔸Hỏi: " + q_listcv[idx]
    ret_text += "\n🔸Đáp:️ " + a_listcv[idx]
    ret_text += "\n🔸Ngoài ra, bạn có thể gọi hotline số  1900633682 - phím 1 để được tư vấn thêm." 
    return ret_text
class act_cv(Action):
    
    def name(self) -> Text:
        return "action_cv"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        gift_cv = get_cv()
        # dispatcher.utter_message(
        #     text="Bạn truy cập vào link https://timviec365.vn/cv-xin-viec để tạo cv nhé")
        # dispatcher.utter_message(text="Ngoài ra bạn có thể gọi trực tiếp cho nhân viên timviec365 vào số 1900633682 - phím 1 nếu gặp phải vấn đề trong quá trình tạo cv.")
        
        dispatcher.utter_message(
            text="Bạn truy cập vào link https://timviec365.vn/cv-xin-viec để tạo cv nhé"+gift_cv)
        
        return []


#những vấn đề về ứng viên tìm việc làm
def load_job():
    q_list = []
    a_list = []

    filepath = str(pathlib.Path().absolute()) + '/data/timviec365/ungvien.txt'.replace('/', os.sep)
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            # Process
            # print("Process line ", line)
            q_list.append( line.split("|")[0].replace("\n",""))
            a_list.append( line.split("|")[1].replace("\n",""))
            line = fp.readline()
            cnt += 1
    return q_list,a_list
q_listuv,a_listuv=load_job()

def get_uv():
    idx =random.randint(0,len(q_listuv)-1)
    ret_text = "\nMột số vấn đề liên quan:"
    ret_text += "\n🔸Hỏi: " + q_listuv[idx]
    ret_text += "\n🔸Đáp:️ " + a_listuv[idx]
    ret_text += "\n🔸Ngoài ra, bạn có thể gọi hotline số  1900633682 - phím 1 để được tư vấn thêm." 
    return ret_text

class act_job(Action):
    def name(self) -> Text:
        return "action_job"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        gift_uv = get_uv()
        dispatcher.utter_message(
            text="Để tìm kiếm việc làm, bạn vui lòng truy cập https://timviec365.vn/dang-ky-ung-vien.html"+gift_uv)
        return []


# Nhà tuyển dụng tìm kiếm ứng viên 
def load_ntd():
    q_list = []
    a_list = []

    filepath = str(pathlib.Path().absolute()) + '/data/timviec365/ntd.txt'.replace('/', os.sep)
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            # Process
            # print("Process line ", line)
            q_list.append( line.split("|")[0].replace("\n",""))
            a_list.append( line.split("|")[1].replace("\n",""))
            line = fp.readline()
            cnt += 1
    return q_list,a_list
q_listntd,a_listntd=load_ntd()
def get_ntd():
    idx =random.randint(0,len(q_listntd)-1)
    ret_text = "\nMột số vấn đề bạn có thể quan tâm khác:"
    ret_text += "\n🔸Hỏi: " + q_listntd[idx]
    ret_text += "\n🔸Đáp:️ " + a_listntd[idx] 
    ret_text += "\n🔸Ngoài ra, bạn có thể gọi hotline số  1900633682 - phím 1 để được tư vấn thêm." 
    return ret_text

class act_offer_job(Action):
    
    def name(self) -> Text:
        return "action_offer_job"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        gift_ntd = get_ntd()
        dispatcher.utter_message(
            text="Bạn đã đăng kí tài khoản nhà tuyển dụng trên web chưa ạ?\nNếu chưa mời truy cập https://timviec365.vn/dang-ky-nha-tuyen-dung.html"+gift_ntd+"\n       Ngoài ra bạn cần thêm thông tin gì nữa không ạ?")
        
        
        return []

## tài khoản 
class action_taikhoan(Action):
    
    def name(self) -> Text:
        return "action_taikhoan"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Hi, Chào bạn.\nNếu bạn chưa có tài khoản ở timviec365, vui lòng truy cập vào https://timviec365.vn/dang-ky.html nhé.\nNếu đã có tài khoản rồi, vui lòng truy cập https://timviec365.vn/dang-nhap.html để tìm kiếm việc làm hoặc tìm ứng viên.")
        
        return []