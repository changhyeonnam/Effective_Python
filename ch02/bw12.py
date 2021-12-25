
x=['빨강','주황','노랑','초록','파랑','자주']
odds = x[::2]
evens =x[1::2]
print(odds)
print(evens)
# ['빨강', '노랑', '파랑']
# ['주황', '초록', '자주']

w='가나다'
x=w.encode('utf-8')
y=x[::-1]
z=y.decode('utf-8')
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0x98 in position 0: invalid start byte

print(x[::2])
print(x[::-2])

