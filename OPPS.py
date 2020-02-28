# class Employee:
#
#     def __init__(self):
#         self.name = "kunal"
#         self.number = 90
#         self.c = 100
#
#     def t1(self):
#         # self.c = 100
#         pass
#
# e = Employee()
# e1 = Employee()
# e.t1()
# del e.c
# print(e1.__dict__)
# print(e.__dict__)


# def getDuplicatesWithCount(listOfElems):
#
#     dictOfElems = {}
#
#     for elem in listOfElems:
#             if elem in dictOfElems:
#                 dictOfElems[elem] += 1
#             else:
#                 dictOfElems[elem] = 1
#
#     dictOfElems = {key:value for key,value in dictOfElems.items() if value > 1}
#     print(dictOfElems)
#
# listOfElems = [1,2,1,1,1,3,6,4,5,5,5,5,6,6]
# dictOfElems = getDuplicatesWithCount(listOfElems)

# for key, value in dictOfElems.items():
#     print(key, ' :: ', value)


# str1 = "{({})}"
# str2 = str1.split()
# # print(type(str2))
# for i in str2:
#     if str2[0] == str2[-1]:
#         str2.remove(str2[0])
#         str2.remove(str2[-1])
#
#     else:
#         print("mismatch pattern")
#
# print()


import os
# file_path = 'myfile.txt'
# print(os.path.getsize(file_path))
# if os.stat(file_path).st_size == 0:
#     print("File is empty")
#
# else:
#     print("File is not empty")


def find(name,path):
    # print(len(path))
    # if len(path) == 0:
    #     print("empty dir")
    # else:
    #     print("not empty dir")
    for root, dirs,files in os.walk(path):
        if name in files:
            os.remove(name)
            print("removed successfully")
            # return os.path.join(root, name)
        else:
           print("NO file is there")


name = 'xyz.py'
path = "D:\studProduce\django_rest_framework"
a = find(name, path)
print(a)




