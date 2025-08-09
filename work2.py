val1=10
val2=3+4j
val3=20
print(int(val1))
#print(int(val2)) #gives error
print(int(val3))
print(int(val1+val3))
print(int(val1-val3))
print(int(val1*val3))


val1=10
val2="21"
val3=30
print(float(val2))
#print(float(val2+val1))
print(float(val1+val3))


val1=10
val2=20
print(complex(val1))
print(complex(val2,val1))
val3=complex(val1,val2)
print(complex(val3))
print(val3.real)



#Absolute:-
a=10.23
b=4+8j
c=19
d=20
print(abs(a),abs(b))
print(abs(c+d))

#Power:
a=63
b=4
print(pow(a,b))
print(pow(b,a))


#divmod:-
a=10
b=4
print(divmod(10,4))
print(a+b)
print(a*b)
print(a//a)
print(divmod(a,b))

#round:-
var1=10.4
var2=6.8
print(round(var1),round(var2))
val3=3.14159265
print(round(val3,))
val4=3.5
print(round(val3),round(val4))


#min and max:-
list1=[1,5,89,10,3,88]
list2=[100,200,6,8,9,2,]
print(min(list1),max(list1))
print(min(list2),max(list1))
   

print("my name is:sneha")  


for i in range(1,21,2):
    print(i)


a=33
b=20
c=11
if a>=b and a>=c:
    print("large number", a) 
elif(b>=c and b>=a) :
    print("large number", b)
else:
    print(" large number",c)  


a=3
b=33
if a>b:
    print("a is bigger:",a)
else:
    print("b is bigger:",b) 


num=5
if num%2==0:
    print("Even") 
else:
    print("odd") 

age=16
if age>=18:
    print("your are eligbule")
else:
    print("you are not eligibule")



i=1
while i<=10:
    print(i)
    i+=1    

markes=40
if markes>=90:
    print("grade is a")
elif markes>=80:
    print("grade is b")
elif markes>=70:
    print("grade is c")
elif markes>=60:
    print("grade is d")
else:
    print("faile")


a=87
b=21
if a>=b:
    print("largest number",a)
else:
    print("largest number",b) 


count=0
num=101
if num%2==0:
    print("not a prime number")
    count+=1
else:
    print("prime")

for i in range(1,31):
    if(i%5==0 and i%3==0):
        print("it is fizzbuzz")
    elif(i%5==0):
        print("it is buzz") 
    elif(i%3==0):
        print("it is fizz")
    else:
        print(i) 

total=0
for i in range(1,100):
    if i%2==0:
        total+=i
        print("even numbers from 1to 100", total)

                           

       



        


          

