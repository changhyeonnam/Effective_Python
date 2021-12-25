for i in range(3):
    print("Loop",i)
    if i==1:
        break
else:
    print('Else block!')
# Loop 0
# Loop 1
# Loop 2
# Else block!
for x in []:
    print('이 줄은 실행되지 않음')
else:
    print('For Else block!')
# For Else block!

a = 4
b = 9
for i in range(2,min(a,b)+1):
    print('검사 중',i)
    if a % i == 0 and b % i == 0:
        print('서로소 아님')
        break
else:
    print('서로소')
# 서로소