#
# import time
# a = 3
# while a < 100000:
#    start = time.time()
#    print(a)
#    a+=2
#
# if a > (100000 - 2):
#     end = time.time()
#
#
# c = end - start
# print(start)
# print(end)
# print(c)

# num = int(input('diyige'))
# num2 = int(input('dierge'))
# sum = num + num2
# print(sum)
#

# x = True
# y = False
# z = False
#
# if not x or y:
#     print(1)
# elif not x or not y and z:
#     print(2)
# elif not x or y or not y and x:
#     print(3)
# else:
#     print(4)

#
# for i in [1, 0]:
#     print(i+1)

# while 4 == 4:
#     print('4')

# a = ','
# b = ['a','c','d']
#
# print( a.join(b))

# if __name__ == '__main__':
#     zi = int(input('输入一个数字:\n'))
#     n1 = 1
#     c9 = 1
#     m9 = 9
#     sum = 9
#     while n1 != 0:
#         if sum % zi == 0:
#             n1 = 0
#         else:
#             m9 *= 10
#             sum += m9
#             c9 += 1
#     print ('%d 个 9 可以被 %d 整除 : %d' % (c9,zi,sum))
#     r = sum / zi
#     print( '%d / %d = %d' % (sum,zi,r))

# i = int(input('净利润:'))
# arr = [1000000,600000,400000,200000,100000,0]
# rat = [0.01,0.015,0.03,0.05,0.075,0.1]
# r = 0
# for m  in range(0,6):
#     n=m+1
#     if i>arr[m]:
#         r+=(i-arr[m])*rat[m]
#         print(f'%d / = %d' % (arr[m],(i-arr[m])*rat[m]))
#         i=arr[m]
# print (r)

# import math
# help(math)
# dir(math)

import random
print(dir(random))

print(random.random())

