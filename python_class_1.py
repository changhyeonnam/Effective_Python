class Shell:
    def fork(self):
        print('implement command')

class Parent(Shell):
    pass
    # def fork(self):
    #     print('I make child')

class Parent2(Shell):
    def fork(self):
        print('I make child too.')

class Child(Parent,Parent2):
    pass
    # def fork(self):
    #     print('I make grandchild.')

# print(Child.__mro__)
# # (<class '__main__.Child'>, <class '__main__.Parent'>, <class '__main__.Parent2'>, <class '__main__.Shell'>, <class 'object'>)
#
# grandchild = Child()
# grandchild.fork()
# I make grandchild.
# I make child
# I make child too.

class Shell:
    def fork(self):
        print('implement command')

class Parent(Shell):
    pass
    # def fork(self):
    #     print('I make child')

class Parent2(Shell):
    def fork(self):
        print('I make child too.')

class Child(Parent,Parent2):
    pass
    # def fork(self):
    #     print('I make grandchild.')
