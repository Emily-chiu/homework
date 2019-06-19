from random import *

b = []  # b 放 20 個隨機抓的數字
x = []  # x 放 兩位數的數字
y = []  # y 放偶數
z = []  # z 放奇數
a=1
while a <= 20:
    number = randint(1,201)
    if number not in b:     #判斷隨機取出的數字有沒有重複
        b.append(number)    #放進b陣列
        if number > 9 and number < 100: #判斷隨機取出的數字是不是二位數
            x.append(number) #放進x陣列
            if number%2 == 0:       #判斷隨機取出的數字除餘二是不是餘0
                y.append(number)    #放進y陣列
            else:
                z.append(number)    #放進z陣列
        
        a=a+1
    
print("隨機取出的20個數字" , b)
print("陣列長度:" , len(b))
print("兩位數:" , x)
print("偶數:" , y)
print("奇數:" , z)