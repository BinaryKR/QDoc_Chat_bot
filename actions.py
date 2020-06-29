from typing import Dict, Text, Any, List, Union, Optional
import openpyxl
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from typing import Any, Text, Dict, List
import glob
import pdfkit as pdf
import pandas as pd
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet
import matplotlib as plt
import pymysql
import sys
import matplotlib.image as mpimg
sys.path.insert(0,'/home/webroot/ryu/PyTorch-YOLOv3')
import detect1
import detect2
import shutil
import os
import time
connect = pymysql.connect(host='localhost',user='root',password='123',db='rasa',charset='utf8',autocommit=True)
cursor = connect.cursor(pymysql.cursors.DictCursor)

import webbrowser as w




cnt = 110
wb = openpyxl.load_workbook('caps.xlsx')
wb.get_sheet_names()
test = wb.get_sheet_by_name("Sheet1")


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #f = open('corona.txt', 'r')
        #data = f.read()
        #f.close()
        # dispatcher.utter_message(text="안녕하세요 동국대학교 일산병원입니다.\n 처음 방문하셨나요?",image='http://blogfiles.naver.net/MjAxNjExMDhfMTE0/MDAxNDc4NTc0ODAzODA4.CQWFjXLjEE7S8qI2Eqv4W4SYykMyE9B0ktPIQotlFoYg.vfP4mFbTLtCNrMJXlh0obJwxCKuPeL9MLABf0HgpVhUg.JPEG.bambi2646/45345.jpg')
        #dispatcher.utter_message(text=data)
        dispatcher.utter_message(text="안녕하세요 동국대학교 일산병원입니다.\n 처음 방문하셨나요?",image='https://previews.123rf.com/images/dvolkovkir1980/dvolkovkir19801703/dvolkovkir1980170300220/74395939-%EB%B3%91%EC%9B%90-%EC%95%84%EC%9D%B4%EC%BD%98%EC%9E%85%EB%8B%88%EB%8B%A4-%ED%8F%89%EB%A9%B4-%EB%94%94%EC%9E%90%EC%9D%B8-%EB%B2%A1%ED%84%B0-%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8-%EB%A0%88%EC%9D%B4-%EC%85%98-%EB%B2%A1%ED%84%B0-.jpg')

        return []
class ActionQuestion(Action):

    def name(self) -> Text:
        return "action_question"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        id = tracker.get_slot('id')
        print(id)
        sql = "SELECT * FROM info where id='{}';".format(id)
        cursor.execute(sql)
        a = cursor.fetchall()
        name = a[0]['name']
        age = a[0]['age']
        disease = a[0]['disease']
        medicine = a[0]['medicine']
        
        dispatcher.utter_message(text="안녕하세요 {}님\n어디가 아파서 오셨나요?\n1.치과 \n2.피부과\n3.코로나 확진자 경로확인".format(name))

        return []

class ActionCorona(Action):
    def name(self) -> Text:
        return "action_corona"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="방문하신 구 이름을 말해주세요")

        return []

class ActionCorona2(Action):
    def name(self) -> Text:
        return "action_gangdong"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="강동구35(번호미부여) \n 6.22. 암사동,40대,여 \n 6.18. 08:00 ~ 09:00  자택 → 타지역 직장(버스, 지하철, 도보 이동)※ 버스 → 지하철(8호선), 자택 엘리베이터 CCTV 확인중 \n 09:00 ~ 20:30  타지역 이동동선 \n 20:30 ~ 21:30  자택 귀가(지하철, 버스, 도보 이동)※ 지하철(8호선) → 버스, 자택 엘리베이터 CCTV 확인중\n 6.19.\n 08:00 ~ 09:00 자택 → 타지역 직장(버스, 지하철, 도보 이동)※ 버스 → 지하철(8호선), 자택 엘리베이터 CCTV 확인중\n 09:00 ~ 23:10  타지역 이동동선\n 23:10   자택 귀가(택시 이동)※ 자택 엘리베이터 CCTV 확인 중\n 6.20.\n 12:32 ~ 12:37   서울삼성내과의원(암사3동, 도보 이동)※ 병원 내부 확인 불가(CCTV 고장)\n 12:38 ~ 12:40  조은온누리약국(암사3동, 도보 이동)※ 전원 마스크 착용(접촉자 없음)\n 12:45  자택 귀가(도보 이동)※ 자택 엘리베이터 CCTV 확인 중\n 6.21.\n 09:04 ~ 09:24  강동구보건소, 코로나19 상담(자차 이동)※ 전원 마스크 착용(접촉자 없음)\n 09:45   자택 귀가(자차 이동)※ 자택 엘리베이터 CCTV 확인 중\n 6.22.\n 15:34 ~ 15:48  강동구보건소 코로나19 검사(자차 이동)※ 전원 마스크 착용(접촉자 없음)\n 16:00   자택 귀가(자차 이동)※ 자택 엘리베이터 CCTV 확인 중\n 23:00   확진(양성) 판정")
         

        return []

