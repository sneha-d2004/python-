print("\thello word")# \t it means tab
print("hello\n word")# \n it means new line

#vowels
name="e"
if name in "aeiou":
    print("vowel") 
else:
    print("consonant")

names=["a","e","i","o","u"] 
word="r"
if word in names:
       print("vowel")  
else:
    print("consonant")

list1=[1,3,4,6,7] 
num=2
if num in list1:
    print("yes")
else:
    print("no")

list=[1,2,3,4,5,6,7]
sum=0
for i in list:
    if i%2==0:
        sum+=i
        print("sum of all digitis",sum)

for i in range(1,5):
    for j in range(1,i+1):
        print(j, end=' ')
    print()

name="python"
for i in range(1,len(name)+1):
    print(name[::i])

name="mom"
rev=name[::-1] 
if rev==name:
    print("palindrome")
else:
    print("not a palindrome")

name="mom"
rev=name[::-1]
print(rev)

name="mom"
print(name[1])

name="mom"
if len(name)%2==0:
    print("even")
else:
    print("odd")

name="sunny"
rev=name[::-1]
if len(name)%2==0:
    print("even")
else:
    print("odd")
rev==name
print(rev)


name="prashanth"
if len(name)%4==0 and len(name)%6==0:
   print("it is divisible")
else:
   print("it not a divisible")



t1=tuple(range(1,11))
op=[x**2 for x in t1 ]
print(op)


l1=[1,2,3,4]
conv=tuple(l1)
print(conv)

#perfect number:
num=6
sum=0
for i in range(1,num):
    if num%i==0:
        sum+=i 
if sum == num:
    print("perfect")
else:
    print("not a perfect")

#perfect square:
num=4
for i in range(1,num+1):
    if i*i == num:  
       print("perfect  square")
else:
    print("not a perfect square") 
  
 
num=153
s=1**3+5**3+3**3
if s==num:
    print("armstrong")
else:
    print("not a armstrong")  
 