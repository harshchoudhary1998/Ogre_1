from pyfcm import FCMNotification

push_service = FCMNotification(
    api_key="AAAA_-yO3Ds:APA91bHZQC8mkZO_duCypk_8FBJeC14szbuP_iFviyCveO13za1MmS3fPm1paWz42EB44_ZbAjbmih7KYF5Lfry0GCD9zLqJD8rlD8pyhUgGh-ANS3oTkIfbw2ol7fJq28s9e8XDJCPF")
token = "epEfc5gn7KM:APA91bF_yKx0YWZUmon46JyEHpd20xYGjLOEFa03FvxtTnZGEU8GvQ9a8stPI1Qsn18QefhfJWDE2_-lTp6G2Cov5y612ZVXeP3ecN1J3woRfRyzTEiGUI7cpihHMArZOGQ2dk22ttzm"
result = push_service.notify_single_device(token, "Hello", "hiiiii")
print(result)

# [6205036741361962480]
# [8748947870327364814]
# with open("user_data.csv", "r") as hour_file:
#     # print(hour_file.read().split()[0])
#     del hour_file.read().split()[0] # remove header
#     print(hour_file.read())
# userdata = open("user_data.csv", "r")
# print(userdata.read().split(",")[0])
#

# data = open("token_id.csv", "r")
# for line in data:
#     print(line)

# str1 = "asi@gmail@@kk@"
# list1 = str1.split("@")
# print(list1)
# list1 = [["Asish"], "", ""]
# header = list1[0]
# del list1[0]
# # list1.remove(["Asish"])
# print(list1)
# print(header)
# import datetime
#
# cur_time = datetime.datetime.now()
# print(cur_time)
# print(cur_time.hour, cur_time.minute)

# import re
#
# x = re.compile("[0-9]")
# y = x.findall("Helllo02027719")
# z = 0
# for k in y:
#     z = z * 10 + int(k)
# print(z)
#
# with open("", 'r+') as f:
#     f.writelines()
#
# str1 = ""
# str1.join()
# #import re
# import math
# print(math.isnan(4))
# #x=re.compile('[a-z]')
# #print(x.search("m234people"))
# # try:
# #     x = int(input())
# #     k = 2/x
# # except ValueError:
# #     print(ValueError)
# # except ZeroDivisionError:
# #     print("ZeroDivisionError")
# #
# # # # with open("examp.txt", "w") as fle:
# # # #     fle.write("abcdefghijkhlm")
# # # #
# # # # with open("examp.txt", "r+") as fle:
# # # #     fle.write("kk")
# # # #
# # # # with open("examp.txt", "w+") as fle:
# # # #     fle.write("ab")
# # # #     print(fle.read())
# # # #
# # # #
# # # # with open("examp.txt", "r") as fle:
# # # #     print(fle.read())
# # # #
# # #
# # # print()
# # #
# # # def fun_a():
# # #     print("x, yx")
# # #
# # # def fun_b():
# # #     print('k')
# # #
# # # print(fun_a(1,2) + fun_b(3))
# # # # print(23/5)
# # #
# # # # def sum(a, b=10):
# # # #     return a+b
# # # #
# # # #
# # # # def sub(a, b=10):
# # # #     return a-b
# # # #
# # # #
# # # # print(sub)
# # # # print(sum)
# # # # result = sum = sub
# # # # print(sum(20), sub(20), result)
# # #
# # # # import requests
# # # #
# # # # list1 = []
# # # # # get user id or folder name of the specific user
# # # # get_tokenid_url = "https://storage.googleapis.com/ecommercenotify.appspot.com/token_id.csv"
# # # # r = requests.get(get_tokenid_url)
# # # # for i in r.text.split():
# # # #     print(i)
# # # # # userid = r.text.rstrip()
# # # # # print(userid)
# # # #
# # # #
# # # # # # class someClass:
# # # # # #     __myName = 'A'
# # # # # #     __myAge = 0
# # # # # #
# # # # # #     def change_data(self, name, age):
# # # # # #         self.__myName = name
# # # # # #         self.__myAge = age
# # # # # #
# # # # # #     def __init__(self, gender):
# # # # # #         self.__myGender = gender
# # # # # #
# # # # # #     def printData(self):
# # # # # #         print(self.__myName, self.__myAge, self.__myGender)
# # # # # #
# # # # # #
# # # # # # obj1 = someClass("M")
# # # # # # obj1.printData()
# # # # # class A:
# # # # #     def __init__(self):
# # # # #         self.x = 1
# # # # #
# # # # # class B():
# # # # #     def display(self):
# # # # #         print(self.x)
# # # # #
# # # # # def test():
# # # # #     obj = B()
# # # # #     obj.display()
# # # # #
# # # # # test()
