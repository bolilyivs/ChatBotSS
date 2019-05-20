import settings

from modules.botServerBase import BotServerBase
from modules.message import Message
from modules.xlsxparser import XLSXExporter
from messeges.schedule_messeges import UpdateState


class ScheduleExecute():

    def __init__(self):
        self.days = settings.DAYS
        self.week = settings.WEEK
        self.groups = settings.GROUPS

    def run(self, person, server, event):
        updt = UpdateState()
        updt.server = server
        updt.event = event

        if person["state"] == "group":
            data = ""
            for group in self.groups.keys():
                if group == updt.getRequest():
                    updt.sendSetDay()
                    return True
                else:
                    data = "not"
            if data == "not":
                return False
            return True

        elif person["state"] == "day":
            data = ""
            for day in self.days.keys():
                if day == updt.getRequest():
                    set_data = person["data"] + ":" + updt.getRequest()
                    updt.sendSetWeek(set_data)
                    return True
                else:
                    data = "not"
            if data == "not":
                return False
            return True

        elif person["state"] == "week":
            data = ""
            for day in self.week.keys():
                print(str(updt.getRequest()))
                if day == updt.getRequest():
                    set_data = person["data"] + ":" + updt.getRequest()
                    updt.sendFinish(set_data)
                    return True
                else:
                    data = "not"
            if data == "not":
                return False
            return True

        else:
            return False