Denti_list = [ "Q. 원하시는 진료는 무엇인가요?","Q. 어떻게 불편하신가요?","Q. 증상이 나타난지 얼마나 됐나요?", "Q. 어느 부위가 불편하신가요?", "Q. 출혈이 있으신가요?", "Q, 교정 한 적이 있으십니까?"]
Denti_answer = []
Derma_list = ["Q. 원하시는 진료는 무엇인가요?", "Q. 어떻게 불편하신가요?", "Q. 언제부터 증상이 나타나셨나요?", "Q. 증상이 나타나는 부위가 어디신가요?"]
Derma_answer = []
class Actiondencate(Action):

    def name(self) -> Text:
        return "action_dencate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="원하시는 진료를 말씀 해주세요. \n1.충치치료 \n2.치아교정 \n3.심미치료 \n4.임플란트")

        return [SlotSet("subject","Denti")]

class Actionden1(Action):

    def name(self) -> Text:
        return "action_den1"
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Denti_answer.append(tracker.latest_message.get('text'))
        dispatcher.utter_message(text="어떻게 불편하신가요?")
        
        return []
class Actiondensymp1(Action):

    def name(self) -> Text:
        return "action_densymp1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Denti_answer.append(tracker.latest_message.get('text'))

        dispatcher.utter_message(text="이가 시리시군요, 시린지 얼마나 됐나요?")
        test['H5'] = '치과'
        return []

class Actiondensymp2(Action):

    def name(self) -> Text:
        return "action_densymp2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="이가 아프시군요, 아픈지 얼마나 됐나요?")
        Denti_answer.append(tracker.latest_message.get('text'))

        return []
class Actiondensymp3(Action):

    def name(self) -> Text:
        return "action_densymp3"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Denti_answer.append(tracker.latest_message.get('text'))

        dispatcher.utter_message(text="이가 흔들리시군요, 흔들린지 얼마나 됐나요?")

        return []
class Actiondensymp4(Action):

    def name(self) -> Text:
        return "action_densymp4"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="이가 시큰거리시군요, 시큰거린지 얼마나 됐나요?")
        Denti_answer.append(tracker.latest_message.get('text'))

        return []

class Actiondenpart(Action):

    def name(self) -> Text:
        return "action_denpart"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Denti_answer.append(tracker.latest_message.get('text'))

        dispatcher.utter_message(text="그러시군요, 어느 부위가 불편하신가요?")

        return []
class Actionden4(Action):

    def name(self) -> Text:
        return "action_den4"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="출혈이 있으십니까?")
        Denti_answer.append(tracker.latest_message.get('text'))

        return []
class Actionden5(Action):

    def name(self) -> Text:
        return "action_den5"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Denti_answer.append(tracker.latest_message.get('text'))

        dispatcher.utter_message(text="교정을 한 적이 있으십니까?")

        return []

class Actioncorrect1(Action):

    def name(self) -> Text:
        return "action_correct1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="어떤 교정을 원하시나요? (부분교정, 전체교정)")

        return []

class Actioncorrect2(Action):

    def name(self) -> Text:
        return "action_correct2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="원하는 교정장치가 있으신가요?")

        return []


class Actioncorrect2(Action):

    def name(self) -> Text:
        return "action_correct2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="원하는 교정장치가 있으신가요?")

        return []
class Actionderma1(Action):

    def name(self) -> Text:
        return "action_derma1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="원하시는 진료를 말씀 해주세요 (일반진료/피부클리닉/레이저클리닉)")
        test['H5'] = '피부과'
        return [SlotSet("subject","Derma")]
    

class Actionderma2(Action):

    def name(self) -> Text:
        return "action_derma2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Derma_answer.append(tracker.latest_message.get('text'))
        dispatcher.utter_message(text="어떻게 불편하신가요?")

        return []
class Actionderma3(Action):

    def name(self) -> Text:
        return "action_derma3"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Derma_answer.append(tracker.latest_message.get('text'))

        dispatcher.utter_message(text="언제부터 증상이 나타나셨나요?")

        return []
