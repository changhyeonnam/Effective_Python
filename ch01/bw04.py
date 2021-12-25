# a = 0b10111011
# b = 0xc5f
# # print('이진수: %d, 십진수: %d'%(a,b))
# # 이진수: 187, 십진수: 3167
#
# # key = 'my_var'
# # value = 1.234
# # formatted = '%-10s = %.2f' % (key,value)
# # print(formatted)
# # # my_var     = 1.23
# # formatted = '%-10s = %.2f' % (value,key)
# # print(formatted)
# # # Traceback TypeError: must be real number, not str
# #
# # pantry=[
# #     ('아보카도', 1.25),
# #     ('바나나', 2.5),
# #     ('체리', 15),
# # ]
# # for i, (item,count) in enumerate(pantry):
# #     print('#%d: %-10s = %.2f'%(i,item,count))
# # #0: 아보카도       = 1.25
# # #1: 바나나        = 2.50
# # #2: 체리         = 15.00
#
# # for i, (item,count) in enumerate(pantry):
# #     print('#%d: %-10s = %d'%(
# #         i+1,
# #         item.title(),
# #         round(count)))
# # #1: 아보카도       = 1
# # #2: 바나나        = 2
# # #3: 체리         = 15
#
# # template = '%s는 음식을 좋아해. %s가 요리하는 모습을 봐요.'
# # name = '철수'
# # formatted = template % (name, name)
# # print(formatted)
# # # 철수는 음식을 좋아해. 철수가 요리하는 모습을 봐요.
#
# # key = 'my_var'
# # value = 1.234
# # old_way = '%-10s = %.2f' % (key,value)
# # new_way = '%(key)-10s = %(value).2f'% {'key':key, 'value':value}
# # reordered = '%(key)-10s = %(value).2f'% {'value':value,'key':key}
# # assert (old_way == new_way == reordered)
#
#
# # template = '%s는 음식을 좋아해. %s가 요리하는 모습을 봐요.'
# # name = '철수'
# # before = template % (name, name) # tuple
# # template = '%(name)s는 음식을 좋아해. %(name)s가 요리하는 모습을 봐요.'
# # after = template %{'name':name} # dictionary
# # assert(before == after)
#
# pantry=[
#     ('아보카도', 1.25),
#     ('바나나', 2.5),
#     ('체리', 15),
# ]
#
# for i, (item,count) in enumerate(pantry):
#     before= '#%d: %-10s = %d'%(
#         i+1,
#         item.title(),
#         round(count))
#
#     after = '#%(loop)d: %(item)-10s = %(count)d'%{
#         'loop' : i+1,
#         'item' : item.title(),
#         'count' : round(count),
#     }
#     assert before == after

a = 1234.5678
formatted = format(a,',.2f')
print(formatted)
# 1,234.57

b = 'my 문자열'
formatted = format(b,'^20s')
print('*',formatted,'*')
# *        my 문자열        *

key = 'my_var'
value = 1.234

formatted = '{} = {}'.format(key,value)
print(formatted)
# my_var = 1.234

formatted = '{:<10} = {:.2f}'.format(key,value)
print(formatted)

print('%.2f%%' %12.5)
print('{} replace {{}}'.format(1.23))
# 12.50%
# 1.23 replace {}

key = 'my_var'
value = 1.234
formatted = '{1} = {0}'.format(key,value)
print(formatted)
# 1.234 = my_var

name = '철수'
formatted = '{0}는 음식을 좋아해. {0}가 요리하는 모습을 봐요.'.format(name)
print(formatted)
# 철수는 음식을 좋아해. 철수가 요리하는 모습을 봐요.


pantry=[
    ('아보카도', 1.25),
    ('바나나', 2.5),
    ('체리', 15),
]
for i, (item,count) in enumerate(pantry):
    old_style = '#%d: %-10s = %d'%(
        i+1,
        item.title(),
        round(count))

    new_style = '#{}: {:<10s} = {}'.format(
        i + 1,
        item.title(),
        round(count))

    assert old_style == new_style



soup ='lentil'
formatted ='Today\'s soup is %(soup)s.' %{'soup':soup}
print(formatted)
# Today's soup is lentil.

menu = {
    'soup': 'lentil',
    'oyster': 'tongyoung',
    'special': 'schnitzel',
}
template = ('Today\'s soup is %(soup)s, buy one get two %(oyster)s oysters, and our special entrée is %(special)s.')
formatted = template % menu
print(formatted)
# Today's soup is lentil, buy one get two tongyoung oysters, and our special entrée is schnitzel.

key ='my_var'
value=1.234
formatted = f'{key} = {value}'
print(formatted)
# my_var = 1.234
places = 3
number = 1.23456
print(f'내가 고른 숫자는 {number:.{places}f}')
