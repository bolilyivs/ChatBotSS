from messeges.document_messeges import *
import settings


class Documents():
    def run(self, state, server, event):
        if (state == "listDocsIsActiv"):
            for doc in settings.DOCUMENTS:
                if (eval(doc + "()").get(server, event)):
                    return True
            return False
        return False
