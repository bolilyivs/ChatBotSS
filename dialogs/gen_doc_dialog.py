from messeges.document_messeges import *

class GenDocDialog():
    def run(self, state, server, event):
        if (state == "gen_course"):
            GetMoneyCourse().get(server, event))
        elif (state == "gen_group"):
            GetMoneyGroup().get(server, event))
        elif (state == "gen_secondName"):
            GetMoneySecondName().get(server, event))
        elif (state == "gen_mobile"):
            GetMoneyMobile().get(server, event))
        elif (state == "gen_active"):
            GiveMeMoneyFinal().get(server, event))
        else:
            return False
        return True