class Actionderma4(Action):

    def name(self) -> Text:
        return "action_derma4"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Derma_answer.append(tracker.latest_message.get('text'))

        dispatcher.utter_message(text="증상이 나타나는 부위가 어디인가요?")

        return []

class ActionImageDenti(Action):

    def name(self) -> Text:
        return "action_imagedenti"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Denti_answer.append(tracker.latest_message.get('text'))
        dispatcher.utter_message(text="충치 위험을 판단하려 합니다.\n 구강 내 이미지를 제출해주세요\n제출하기\n http://121.67.246.252:5003/upload")

        tracker.slots['subject'] = 'Denti'
        return [SlotSet("subject", "Denti")]

class ActionImageDerma(Action):

    def name(self) -> Text:
        return "action_imagederma"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Derma_answer.append(tracker.latest_message.get('text'))

        dispatcher.utter_message(text="증상이 나타난 환 이미지를 제출해주세요\n")
        dispatcher.utter_message(text="제출하기\nhttp://121.67.246.252:5003/upload")
        tracker.slots['subject'] = 'Derma'
        return [SlotSet("subject", "Derma")]
class ActionQ_Date(Action):

    def name(self) -> Text:
        return "action_Q_Date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="날짜를 입력해주세요\nyyyy-mm-dd")

        return []

class ActionQ_Reserve(Action):

    def name(self) -> Text:
        return "action_Q_Reserve"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if(test['H5'] == '피부과'):
            detect2.sss()
        else:
            detect1.sss()
        global cnt
        path = "/home/webroot/ryu/output"
        file_list = os.listdir(path)
        filename1 = file_list[0]
        filename2 = '{}.png'.format(cnt)

        src = '/home/webroot/ryu/output/'
        dirs = '/home/webroot/ryu/static/img/'

        shutil.move(src+filename1, dirs+filename2)
        dispatcher.utter_message(text=
                "result",image="http://121.67.246.252:5004/static/img/{}.png".format(cnt))
        path2 = "/home/webroot/ryu/uploads"
        file_list2 = os.listdir(path2)
        for i in file_list2:
            os.remove('/home/webroot/ryu/uploads/'+str(i))
        cnt = cnt + 1


        dispatcher.utter_message(text="진료를 예약하시겠습니까?")

        return []

class ActionShowSchedule(Action):

    def name(self) -> Text:
        return "action_show_schedule"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        result = []
        flag = tracker.get_slot('subject')
        global date
        date = tracker.latest_message.get('text')

        if flag == 'Denti':
            sql = "select * from SCHEDULE_DENTI where date = '{}';".format(date)
            cursor.execute(sql)
            for i in cursor.fetchall():
                result = list(i.values())
            str = ''
            cnt = 0
            if result[1] == 'N':
                str = str + '1. 10:00~11:00    O\n'
            elif result[1] != 'N':
                str = str + '1. 10:00~11:00    X\n'
            if result[2] == 'N':
                str = str +'2. 11:00~12:00    O\n'
            elif result[2] != 'N':
                str = str+'2. 11:00~12:00    X\n'
            if result[3] == 'N':
                str = str +'3. 13:00~14:00    O\n'
            elif result[3] != 'N':
                str = str + '3. 13:00~14:00    X\n'
            if result[4] == 'N':
                str = str + '4. 14:00~15:00    O\n'
            elif result[4] != 'N':
                str = str + '4. 14:00~15:00    X\n'
            if result[5] == 'N':
                str = str + '5. 15:00~16:00    O\n'
            elif result[5] != 'N':
                str = str + '5. 15:00~16:00    X\n'
            if result[6] == 'N':
                str = str + '6. 16:00~17:00    O\n'
            elif result[6] != 'N':
                str = str + '6 16:00~17:00    X\n'
            if result[7] == 'N':
                str = str + '7. 17:00~18:00    O\n'
            elif result[7] != 'N':
                str = str + '7. 17:00~18:00    X\n'

            dispatcher.utter_message(text=str)
            dispatcher.utter_message("원하는 시간대의 번호를 입력하여 주세요.")
        print(result)
        if flag == 'Derma':
            sql = "select * from SCHEDULE_DERMA where date = '{}';".format(date)
            cursor.execute(sql)
            for i in cursor.fetchall():
                result = list(i.values())
            str = ''
            if result[1] == 'N':
                str = str +'1. 10:00~11:00    O\n'
            elif result[1] != 'N':
                str = str + '1. 10:00~11:00    X\n'
            if result[2] == 'N':
                str = str +'2. 11:00~12:00    O\n'
            elif result[2] != 'N':
                str = str+'2. 11:00~12:00    X\n'
            if result[3] == 'N':
                str = str +'3. 13:00~14:00    O\n'
            elif result[3] != 'N':
                str = str + '3. 13:00~14:00    X\n'
            if result[4] == 'N':
                str = str + '4. 14:00~15:00    O\n'
            elif result[4] != 'N':
                str = str + '4. 14:00~15:00    X\n'
            if result[5] == 'N':
                str = str + '5. 15:00~16:00    O\n'
            elif result[5] != 'N':
                str = str + '5. 15:00~16:00    X\n'
            if result[6] == 'N':
                str = str + '6. 16:00~17:00    O\n'
            elif result[6] != 'N':
                str = str + '6 16:00~17:00    X\n'
            if result[7] == 'N':
                str = str + '7. 17:00~18:00    O\n'
            elif result[7] != 'N':
                str = str + '7. 17:00~18:00    X\n'
            dispatcher.utter_message(text=str)
            dispatcher.utter_message("원하는 시간대의 번호를 입력하여 주세요.")

        return []
