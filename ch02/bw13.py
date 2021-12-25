
car_ages =[0,9,4,5,2,3]
car_ages_descending = sorted(car_ages,reverse=True)
# oldest,  second_oldest = car_ages_descending
# Traceback (most recent call last):
# ValueError: too many values to unpack (expected 2)

oldest = car_ages_descending[0]
second_oldest = car_ages_descending[1]
others = car_ages_descending[2:]
print(oldest,second_oldest,others)
# 9 5 [4, 3, 2, 0]

oldest, second_oldest, *others = car_ages_descending
print(oldest,second_oldest,others)
# 9 5 [4, 3, 2, 0]

oldest, *others,  youngest = car_ages_descending
print(oldest,others,youngest)
# 9 [5, 4, 3, 2] 0

*others, second_youngest, youngest = car_ages_descending
print(others,second_youngest,youngest)
# [9, 5, 4, 3] 2 0

# *others = car_ages_descending
# SyntaxError: starred assignment target must be in a list or tuple

# first, *middle, *second_middle, last = car_ages_descending
# SyntaxError: two starred expressions in assignment

car_inventory = {'시내':('그랜저','아반떼','티코'), '공항':('제네시스 쿠페','소나타','K5','엑센트')}
((loc1,(best1,*rest1)),(loc2,(best2,*rest2))) = car_inventory.items()
print(f'{loc1}에서 최고의 차는 {best1}, 나머지는 {rest1}')
# 시내에서 최고의 차는 그랜저, 나머지는 ['아반떼', '티코']

sort_list = [1,2]
first,second, *rest = sort_list
print(first,second,rest)
# 1 2 []
def generate_csv():
    yield ('날짜', '제조사' , '모델', '연식', '가격')
    for i in range(100):
        yield ('2019-03-25', '현대', '소나타', '2010', '2400만원')
        yield ('2019-03-26', '기아', '프라이드', '2008', '1400만원')

all_csv_rows = list(generate_csv())
header = all_csv_rows[0]
rows = all_csv_rows[1:]
print('CSV 헤더:', header)
print('행 수: ', len(rows))

it = generate_csv()
header, *rows = it
print('CSV 헤더:', header)
print('행 수: ', rows)
# CSV 헤더: ('날짜', '제조사', '모델', '연식', '가격')
# 행 수:  200
# CSV 헤더: ('날짜', '제조사', '모델', '연식', '가격')
# 행 수:  200
