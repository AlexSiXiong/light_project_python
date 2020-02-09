
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


template = 'Alex, Captain, {} {} off the larboard bow!'
print(template.format('a', 'bird'))