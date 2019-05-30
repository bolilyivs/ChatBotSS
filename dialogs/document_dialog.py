from messages.document_messages import *
import settings


class DocumentDialog():
    def run(self, person, server, event):
        state = person["state"]
        if (state == "listDocsIsActive"):
            for doc in settings.DOCUMENTS:
                text = eval(doc + "()").get(server, event)
                if text != "":
                    server.send_message(event, text)
                    server.saveUserData(event, "default", "")
                    return True     
            return False
        return False
