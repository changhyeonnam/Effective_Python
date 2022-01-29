
class Parent:
    def __init__(self,value):
        self.value=value

class Child_times_two(Parent):
    def __init__(self,value):
        super().__init__(value)
        self.value*=2

class Child_plus_Five(Parent):
    def __init__(self,value):
        super().__init__(value)
        self.value+=5

class Grandchild(Child_times_two,Child_plus_Five):
    def __init__(self,value):
        super(Grandchild,self).__init__(value)



foo = Grandchild(3)
print(f'클래스 생성자에 따른 순서의 결과 :{foo.value}')
# 클래스 생성자에 따른 순서의 결과 :16

mro_str = '\n'.join(repr(cls)for cls in Grandchild.mro())
print(mro_str)
# <class '__main__.Grandchild'>
# <class '__main__.Child_times_two'>
# <class '__main__.Child_plus_Five'>
# <class '__main__.Parent'>
# <class 'object'>
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases Parent, Child_times_two, Child_plus_Five


