
# def test():
#     return 0
# print(type(test))
#
# def test():
#     yield 1
#     yield 2
#
# gen = test()
# print(type(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# <class 'generator'>
# 1
# 2
# StopIteration

def test():
    val = yield 1
    print(val)
    yield 2
    yield 3

# gen = test()
# print(next(gen))
# print(gen.send('abc'))
# print(next(gen))
# print(gen.throw(Exception('!')))
# 1
# abc
# 2
# 3
# Exception: !
#
# def test():
#     yield 1
#     return 'abc'
# gen = test()
# print(next(gen))
# # 1
#
# try:
#     next(gen)
# except StopIteration as exc:
#     print(exc.value)
# abc

# def inner():
#     inner_result = yield 2
#     print('inner', inner_result)
#     return 3
# def outer():
#     yield 1
#     val = yield from inner()
#     print('other',val)
#     yield 4
# gen = outer()
# print(next(gen))
# print(next(gen))
# print(gen.send('abc'))
# # 1
# # 2
# # inner abc
# # other 3
# # 4

async def inner():
    return 1
async def outer():
    await inner()

print(outer())