class ActionRe(Action):

    def name(self) -> Text:
        return "action_re"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="주민등록번호를 입력해주세요")

        return []
class ActionReservation(Action):

    def name(self) -> Text:
        return "action_reservation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        id = tracker.get_slot('id')
        num = tracker.latest_message.get('text')
        flag = tracker.get_slot('subject')
        global date

        if flag == 'Denti':

            if '1' in num:
                sql = "UPDATE SCHEDULE_DENTI set time1 = 'O' where date = '{}';".format(date)
                print(sql)
                cursor.execute(sql)
            if '2' in num:
                sql = "UPDATE SCHEDULE_DENTI set time2 = 'O' where date = '{}';".format(date)
                cursor.execute(sql)
            if '3' in num:
                sql = "UPDATE SCHEDULE_DENTI set time3 = 'O' where date = '{}';".format(date)
                cursor.execute(sql)
            if '4' in num:
                sql = "UPDATE SCHEDULE_DENTI set time4 = 'O' where date = '{}';".format(date)
                cursor.execute(sql)
            if '5' in num:
                sql = "UPDATE SCHEDULE_DENTI set time5 = 'O' where date = '{}';".format(date)
                cursor.execute(sql)
            if '6' in num:
                sql = "UPDATE SCHEDULE_DENTI set time6 = 'O' where date = '{}';".format(date)
                cursor.execute(sql)
            if '7' in num:
                sql = "UPDATE SCHEDULE_DENTI set time7 = 'O' where date = '{}';".format(date)
                cursor.execute(sql)
            if '8' in num:
                sql = "UPDATE SCHEDULE_DENTI set time8 = 'O' where date = '{}';".format(date)
                cursor.execute(sql)
        if flag == 'Derma':
            if '1' in num:
                sql = "UPDATE SCHEDULE_DERMA set time1 = 'O' where date = '{}';".format(date)
                cursor.execute(sql)
            if '2' in num:
                sql = "UPDATE SCHEDULE_DERMA set time2 = 'O' where date = '{}';".format(date)
                cursor.execute(sql)
            if '3' in num:
                sql = "UPDATE SCHEDULE_DERMA set time3 = 'O' where date = '{}';".format(date)
                cursor.execute(sql)
            if '4' in num:
                sql = "UPDATE SCHEDULE_DERMA set time4 = 'O' where date = '{}';".format(date)
                cursor.execute(sql)
            if '5' in num:
                sql = "UPDATE SCHEDULE_DERMA set time5 = 'O' where date = '{}';".format(date)
                cursor.execute(sql)
            if '6' in num:
                sql = "UPDATE SCHEDULE_DERMA set time6 = 'O' where date = '{}';".format(date)
                cursor.execute(sql)
            if '7' in num:
                sql = "UPDATE SCHEDULE_DERMA set time7 = 'O' where date = '{}';".format(date)
                cursor.execute(sql)
            if '8' in num:
                sql = "UPDATE SCHEDULE_DERMA set time8 = 'O' where date = '{}';".format(date)
                cursor.execute(sql)
        dispatcher.utter_message(text="예약이 완료 되었습니다.")
        path = "/home/webroot/ryu/static/img/"
        file_list = os.listdir(path)
        filename1 = file_list[-1]


        img = openpyxl.drawing.image.Image(path+'{}'.format(filename1))
        img.width = 150
        img.height = 150
        test.add_image(img,'E23')
        if flag == 'Denti':
            test['B10'] = Denti_list[0]
            test['B12'] = Denti_list[1]
            test['B14'] = Denti_list[2]
            test['B16'] = Denti_list[3]
            test['B18'] = Denti_list[4]
            test['B20'] = Denti_list[5]
            test['B11'] = 'A. '+Denti_answer[0]
            test['B13'] = 'A. '+Denti_answer[1]
            test['B15'] = 'A. '+Denti_answer[2]
            test['B17'] = 'A. '+Denti_answer[3]
            test['B19'] = 'A. '+Denti_answer[4]
            test['B21'] = 'A. '+Denti_answer[5]
        else:
            test['B10'] = Derma_list[0]
            test['B12'] = Derma_list[1]
            test['B14'] = Derma_list[2]
            test['B16'] = Derma_list[3]
            test['B11'] = 'A. '+Derma_answer[0]
            test['B13'] = 'A. '+Derma_answer[1]
            test['B15'] = 'A. '+Derma_answer[2]
            test['B17'] = 'A. '+Derma_answer[3]

        wb.save("{}.xlsx".format(id)) 
        
        return []

