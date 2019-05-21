from messeges.document_messeges import *
import settings


class KUGDialog():
    def run(self, person, server, event):
        state = person["state"]
        if (state == "kug"):
            for doc in settings.KUG:
                text = eval(doc + "()").get(server, event)
                if text != "":
                    server.send_message(event, text)
                    server.saveUserData(event, "default", "")
                    return True     
            return False
        return False
