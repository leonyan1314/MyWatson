
if __name__ == '__main__':
    str1="6,3,7,2"

    li = str1.split(",")
    print(li)
    print(li.sort())

#def ordy(arry)


##ordby("6,3,8,10")

'''
#递归算法:
def func(arg1,arg2):
    if arg1<10000:
        if arg1 == 0:
            print(arg1, arg2)
        arg3 = arg1 + arg2
        print(arg3)
        func(arg2, arg3)
func(0,1)
#冒泡排序算法
li = [13, 22, 6, 99, 11]

for i in range(1,5):
    for m in range(len(li)-i):
        if li[m] > li[m+1]:
            temp = li[m+1]
            li[m+1] = li[m]
            li[m] = temp

            print(li)
'''
