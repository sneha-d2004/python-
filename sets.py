sets={1,2,3,4,5}
print(type(sets))
sets.add(6)
print(sets)
sets.update({6,7,8,9})
print(sets)
sets.remove(8)
print(sets) 
sets.pop()
print(sets)

s1={1,2,3,4,5}
s2={5,6,7}
print(s1.union(s2))#is nothing but all
print(s1.intersection(s2))#is nothing but commn
print(s1.difference(s2))#commn values are remove print the s1
print(s1.issuperset(s2))#s1 value s2 values are same ouput is true not a smae out put is false


for i in {1,2,3,4}:
    print(i)
print(type(i))



names={"sneha","chanti",True,}
print(names)
names.pop()
print(names)
names.add("nani")
print(names)
names.add("prashanth")
print(names)