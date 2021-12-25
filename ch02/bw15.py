#
# # python 3.5 버전
# baby_names={'cat':'kitten','dog':'puppy'}
# print(baby_names)
# # {'dog': 'puppy', 'cat': 'kitten'}
#
# # python 3.6 버전이후
# baby_names={'cat':'kitten','dog':'puppy'}
# print(baby_names)
# # {'cat': 'kitten', 'dog': 'puppy'}
#
# print(list(baby_names.keys()))
# print(list(baby_names.values()))
# print(list(baby_names.items()))
# print(list(baby_names.popitem())) #마지막에 삽입된 원소
# # ['cat', 'dog']
# # ['kitten', 'puppy']
# # [('cat', 'kitten'), ('dog', 'puppy')]
# # ['dog', 'puppy']
#
# def func(**kwargs):
#     for key,value in kwargs.items():
#         print(f'{key}={value}')
# func(goose='gosling',kangaroo='joey')
# goose=gosling
# kangaroo=joey

# class MyClass:
#     def __init__(self):
#         self.alligator = 'hatchling'
#         self.elephant = 'calf'
# a = MyClass()
# for key,value in a.__dict__.items():
#     print(f'{key}:{value}')
# alligator:hatchling
# elephant:calf

votes = {
    'otter':1281,
    'polar bear': 587,
    'fox' : 863
}

# def populate_ranks(votes,ranks):
#     names = list(votes.keys())
#     names.sort(key=votes.get, reverse = True)
#     for i,name in enumerate(names,1):
#         ranks[name]=i
# def get_winner(ranks):
#     return next(iter(ranks))

ranks={}
# populate_ranks(votes,ranks)
# print(ranks)
# winner = get_winner(ranks)
# winner = get_winner(ranks)
# print(winner)

# {'otter': 1, 'fox': 2, 'polar bear': 3}
# otter

from collections.abc import MutableMapping

class SortedDict(MutableMapping):
    def __init__(self):
        self.data={}
    def __getitem__(self, item):
        return self.data[key]
    def __setitem__(self,key,value):
        self.data[key] = value
    def __delitem__(self, key):
        del self.data[key]
    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key
    def __len__(self):
        return len(self.data)
# sorted_ranks = SortedDict()
# populate_ranks(votes,sorted_ranks)
# print(sorted_ranks.data)
# winner = get_winner(sorted_ranks)
# print(winner)
# {'otter': 1, 'fox': 2, 'polar bear': 3}
# fox
#
# def get_winner(ranks):
#     for name,rank in ranks.items():
#         if rank ==1:
#             return name
# winner = get_winner(sorted_ranks.data)
# print(winner)
# otter

# def get_winner(ranks):
#     if not isinstance(ranks,dict):
#         raise TypeError('dict 인스턴스가 필요합니다')
#     return next(iter(ranks))
# get_winner(sorted_ranks)
# TypeError: dict 인스턴스가 필요합니다

from typing import Dict,MutableMapping
def populate_ranks(votes:Dict[str,int],
             ranks:Dict[str,int])->None:
    names = list(votes.keys())
    names.sort(key=votes.get,reverse=True)
    for i, name in enumerate(name,i):
        ranks[name]=i
def get_winner(ranks:Dict[str,int])->str:
    return next(iter(ranks))
sorted_ranks=SortedDict()
populate_ranks(votes,sorted_ranks)
print(sorted_ranks.data)
winner=get_winner(sorted_ranks.data)
print(winner)
# bw15.py:112: error: Call to untyped function "SortedDict" in typed context
# bw15.py:113: error: Argument 2 to "populate_ranks" has incompatible type "SortedDict"; expected "Dict[str, int]"
