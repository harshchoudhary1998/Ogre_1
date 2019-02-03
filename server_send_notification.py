"""
1. Download noti_to_send.csv
2. for every row in it check if time == current_time
                            --> read category,message and send this notification to the token id
                            --> remove this row from the file and re-upload it
                            else:
                                --> repeat from start
"""
import datetime
import os

import requests
from pyfcm import FCMNotification

push_service = FCMNotification(
    api_key="AAAA_-yO3Ds:APA91bHZQC8mkZO_duCypk_8FBJeC14szbuP_iFviyCveO13za1MmS3fPm1paWz42EB44_ZbAjbmih7KYF5Lfry0GCD9zLqJD8rlD8pyhUgGh-ANS3oTkIfbw2ol7fJq28s9e8XDJCPF")
num = 0
while True:
    if datetime.datetime.now().hour == 12 or datetime.datetime.now().hour == 00:
        from maintain_intent_list import Maintain

        obj1 = Maintain()
        obj1.maintain_intent_list()

    list1 = []
    # --> token_id,category,message,time_to_send_at,email,mob_no
    print("INSIDE WHILE TRUE======================================================")
    cur_time = datetime.datetime.now()

    path = "https://storage.googleapis.com/ecommercenotify.appspot.com/noti_to_send.csv"
    save_as = "noti_to_send.csv"
    r = requests.get(path)
    print(num, "REQUESTS****************************************************************")
    num += 1
    data_list = r.text.split()
    header = data_list[0]
    del data_list[0]
    go_ahead = False
    for j in data_list:
        j = j.split(",")
        j[3] = j[3].split(":")
        if (int(j[3][0]) == cur_time.hour) and (int(j[3][1]) < cur_time.minute + 3):
            go_ahead = True

    if go_ahead:
        with open(save_as, 'w') as fle:
            fle.write(header + "\n")
        for i in data_list:
            i = i.split(",")
            print("This is i", i)
            if (int(i[3].split(":")[0]) == cur_time.hour) and (int(i[3].split(":")[1]) < cur_time.minute + 3):
                # send now and skip this row in rewriting
                email_message_send = True
                for item in list1:
                    if item[1:] == i[1:]:
                        # do not send email and message
                        email_message_send = False
                if email_message_send:
                    list1.append(i)
                    intent_file = requests.get(
                        "https://storage.googleapis.com/ecommercenotify.appspot.com/users/" + i[4] + "/intent_list.csv")
                    intent_file_data = intent_file.text.split()
                    from Send_SMS_EMAIL import Send_sms_email
                    s = Send_sms_email()

                    for item in intent_file_data:
                        if i[1] == item.split(",")[0]:
                            if int(item.split(",")[1]) == 0:
                                # send email and message
                                s.send_email(email=i[4], category=i[1], message=i[2])
                                s.send_message(mob=i[5], category=i[1], message=i[2])
                            elif int(item.split(",")[1]) == -1:
                                # send email only
                                s.send_message(mob=i[5], category=i[1], message=i[2])
                            # else by default push notification is already being sent

                print(i[0])  # print token id
                try:
                    result = push_service.notify_single_device(i[0], str(i[2]), str(i[1]))
                    # message_email check and send
                    print(result)
                except:
                    print("Sorry! Firebase server has terminated connection with the mobile device.")

            else:
                with open(save_as, 'a') as fle:
                    fle.write(",".join(i) + "\n")
        # upload this file
        files = {'file': open(save_as, "rb")}
        response = requests.post(path, files=files)
        print(response.text)
        files["file"].close()
        os.remove(save_as)
