counters ={
    '소보로':1,
    '단팥빵':2,
}
key ='꽈베기'
if key in counters:
    count = counters[key]
else:
    count=0
counters[key]=count+1

try:
    count = counters[key]
except KeyError:
    count =0
counters[key]=count+1

count = counters.get(key,0)
counters[key]= count+1

votes = {
    '소보로':['철수','민수'],
    '단팥빵':['미애','미정'],
}
key = '꽈베기'
who = '종원'
if key in votes:
    names = votes[key]
else:
    votes[key]=names=[]
names.append(who)
print(votes)

try:
    names = votes[key]
except KeyError:
    votes[key]=names=[]
names.append(who)
print(votes)

if(names:=votes.get(key)) is None:
    votes[key] = names=[]
names.append(who)
print(votes)

names = votes.setdefault(key,[])
names.append(who)

# data = {}
# key = 'foo'
# value = []
# data.setdefault(key,value)
# print('이전',data)
# value.append('hello')
# print('이후',data)
# 이전 {'foo': []}
# 이후 {'foo': ['hello']}
data = {}
value = []
for i  in range(3):
    key = i
    data.setdefault(key, value)
    value.append('hello')
    print(data)
# {0: ['hello']}
# {0: ['hello', 'hello'], 1: ['hello', 'hello']}
# {0: ['hello', 'hello', 'hello'], 1: ['hello', 'hello', 'hello'], 2: ['hello', 'hello', 'hello']}

count = counters.setdefault(key,0)
counters[key]=count+1
# >>> my_dict = {}
# >>> my_dict.setdefault('some key', 'a value')
# 'a value'
# >>> my_dict
# {'some key': 'a value'}
# >>> my_dict.get('some key2', 'a value2')
# 'a value2'
# >>> my_dict
# {'some key': 'a value'}