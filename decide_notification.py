# Author : Asish Kumar
import datetime

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

    def whom_to_send(self, message, category, validity: list):  # validity is [hour, minute]
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
                self.when_to_send(email=email, validity=validity)

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

    def when_to_send(self, email, validity):
        # use ML to decide best time to send the notification to the user
        """
        1. download active_hours.csv
        2. leave header and count number of rows, if < 7:
                                                --> send NOW
                                                else:
                                                --> need to decide - go to step 3
        3. do not include last column
        4. calculate sum of all the row elements column wise and store in a list
        5. now get the maximum nearest value from the list based on current time but not exceeding validity time of the notification
        6. download token_id.csv of the user
        7. now download the noti_to_send.csv file from outside users folder in the firebase
        8. add all the token_ids of the current user in the following format:
                --> token_id,category,message,time_to_send_at
        9. upload back the noti_to_send.csv file with updated values

        """

        self.download("https://storage.googleapis.com/ecommercenotify.appspot.com/users/" + email + "/active_hours.csv",
                      "active_hours.csv")
        hour_list = []
        sum_list = [0] * 24
        with open("active_hours.csv", "r") as hour_file:
            for i in hour_file:
                hour_list.append(i)
            print(hour_list)
            hour_list.remove(hour_list[0])  # remove header
            print(hour_list)
            for i in hour_list:
                del hour_list[24]  # remove last column
            print(hour_list)
            # calculate sum column wise
            for i in hour_list:
                for j in range(0, 24):
                    sum_list[j] += i[j]
            cur_time = datetime.datetime.now()
            time_list = [cur_time.hour, cur_time.minute]
