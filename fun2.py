def add(a,b):
    print(a+b)
add(2,8)


def sequare():
    num=2
    return num* num
print(sequare())

def sequare(num):
    print(num*num)
sequare(4) 

def greater(a,b):
    if a>b:
        print("a is greater")
    else:
        print("b is greater") 
greater(2,8)

def even_or_odd(num):
    if num%2==0:
        print("even")
    else:
        print("odd")    
even_or_odd(4)

def prime(num):
    if num%2!=0:
        print("prime",num)
    else:
        print("not a prime",num)
prime(3) 

def table(num):
    for i in range(1,11):
        print(f"{i}*{num} = {i*num}")
table(2)

def divisable(a):
    if a%3==0 and a%5==0:
       print("it is divisable 3,5")
    elif a%3==0:
        print("it is divisible 3")
    elif a%5==0:
        print(" it is divisable 5")
    else:
        print("it is not a divisible")
divisable(15)

def even(number):
    count=0
    for num in number:
        if num%2==0:
            count+=1
    return count
my_list=[1,2,3,4,5,8] 
print(even(my_list))           







