# item =('호박엿','식혜')
# first = item[0]
# second = item[1]
# print(first,'&',second)
# # 호박엿 & 식혜
#
# pair = ('호박엿','식혜')
# pair[0] = '타래과'
# # TypeError: 'tuple' object does not support item assignment
item =('호박엿','식혜')
first,second = item #unpacking

# today_health = {
#     '어깨':('숄더 프레스',3),
#     '다리':('레그 프레스',3),
#     '가슴':('벤치 프레스',3)
# }
# ((type1,(name1,num1)),
#  (type2,(name2,num2)),
#  (type3,(name3,num3))) = today_health.items()
# print(f'오늘 운동한 부위는 {type1},{type2},{type3}이고 '
#       f'각각 {name1}/{num1},{name2}/{num2},{name3}/{num3}세트씩 했습니다.')
# # 오늘 운동한 부위는 어깨,다리,가슴이고 각각 숄더 프레스/3,레그 프레스/3,벤치 프레스/3세트씩 했습니다.

# def bubble_sort(a):
#     for _ in range(len(a)):
#         for i in range(1,len(a)):
#             if a[i]<a[i-1]:
#                 temp = a[i]
#                 a[i] = a[i-1]
#                 a[i-1] = temp
# names =['c','a','d','b']
# bubble_sort(names)
# print(names)

# def bubble_sort(a):
#     for _ in range(len(a)):
#         for i in range(1,len(a)):
#             if a[i]<a[i-1]:
#                 a[i-1],a[i]=a[i],a[i-1]
# names =['c','a','d','b']
# bubble_sort(names)
# print(names)
# # ['a', 'b', 'c', 'd']

# snacks =[('베이컨',350),('도넛',240),('머핀',190)]
# for rank,(name,calories) in enumerate(snacks,1):
#     print(f'#{rank}: {name}은 {calories} 칼로리 입니다.')
# # 1: 베이컨은 350 칼로리 입니다.
# # 2: 도넛은 240 칼로리 입니다.
# # 3: 머핀은 190 칼로리 입니다.