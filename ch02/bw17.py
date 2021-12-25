visits = {
    '미국':{'뉴욕','로스엔젤레스'},
    '일본':{'하코네'}
}

visits.setdefault('프랑스',set()).add('칸')

if(japan := visits.get('일본')) is None:
    visits['일본']=japan=set()
japan.add('교토')
print(visits)
# {'미국': {'뉴욕', '로스엔젤레스'}, '일본': {'하코네', '교토'}, '프랑스': {'칸'}}
print(type(japan))
v={'a':[1,2]}
print(type(v))

class Visits:
    def __init__(self):
        self.data = {}
    def add(self,country,city):
        city_set = self.data.setdefault(country,set())
        city_set.add(city)

visits = Visits()
visits.add('러시아','모스크바')
visits.add('탄자니아','잔지바르')
visits.add('러시아','스바시바')
print(visits.data)
# {'러시아': {'모스크바', '스바시바'}, '탄자니아': {'잔지바르'}}

from collections import defaultdict

class Visits:
    def __init__(self):
        self.data  = defaultdict(set)
    def add(self,country,city):
        self.data[country].add(city)
visits = Visits()
visits.add('러시아','모스크바')
print(id(visits))
print(visits.data)
# defaultdict(<class 'set'>, {'러시아': {'모스크바'}})
