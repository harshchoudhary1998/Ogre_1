# Author: Asish Kumar

"""
1. Admin enters text, title and chooses category of notification
2. This script generates a notification and sends to decide_notification.py script
3. which decides the specific users to whom this notification needs to be sent based on their intent.
"""

message = input("Enter message: ")
categoryies = {1: "Cloths",
               2: "Electronics",
               3: "Beauty and cosmetic",
               4: "Study related"}
print(categoryies)
category = int(input("Enter your category number: "))
print("Enter validity time as hour then minute: ")
validity = [int(input()), int(input())]

if category in categoryies.keys():
    from decide_notification import Decide

    d = Decide()
    d.whom_to_send(message=message, category=categoryies[category], validity=validity)
else:
    print("\n########Invalid category number.###########")

#
