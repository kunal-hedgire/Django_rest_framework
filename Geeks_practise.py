# price = int(input("Enter the grand total: "))
# dis = int(input("Enter the discount percentage: "))
#
# dis = dis / 100
# new_price = price * dis
# print(price - new_price)


# Simple interest

# principle = int(input("Enter the principle: "))
# interest = int(input("Enter the interest: "))
# time = int(input("Enter the unit of time: "))
#
# Simple_interest = (principle * interest * time) / 100
#
# print(Simple_interest)

# Fab series
# terms = int(input("Enter the terms: "))
# n1 = 0
# n2 = 1
# count = 0
#
# if terms <= 0:
#     print("wrong input")
#     exit(1)
#
# elif terms == 1:
#     print(0)
#
# else:
#     while count < terms:
#         print(n1)
#         nth = n1 + n2
#         n1 = n2
#         n2 = nth
#         count += 1

# def fab(n):
#     # terms = int(input("Enter the terms: "))
#     if n < 0:
#         print("Wrong input")
#
#     elif n == 1:
#         return 0
#
#     elif n == 2:
#         return 1
#
#     else:
#         return fab(n-1) + fab(n-2)
#
#
# print(fab(9))
# import math
#
# def perfect_sqr(n):
#     x = int(math.sqrt(n))
#     return x*x == n
#
# def fab_num(num):
#     return perfect_sqr(5*num*num - 4) or perfect_sqr(5*num*num + 4)
#
# if fab_num(8):
#     print("fab num")
#
# else:
#     print("not fab num")

#
# def larger_number(arr):
#
#     max = arr[0]
#     max1 = arr[1]
#     for i in range(len(arr)):
#         if arr[i] > max:
#             max = arr[i]
#     return max
#
# arr = [20, 10, 20, 4, 100]
# ans = larger_number(arr)
# print(ans)


def second_larger_number(arr):

    max = arr[0]
    max1 = arr[1]

    for i in range(len(arr)):
        if max1 > max:
            max1 = max
            max = arr[i]
        else:
            max1 = arr[i]
    print(max1)


# arr = [10, 20, 45, 4, 20]
# second_larger_number(arr)

def find_snd_max(arr):
    first = 0
    snd = 0
    for num in arr:
        if num >= first:
            snd = first
            first = num
    return snd

arr = [44,10, 20, 45, 4, 20]
a = find_snd_max(arr)
print(a)
# def rverselist(arr, start, end):
#     temp = arr[start]
#     arr[start] = arr[end]
#     arr[end] = temp
#     start += 1
#     end -= 1
#     print(arr)
#
#
# def left_rotate(arr,d):
#     n = len(arr)
#     rverselist(arr, 0, d - 1)
#     rverselist(arr, d, n - 1)
#     rverselist(arr, 0, n - 1)
#
#
# def print_arr(arr):
#     for i in range(len(arr)):
#         print(arr[i],)
#
# arr = [15, 20, 34, 45, 50, 65, 70]
# left_rotate(arr, 2) # Rotate array by 2
# print_arr(arr)


# def find_remonder(arr,n):
#     mul = 1
#     for i in range(len(arr)):
#         mul = (mul * (arr[i] % n)) % n
#
#     return mul % n
#
#
# arr = [ 100, 10, 5, 25, 35, 14 ]
# n = 11
# print(find_remonder(arr,n))

#
# def ismono(arr):
#     return (all(arr[i] <= arr[i] for i in range(len(arr) - 1) or
#                 all(arr[i] >= arr[i] for i in range(len(arr) - 1))))
#
#
# print(ismono([5, 4, 3, 3]))


# list1 = [10,20,30,40,50]
# print(list1)
# list1[0], list1[-1] = list1[-1], list1[0]
# print(list1)
#
# def nearest_number(num1, num2):
#
#     q = int(num1 / num2)
#
#     n1 = q * num2
#     import pdb;pdb.set_trace()
#     if (num1 * num2) > 0:
#         n2 = num2 * (q + 1)
#
#     else:
#         n2 = num2 * (q - 1)
#
#     if (abs(num2 - n1) < abs(num2 - n2)):
#         return n1
#     return n2
#
# n = -13; m = 4
# print(nearest_number(n, m))

# def palindrome_number(num):
#     return str(num) == str(num)[::-1]
#
# if palindrome_number(999):
#     print("number is palindrome")
#
# else:
#     print("Not")

# class Singleton:
#     __instance = None
#
#     def __init__(self):
#         if Singleton.__instance != None:
#             raise Exception ("This class is singleton")
#
#         else:
#             Singleton.__instance = self
#
#     @staticmethod
#     def get_instance(self):
#         if Singleton.__instance == None:
#             Singleton()
#         return Singleton.__instance
#
# s = Singleton()
# print(s)


# def sum_of_num(num):
#
#     sum_num = 0
#
#     while num > 0:
#         rem = num % 10
#         sum_num = sum_num + rem
#         num = num // 10
#     print("the sum of number:", sum_num)
#     b = palindrome(sum_num)
#     print(b)
#
# def palindrome(sum_num):
#     return str(sum_num) == str(sum_num)[::-1]
#
#
# num = int(input("Enter the number: "))
# a = sum_of_num(num)
#

# def num_rev(num):
#     return str(num)[::-1]
#
#
# num = int(input("Enter the number: "))
# print(num_rev(num))


