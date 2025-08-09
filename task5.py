#1. Add all elements of a list.
list1=[1,2,3,4,5]
print(sum(list1))
#2. Find max and min in a list.
list=[4,6,8,1,2]
print(max(list))
print(min(list))
#3. Count even and odd numbers in a list.
count1=0
count2=0
list2=[1,4,5,8,7,6]
for i in list2:
    if i%2==0:
        print(i,"even")
        count1+=1
    else:
        print(i,"odd") 
        count2+=1    

#4. Reverse a list without using reverse().
list=[1,4,5,6,9]
rev=list[::-1]
print(rev)
#5. Remove duplicates from list.
list3=[1,1,2,2,3,4,4,5,6]
unique=list(set(list3))
print(unique)
#6. Sort a list of strings by length.
words=["apple","bat","banana","dog"]
sorted_words=sorted(words,key=len)
print(sorted_words)
#7. Find the second largest number in the list.
list2=[10,20,4,45,99]
list2=list(set(list2))
list2.sort()
print(list2[-2])
#8. Find sum of all nested list elements.
lis1=[[1,2],[3,4],[5]]
total=sum(sum(i) for i in lis1)
print(total)
#9. Check if two lists are equal.
a=[1,2,3]
b=[1,2,3]
print(a==b)
#10. Merge two lists and sort them.
a=[3,1,4]
b=[2,5]
merged=sorted(a+b)
print(merged)
#11. Convert tuple to list and back.
t=(1,2,3)
lis=list(t)
t2=tuple(lis)
prit(lis,t2)
#12. Check if the tuple contains a value.
t=(1,2,3,4)
print(3 in t)
#13. Unpack a tuple into variables
t=(1,2,3)
a,b,c=t
print(a,b,c)
#14. Create a list of squares using comprehension.
suares=[x**2 for x in range(1,6)]
print(suares)
#15. Count how many times a number appears in a list
list1=[1,2,2,3,2,4]
print(list1.count(2))
#16. Find index of element in tuple.
t=(5,10,15)
print(t.index(10))
#17. Slice a tuple from index 1 to 3.
t=(1,2,3,4,5)
print(t[1:4])
#18. Replace element in list with another.
list=[1,9,6,3,7]
list[2]=3
print(list)
#19. Filter only strings from mixed lists.
lst = [1, 'apple', 3.5, 'banana', True]
strings = [x for x in lst if isinstance(x, str)]
print(strings)
#20. Take input of the list from the user and print sum.
lst = list(map(int, input("Enter numbers separated by space: ").split()))
print(sum(lst))
