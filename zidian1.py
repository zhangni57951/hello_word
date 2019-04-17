shengxiao = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
xingzuo = (u"摩羯座", u"水瓶座", u"双鱼座", u"白羊座", u"金牛座", u"双子座",
            u"巨蟹座", u"狮子座", u"处女座", u"天秤座", u"天蝎座", u"射手座")
yuefen = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
              (7, 23), (8, 23),(9, 23), (10, 23), (11, 23), (12, 23) )
# shengxiao_num ={}
# for i in shengxiao:
#     shengxiao_num[i]=0

shengxiao_num={i:0 for i in shengxiao}#字典推导式写法同上面语句
# xingzuo_num = {}
# for i in xingzuo:
#     xingzuo_num[i]=0
xingzuo_num ={i:0 for i in xingzuo }

while True :
    year = int(input("请输入年份:"))
    month = int(input("请输入月份:"))
    day = int(input("请输入日期:"))
    n =0
    while yuefen[n] < (month , day):
        if month==12 and day>23:
            break
        elif month == 12 and day > 23:
            print(xingzuo[0])
            break

        elif month>12 or day>31:
            print("请输入正确日期")
            break
        n += 1
    #打印星座和生肖
    print(xingzuo[n])
    print("%s年的生肖是%s" % (year,shengxiao[year % 12]))
    #生肖、星座计数
    shengxiao_num[shengxiao[year%12]] +=1
    xingzuo_num[xingzuo[n]] +=1
    #输入生肖和星座的统计信息
    for each_key in shengxiao_num.keys():
        print("生肖%s有%d个" % (each_key,shengxiao_num[each_key]))
    for each_key in xingzuo_num.keys():
        print("星座%s有%d个" % (each_key,xingzuo_num[each_key]))
