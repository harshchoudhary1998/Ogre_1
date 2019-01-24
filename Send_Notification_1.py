# Author: Asish Kumar
# Working Correctly
from pyfcm import FCMNotification
import datetime

curTime = datetime.datetime.now()

push_service = FCMNotification(api_key="AAAA_-yO3Ds:APA91bHZQC8mkZO_duCypk_8FBJeC14szbuP_iFviyCveO13za1MmS3fPm1paWz42EB44_ZbAjbmih7KYF5Lfry0GCD9zLqJD8rlD8pyhUgGh-ANS3oTkIfbw2ol7fJq28s9e8XDJCPF")

# OR initialize with proxies

"""
proxy_dict = {
    "http"  : "http://127.0.0.1",
    "https" : "http://127.0.0.1",
}
"""
#push_service = FCMNotification(api_key="AIzaSyAoGpvav8p6HK_Jak6vejS8OP9vMmYhMKk", proxy_dict=proxy_dict)

# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

registration_id = "fr748vXjdFg:APA91bFGrkqq-QiMRn4eDsZe8RyurfTqEzjnaGFi91J3uKNAoLzjqQQVJyRg04fSlxu5MhqPAwl-544Yo0cctuY6OwtR1jTjwZqXpc0B2PXyAD9qCNv9l60LV0L9jIO3ocN9tMKH013i"
message_title = "Python__N"
message_body = "Hi time is:"+str(curTime)
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

print(str(datetime.datetime.now()))
print(result)

# Send to multiple devices by passing a list of ids.
# registration_ids = ["<device registration_id 1>"]
# message_title = "Uber update"
# message_body = "Hope you're having fun this weekend, don't forget to check today's news"
# result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)
#
# print(result)

