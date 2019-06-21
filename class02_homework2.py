#算出每個f(n)的值
def fibonacci(number):
    if ( number == 0 or number == 1):
        return number
        
    else:
        return  fibonacci(number-1) + fibonacci(number-2)

#遞減，算出從f(0)開始之後的值，並一個一個印出來
# def loop(i):
#     if (i == 0):
#         print("F(",i,")= "  , fibonacci(i))
    
#     elif(i == 1):
#         print("F(",i,")= "  , fibonacci(i))
#         return loop(i -1 )
#     else:
#         print("F(" , i ,") = " , "F(" , i-2 , ") + " , "F(" , i-1 , ") = " ,fibonacci(i))
#         return loop(i -1 )

# number = int(input("請輸入要算出的費氏數列:"))
# loop(number-1)

#遞增，算出從f(0)開始之後的值，並一個一個印出來
def loop(a , i):
    if (a == 0 or a == 1):
        print("F(" , a , ")= "  , fibonacci(a))
        return loop(a = (a+1) , i = i)

    elif (a < i):
        print("F(" , a ,") = " , "F(" , a-2 , ") + " , "F(" , a-1 , ") = " ,fibonacci(a))
        return loop(a = (a+1) , i = i )

number = int(input("請輸入要算出的費氏數列:"))
loop(a = 0 , i = (number))

#用for迴圈，算出從f(0)開始之後的值，並一個一個印出來
# for n in range(number):
#     if (n == 0 or n == 1):
#         print("Fib(" , n , ") = ",fibonacci(n))

#     else:
#         print("Fib(", n ,") = Fib(", n-2 ,") + Fib(", n-1 ,") = ",fibonacci(n))