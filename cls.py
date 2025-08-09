num=int(input("Enter a number:"))
if num%2==0:
    print("Even number")
else:
    print("Odd number") 

num=int(input("Enter a number:"))
if num%5==0 and num%10!=0:
    print("satisfy")
else:
    print("not satisfy") 

a=4
b=7
if a>b :
    print("a is small") 
else:
   print("b is big") 


n=4
for i in range(n):
    for j in range(n,i+1):
        for j in range(j+1):
          print("*")
    print("*" *i)

n=7
for i in range(n):
    n=i 
    i=n 
    print("*"*i)



 
for i in range(6):
    op=0
    for j in range(i+1):
        op=op*10+j**2
    print(op)  

for i in range(6):
    op=0
    for j in range(1,i+1):
        op=op*10+j**2
    print(op)


op=1*10+1
print(op) 


   
        
    



    




       
