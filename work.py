n=int(input("enter the number:"))
n1=n
sum=0
p=(n)
while n>0:
    l1=n%10
    sum+=l1**p
    n=n//10
if sum==n1:
    print("it is armstrong number")
else:
    print("it is not a armstrong number") 

name="sneha","prashanth"
for x in range(len(name)-1,-1,-1):
    print(x)
    print(name[x])

n=3
for i in range(n):
    for j in range(n):
        print("#", end=" ") 
    print() 

for i in range(1,20):
    if i%2==0:
        print(i)

for i in range(1,10):
    print(i* i, end=" ")  


for i in range(6):
    print("hello python")

names=["apple","banana","mango"] 
for i in range(4):
    for x in names:
        print(names) 

n=5
for i in range(n,0,-1):
    print(i)


for i in range(1,101,5):
    print(i)  



name=5
for i in range(name):
    for j in range(name):
        print("sneha")
        print()





        

    
      
    