"""
Steps:
1. Download intent_list.csv and store in intent_list
2. Download recent_search.csv and store in recent_search
3. all the categories in the recent_search are to be moved to intent_list with a value = 0,<NO REPETITION>
4. Clear data of recent_search.csv.
5. Download noti_action.csv and store in noti_action
6. for every category in noti_action
    --> if action is "YES" -> value of this category in intent_list += 1 <but always less than 1>
    --> if action is "NO" -> value of this category in intent_list -= 1
7. Clear data of noti_action.csv
8. Now in intent_list
    --> remove all the entries where value less than -3
    --> set value of all the entries =0 where value > 0
9. Upload all the edited files
10. remove all downloaded files from local storage.
"""
import os

import requests


class Maintain:

    def __init__(self):
        self.__email_list = []  # this is an instance variable
        self.__intent_list = []
        self.__recent_search = []
        self.__noti_action = []

    def maintain_intent_list(self):
        self.download("https://storage.googleapis.com/ecommercenotify.appspot.com/users.txt", "users.txt")
        for email in self.__email_list:
            self.download(
                "https://storage.googleapis.com/ecommercenotify.appspot.com/users/" + email + "/intent_list.csv",
                "intent_list.csv")
            self.download(
                "https://storage.googleapis.com/ecommercenotify.appspot.com/users/" + email + "/recent_search.csv",
                "recent_search.csv")
            recent_search_header = self.__recent_search[0]
            del self.__recent_search[0]  # remove header
            if self.__recent_search:  # if list not empty
                for element in self.__recent_search:
                    present = False
                    for intent_elememnt in self.__intent_list:
                        if element[0] == intent_elememnt[0]:
                            present = True
                    if not present:
                        self.__intent_list.append([element[0], 0])
                self.__recent_search = [recent_search_header]
                self.write_and_upload(
                    path="https://storage.googleapis.com/ecommercenotify.appspot.com/users/" + email + "/recent_search.csv",
                    upload_file="recent_search.csv",
                    data_list=self.__recent_search)
                os.remove("recent_search.csv")

            self.download(
                "https://storage.googleapis.com/ecommercenotify.appspot.com/users/" + email + "/noti_action.csv",
                "noti_action.csv")

            noti_action_header = self.__noti_action[0]
            del self.__noti_action[0]  # save header
            if self.__noti_action:  # if list not empty
                for element in self.__noti_action:
                    i = 0
                    for intent_element in self.__intent_list:
                        if element[1] == intent_element[0]:  # match category
                            if element[3] == "Yes":
                                if intent_element[1] < 0:
                                    intent_element[1] += 1
                            elif intent_element[1] > -3:
                                intent_element[1] -= 1
                            else:
                                del self.__intent_list[i]  # remove value at index i
                        i += 1
                self.__noti_action = [noti_action_header]
                self.write_and_upload(
                    path="https://storage.googleapis.com/ecommercenotify.appspot.com/users/" + email + "/noti_action.csv",
                    upload_file="noti_action.csv",
                    data_list=self.__noti_action)
                os.remove("noti_action.csv")

            self.write_and_upload(
                path="https://storage.googleapis.com/ecommercenotify.appspot.com/users/" + email + "/intent_list.csv",
                upload_file="intent_list.csv",
                data_list=self.__intent_list)
            os.remove("intent_list.csv")

    def download(self, path, save_as):
        r = requests.get(path)
        for i in r.text.split():
            if save_as == "users.txt":
                if self.__email_list:  # if list not already empty
                    self.__email_list = []
                self.__email_list.append(i)
            elif save_as == "intent_list.csv":
                if self.__intent_list:
                    self.__intent_list = []
                self.__intent_list.append(i)
            elif save_as == "recent_search.csv":
                if self.__recent_search:
                    self.__recent_search = []
                self.__recent_search.append(i)
            elif save_as == "noti_action.csv":
                if self.__noti_action:
                    self.__noti_action = []
                self.__noti_action.append(i)

    def write_and_upload(self, path, upload_file, data_list: list):
        with open(upload_file, "w") as fle:
            for line in data_list:
                str1 = ','.join(line)
                fle.write(str1)
        files = {'file': open(upload_file, "rb")}
        response = requests.post(path, files=files)
        print(response.text)
