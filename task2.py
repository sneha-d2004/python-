#even and odd
for i in range(2):
    num=7
if num%2==0:
    print("even")
else:
    print("odd")

#positive,negitive,or zero
for i in range(3):
    num=7
if num>0:
    print("positive")
elif(num<0):
    print("negitive")
else:
    print("zero")

# divisibilly checker 3 and 5
for x in range(3):
    i=5
    if(i%5==0 and  i%3==0):
        print("divisible on 3 and 5")
    elif(i%5==0):
        print("divisible on 5")
    elif(i%3==0):
        print("divisible on 3")
    else:
        print("not a divisible")

#largest number
for i in range(3):
    a=8
    b=7
    if a<b:
        print("a is larger",a)
    elif a>b:
        print("b is larger",b)

#Age group classifier
for i in range(3):
    age=16
    if age<=13:
        print("child")
    elif age<=20:
        print("teen")
    elif age>=20:
        print("adult") 
    else:
        print("young") 

#triangle validity checker
s1=15
s2=10
s3=23
if s1+s2>=s3 or s2+s3>=s1 or s3+s1>=s1:
    print("validty triangle")
else:
    print("not a validity triangle")

#print each charecter of a string
name="hello"
for chr in name:
    print(chr, end=" ")


#print even numbers from  1to 20
for i in range(1,21):
    if i%2==0:
       print(i,end=" ") 
 

#sum of first 10 natural numbers
count=0
for i in range(1,11):
    count+=i 
print("sum of first 10 natural numbers",count)

#print elements in a set
list1=["pen","pencile","eraser"]
for i in list1:
    print(i)

#print common elements in two list
list1=["pen","pencile","eraser","paper"]    
list2=["pen","pencile","eraser","book"]
for i in list1:
    if i in list2:
        print(i)

#print all elements in a set
my_self={"apple","banana","cherry"} 
for i in my_self:
    print(i) 

#count how many items are in a set using a loop
count=0
colors={"red","blue","green","yellow"}
for i in colors:
    count+=1
    print("number of items in the set",count)

#print all keys and values in a dictionary
person={"name":"sneha","age":21,"city":"hyb"} 
for i,value in person.items():
    print(i,":",value)  
#count how many values in a dictionary are greater than 50
count=0
score={"math":45,"english":55,"science":80,"history":40}
for i in score:
    if score[i]>50:
        count+=1
        print("number of subjects",count)

#create a new dictionary with only items where the value is even 
data={"a":1,"b":4,"c":6,"d":3} 
for key,value in data.items():
    if value%2==0:
        print("even value",value)       


    





    