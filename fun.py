def sayhello():
    print("hello sneha")
sayhello() 

def details(name,pin):
    print(name)
    print(pin)
details("sneha",521125)

def add():
    a=53
    b=12
    print(a+b)
add()   

#def add(*numbers):
   # print(sum(numbers))
    #add(1,2,3,4,5,6,7,)
#add()

def name(name,clg,roll):
    print(name)
    print(roll)
    print(clg)
name("sneha","st mary's womes clg",21)

def fruits(name,cost):
    print(name)
    print(cost)
fruits("apple",20)

def num(a,b,c):
    print("this is numbers:",a,b,c)
num(4,5,6)

def sequare():
    num=5
    return num*num
print(sequare())

def sequare():
    num=6
    return num*2
print(sequare()) 

def cube():
    num=3*3
    return num
print(cube())  

def detalis(name):
    print(name)
detalis("sneha")

def add(a,b):
    print("sum:",a+b)
add(3,4)  

def sub(a,b):
    print("subtraction:",a-b)
sub(9,3)

def is_palindrome(name):
   return name == name[::-1]
word="sneha" 
if is_palindrome (word):  
   print("palindrome")
else:   
   print(" not palindrome")

def fibonaccise(a,b):
    for fibonaccise in range(10):
        c=a+b
        print(c)
        a=c 
        c=a 
        if c%2==0:
            print("even")
        else:
            print(" not a even")
            if c%2!=0:
                print("prime")
            else:
                print("not a prime")    
fibonaccise(1,2) 

def prime():
    for prime in range(10):
        if prime%2!=0:
           print("prime number",prime)
        else:
          print("not a prime",prime)
prime()  

def details(name):
    print(len(name))
    print(type(name))
    print(list(name))
    print(tuple(name))
    print(set(name))
    print(name.count("h"))
    
    name1="motupalli"
    add=(name1+name)
    print(add)
    print(add.upper())
    if len(name)%2==0:
        print("even")
    else:
        print("odd")    

details("prashanth") 

def sequares(a,b):
    for sequares in range(10):
        c=a*a
        d=b*b 
        e=c,d
    print(c)
    
    print(e)
sequares(4,6)        
  


