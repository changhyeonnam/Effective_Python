
def careful_divdie(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return None

x,y = 1,0
result = careful_divdie(x,y)
if result is None :
    print('input error')
# input error

x,y = 0,5
result = careful_divdie(x,y)
if not result:
    print('input error')
# input error

def careful_divide(a,b):
    try:
        return True,a/b
    except ZeroDivisionError:
        return False,None
x,y = 0,5
success,result = careful_divide(x,y)
if not success:
    print('input error')

_,result = careful_divide(x,y)
if not success:
    print('input error')

def careful_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        raise ValueError('input error')

x,y =5,2
try:
    result = careful_divide(x,y)
except ValueError:
    print('input error')

else:
    print(f'결과 {result:.1f}')
# 결과 2.5

def careful_divide(a: float, b:float)->float:
    """
    :param a:numerator
    :param b:denominator
    :return: a/b

    Raise :
        ValueError : ZeroDivisionError
    """
    try:
        return a/b
    except ZeroDivisionError as e:
        raise ValueError('input error')