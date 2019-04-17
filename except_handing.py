# coding=gbk
# try:
#     year = int(input("inputyear:"))
# except ValueError:
#     print('年份要输入数字')
try:
    a = open("name.txt")
except Exception as e:
    print(e)
finally:
    a.close()

