def normalize(getiter):
    # print(getiter)
    # print(iter(getiter()))
    if iter(getiter) is getiter:
        raise TypeError
    total = sum(getiter())
    result = []
    for value in getiter():
        precent = 100 * value / total
        result.append(precent)
    return  result

def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

# visits = [15,35,80]
# percentages = normalize(visits)
# print(percentages)



# it = read_visits('my_numbers.txt')
# percentages = normalize(it)
# print(percentages)

# it = lambda: read_visits('my_numbers.txt')
# perceptages = normalize(it)
# print(perceptages)
# print(list(it))
# []
# []

class ReadVisits:
    def __init__(self,datapath:str='my_numbers.txt'):
        self.datapath = datapath
    def __iter__(self):
        with open(self.datapath) as f:
            for line in f:
                yield int(line)
it = ReadVisits
perceptages = normalize(it)
print(perceptages)
print(list(it()))

