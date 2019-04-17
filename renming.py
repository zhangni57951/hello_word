# encoding:utf-8
import re
def find_item(hero):
    with open("name.txt") as f:
        data = f.read().replace("|","")
        name_num = re.findall(hero,data)
 #       print("主角 %s 出现 %s 次"%(hero,len(name_num)))
    return  len(name_num)

name_dict = {}
with open("name.txt",encoding='cp936') as f:
    for line in f:
        names = line.split("|")
        for n in names:
            if n == "":
                continue
            print(n)
            name_num = find_item(n)
            name_dict[n] = name_num
print(name_dict)
# def func(filename):
#     print(open(filename).read().split("|"))
# func("name.txt")