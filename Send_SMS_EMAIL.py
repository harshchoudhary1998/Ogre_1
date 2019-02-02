import smtplib

import requests


# import json


class Send_sms_email:

    def sendPostRequest(self, reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
        req_params = {
            'apikey': apiKey,
            'secret': secretKey,
            'usetype': useType,
            'phone': phoneNo,
            'message': textMessage,
            'senderid': senderId
        }
        return requests.post(reqUrl, req_params)

    def send_email(self, email: str, category: str, message: str):
        s = smtplib.SMTP('smtp.gmail.com', 587)  # creates SMTP session
        s.starttls()  # start TLS for security

        sender_email = "ogreghosts@gmail.com"
        sender_password = "verystrongpassword"
        receiver_email = email

        s.login(sender_email, sender_password)  # Authentication
        # message = "OGREs are testing to send mail to you."  # message to be sent
        s.sendmail(sender_email, receiver_email, category + "\n" + message)  # sending the mail

        s.quit()  # terminating the session

    def send_message(self, mob: str, category: str, message: str):
        URL = 'http://www.way2sms.com/api/v1/sendCampaign'

        response = self.sendPostRequest(URL, 'KM3QG6OS8HZTWIC5B4WOLYUEAMUFFJWZ', 'ZI79PXQWMT3QMG3F', 'stage', mob,
                                        'www.way2sms.com/api/v1/createSenderId', category + "\n" + message)
        print(response.text)


# ******************Send an message(25 messages limit)******************************


# get request

# get response
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# print response if you want

"""
# ******************Send a message(Working but has a very low daily limit)******************************
url = "https://smsapi.engineeringtgr.com/send/"
params = dict(
    Mobile='7726068614',
    Password='strongpassword',
    Key='ogregDr1AaI3YThJu6oeLUkS5xCv',
    Message='Hello my friend',
    To='8426875860')

resp = requests.get(url, params)
print(resp, resp.text)
"""
"""
# ********************Send an email********************************

s = smtplib.SMTP('smtp.gmail.com', 587)  # creates SMTP session
s.starttls()  # start TLS for security

sender_email = "ogreghosts@gmail.com"
sender_password = "verystrongpassword"
receiver_email = "akhc147@gmail.com"

s.login(sender_email, sender_password)  # Authentication
message = "OGREs are testing to send mail to you."  # message to be sent
s.sendmail(sender_email, receiver_email, message)  # sending the mail

s.quit()  # terminating the session
"""

# ================Not working bcoz sinch asked for $2.4=======================
# from sinchsms import SinchSMS
#
# number = '8426875860'
# app_key = '09082229-9c79-4153-8da8-e59efb0b467c'
# app_secret = 'Nl960gDLeka7U/esSuhByw=='
#
# # enter the message to be sent
# message = 'Hello Message!!!'
#
# client = SinchSMS(app_key, app_secret)
# print("Sending '%s' to %s" % (message, number))
#
# response = client.send_message(number, message)
# message_id = response['messageId']
# response = client.check_status(message_id)
#
# # keep trying unless the status retured is Successful
# while response['status'] != 'Successful':
#     print(response['status'])
#
#     response = client.check_status(message_id)
#
# print(response['status'])

"""
1. download users.txt
2. download intent_list.csv for this user
"""
