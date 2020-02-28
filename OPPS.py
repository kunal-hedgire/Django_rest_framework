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


# def find(name,path):
#     # print(len(path))
#     # if len(path) == 0:
#     #     print("empty dir")
#     # else:
#     #     print("not empty dir")
#     for root, dirs,files in os.walk(path):
#         if name in files:
#             return os.path.join(root, name)
#     else:
#        print("NO file is there")
#
#
# name = 'myfile.txt'
# path = "D:\studProduce\django_rest_framework"
# a = find(name, path)
# print(a)


# def read_file_line():
#     with open("D:\studProduce\django_rest_framework\StudProduce\myfile.txt"
#               ) as file:
#         for i, line in enumerate(file, 1):
#             if i == 23:
#                 break
#         print(line)
# read_file_line()

def additionofnumber():
    sum = 0
    with open("D:\studProduce\django_rest_framework\StudProduce\Examples\myfile.txt",
              'r')as file:
        sum = 0
        for i in file:
            try:
                num = int(i)
                # import pdb;pdb.set_trace()
                if num%2==1:
                    print(i)

            except:
                continue


        # for i in file:
        #     try:
        #         num = int(i)
        #         sum += num
        #
        #     except ValueError:
        #         print('{} is not a number'.format(i))
        #
        # print(sum)


additionofnumber()


#
# class A(object):
#     def dispaly(self):
#         print("A")
#
#
# class B(A):
#     def dispaly(self):
#         print("B")
#
#
# class C(A):
#     # def dispaly(self):
#     #     print("C")
#     pass
#
# class D(C,B):
#     pass
#
# c1 = D()
# c1.dispaly()
#
#
# def add_digits():
#     num = 231
#     sum = 1
#     while num > 0:
#         rem = num % 10
#
#         sum = sum * rem
#         num = num // 10
#     print(sum)
#
#
# add_digits()