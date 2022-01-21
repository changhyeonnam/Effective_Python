import pickle

class example:
    a_number=35,
    a_string='hi'
    a_list = [1,2,3]

obj = example()
pickled_obj = pickle.dumps(obj) # piclking the object
print(f'This is pickled object:{pickled_obj}')

unpickled_obj = pickle.loads(pickled_obj)
print(f'This is unpickled object:{unpickled_obj.a_string}')
