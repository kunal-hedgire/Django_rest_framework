# list1 = [6, 6, 6, 6, 6, 6, 6, 6, 6, 5]
#
# first = second = list1[0]
#
# for j in range(len(list1)):
#     if list1[j] > first:
#         second = first
#         first = list1[j]
#
#     elif list1[j] > second and list1[j] < first:
#         second = list1[j]
#
#
# print("runner-up", second)


# list1 = [2, 4, 9, 3, 6, 1]
# list2 = []
#
# for i in range(len(list1)):
#     flag = False
#     for j in range(i+1, len(list1)):
#         if list1[i] > list1[j]:
#             flag = True
#             continue
#         else:
#             flag = False
#             break
#     if flag:
#         list2.append(list1[i])
#
# print(list2)


# x =1
# def f():
#     x =2
#     return x
#
# class c(object):
#     x = 3
#
# if True:
#     x = 4
#
# f()
# c()
# print(x)

class Tree(object):
    def print(self):
        print ('Tree')

class Banyan(Tree):
    def print(self, banyan_type=None):
        if banyan_type:
            print ('Banyan: {}'.format(banyan_type))
        else:
            print('Banyan')

class Peepal(Tree):
    def print(self, *args, **kwargs):
        super(Peepal, self).print(*args, **kwargs)

if __name__ == '__main__':
    a = [Tree(), Banyan(), Peepal()]
    for tree in a:
        tree.print() # Tree, Banyan, Tree


class Tree(object):
    def name(self):
        return ('Tree')

    def print(self):
        print (self.name())

class Banyan(Tree):
    def name(self):
        return 'Banyan'

class Peepal(Tree):
    pass

if __name__ == '__main__':
    a = [Tree(), Banyan(), Peepal()]
    for tree in a:
        tree.print()

#
#
#

class Tree(object):
    name = 'Tree'

    def print(self):
        print (self.name)

class Banyan(Tree):
    name = 'Banyan'

class Peepal(Tree):
    name = 'Peepal'

if __name__ == '__main__':
    a = [Tree(), Banyan(), Peepal()]
    for tree in a:
        tree.print()



def extendList(val, list = []):
    # import pdb;pdb.set_trace()
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print(list1)
print(list2)
print(list3)


names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
names2 = names1
names3 = names1[:]

names2[0] = 'Alice'
names3[1] = 'Bob'

sum = 0
for ls in (names1, names2, names3):
    if ls[0] == 'Alice':
        sum += 1
    if ls[1] == 'Bob':
        sum += 10

print(sum)






















