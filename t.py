#WAP to check whether given num is armstrong or not
num=153
sum=0
temp=num
n=(len(str(num)))
while temp>0:
    digit=temp%10
    sum+=digit**n 
    temp=temp//10
if sum==num:
    print("armstrong number")
else:
    print("not a armstrong nuber")    
#Check what is neon number and sunny number
#sunny number:
num=15
sunny=False
for x in range(1,num):
    if(x**2==num+1):
        sunny=True
if sunny:
    print("it is sunny number")
else:
    print("not a sunny number") 
#neno number:
num=9
square=num**2
sum=0
while(square>0):
    id =square%10
    sum+=id
    square=square//10
if (sum==num):
    print("it is neno")
else:
    print("it is not a neno")               


