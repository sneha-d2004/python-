list=["hi","hello","wellcome","some","python"]
for x in list:
    print(x)
    print(x[0])

list=["javascript","python","html","css","java","sql","hello","hi"]
for x in range(len(list)-1,-1,-1):
    print(x)
    print(list[x])


list=["javascript","python","html","css","java","sql","hello","hi"]
for x in range(1,len(list)-1):
    print(list[x])

list=["javascript","python","html","css","java","sql","hello","hi"]
for x in range(1,len(list)-2+1):
    print(list[x])



list=["king","queen","minister","assistance","empolyee"]
for x in list:
    if(len(x)%2==0):
        print(x) 

list=["king","queen","minister","assistance","empolyee"]
for x in list:
    if(len(x)%2==0):
        print(f"{x}is having lenght of {len(x)}")

dict={"name":"sneha","gender":"female","age":21,"city":"hyb"} 
for x in dict:
    print(x)
    print(x,dict[x])
    print(dict[x])
    print(f"{x}:{dict[x]}")

def table(n):
    for i in range(1,11):
        print(f"{n}x{i}={n*i}")
table(3)   

def name_add(name):
  print(name)
name_add("sneha")

#primenumbers
def is_prime(n):
 if n<=1:
    return False
    for i in range(2, int(n/2)+1):
        if n%i==0:
            return False
    return True
print("is_prime:",is_prime(2))



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







    