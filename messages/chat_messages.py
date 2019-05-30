from modules.message import Message
from modules.xlsxparser import XLSXExporter

class HelloMsg(Message):
    def request(self):
        return "привет"
    def response(self):
        return  "Ну привет, {} {}".format(self.user.first_name, self.user.last_name)
        
class ByeMsg(Message):
    def request(self):
        return "пока"
    def response(self):
        return  "Ну пока!"

class WhoIMsg(Message):
    def request(self):
        return "кто я"
    def response(self):    
        return  self.user.get_full_info()

class WhoYouMsg(Message):
    def request(self):
        return "(кто ты)|(ты кто)"
    def response(self):
        return  "Я, Секретарша студента 😃"

class IDontNow(Message):
    def get(self, server, event):
        self.setup(server, event)
        return "Не понял, что ты написал 🤔\n Введите помощь!"

class PersonalRoom(Message):
    def request(self):
        return "личный кабинет"
    def response(self):
        return  "https://ssoauth.pstu.ru/LoginForm.aspx"

class Web(Message):
    def request(self):
        return "сайт пнипу"
    def response(self):
        return  "http://pstu.ru/"

class ITAS(Message):
    def request(self):
        return "итас"
    def response(self):
        return  "http://itas.pstu.ru/wiki/"
        
class AT(Message):
    def request(self):
        return "ат"
    def response(self):
        return  "http://at.pstu.ru/view/"

class KTE(Message):
    def request(self):
        return "ктэ"
    def response(self):
        return  "http://ktei.pstu.ru/"

class Help(Message):
    def request(self):
        return "помощь"
    def response(self):
        return  """
        Команды:
        -> список документов
        -> расписание
        -> заполни заявление | заполни
        -> календарный план | календарный график
        -> сайт пнипу
        -> личный кабине
        -> итас
        -> ат
        -> ктэ
        -> помощь  
        """
