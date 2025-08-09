num=int(input("Enter the number:"))
if num%2==0:
    print("Even number")
else:
    print("Odd number")

age=14
 if(age>=18):
    print("you are eligible")
else:
    print("you are not a eligible") 


year=int(input("Enter a year:"))
if(year%4==0):
    if (year%100!=0 or year%400==0):
        print(f"{year} is a leap")
    else:
        print(f"{year} is a not a leap")
else:
    print(f"{year} is a not a leap")

sub1=int(input("Enter markes for subject1:")) 
sub2=int(input("Enter markes for subject2:"))
sub3=int(input("Enter markes for subject3:"))
if(sub1>=35 and sub2>=35 and sub3>=35): 
    print("student is pass") 
else:
    print("student is faill")

a=7
b=4
c=9
if(a<=b and b<=c):
    print("small number:", a) 
elif(b<=c and b<=a):
     print("small number:", b)  
else:
    print("small number:",c)


a=7
b=4
c=9
if(a>=b and a>=c):
    print("bigest number:",a)
elif(b>=c and b>=c):
    print("bigest number:",b)
else:
    print("bigest number:",c)  


x=3
if x>5:
    print("x is greater")
else:
    print("x is less")


for i in range(1,101):
    if i%2!=0:
        print(i, end =" ")


for i in range(1,11):
    if i%2==0:
        print(i, end = " ")
for i in range(1,51):
    if (i%3==0 and i%5==0):
          print(i,"mutiple of both")
    elif(i%5==0):
        print(i, "mutiple of 5")
    elif(i%3==0):
        print(i, "multipe of 3")


count=0
for i in range(1,10):
    if(i%3==0 and i%7==0):
        print(i)
        count+=1
    print(count)               
                             
    



      



    