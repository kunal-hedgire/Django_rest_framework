# # dict_1 = {'a': {'b': {'c': [1, 2, 3, 4],'e': [5, 6, 7, 8]}}, 'd': 2}
#
# # class Struct:
# #     def __init__(self, **kwargs):
# #         self.__dict__.update(**kwargs)
# #
# #
# # dict_1 = {'a': {'b': {'c': [1, 2, 3, 4],'e': [5, 6, 7, 8]}}, 'd': 2}
# # s = Struct(**dict_1)
# # print(s.a['b'])
#
# # s = Struct()
# # setattr(s,'a',"'b': {'c': [1, 2, 3, 4],'e': [5, 6, 7, 8]}}, 'd': 2}")
# # print(s.a.b)
# #
#
#
# class Map(dict):
#     """
#     Example:
#     m = Map({'first_name': 'Eduardo'}, last_name='Pool', age=24, sports=['Soccer'])
#     """
#     def __init__(self, *args, **kwargs):
#         super(Map, self).__init__(*args, **kwargs)
#         for arg in args:
#             if isinstance(arg, dict):
#                 for k, v in arg.items():
#                     self[k] = v
#
#         if kwargs:
#             for k, v in kwargs.items():
#                 self[k] = v
#
#     def __getattr__(self, attr):
#         return self.get(attr)
#
#     def __setattr__(self, key, value):
#         self.__setitem__(key, value)
#
#     def __setitem__(self, key, value):
#         super(Map, self).__setitem__(key, value)
#         self.__dict__.update({key: value})
#
#     def __delattr__(self, item):
#         self.__delitem__(item)
#
#     def __delitem__(self, key):
#         super(Map, self).__delitem__(key)
#         del self.__dict__[key]
#
# m = Map({'a': {'b': {'c': [1, 2, 3, 4],'e': [5, 6, 7, 8]}}, 'd': 2})
# # print(m.a)
#
# class Apple():
#     pass
#
# a1 = Apple()
#
# a1.__setattr__("a1","b1")
# a1.__getattribute__("a1")
#


#
# from itertools import permutations,combinations
# a = input().split()
# pp = list(combinations(a[0],int(a[1])))
# # po = list(permutations(a[0], int(a[1])))
# pp.sort()
# for i in pp:
#     print("".join(i))



str1 = "gooD Morning"

# print(str1.swapcase())
# print(str1.split("-"))
print("")