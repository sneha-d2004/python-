#1. Create a tuple with 5 elements and print it.
tuple=(1,2,3,4,5)
print(tuple)
#2. Access the third element of a tuple.
tuple=(1,2,3,4,5,6,7)
print(tuple[3])
#3. Slice a tuple to get the first 3 elements.
t=(1,2,3,4,6,9)
sliceing=t[:3]
print(sliceing)
#4. Check if an item exists in a tuple.
t1=(1,2,3,4,5,6)
if 5 in t1:
    print("5 is exitsts in the",t1)
else:
    print("5 is not a exists",t1)    
#5. Concatenate two tuples.
tuple1=(1,2,3,4,5,6)
tuple2=(2,5,6,7,8)
add=tuple1+tuple2
print(add)
#6. Repeat a tuple three times.
t1=(1,3,6,8)
repeat=(t1*3)
print(repeat)
#7. Find the length of a tuple.
tuple=(5,8,9,10)
print(len(tuple))
#8. Convert a list into a tuple.
'''t=[1,4,7,8]
t2=tuple(t)
print(t2)'''
#9. Convert a tuple into a list.
'''t=(1,2,3,4,6)
t1=list(t)
print(t1)'''
#10. Find the index of an element in a tuple.
t1=(1,2,4,6,8)
print(t1.index(8))
#11. Count occurrences of an element in a tuple.
tuple2=(2,4,5,9,8,2)
print(tuple2.count(2))
#12. Create a nested tuple and access inner elements.
tuple=((1,2),(3,4),(5,6))
print(tuple[1][0])
#13. Check if all elements in a tuple are integers.
t=(1,2,4,3)
are_int=all(isinstance(i,int)for i in t)
print(are_int)
#14. Unpack a tuple into variables.
'''t=(1,2,3,4,5)
a,b,c,d,e=t 
print(a)
print(c)'''

#15. Swap values of two variables using a tuple.
z=8
u=6
z,u = u,z 
print(z,u)
#16. Iterate through a tuple using a loop.
t=(1,2,3,4,5)
for i in t:
    print(i)
#17. Find the max and min values in a numeric tuple.
tuple1=(9,4,5,7,8,4)
max=max(tuple1)
min=min(tuple1)
print(max)
print(min)
#18. Sort elements of a tuple (convert and sort).
#tuple is a immutabele so we cannot sort directly first you convert the tuple in a list
'''tuple1=(5,2,9,4,8,6)
convrt=list(tuple1)
convrt.sort()
sorted_tuple=tuple(convrt)
print(tuple1)'''
#19. Merge tuples of equal length into pairs.
'''a=(1,2)
b=("x","y","z")
print(tuple(zip(a,b)))'''
#20. Create a tuple of even numbers using range().
'''even=tuple(range(2,21,2))
print(even)
'''

even=tuple(range(3,31,3))
print(even)
