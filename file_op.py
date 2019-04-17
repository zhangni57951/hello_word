file=open("name.txt","a")
file.write("诸葛亮|"+"曹操|"+"刘备|" )
file.close()
# file3=open("name.txt")
# print(file3.tell())
# #file3.read(1)
# print("读取到一个字符%s" % file3.read(1))
# print("当前文件指针位置%s" % file3.tell())
# file3.seek(0)
# print("当前文件指针位置%s" % file3.tell())
# #file3.read(1)
# print("读取到一个字符%s"%file3.read(1))
# print("当前文件指针位置%s" % file3.tell())
#
# file4=open("name.txt")
# print(file4.tell())
# for line in file4.readlines():
#     print(line)
#     #file4.read(5)
#     print("当前文件指针位置%s" %file4.tell())
#     file4.seek(0)
#     print("========")

file6 = open("name.txt","rb")
print('当前文件指针的位置 %s' %file6.tell())
print ( '当前读取到了一个字符，字符的内容是 %s' %file6.read(1))
print('当前文件指针的位置 %s' %file6.tell())
# 第一个参数代表偏移位置，第二个参数  0 表示从文件开头偏移  1表示从当前位置偏移，   2 从文件结尾
file6.seek(5,0)
print('我们进行了seek操作')
print('当前文件指针的位置 %s' %file6.tell())
print ( '当前读取到了一个字符，字符的内容是 %s' %file6.read(1))
print('当前文件指针的位置 %s' %file6.tell())
file6.close()