# num = int(input("Enter the number: "))
# fact = 1
# for i in range(1, num+1):
#     fact = fact * i
# print(fact)


# def Largest_Prime_Factor(n):
#     prime_factor = 1
#     i = 2
#
#     while i <= n / i:
#         if n % i == 0:
#             prime_factor = i
#             n /= i
#         else:
#             i += 1
#
#     if prime_factor < n:
#         prime_factor = n
#
#     return prime_factor
#
#
# print(Largest_Prime_Factor(6))
'''
def perfect_number(num):
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            print(i)
            sum = sum + i

    if num == sum:
        print("the",num,"is perfect number")

    else:
        print("the", num, "is not perfect number")


num = int(input("Enter the number: "))
perfect_number(num)
'''


# def prime_number(num):
#     list1 = []
#     if num > 1:
#         for item in range(2,num):
#             if num % item == 0:
#                 print("not prime number")
#                 break
#         else:
#             print("prime number")
#
#     else:
#         print("num is not prime")
#
#
# num = int(input("Enter the number: "))
# prime_number(num)


# import math
#
# def find_square(arr):
#     for i in arr:
#         sr = math.sqrt(i)
#         if sr - math.floor(sr) == 0:
#             print(sr)
#
# arr = [9, 3, 4, 10, 16]
# # print(find_square(arr))
# find_square(arr)

# def find_three_div(arr):
#     temp = {}
#     for i in range(0, len(arr)):
#         num = arr[i]
#         for j in range(2, num):
#             if arr[i] % j == 0:
#                 try:
#                     temp[num] +=1
#                 except KeyError:
#                     temp[num] = 1
#     print(temp)
#
#
# arr = [7, 10, 12]
# find_three_div(arr)

#
# class Point:
#
#     # Structure of a point in 2D space
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     # A utility function to find square of
#
#
# # distance from point 'p' to point 'q'
# def distSq(p, q):
#     return (p.x - q.x) * (p.x - q.x) + (p.y - q.y) * (p.y - q.y)
#
#
# # This function returns true if (p1, p2, p3, p4)
# # form a square, otherwise false
# def is_square(p1, p2, p3, p4):
#     d2 = distSq(p1, p2)  # from p1 to p2
#     d3 = distSq(p1, p3)  # from p1 to p3
#     d4 = distSq(p1, p4)  # from p1 to p4
#
#     # If lengths if (p1, p2) and (p1, p3) are same, then
#     # following conditions must be met to form a square.
#     # 1) Square of length of (p1, p4) is same as twice
#     # the square of (p1, p2)
#     # 2) Square of length of (p2, p3) is same
#     # as twice the square of (p2, p4)
#
#     if d2 == d3 and 2 * d2 == d4 and \
#             2 * distSq(p2, p4) == distSq(p2, p3):
#         return True
#
#     # The below two cases are similar to above case
#     if d3 == d4 and 2 * d3 == d2 and \
#             2 * distSq(p3, p2) == distSq(p3, p4):
#         return True
#
#     if d2 == d4 and 2 * d2 == d3 and \
#             2 * distSq(p2, p3) == distSq(p2, p4):
#         return True
#
#     return False
#
#
# # Driver Code
# if __name__ == "__main__":
#     p1 = Point(20, 10)
#     p2 = Point(10, 20)
#     p3 = Point(20, 20)
#     p4 = Point(10, 10)
#
#     if is_square(p1, p2, p3, p4):
#         print('Yes')
#     else:
#         print('No')


# def check_power(x, y):
#     power = x * x * x
#     if power == y:
#         print(y, "is power of", x)
#
#     else:
#         print(y, "is not power of", x)


# check_power(1,1)


# def clockangles(hour, minute):
#     return abs((hour * 30 + minute * 0.5) - (minute * 6))
#
#
# a = clockangles(3, 30)
# print(a)

# import datetime
# import calendar
#
# def find_day(date):
#     born = datetime.datetime.strptime(date,'%d %m %Y').weekday()
#     return calendar.day_name[born]

# date = '25 06 1993'
# a = find_day(date)
# print(a)

# import sys
#
#
# class ArrayOperation:
#     def __init__(self, item):
#         self.item = item
#         self.arr = []
#
#     def input_user(self):
#         choose = input("Enter your choice:"
#                        "1. Insert item to array:"
#                        "2. search element from array:"
#                        "3. remove element from array:"
#                        "4. exit")
#
#         if choose == 1:
#             self.insert_array(self.item)
#         elif choose == 2:
#             self.search_element()
#         elif choose == 3:
#             self.remove_array()
#         elif choose == 'exit':
#             sys.exit(0)
#
#         else:
#             print("wrong input!!!try again")
#
#     def insert_array(self):
#
#         self.arr.append(self.item)
#         print(self.arr)
#
#     def remove_array(self):
#         self.arr.remove(self.item)
#         print(self.arr)
#
#     def search_element(self):
#         for i,j in enumerate(self.arr):
#             if i == self.item:
#                 print(i,"is in array at position",j)
#
#             else:
#                 print("element is not in array")
#
#
#
#
# a = ArrayOperation()


# list1 = [1,2,3,4,5,6]
#
# # print(list1[::2])
#
# for i,index in enumerate(list1):
#     # print(index,i)
#     if i% 2 == 0:
#         print(index)






