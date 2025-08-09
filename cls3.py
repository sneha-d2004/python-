i=2
while i<=20:
    print(i)
    i+=2

i=10
while i<=100:
    print(i)
    i+=10 
#reverse from 1 to 10
i=10
while i>=1:
    print(i)
    i-=1  

i=1
total=0
while i<=0:
    total+=1
    i+=1
print("sum is:", total)


def table(n):
    for i in range(1,11):
        print(f"{n}x{i}={n*i}")
table(3) 

for i in range(10):
    print("supraja")


for i in range(5):
    str=" "
for j in range(i+1):
    str+="*"
    print(str) 

name="sneha"
for i in range(len(name)):
	print(name[:i+1])

name="sneha"
for i in range(len(name)):
    print(name[i]*(i+1)) 

name1="sneha"
name2="prashanth"
sum=name1+name2
print(sum)

num=7
sum=0
if num%2==0:
    sum+=num
    print(num,"perfet number")
else:
    print(num,"not a perfet") 

name="sNEha"
count=0
for i in name:
    if i. isupper():
        count+=1
        print(i," upper")
    else:
        print(i," lower")
count=0
name="prashanth"
for i in name:
    count+=1
    if i. islower(): 
       print(i, "lower")
    else:
        print(i,"upper") 

name ="sneha"
for i in name:
    if i. isupper() and i. islower():
        print(i,"upper",end="")
    else:
        print(i,"lower" ,end=" ") 

num=[1,2,3,4,5]
smaller=num[1]
for i in num:
    if i<smaller:
        print(i,'smaller')
    else:i>smaller
    print(i,"larger")    
    
print(smaller)

num= 23
sum=0
for i in range(1, num):
    if num%i==0:
        sum+=i 
if num==sum:
    print("perfect number")
else:
    print("not a perfect number") 

num=28
sum=0
for i in range(1,num+1):
    if i*i==num:
        print("suare")
else:
    print("not a suare") 

num=67
sum=0
for i in range(1,num):
    if num%i==0:
        sum+=1
if num==sum:
    print("perfect ")
else:
    print("perfect not") 

num=20
sunny = False
for i in range(1, num):
    if(i**2==num+1):
       sunny=True
       break
if sunny:
    print("sunnt") 
else:
    print("not a sunny")
    
                                                   









