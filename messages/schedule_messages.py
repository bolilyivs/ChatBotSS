from modules.message import Message
from modules.xlsxparser import XLSXExporter

class Schedule(Message):
    def request(self):
        return "расписание"
    def response(self):
        self.server.saveUserData(self.event, "group",  "")
        return "Какая группа? (Формат: рис-16-1б)"

class UpdateState(Message):

    def getRequest(self):
        return self.event.obj.text
    def getData(self):
        return self.server.loadUserData(self.event)
    def setData(self, event, state, data):
        self.server.saveUserData(event, state, data)
    def showKeyboardDay(self):
        return self.server.keyboardDays()
    def showKeyboardWeek(self):
        return self.server.keyboardWeek()
    def sendSetDay(self):
        self.setData(self.event, "day", self.server.groups[self.getRequest()])
        self.server.send_message_keyboard(self.event, "Какой день недели?", self.showKeyboardDay().get_keyboard())
    def sendSetWeek(self, data):
        self.setData(self.event, "week", data)
        self.server.send_message_keyboard(self.event, "Какая неделя?", self.showKeyboardWeek().get_keyboard())
    def sendFinish(self, data):
        self.setData(self.event, "default", "")
        arr = data.split(":")
        path = '{0}{1}{2}'.format('documents/Schedules/', arr[0], '.xlsx')
        text = XLSXExporter().getSchedule(path, self.server.days[arr[1]], self.server.week[arr[2]])
        self.server.send_message(self.event, text)


