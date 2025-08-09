'''str1="SNEhaNANIchaNTI"
count1=0
count2=0
for char in str1:
    if char. isupper():
        print(char,"is upper")
        count1+=1
    else:
        print(char,"is lower")
    count2+=1'''
                   
                  

#add two numbers:
'''a=4
b=3
sum=a+b
print("The sum is:",sum)''' 

'''num=0
if num>0:
    print("Positive number")
elif num<0:
    print("Negitive number")
else:
    print("zero")'''

'''for i in range(1,10):
    print(i)''' 

'''total=0
for i in range(1,101):
    total+=i
    print("sum is:",total)'''

list=[1,2,3,4,5]
print(list)
print(list[3])
list[3]=9
print(list)
list.append(7)
print(list)
#list.clear()
#print(list)
list.remove(3)
print(list)   
print(len(list))
for i in list:
    print(i,end=" ")
list=[1,1,2,3,4,4,7]
empty=[]
for i in list:
    if i not in empty:
        empty.append(i)
    print(empty)

list=[1,2,3,4,5]
#total=sum(list)
total=dir(list)
print("sum",total)

num=[1,2,3,4]
for x in num:
    seqer=x**2
    print(seqer)

num=[2,3,4,5,6]
for x in num:
    if x%2==0:
        print("even",x)
    else:
        print("odd",x)

#convert list to string
my_list=["hello", "world"]
string=",".join(my_list)
print(string)

#convert string to list
s="hello"
l=s.split()
print(l)

for i in range(1,11):
    print(f"2*{i}={2*i}")

def table(num):
    for i in range(1,21):
        print(f"{num}*{i}={num*i}") 
table(8)

def add(a,b):
    print(a+b)
add(5,8)

#swap two elements
num=[1,2,3,4]
num[2],num[1]=num[1],num[2]
print(num)
        
        
#armstrong number
u=1234
v=1*4+2*4+3*4+4*4
if u==v:
    print("armstrong")
else:
    print('no') 


number=12345
if number>0:
    print("positive")
elif number<0:
    print("negive")
else:
    print("it is zero")
if number%2==0:
    print("divible2")
else:
    print("no")

#find the index
list1=[10,20,30,40]
find=list1.index(40)
print(find)

#sort
list=[10,70,60,80]
num.sort()
print(num)
for i in list:
    print(i)

#sort descending order
list=[10,25,70,40,30] 
num.sort(reverse=True) 
print(num) 

#conver to list ta a string with commas
num=[10,20,30,40,60,70]
name=",".join(map(str,num))#(or)#[str(num) for num in nums]
print(name)

name=["hello,sneha"]
con=",".join(name)
print(con)

num=[1,2,3,4,5]
con=",".join(map(str,num))
print(con)
if con in num:
    if num%2==0:
        print("even")
    else:
        print("odd")    






    

    


