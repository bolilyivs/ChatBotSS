from messeges.document_messeges import *
import settings


class DocumentDialog():
    def run(self, state, server, event):
        if (state == "listDocsIsActive"):
            for doc in settings.DOCUMENTS:
                text = eval(doc + "()").get(server, event)
                if text != "":
                    server.send_message(event, text)
                    server.saveUserData(event, "default", "")
                    return True     
            return False
        return False
