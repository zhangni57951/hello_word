# coding=gbk
# try:
#     year = int(input("inputyear:"))
# except ValueError:
#     print('���Ҫ��������')
try:
    a = open("name.txt")
except Exception as e:
    print(e)
finally:
    a.close()

