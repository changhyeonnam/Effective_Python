stock = {
    '못': 125,
    '나사못': 35,
    '와셔': 24,
    '나비너트' : 8
}

order = ['나사못','클립','나비너트']

def get_batches(count,size):
    return count//size

result = {}

for name in order:
    count = stock.get(name,0)
    batches = get_batches(count,8)
    if batches:
        result[name]= batches

print(result)

found = {name: get_batches(stock.get(name,0),8)
         for name in order
         if get_batches(stock.get(name,0),8)}
print(found)

has_bug = {name: get_batches(stock.get(name,0),4)
           for name in order
           if get_batches(stock.get(name,0),8)}

print('예상:', found)
print('실제:', has_bug)

found = {name:batches for name in order
         if (batches:=get_batches(stock.get(name,0),8))}

result = {name:tenth for name,count in stock.items() if (tenth:=count//10)>0}
print(result)

found = ((name,batches) for name in order if(batches := get_batches(stock.get(name,0),8)))
print(found)
print(next(found))
print(next(found))