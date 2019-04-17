
xingzuo = ("金牛座","白羊座","水瓶座","摩羯座","狮子座","天蝎座")
zodiac_days = ((1,20),(2,19),(3,15),(4,18),(5,21),(7,20))
(month,day)=(4,15)
zodiac_day = filter(lambda x:x<=(month,day),zodiac_days)
print(zodiac_day)
print(list(filter(lambda x:x<=(month,day),zodiac_days)))
print(list(zodiac_day))
print(len(list((zodiac_day))))
zodiac = len(list(zodiac_day))%6
print(xingzuo[zodiac])