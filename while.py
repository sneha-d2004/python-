#y=0
#while(y<=10):
    #print(y)
    #y+=1

#list=[4,6,8,912,34,56] 
#for x in list:
    #print(x)
#x=0
#while(x<len(list)):
    #print(list[x])
    #x+=1 

#flashsale=True
#while(flashsale):
    #print("do shopping with more offers")

#num=2
#while(num%2==0 and num<=20):
    #print(num)
    #num+=2  

#num=1
#while(num<=20):
    #print(num)
    #num+=1 


#num=1
#while(num<=20):
    #if(num%2==0):
        #print(num)
        #num+=1 

'''x1=["a","b","e","d","e"]
for x in range(len(x1)-1,-1,-1):
  print(x1[x])'''

'''str="hello"
for char in range(len(str)-1,-1,-1):
    print(str[char])'''

'''str="hello"
op=""
for char in range(len(str)-1,-1,-1):
    op+=str[char]
    print(op) '''     

'''str="sneha"
op=""
for char in range(len(str)-1,-1,-1):
    if(op==str):
        print("it is plaindrome")
    else:
        print("it is not a plaindrome") '''


num=123
sum=0
while(num>0):
    id=num%10
    sum+=id
    num=num//10
    print(sum)


num=125
sum=0
while(num>0):
    id=num%10
    sum+=id**2
    num=num//10
    print(sum)


count=0
num=12345
while(num>0):
    id=num%10
    count+=1
    num=num//10
    print(count)

num=123654
rev=0
while(num>0):
    id=num%10
    rev=rev*10+id
    num=num//10
    print(rev)

num=1289507545
covrt=str(num)
for x in covrt:
    print(x) 

num=125
rev=0
while num>0:
    id=num%10
    rev=rev*10+id
    num=num//10
print(rev) 

num=123654
num1=num
rev=0
if(num%10==0):
    while(num>0):
        id=num%10
        rev=rev*10+id
        num=num//10
        print(rev)
        if(num1==rev):
            print("given num is palindome")
        else:
            print("gives num is not a palindome")


i=1
while i <=5:
    print(i)
    i+=1 

i=1
while i<=10:
    print(i)
    i+=1

i=1
total=0
while i<=10:
    total+=i 
    i +=1
    print(total) 

i=0
while i<=10:
    i+=1
    if i==5:
        continue

    print(i)

i=1
while i<=9:

    print(i)
    i+=1
    
i=1
while i<=21:
    print(i)
    i+=1  

num=1234
rev=0
while num!=0:
    digit = num%10
    rev=rev*10+digit 
    num=num//10 
print(rev)   

for i in range(5):
    str=""
    for j in range(i+1):
        str+="*" 
    print(str)

num=1
sum=0
while num<=4:
    num+=1
    sum+=num
print(sum)

num=4
fact=1
while num!=0:
    fact =fact*num
    num= num-1 
print(fact)

i=1
while i<=5:
    j=1
    while j<=i:
        print(j,end="")
        j+=1
    print()
    i+=1

'''for i in range(5):
    num=" "
    for j in range(i+1):
        num+=num(j+1)
    print(num)''' 

i=1
while i<=10:
    i+=1
print(i)

i=1
while i<=20:
    if i%2==0:
        print(i)
    i+=1

i=1
total=0
while i<=10:
    total+=i 
    i+=1
print(total) 

i=1
while i<=10:
    if i%2!=0:
        print(i)
    i+=1

i=1
total=0
while i<20:
    total+=i 
    i+=1
print(total) 


num=4321
rev=0
while num!=0:
    digit =num%10
    rev=rev*10+digit
    num = num//10
    print(rev) 

name ="sneha"
rev=0
rev =name[::-1] 
if name == rev:
    print("palindrome")
else:
    print("not a palindrome")


i=4
fact=1
while i!=0:
    fact=fact*i 
    i=i-1
print(fact) 

num=121
rev=0
while num>0:
    digit =num%10
    rev=rev*10+digit
    num=num//10
if rev == num:
    print("palindrome")
else:
    print("not a palindrome")    
      
