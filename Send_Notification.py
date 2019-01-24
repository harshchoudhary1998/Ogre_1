from txfcm import TXFCMNotification
from twisted.internet import reactor

push_service = TXFCMNotification(api_key="AAAA_-yO3Ds:APA91bHZQC8mkZO_duCypk_8FBJeC14szbuP_iFviyCveO13za1MmS3fPm1paWz42EB44_ZbAjbmih7KYF5Lfry0GCD9zLqJD8rlD8pyhUgGh-ANS3oTkIfbw2ol7fJq28s9e8XDJCPF")

# server key in the cloud messaging tab is the api key
# Your api-key can be gotten from:  https://console.firebase.google.com/u/3/project/<your_project_name>/settings/cloudmessaging/android:com.allandroidprojects.ecomsample
# Send to multiple devices by passing a list of ids.
registration_ids = ["fr748vXjdFg:APA91bFGrkqq-QiMRn4eDsZe8RyurfTqEzjnaGFi91J3uKNAoLzjqQQVJyRg04fSlxu5MhqPAwl-544Yo0cctuY6OwtR1jTjwZqXpc0B2PXyAD9qCNv9l60LV0L9jIO3ocN9tMKH013i"]
message_title = "Uber update"
message_body = "Hope you're having fun this weekend, don't forget to check today's news"
df = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)


def got_result(result):
    print(result)


df.addBoth(got_result)
reactor.run()
