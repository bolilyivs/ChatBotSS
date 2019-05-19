from modules.botServerBase import BotServerBase
from modules.gendoc import GenDoc

from messeges.chat_messeges import *
from messeges.document_messeges import *
from messeges.docgen_messeges import *
from messeges.schedule_messeges import *

import settings
import time
import datetime
import os
import random
from modules.models import *

class BotServer(BotServerBase):
    def __init__(self):
        super().__init__(settings.GROUP_TOKEN, settings.GROUP_ID)
        self.modules = settings.MODULES
    
    def newMessage(self, event):
        super().newMessage(event)

        ok = False
        for module in self.modules:
            msg = eval(module+"()")
            text = msg.get(self, event)
            if text != "":
                ok = True
                self.send_message(event,text)        
        if not ok:
            person = self.loadUserData(event)

            if person["state"] == 1:
                self.send_message(event, IDontNow().get(self, event))

            else:
                self.send_message(event, IDontNow().get(self, event))
    
    def seqName(self, event):
        "Создание уникального названия"

        return str(event.obj.from_id)+ str(time.time()) + str(random.randint(0, 10000000)) +".docx"
    
    def upload_gen_document(self, event, file, values, title = "out"):
        "Генерация и загрузка документа"

        file_name = self.seqName(event)
        GenDoc().get(file, values,  file_name)
        self.upload_document(event, file_name, title)
        os.remove(file_name)

    def saveUserData(self, event, state = "default", data = ""):
        """ Сохранить данные данного пользователя """
         
        try:
            person = Person.get(Person.userid == event.obj.from_id)
            person.state = state
            person.data = str(data)
            person.date = str(datetime.datetime.now())
        except:      
            person = Person.create(
                userid = event.obj.from_id ,
                state = str(state),
                data = str(data),
                date = str(datetime.datetime.now())
            )

    def loadUserData(self, event):
        """ Загрузить данные данного пользователя """

        print("test")
        person = Person.get(Person.userid == event.obj.from_id)
        return {"userid": person.userid,
            "state": person.state,
            "data": person.data,
            "date": person.date,
           }
        
    
