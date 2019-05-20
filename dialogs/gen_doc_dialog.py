from messeges.docgen_messeges import *

class GenDocDialog():
    def run(self, person, server, event):
        state = person["state"]
        text = ""
        if (state == "gen_course"):
            text = GetMoneyCourse().get(server, event)
        elif (state == "gen_group"):
            text = GetMoneyGroup().get(server, event)
        elif (state == "gen_secondName"):
            text = GetMoneySecondName().get(server, event)
        elif (state == "gen_mobile"):
            text = GetMoneyMobile().get(server, event)
        elif (state == "gen_active"):
            text = GiveMeMoneyFinal().get(server, event)
        else:
            return False
        if text != "":
            server.send_message(event, text)   
            return True
        return False