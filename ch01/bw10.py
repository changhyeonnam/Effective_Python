def make_cider(count):
    ...
def out_of_stock():
    ...
count = fresh_fruit.get('사과',0)
if count >=4:
    make_cider(count)
else:
    out_of_stock()


if (count:= fresh_fruit.get('사과',0)>=4):
    make_cider(count)
else:
    out_of_stock()

count = fresh_fruit('바나나',0)
if count>=2:
    pieces = slice_banna(count)
    to_enjoy = make_smoothies(pieces)
else:
    count = fresh_fruit('사과',0)
    if count >= 4:
        to_enjoy = make_cider(count)
    else:
        count = fresh_fruit('레몬',0)
        if count:
            to_enjoy = make_cider(count)
        else:
            to_enjoy = '아무것도 없음'

if(count := fresh_fruit('바나나',0))>=2:
    pieces = slice_banna(count)
    to_enjoy = make_smoothies(pieces)
elif (count := fresh_fruit('사과',0))>=4:
    to_enjoy = make_cider(count)
elif count:=fresh_fruit('레몬',0):
    to_enjoy = make_cider(count)
else:
    to_enjoy = '아무것도 없음'

bottles = []
while True: # 무한 루프
    fresh_fruit = pick_fruit()
    if not fresh_fruit: # 중간에서 끝내기 loop-and-a half
        break
    ...

bottles=[]
while fresh_fruit:=pick_fruit():
    ...
