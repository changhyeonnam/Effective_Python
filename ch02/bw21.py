def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0,x)
        return (1,x)
    values.sort(key=helper)

numbers=[8,3,1,2,5,4,7,6]
group = {2,3,5,7}
sort_priority(numbers,group)
print(numbers)
# [2, 3, 5, 7, 1, 4, 6, 8]

def sort_priority2(numbers,group):
    found = False
    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return(0,x)
        return (1,x)
    numbers.sort(key=helper)
    return found

found = sort_priority2(numbers,group)
print('found: ', found)
print(numbers)
# found:  True
# [2, 3, 5, 7, 1, 4, 6, 8]

class Sorter:
    def __init__(self,group):
        self.group = group
        self.found = found

    def __call__(self,x):
        if x in self.group:
            self.found = True
            return (0,x)
        return (1,x)

sorter = Sorter(group)
numbers.sort(key=sorter)
print(numbers)
# [2, 3, 5, 7, 1, 4, 6, 8]
print(sorter.found)
# True

def double(n):
    return 2*n
def call_function(x,func):
    print(func(x))

def odd(x):
    print(f'{x} is odd.')
def even(x):
    print(f'{x} is even.')
def return_function(x):
    if x%2==1:
        return odd(x)
    else:
        return even(x)
return_function(3)
# 3 is odd.

call_function(10,double)
# 20

def multiply_function(n):
    def multiply(x):
        return n*x
    return multiply

value = multiply_function(5)
value2 = multiply_function(3)

print(value(4))
print(value2(3))
# 20
# 9
del(multiply_function)
print(value(4))
print(value2(3))
# 20
# 9
print(value.__closure__[0].cell_contents)
# 5
print(value2.__closure__[0].cell_contents)
# 3
class Stuff(object):

    def __init__(self, x, y):
        super(Stuff, self).__init__()
        self.x = x
        self.y = y
        print(f'__init__ with ({self.x},{self.y})')

    def __call__(self, x, y):
        self.x = x
        self.y = y
        print (f'__call__ with ({self.x},{self.y})')

    def __del__(self):
        del self.x
        del self.y

s = Stuff(1, 2)
# __init__ with (1,2)

s(7, 8)
# __call__ with (7,8)

