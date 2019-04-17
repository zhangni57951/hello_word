# def func(a,b):
#     def ary_y(x):
#         return a*x+b
#     return ary_y
# a = func(3,5)
# print(a(2))
# print(a(3))

def a_line(a,b):
    return lambda x:a*x+b
a=a_line(3,4)
print(a(10))