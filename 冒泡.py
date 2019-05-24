# Author :lixinhao
a = [1, 3, 10, 9, 21, 35, 4, 6]
b = range(1,len(a))[::-1]

for i in b:
    for j in range(1,i):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
    print("第 %s 轮交换后数据：%s" %(len(a)-i,a))
print(a)