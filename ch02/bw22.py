def log(message, values):
    if not values:
        print(message)
    else:
        values_str =','.join(str(x)  for x in values)
        print(f'{message}: {values_str}')

log('내 숫자는',[1,2])
log('안녕',[])

def log(message, *values):
    if not values:
        print(message)
    else:
        print(type(values))
        values_str =','.join(str(x)  for x in values)
        print(f'{message}: {values_str}')

log('내 숫자는',1,2)
log('안녕',[])