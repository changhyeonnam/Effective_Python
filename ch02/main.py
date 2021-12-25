# import sys
# from collections import deque
#
# n = int(input())
# arr = list(map(int, input().split()))
#
# s = input()
#
# ans = list(range(n))
#
# lst = deque()
# rst = deque()
# for  i in range(0,n):
#     if i == 0:
#         if s[i]=='L':
#             ans[0]=0;
#         lst.append((arr[i],i))
#         continue
#     if s[i]=='L':
#         ans[i]=(i-lst[-1][1])
#     if lst[-1][0] < arr[i] :
#         lst.pop()
#         lst.append((arr[i],i))
# for i in range(n-1,-1,-1):
#     if i ==n-1:
#         if s[i]=='R':
#             ans[i]=0;
#         rst.append((arr[i],i))
#         continue
#     if s[i]=='R':
#         ans[i]=(rst[-1][1]-i)
#     if rst[-1][0] < arr[i] :
#         rst.pop()
#         rst.append((arr[i],i))
#
# for i in range(0,n):
#     print(ans[i],end=' ')
