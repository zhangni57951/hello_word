from decimal import Decimal
#encoding:utf-8
# def  func(a,b,c):
#     print("第一个参数是：%a"%a)
#     print("第二个参数是：%a" % b)
#     print("第三个参数是：%a" % c)
# func(a=2,c=5,b=4)


# def func(first,*other):
#     print(len(first)+len(other))
# func("abc")


# a=123
# def func():
#     global a
#     a=789
#     print(a)
# func()
# print(a)

# for i in range(10,20,2):
#      print(i)
# list1=[1,2,3]
# it=iter(list1)
# print(next(it))
# print(next(it))
# print(next(it))
# try:
#     print(next(it))
# except Exception as e:
#     print("数据越界")

# def frange(start,stop,step):
#     x=start
#     while x<stop:
#         yield x
#         x+=step
# for i in frange(10,20,0.2):
#     print(i)
#

a =Decimal(1.231)
b =Decimal(0.2)
print(a+b+b)