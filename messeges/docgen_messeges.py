from modules.message import Message
from modules.xlsxparser import XLSXExporter

class Statement(Message):
    def getData(self):
        return self.server.loadUserData(self.event)["data"]
    def saveData(self, state):
        self.server.saveUserData(self.event, state, "{}:{}".format(self.getData(), self.event.obj.text))
    def clearData(self, state):
        self.server.saveUserData(self.event, state, "")

class GiveMeMoney(Statement):
    def request(self):
        return r"(заполни заявление)|(заполни)"
    def response(self):
        self.clearData("gen_course")
        print(self.getData())
        return  "Введите номер курса!"

class GetMoneyCourse(Statement):
    def request(self):
        return r".+"
    def response(self):
        self.saveData("gen_group")
        return  "Введите название группы!"

class GetMoneyGroup(Statement):
    def request(self):
        return r".+"
    def response(self):
        self.saveData("gen_secondName")
        return  "Введите свое отчество!"

class GetMoneySecondName(Statement):
    def request(self):
        return r".+"
    def response(self):
        self.saveData("gen_mobile")
        return  "Введите номер мобильного телефона!"

class GetMoneyMobile(Statement):
    def request(self):
        return r".+"
    def response(self):
        self.saveData("gen_active")
        return  "Введите: за какую активность стипендия? "

class GiveMeMoneyFinal(Statement):
    def request(self):
        return r".+"
    def response(self):
        data = self.getData().split(":")
        data.append(self.event.obj.text)
        print(data)
        values = {
            "course" : data[1],
            "group" : data[2],
            "fio" : self.user.last_name + " " + self.user.first_name[0] + ". " + data[3][0] + ".",
            "mobile" : data[4],
            "active" : data[5]}
        self.server.upload_gen_document(self.event, "documents/SchApp.docx", values, "Степуха!")
        self.clearData("default")
        return  "Готово!"

