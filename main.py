# -*- coding: utf-8 -*-

from wox import Wox
import pyperclip
import uuid


class Exchange(Wox):

    def query(self, query):
        results = []
        results.append({
            "Title": "生成UUID",
            "SubTitle": self.generateUUID(),
            "IcoPath": "./Images/app.png",
            "JsonRPCAction": {
                "method": "copyToClipBoard",
                "parameters": [self.uuid_str],
                "dontHideAfterAction": False
            }
        })
        return results

    def generateUUID(self):
        uuid_str = str(uuid.uuid4())
        self.uuid_str = uuid_str
        uuid.NAMESPACE_OID
        return uuid_str

    def copyToClipBoard(self, str):
        pyperclip.copy(str)


if __name__ == "__main__":
    Exchange()
