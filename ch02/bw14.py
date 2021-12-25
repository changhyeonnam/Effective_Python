
numbers =[93,86,11,68,70]
numbers.sort()
print(numbers)
# [11, 68, 70, 86, 93]

class Person:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'(이름:{self.name!r},무게:{self.weight})'

people =[
    Person('철수',65.7),
    Person('미애',56),
    Person('덕구',83),
]

# people.sort()
# TypeError: '<' not supported between instances of 'Person' and 'Person'

print("미정렬: ",repr(people))
people.sort(key=lambda x:x.weight)
print("\n정렬: ",repr(people))
# 정렬: [(이름:'미애',무게:56), (이름:'철수',무게:65.7), (이름:'덕구',무게:83)]

places = ['home','work','New York','Paris']
places.sort()
print('대소문자 구분:',places)
# 대소문자 구분: ['New York', 'Paris', 'home', 'work']
places.sort(key=lambda x:x.lower())
print('대소문자 무시:',places)
# 대소문자 무시: ['home', 'New York', 'Paris', 'work']

fat_people = [
    Person('민수',97),
    Person('인호',103),
    Person('종원',92),
    Person('형섭',92)
]

drill = (4,'드릴')
sander =(4,'연마기')
assert drill[0] == sander[0]
assert drill[1] <sander[1]
assert drill < sander

fat_people.sort(key=lambda x:(x.weight,x.name))
print("fat people:",repr(fat_people))
# fat people: [(이름:'종원',무게:92), (이름:'형섭',무게:92), (이름:'민수',무게:97), (이름:'인호',무게:103)]
fat_people.sort(key=lambda x:(x.weight,x.name),reverse=True)
print("fat people:",repr(fat_people))
# fat people: [(이름:'인호',무게:103), (이름:'민수',무게:97), (이름:'형섭',무게:92), (이름:'종원',무게:92)]
fat_people.sort(key=lambda x:(-x.weight,x.name))
print("fat people:",repr(fat_people))
# fat people: [(이름:'인호',무게:103), (이름:'민수',무게:97), (이름:'종원',무게:92), (이름:'형섭',무게:92)]
# fat_people.sort(key=lambda x:(x.weight,-x.name))
# # TypeError: bad operand type for unary -: 'str'

fat_people.sort(key=lambda x:x.name)
print("fat people:",repr(fat_people))
# fat people: [(이름:'민수',무게:97), (이름:'인호',무게:103), (이름:'종원',무게:92), (이름:'형섭',무게:92)]

fat_people.sort(key=lambda x:x.weight,reverse=True)
print("fat people:",repr(fat_people))
# fat people: [(이름:'인호',무게:103), (이름:'민수',무게:97), (이름:'종원',무게:92), (이름:'형섭',무게:92)]
