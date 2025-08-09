num=list(range(1,11))
print(num)

number=list(range(1,11))
add=[num**2 for num in number]
print(add)

num=list(range(1,11))
add=[number for number in num if number%2==0]
print(add)

num=list(range(1,11))
add=[number for number in num if number%2!=0]
print(add)

number=list(range(1,11))
maximum=max(number)
print(maximum)

number=list(range(1,11))
minmum=min(number)
print(minmum)

#dublicate value
num=[1,2,3,4,4]
unique=list(set(num))
print(unique)

colors=["red","green","green","yellow"]
print(colors)
print(len(colors))
colors.append("purpel")
print(colors)
colors.remove("green")
print(colors)

#check 
animals=["dog","cat","lion","bear"]
if "dog" in animals:
    print("dog is in the list")
else:
    print("dog is not in the list")
print(animals[3])
animals.append("zebera")
print(animals)
animals.remove("cat")
print(animals)
animals.sort(reverse=True)
print(animals)
animals.insert(2,"lion")#add an element specipic place in the index
print(animals)

num=[1,2,3,4,5]
add=sum(num)
print(add)

alphabetical=["a","d","y","p","e"]
alphabetical.sort()#assining
print(alphabetical)
alphabetical.sort(reverse=True)#dessining
print(alphabetical)
alphabetical.clear()
print(alphabetical)

#count occurrences of a number in a list
list1=[1,2,3,4,5,6,6]
count=list1.count(4)
print(count)

list1=[1,2,3,4,5,6,6]
add=sum(list1)
print(add)
num=min(list1)
print(num)   

z="sneha"
s=list(z)
print(s)

for i in range(100):
    print("I love you❤️ prashanth")

num=7
factorial=1
for i in range(1,num+1):
    factorial *= i
print(factorial)    


name="sneha"
for i in range(1,len(name)+1):
    print(name[:1])

l1=[1,3,4]
repeart=l1*3
print(repeart)
#convert to tuple to list:
t=(1,2,3,4)
s=list(t)
print(s)
for num in t:
    if num%2!=0:
        print("odd",num)



def square():
    num=int(input("enter the number"))
    return num*num
print(square())    