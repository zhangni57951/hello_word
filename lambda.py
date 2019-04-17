# def add (x,y):
#     return x+y
# print(add(3,5))
#
# add2 =lambda x,y:x+y
# print(add2(7,8))

# def is_odd(n):
#     return n % 2 == 0
# newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(list(newlist))
from functools import reduce

a = [1,2,3,4,5,6,7]

# list1 =filter(lambda x:x>3 ,a)
# print(list(list1))

b=[1,2,3,4,5,6,7]
newlist =map(lambda x,y:x+y, a,b)
print(list(newlist))
# def add(x,y):
#     return x+y
# print(reduce(add,a))
#
# c=[2,3,5,6]
# zipped = zip(a,b)
# print(list(zip(*zipped)))
# print(list(zipped))
#
# print(list(zip(a,c)))
# print(list(zip(*zipped)))
# print(list(zip(*zip(a,b))))