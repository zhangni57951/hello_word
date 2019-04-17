alist=[]
for i in range(1,11):
    if (i%2 == 0):
        alist.append(i*i)
print(alist)

alist=[i*i for i in range(1,11) if(i%2==0)]
print(alist)
