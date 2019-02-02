# Author : Asish Kumar
import datetime

import requests
from pyfcm import FCMNotification

push_service = FCMNotification(
    api_key="AAAA_-yO3Ds:APA91bHZQC8mkZO_duCypk_8FBJeC14szbuP_iFviyCveO13za1MmS3fPm1paWz42EB44_ZbAjbmih7KYF5Lfry0GCD9zLqJD8rlD8pyhUgGh-ANS3oTkIfbw2ol7fJq28s9e8XDJCPF")

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

    def whom_to_send(self, message, category,
                     validity: list):  # validity is [number of hours left, number of minute left]
        print(message, category)
        self.download("https://storage.googleapis.com/ecommercenotify.appspot.com/users.txt", "users.txt")
        for email in self.__email_list:
            self.download(
                "https://storage.googleapis.com/ecommercenotify.appspot.com/users/" + email + "/intent_list.csv",
                "intent_list.csv")
            self.download(
                "https://storage.googleapis.com/ecommercenotify.appspot.com/users/" + email + "/token_id.csv",
                "token_id.csv")
            for element in self.__intent_list:
                if category == element[0]:
                    # we have to send this notification to this user
                    self.when_to_send(email=email, category=category, message=message, validity=validity)

    def download(self, path, save_as):
        r = requests.get(path)
        for i in r.text.split():  # here r.text.split() is a list of strings where each string is a line in the file
            if save_as == "users.txt":
                self.__email_list = r.text.split()
                break
            elif save_as == "intent_list.csv":
                if i == "Category,Value":
                    continue
                self.__intent_list.append([i.split(",")[0], int(i.split(",")[1])])
            elif save_as == "token_id.csv":
                self.__token_ids.append(i)
            with open(save_as, 'w') as fle:
                fle.write(i + "\n")

    def when_to_send(self, email, category, message, validity):
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
        6. download token_id.txt of the user
        7. now download the noti_to_send.csv file from outside users folder in the firebase
        8. add all the token_ids of the current user in the following format:
                --> token_id,category,message,time_to_send_at,email,mob_no
        9. upload back the noti_to_send.csv file with updated values

        """

        self.download("https://storage.googleapis.com/ecommercenotify.appspot.com/users/" + email + "/active_hours.csv",
                      "active_hours.csv")
        hour_list = []
        hour_list1 = []
        sum_list = [0] * 24
        with open("active_hours.csv", "r") as hour_file:
            for i in hour_file:
                hour_list1.append(i.split(","))

            hour_list1.remove(hour_list1[0])  # remove header
            print(hour_list1)
            for i in hour_list1:
                print(i)
                hour_list.append([int(k) for k in i])
            print(hour_list)
            # print(hour_list)
            for i in hour_list:
                del i[24]  # remove last column
            print(hour_list)
            # calculate sum column wise
            for i in hour_list:
                for j in range(0, 24):
                    sum_list[j] += i[j]
            cur_time = datetime.datetime.now()
            time_list = [cur_time.hour, cur_time.minute]
            expiry_min = (time_list[1] + validity[1]) % 60
            expiry_hrs = (time_list[0] + validity[0] + ((time_list[1] + validity[1]) // 60)) % 24
            print(expiry_hrs)
            # expiry_hrs bj k expiry_min tk to bhejna hi pdega
            if expiry_hrs < time_list[0]:
                maximum1 = max(sum_list[time_list[0]:24])
                maximum2 = max(sum_list[0:expiry_hrs + 1])
                maximum = max([maximum1, maximum2])
            elif expiry_hrs == time_list[0]:
                maximum = sum_list[expiry_hrs]
            else:
                maximum = max(sum_list[time_list[0]:expiry_hrs])

            i = time_list[0]
            while (sum_list[i] != maximum) and (i <= 23):
                i += 1
            if i > 23:
                i = 0
                while (sum_list[i] != maximum) and (i <= expiry_hrs):
                    i += 1
            # i holds the hrs value at which we have to send this notification
            self.download(
                "https://storage.googleapis.com/ecommercenotify.appspot.com/users/" + email + "/token_id.csv",
                "token_id.csv")
            token_file = open("token_id.csv", "r")

            if i == time_list[0]:
                # send now
                for token in token_file:
                    print(id)
                    # token = "epEfc5gn7KM:APA91bF_yKx0YWZUmon46JyEHpd20xYGjLOEFa03FvxtTnZGEU8GvQ9a8stPI1Qsn18QefhfJWDE2_-lTp6G2Cov5y612ZVXeP3ecN1J3woRfRyzTEiGUI7cpihHMArZOGQ2dk22ttzm"
                    print(token)
                    result = push_service.notify_single_device(token.split(",")[0], category, message)
                    # message_email also need to be checked and send
                    print(result)
            else:
                # update in file
                self.download(
                    "https://storage.googleapis.com/ecommercenotify.appspot.com/users/" + email + "/userdata.csv",
                    "userdata.csv")
                userdata = open("userdata.csv", "r")
                mobile_number = userdata.read().split()[0]

                self.download("https://storage.googleapis.com/ecommercenotify.appspot.com/noti_to_send.csv",
                              "noti_to_send.csv")
                # --> token_id,category,message,time_to_send_at,email,mobile_number

                for line in token_file:
                    with open("noti_to_send.csv", "a") as noti_to_send_file:
                        noti_to_send_file.write(
                            ",".join([line.split(",")[0], category, message, i, email, mobile_number]))
                files = {'file': open("noti_to_send.csv", "rb")}
                response = requests.post("https://storage.googleapis.com/ecommercenotify.appspot.com/noti_to_send.csv",
                                         files=files)
                print(response.text)
            token_file.close()

#
# obj = Decide()
# obj.whom_to_send("message", "Electronics", [00, 11])
