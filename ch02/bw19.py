def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum,maximum

lengths = [63,73,72,60,67,66,71]
minimum,maximum = get_stats(lengths)
print(f'maximum:{maximum}, minimum:{minimum}')
# maximum:73, minimum:60

def get_avg_ratio(numbers):
    average = sum(numbers)/len(numbers)
    scaled = [x/average for x in numbers]
    scaled.sort(reverse=True)
    return scaled

longest,*middle,shortest = get_avg_ratio(lengths)
print(f'longest ratio:{longest:>4.0%}, shortest ratio:{shortest:>4.0%}')
# longest ratio:108%, shortest ratio: 89%

def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    count = len(numbers)
    average = sum(numbers)/count

    sorted_numbers = sorted(numbers)
    middle = count//2
    if count%2==0 :
        lower = sorted_numbers[middle-1]
        upper = sorted_numbers[middle]
        median = (lower+upper)/2
    else:
        median = sorted_numbers[middle]
    return minimum,maximum,average,median,count

minimum,maximum,average,median,count = get_stats(lengths)
print(f'min:{minimum}, max:{maximum}, avg:{average:.1f}\nmedian:{median},count:{count}')
# min:60, max:73, avg:67.4
# median:67,count:7

# 잘못쓴 경우
minimum,average,maximum,median,count = get_stats(lengths)

