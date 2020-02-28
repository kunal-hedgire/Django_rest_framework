# def carry_number(x, y):
#   ctr = 0
#   if(x == 0 and y == 0):
#     return 0
#   z = 0
#   for i in reversed(range(10)):
#       z = x%10 + y%10 + z
#       if z > 9:
#         z = 1
#       else:
#         z = 0
#       ctr += z
#       x //= 10
#       y //= 10
#
#   if ctr == 0:
#     return "No carry operation."
#   elif ctr == 1:
#     return ctr
#   else:
#     return ctr
# print(carry_number(786, 457))
# print(carry_number(5, 6))

# number1 = int(input('Number #1: '))
# number2 = int(input('Number #2: '))
# l = len(str(number1))
# l1 = len(str(number2))
# print()
#
# def addition():
#     print(' ',max(number1, number2))
#     print('+')
#     print(' ',min(number1, number2))
#     print('-'*(max(l, l1)+2))
#     print('  ')
#     print(' ', number1+number2)
#
#
# def carrie():
#     num1 = str(number1)
#     num2 = str(number2)
#     carry = 0
#     carries = 0
#     c1 = l
#     c2 = l
#     if l < l1:
#         while c1 < l1:
#             num1 = '0' + num1
#             c1 += 1
#     if l1 < l:
#         while c2 < l:
#             num2 = '0' + num2
#             c2 += 1
#     i = c1
#     while i > 0:
#         if (int(num1[i-1])+int(num2[i-1])+carry > 9):
#             carry = 1
#             carries += 1
#         else:
#             carry = 0
#         i -= 1
#     return carries
#
#
# addition()
# print()
# print('Carries : ',carrie())


# def remove_nth(list, word , n):
#     count = 0
#
#     for i in range(len(list)):
#         if list[i] == word:
#             count += 1
#
#         if count == n:
#             del list[i]
#             return True
#
#
# list = [10, 20, 30, 10, 40, 10, 20, 10]
# word = 10
# N = 3
#
# flag = remove_nth(list, word, N)
#
# if (flag == True):
#     print("Updated list is: ", list)
# else:
#     print("Item not Updated")

# def reverse(num):
#     reverse= 0
#     while num:
#         reverse= reverse*10 + num%10
#         num= num//10
#     return reverse
#
# num= int(input("Enter any number :- "))
# if num==reverse(num):
#     print ("Already palindrome.")
# else:
#     while True:
#         num+= 1
#         if num==reverse(num):
#             print ("Next palindrome is : %s"%num)
#             break


# def rearrange(arr, n):
#     # Auxiliary array to hold modified array
#     temp = n * [None]
#
#
#     # Indexes of smallest and largest elements
#     # from remaining array.
#     small, large = 0, n - 1
#
#     # To indicate whether we need to copy rmaining
#     # largest or remaining smallest at next position
#     flag = True
#     arr.sort()
#
#     # Store result in temp[]
#     for i in range(n):
#         if flag is True:
#             temp[i] = arr[large]
#             large -= 1
#         else:
#             temp[i] = arr[small]
#             small += 1
#
#         flag = bool(1 - flag)
#
#         # Copy temp[] to arr[]
#     for i in range(n):
#         arr[i] = temp[i]
#     return arr
#
#
# # Driver program to test above function
# arr = [2,1,43,32,10,20]
# n = len(arr)
# print("Original Array")
# print(arr)
# print("Modified Array")
# print(rearrange(arr, n))
#
#
# a = [10,20,30,40]
# b=[]
# for a[-1] in a:
#     print("->",a[-1])
#
# for itr, a[-2] in enumerate(a):
#     print(a)
#     print(itr, "->",a[-2])
# print(a)
#
#
# print("---------------------")
# for i in a:
#     print("->", i)
#     # b.append(a[-1])


# def logest_prefix(str1, str2):
#     n1 = len(str1)
#     n2 = len(str2)
#     result = ""
#     i, j = 0, 0
#     while i <= n1 - 1 and j <= n2 - 1:
#         if str1[i] != str2[j]:
#             break
#         result += str1[i]
#         i += 1
#         j += 1
#     return result
#
#
# def prefix_input(arr, n):
#     # n = len(arr)
#     prefix = arr[0]
#     for i in range(1,n):
#         prefix = logest_prefix(prefix,arr[i])
#     return prefix
#
#
# if __name__ == "__main__":
#
#     arr = ["Appple", "Appp", "Apppostrophy"]
#     n = len(arr)
#
#     ans = prefix_input(arr, n)
#
#     if (len(ans)):
#         print("The longest common prefix is -",ans)
#     else:
#         print("There is no common prefix")


#
# def reverse(n):
#     return str(n) == str(n)[::-1]
#
# n = int(input("Enter the number: "))
#
# if reverse(n):
#     print("number",n,"alrady palidrome")
# else:
#     n1 = n
#     while not reverse(n1):
#         n1 = int(n1)+1
#
#     print('You entered {0}, but the next palindrome is {1}'.format(n, n1))
#


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [20,40,10,50]
bubble_sort(arr)
print ("Sorted array is:")
print(arr)
# for i in range(len(arr)):
#     print(i)






















# from PyPDF2 import PdfFileReader
#
# def read_file(pdf_path):
#
#
#     # creating a pdf file object
#     pdfFileObj = open(pdf_path, 'rb')
#     print()
#
#
#     # import pdb;pdb.set_trace()
#     # creating a pdf reader object
#     pdfReader = PdfFileReader(pdfFileObj)
#
#     # printing number of pages in pdf file
#     print(pdfReader.numPages)
#
#     # creating a page object
#     pageObj = pdfReader.getPage(0)
#     # import pdb; pdb.set_trace()
#
#     # extracting text from page
#     page_content = pageObj.extractText()
#     print(page_content)
#
#     # closing the pdf file object
#     pdfFileObj.close()
#
#
# path = "D:\studProduce\django_rest_framework\StudProduce\Examples\problem_statement (1).pdf"
# read_file(path)










