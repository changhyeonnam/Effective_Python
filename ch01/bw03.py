# a = b'h\x65llo'
# print(list(a))
# print(a)
# # [104, 101, 108, 108, 111]
# # b'hello
# a='a\u0300 propos'
# print(list(a))
# print(a)
# # ['a', '̀', ' ', 'p', 'r', 'o', 'p', 'o', 's']
# # à propos
# def to_str(bytes_or_str):
#     if isinstance(bytes_or_str,bytes):
#         value = bytes_or_str.decode('utf-8')
#     else:
#         value = bytes_or_str
#     return value # str 인스턴스
# print(repr(to_str(b'foo')))
# print(repr(to_str('bar')))
# print(repr(to_str(b'\xed\x95\x9c')))
# # 'foo'
# # 'bar'
# # '한'
# def to_bytes(bytes_or_str):
#     if(isinstance(bytes_or_str,str)):
#         value = bytes_or_str.encode('utf-8')
#     else:
#         value = bytes_or_str
#     return value # bytes 인스턴스
#
# print(repr(to_bytes(b'foo')))
# print(repr(to_bytes('bar')))
# print(repr(to_bytes('한글')))
# # b'foo'
# # b'bar'
# # b'\xed\x95\x9c\xea\xb8\x80'

# print(b'one'+b'two')
# # b'onetwo'
# print('one'+'two')
# # onetwo
# print(b'one'+two)
# #NameError: name 'two' is not defined
#
# assert b'red' > b'blue'
# assert 'red' > 'blue'
# assert 'red' > b'blue'
# # TypeError: '>' not supported between instances of 'str' and 'bytes'
# print(b'foo'=='foo')
# #False
# print(b'red %s' % b'blue')
# #b'red blue'
# print('red %s' % 'blue')
# #red blue
# print(b'red %s' % 'blue')
# # TypeError: %b requires a bytes-like object, or an object that implements __bytes__, not 'str'
#
# print('red %s' % b'blue')
# #red b'blue'
# # b'blue' is not expected.

# with open('data.bin','wb') as f:
#     f.write(b'\xf1\xf2\xf3\xf4\xf5')
# # Trackback.. TypeError: write() argument must be str, not bytes
# with open('data.bin','r') as f:
#     data = f.read()
# Trackback.. UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf1 in position 0: invalid continuation byte
with open('data.bin','r',encoding='cp1252') as f:
    data = f.read()
