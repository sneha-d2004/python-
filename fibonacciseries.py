a=1
b=2
for i in range(10):
    c=a+b
    a=b 
    b=c 
    print(c)


a=0
b=3
for i in range(2):
    c=a+b 
    a=b 
    b=c 
    print(c)  

num=2
if num%2==0:
    print("not a prime number")
else:
    print(" prime nuber")

count=0
for i in range(1,11):
    if i%2==0:
        print("not a prime nnumber",i)
        count+=1 
    else:
        print("prime number",i) 

a=2
b=7
#print("select operation:+,-,*,")
operator="-"
if operator=="+":
    print("result",a+b)
elif operator=="-":
    print("result",a-b) 
elif operator=="*":
    print("result",a*b) 
else:
    print("invalid operator")

                              
