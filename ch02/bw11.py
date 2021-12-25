a=['a','b','c','d']
first_twenty_items = a[:20]
last_twenty_items = a[-20:]

a = [1,2,3]
b = a
print('이전 a:',a)
print('이전 b:',b)
a[:] = [4,5,6]
assert a is b
print('이후 a:',a)
print('이후 b:',b)
# 이전 a: [1, 2, 3]
# 이전 b: [1, 2, 3]
# 이후 a: [4, 5, 6]
# 이후 b: [4, 5, 6]

a = [1,2,3,4,5,6,7]
b = a
print('이전 a:',a)
print('이전 b:',b)
a[:] = [1,2,3]
print('이후 a:',a)
print('이후 b:',b)

