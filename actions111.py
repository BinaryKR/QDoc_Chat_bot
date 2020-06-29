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
date = 'Null'
import pymysql
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
connect = pymysql.connect(host='localhost',user='Lee',password='123',db='a',charset='utf8',autocommit=True)
cursor = connect.cursor(pymysql.cursors.DictCursor)
number = 0
import sys
sys.path.insert(0,'/home/lab/PycharmProjects/untitled9/venv/ryu/PyTorch-YOLOv3')
import detect

import os


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="안녕하세요 동국대학교 일산병원입니다.\n 처음 방문하셨나요?",image='http://blogfiles.naver.net/MjAxNjExMDhfMTE0/MDAxNDc4NTc0ODAzODA4.CQWFjXLjEE7S8qI2Eqv4W4SYykMyE9B0ktPIQotlFoYg.vfP4mFbTLtCNrMJXlh0obJwxCKuPeL9MLABf0HgpVhUg.JPEG.bambi2646/45345.jpg')
        print('ㅇㅇㅇㅇㅇㅇㅇㅇ:', tracker.latest_message.get('text'))

        return []
class ActionRe(Action):

    def name(self) -> Text:
        return "action_re"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="주민등록번호를 입력해주세요")

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
        print("a[0]: ",a[0])
        name = a[0]['name']
        age = a[0]['age']

        dispatcher.utter_message(text="안녕하세요 {}님\n어디가 아파서 오셨나요?\n1.치과 \n2.피부과\n".format(name))

        return []

class ActionImageDenti(Action):

    def name(self) -> Text:
        return "action_imagedenti"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="충치 위험을 판단하려 합니다.\n 구강 내 이미지를 제출해주세요\n제출하기\nhttp://210.94.185.43:4002/upload")

        tracker.slots['subject'] = 'Denti'
        return [SlotSet("subject", "Denti")]
class ActionImageShow(Action):

    def name(self) -> Text:
        return "action_imageshow"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        detect.sss()

        path = "/home/lab/PycharmProjects/untitled9/venv/ryu/output/"

        file_lst = os.listdir(path)

        img = mpimg.imread('/home/lab/PycharmProjects/untitled9/venv/ryu/output/'+file_lst[0])
        imgplot = plt.imshow(img)
        plt.show()

        return []
class ActionImageDerma(Action):

    def name(self) -> Text:
        return "action_imagederma"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="증상이 나타난 환 이미지를 제출해주세요\n")
        dispatcher.utter_message(text="제출하기\nhttp://210.94.185.43:4002/upload")

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
                str = str +'1. 10:00~11:00  예약가능\n'
            elif result[1] != 'N':
                str = str + '1. 10:00~11:00  예약불가\n'
            if result[2] == 'N':
                str = str +'2. 11:00~12:00  예약가능\n'
            elif result[1] != 'N':
                str = str+'2. 11:00~12:00  예약불가\n'
            if result[3] == 'N':
                str = str +'3. 13:00~14:00  예약가능\n'
            elif result[3] != 'N':
                str = str + '3. 13:00~14:00  예약불가\n'
            if result[4] == 'N':
                str = str + '4. 14:00~15:00  예약가능\n'
            elif result[4] != 'N':
                str = str + '4. 14:00~15:00  예약불가\n'
            if result[5] == 'N':
                str = str + '5. 15:00~16:00  예약가능\n'
            elif result[5] != 'N':
                str = str + '5. 15:00~16:00  예약불가\n'
            if result[6] == 'N':
                str = str + '6. 16:00~17:00  예약가능\n'
            elif result[6] != 'N':
                str = str + '6 16:00~17:00  예약불가\n'
            if result[7] == 'N':
                str = str + '7. 17:00~18:00  예약가능\n'
            elif result[7] != 'N':
                str = str + '7. 17:00~18:00  예약불가\n'
            dispatcher.utter_message(text=str)
            dispatcher.utter_message("원하는 시간대의 번호를 입력하여 주세요.")
        print(result)
        if flag == 'Derma':
            sql = "select * from SCHEDULE_DERMA where date = '{}';".format(date)
            cursor.execute(sql)
            for i in cursor.fetchall():
                result = list(i.values())
            if result[1] == 'N':
                str = str + '1. 10:00~11:00  O\n'
            elif result[1] !='N':
                str = str+ '1. 10:00~11:00  X\n'
            if result[2] == 'N':
                str = str + '2. 11:00~12:00  O\n'
            elif result[2] != 'N':
                str = str + '2. 11:00~12:00  X\n'
            if result[3] == 'N':
                str = str + '3. 13:00~14:00  O\n'.
            elif result[3] != 'N':
                str = str + '3. 13:00~14:00  X\n'
            if result[4] == 'N':
                str = str + '4. 14:00~15:00  O\n'
            elif result[4] != 'N':
                str = str + '4. 14:00~15:00  X\n'
            if result[5] == 'N':
                str = str + '5. 15:00~16:00  O\n'
            elif result[5]!='N':
                str = str + '5. 15:00~16:00  X\n'
            if result[6] == 'N':
                str = str + '6. 16:00~17:00  O\n'
            elif result[6] != 'N':
                str = str + '6. 16:00~17:00  X\n'
            if result[7] == 'N':
                str = str + '7. 17:00~18:00  O\n'
            elif result[7] != 'N':
                str = str + '7. 17:00~18:00  X\n'
            dispatcher.utter_message(text=str)
            dispatcher.utter_message("원하는 시간대의 번호를 입력하여 주세요.")

        return []
class ActionReservation(Action):

    def name(self) -> Text:
        return "action_reservation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

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



        return []

class RestaurantForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "restaurant_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["name","age","gender","id"]

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
        wb = openpyxl.load_workbook('caps.xlsx')
        wb.get_sheet_names()
        test = wb.get_sheet_by_name("Sheet1")
        name = tracker.get_slot('name')
        gender = tracker.get_slot('gender')
        id = tracker.get_slot('id')
        age = tracker.get_slot('age')
        test['C6'] = name
        test['J6'] = age
        test['F6'] = gender
        test['C7'] = id
        email = "'jinso@gmail.com'"
        sql = 'INSERT INTO info VALUES({},{},{},{},{});'.format(str(name),int(age),str(gender),str(id),email)
        cursor.execute(sql)
        wb.save("{}.xlsx".format(id))
        dispatcher.utter_message(template="utter_submit")
        return []
