op=[x+2 for x in range(2,11)]
print(op)

op=[i+3 for i in range(1,11) if i%2==0]
print(op)

op=[i**2 for i in range(1,10)]
print(op)

list1=["sneha","nani","prashanth","palana"]
op=[i.upper() for i in list1]
print(op)

op=[x**2 for x in range(1,10) if x%2==0]
print(op)

list1=["apple","kiwi","banana","grapes"]
op1=[x.upper() for x in list1 if len(x)%2==0]
print(op1)

list1=["apple","kiwi","banana","grapes"]
def vowelcount(ip):
    count=0
    for x in ip:
        if (x in ["a","e","i","o","u"]):
            count+=1
    if(count%2==0):
       return True
    else:
      return False
op1=[x.upper() for x in list1 if vowelcount(x)]
print(op1)

num=5
sum=0
for i in range(1,num):
    if num%i==0:
        #print(i)
        sum+=i
if (sum==num):
     print("it is a perfect number",num)
else:
    print("it is not a perfect number",num)

'''num=4
sum=0
def perfectnumber(num): 
    for x in range(1,num):
        if num%x==0:
           sum+=x
    if (sum==num):
       return True                
    else:
       return False
op3=[x for x in range(1,50) if perfectnumber(x)]
print(op3)'''

op=[i for i in range(1,51) if i%2!=0]
print(op)

list1=["apple","kiwi","banana","grapes"]
for x in list1:
    #rev=""
    for i in range(len(x)-1,-1,-1):
        print(x[i])
        #rev+=x[i]
        #print(rev)  


