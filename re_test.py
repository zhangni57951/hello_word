#encoding:utf-8
# import re
# p=re.compile(r'(\d+)-(\d+)-(\d+)')   #r表示的是不转义
# print(p.match('2019-4-15').group(3))
# print(p.match('2019-4-15').groups())
# print(p.match('2019-4-15').group())
# year,month,day = p.match('2019-4-15').groups()
# print(year)
# p1 = re.compile('(\d+)-(\d+)-(\d+)')
# print('search1:',p1.search('asd2019-3-1sdf'))
# print('search2:',p1.search('asd2019-ab3-1df'))
# print('search3:',p1.search('asd2019-3sd-1df'))
import re
string = "x abc y 123 z 123"
pattern = re.compile(r'\d+')
#print(re.search(pattern,string))
print(pattern.search("x abc y 123 z 123"))
print(pattern.findall(string))