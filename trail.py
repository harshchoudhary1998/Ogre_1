import requests

list1 = []
# get user id or folder name of the specific user
get_tokenid_url = "https://storage.googleapis.com/ecommercenotify.appspot.com/token_id.csv"
r = requests.get(get_tokenid_url)
for i in r.text.split():
    print(i)
# userid = r.text.rstrip()
# print(userid)


# # class someClass:
# #     __myName = 'A'
# #     __myAge = 0
# #
# #     def change_data(self, name, age):
# #         self.__myName = name
# #         self.__myAge = age
# #
# #     def __init__(self, gender):
# #         self.__myGender = gender
# #
# #     def printData(self):
# #         print(self.__myName, self.__myAge, self.__myGender)
# #
# #
# # obj1 = someClass("M")
# # obj1.printData()
# class A:
#     def __init__(self):
#         self.x = 1
#
# class B():
#     def display(self):
#         print(self.x)
#
# def test():
#     obj = B()
#     obj.display()
#
# test()
