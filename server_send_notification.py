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
    # --> token_id,category,message,time_to_send_at
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
            fle.write(header)
        for i in data_list:
            i = i.split(",")
            i[3] = i[3].split(":")
            print("This is i", i)
            if (int(i[3][0]) == cur_time.hour) and (int(i[3][1]) < cur_time.minute + 3):
                # send now and delete this row
                print(i[0])  # print token id
                try:
                    result = push_service.notify_single_device(i[0], str(i[2]), str(i[1]))
                    print(result)
                except ConnectionError:
                    print("Sorry! Firebase server has terminated connection with the mobile device.")
                    print(ConnectionError)
            else:
                with open(save_as, 'a') as fle:
                    fle.write(",".join(i))
        # upload this file
        files = {'file': open(save_as, "rb")}
        response = requests.post(path, files=files)
        print(response.text)
        files["file"].close()
        os.remove(save_as)
