# dicta = {'a':'aa','b':'bb','c':'cc'}
# dictb = zip(dicta.values(),dicta.keys())
# print(dict(dictb))
from dis import dis
# def counter(first=0):
#     cnt=first
#     def add_one():
#        # nonlocal cnt
#         cnt +=1
#         return cnt
#     return add_one
#dis(counter(3))
# num5  = counter(5)
# num10 = counter(10)
# print(num5())
# print(num5())
# print(num5())
# print(num10())
# print(num10())
#  闭包中引用的变量没有在闭包中，是全局变量，他也会去外层查找
# cnt2 = 1
# def counter():
#     def add_one():
#         a = cnt2 + 1
#        # print(a)
#         return a
#
#     return add_one
#
#
# add_one = counter()
# print(add_one())

def counter() -> object:
    count = 1

    def add_one():
        count += 1   #error
        return count

    return add_one
dis(counter())
