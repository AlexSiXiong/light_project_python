
# test = {}
# test['a'] = 10
# test['b'] = 20

# test = {'a': 10, 'b': 20}
# print(test)
# test.items()
# # 返回数组，得到排序后的key
# sorted(test, key=test.get, reverse=True)
#
# # 返回数组，得到排序后的键值对
# sorted(test.items(), key=lambda d: d[1], reverse=True)


# template = 'Alex, Captain, {} {} off the larboard bow!'
# print(template.format('a', 'bird'))


# food = ['a k','b','c']
#
#
# if len(food) == 1:
#     formatted_food = food
# elif len(food) == 2:
#     formatted_food = ' and '.join(map(str, food))
# elif len(food) >= 3:
#     formatted_food = ', '.join(map(str, food))
#     index = formatted_food.rfind(',')
#     formatted_food = formatted_food[:index] + ' and' + formatted_food[index + 1:]
#
#
# print(formatted_food)
# index = formatted_food.rfind(',')
# formatted_food = formatted_food[:index] + ' and' + formatted_food[index+ 1:]
# print(formatted_food)


#
# # type
# # id
# # name
# # price
# order = {'type': 'beer', 'id': 'beer4', 'name': 'Stella Artois', 'price': 100}
#
# update_order = {'type': 'soda', 'id': 'beer2', 'name': 'Stella Artois', 'price': 1000}
#
# menu = [
#     {'type': 'beer', 'id': 'beer1', 'name': 'Stella Artois', 'price': 5},
#     {'type': 'beer', 'id': 'beer2', 'name': 'Heineken', 'price': 5},
#     {'type': 'beer', 'id': 'beer3', 'name': 'Corona', 'price': 5},
# ]
#
# new_order_id = order.get("id")
#
# # print(id_new_order)
#
# menu_length = len(menu)
# #
#
# digits_dictionary = {
#     '1': '9',
#     '2': '8',
#     '3': '7',
#     '4': '6',
#     '5': '0',
#     '6': '4',
#     '7': '3',
#     '8': '2',
#     '9': '1',
#     '0': '5',
# }
# keys = digits_dictionary.keys()
# result = ''
#
# text= 'That number to call is 098-765-4321.'
#
# for i in text:
#     if i in keys:
#         result += digits_dictionary.get(i)
#     else:
#         result += i
#
# print(result)
#
# print(type(text))


import os
import re
import random
import string
from subprocess import getstatusoutput, getoutput
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
out_file = random_string()
print(out_file)