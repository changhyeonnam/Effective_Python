def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter ==' ':
            result.append(index+1)
    return result

address = '가나다라 마바사 아자차카 타파하'
result = index_words(address)
print(result)
# [0, 5, 9, 14]

def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter ==' ':
            yield index+1

it = index_words_iter(address)
print(next(it))
print(next(it))
# 0
# 5

result = list(index_words_iter(address))
print(result)
# [0, 5, 9, 14]
def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset+=1
            if letter ==' ':
                yield offset