class Actionthanku(Action):

    def name(self) -> Text:
        return "action_thanku"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Denti_answer.append(tracker.latest_message.get('text'))

        dispatcher.utter_message(text="예약이 완료되었습니다.  감사합니다.")
        return []


class RestaurantForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "restaurant_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        #age 
        return ["name","gender","age","id","disease","medicine"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "name": self.from_entity(entity="name", not_intent="chitchat"),
            "age": [
                self.from_entity(
                    entity="age", intent=["inform", "request_restaurant"]
                ),
            ],
            "disease": self.from_entity(entity="disease", not_intent="chitchat"),
            "medicine": self.from_entity(entity="medicine", not_intent="chitchat"),
            "id": self.from_entity(entity="id", not_intent="chitchat"),
            "gender": self.from_entity(entity="gender", not_intent='chitchat'),
            "feedback": [self.from_entity(entity="feedback"), self.from_text()],  
        }

    # USED FOR DOCS: do not rename without updating in docs
    @staticmethod
    def cuisine_db() -> List[Text]:
        """Database of supported cuisines"""

        return [
            "ryu",
            "jinsu"
        ]

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""

        try:
            int(string)
            return True
        except ValueError:
            return False

    # USED FOR DOCS: do not rename without updating in docs
    def validate_cuisine(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate cuisine value."""

        if value.lower() in self.cuisine_db():
            # validation succeeded, set the value of the "cuisine" slot to value
            return {"name": value}
        else:
            dispatcher.utter_message(template="wrong name")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"name": None}

    def validate_num_people(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""

        if self.is_int(value) and int(value) > 0:
            return {"age": value}
        else:
            dispatcher.utter_message(template="utter_wrong_num_people")
            # validation failed, set slot to None
            return {"age": None}

    def validate_outdoor_seating(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate outdoor_seating value."""

        if isinstance(value, str):
            if "Man" == value:
                # convert "out..." to True
                return {"gender": value}
            elif "Woman" == value:
                # convert "in..." to False
                return {"gender": value}
            else:
                dispatcher.utter_message(template="wrong gender!")
                # validation failed, set slot to None
                return {"gender": None}

        else:
            # affirm/deny was picked up as T/F
            return {"gender": value}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        #wb = openpyxl.load_workbook('caps.xlsx')
        #wb.get_sheet_names()
        #test = wb.get_sheet_by_name("Sheet1")
        name = tracker.get_slot('name')
        gender = tracker.get_slot('gender')
        id = tracker.get_slot('id')
        age = tracker.get_slot('age')
        disease = tracker.get_slot('disease')
        medicine = tracker.get_slot('medicine')
        test['C6'] = name
        test['J6'] = age
        test['H6'] = gender
        test['C7'] = id
        test['C8'] = disease
        test['C9'] = medicine
        email = "jinso@gmail.com"
        sql = "INSERT INTO info VALUES('{}','{}','{}','{}','{}','DEFAULT','DEFAULT');".format(str(name),int(age),str(gender),str(id),email)
        cursor.execute(sql)
        #wb.save("{}.xlsx".format(id))
        dispatcher.utter_message(template="utter_submit")
        return []
