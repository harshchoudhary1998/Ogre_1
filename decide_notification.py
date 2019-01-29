# Author : Asish Kumar
import requests

"""
1. download users.txt
2. store all emails in a list-->email_list
3. now for each email in email_list
    --> download /users/<email>/intent_list.csv
    --> and download /users/<email>/token_ids.txt
4. if category in intent_list
    --> store all token_ids of the user in a list and call send_notification(token_ids, message, category)
"""


class Decide:
    def __init__(self):
        self.__email_list = []
        self.__intent_list = []
        self.__token_ids = []

    def whom_to_send(self, message, category):
        print(message, category)
        self.download("https://storage.googleapis.com/ecommercenotify.appspot.com/users.txt", "users.txt")
        for email in self.__email_list:
            self.download(
                "https://storage.googleapis.com/ecommercenotify.appspot.com/users/" + email + "/intent_list.csv",
                "intent_list.csv")
            self.download(
                "https://storage.googleapis.com/ecommercenotify.appspot.com/users/" + email + "/token_ids.txt",
                "token_ids.txt")
            if category in self.__intent_list:
                # we have to send this notification to this user
                self.when_to_send()

    def download(self, path, save_as):
        r = requests.get(path)
        for i in r.text.split():
            if save_as == "users.txt":
                self.__email_list.append(i)
            elif save_as == "intent_list.csv":
                self.__intent_list.append(i)
            elif save_as == "token_ids.txt":
                self.__token_ids.append(i)
            with open(save_as, 'w') as fle:
                fle.writelines(i)

    def when_to_send(self):
        # use ML to decide best time to send the notification to the user
        pass
