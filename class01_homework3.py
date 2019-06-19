print("請輸入要求的質數範圍")
start_number = int(input("輸入起始值(最小要1):"))
end_number = int(input("輸入結束值:"))

Prime_number = []       #放質數的陣列
for i in range(start_number,end_number+1):
    for j in range(2,i+1):  #把每次取的的數字從2開始做除法直到除到自己
        if (i % j == 0 ):   #判斷取到的數字除於除數，餘數是否為零
            if (i == j ):   #如果餘數為零，被除法和除法是否相等，如果相等就是質數
                Prime_number.append(i)
            else :
                break
print(Prime_number)

