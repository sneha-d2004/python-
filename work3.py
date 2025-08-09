list1=[9,7,6,4]
num=3
if num in list1:
    print("number is found")
else:
    print("number is not found")    

vowels=["A","E","I","O","U"] 
word="B"   
if word in vowels:
    print("it is vowel")
else:
    print("it not vowel")

tuple="hello"
print(len(tuple))

def add(a,b):
    print(a+b)
add(6,9)

 
tuple="prashanth"
words=tuple.split()
for i in words:
    print(f"{i}:{len(i)}")
print("total charecters:",len(tuple))


sentence="my name is sneha"
words=sentence.split()
for word in words:
    print(f"{word}:{len(word)} characters")


list=[1,2,3,4,5,6,7,8,9]
for i in list:
    if(i%2==0):
        print("even numbers", i)
    else:
        print("odd numbers", i) 

age_list=[44,3,18,16,20] 
for x in age_list:
    if x>=18:
        print("u are eligible", x)
    else:
        print("u are not eligible",x)
    
word="sneha"
print(word.upper())
  
details={"name":"sneha","age":21}
print(details)

a=4
b=8
sum=a+b
print(sum)

num=4
i=1
while i<=10:
    print(f"{num}*{i}={num*i}")
    i+=1

def table(n):
    for i in range(1,11):
        print(f"{n}*{i}={n*i}")
table(3) 

def mul():
    for i in range(1,11):
        if i%2==0: 
          print(i)
        else:
          print("not a", i)    
mul()  

a=12
print(a//10)


num=9
if num%2==0:
    print("even number")
else:
    print("odd number") 

num=-1
if num>0:
    print("positive")
elif num<0:
    print("negitive")
else:
    print("zero") 

a=4
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)

num=100
if num%5==0 and num%10==0:
    print("num is divisible")
else:
    print("num is not divisible",)


vowels=["a","e","i","o","u"] 
word="c" 
if word in vowels:
    print(" it is vowel") 
else:
    print("it is not a vowel") 

list1=[2,3,4,5,6,7,7]
empty=[]
for i in list1:
        empty.append(i)
        print(empty) 

# sunny number:-
num=15 
sunny =False
for x in range(1, num):
    if (x**2==num+1):                  
        sunny =True
        break
if  sunny:
    print("it is sunny")
else:
    print("it is not a sunny")            


   
