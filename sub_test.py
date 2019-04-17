#encoding:utf-8
import re
phone='123-456-789 #这是电话号码'
p2 = re.sub(r'#.*$','',phone)
print(p2)
p3=re.sub(r'\D','',p2)
print(p3)