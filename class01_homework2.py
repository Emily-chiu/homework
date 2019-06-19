length = input("請輸入要畫的菱形規格:")
#length = 20    #決定繪製菱形的大小
row = int(length)//2
i=0
#菱形上半部
for k in range(row):
    if (2*k-1)<0:
        print (" "*(row-i) + "*")
    else:
        print(" "*(row-i) + "*" + " "*(2*k-1) + "*")
    i=i+1


#菱形下半部
for j in range(row,-1,-1):
    if (2*j-1)<0:
        print (" "*(row-i) + "*" +" ")
    else:
        print(" "*(row-i) + "*" + " "*(2*j-1) + "*")
    i=i-1


    