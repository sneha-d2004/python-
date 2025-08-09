fruits =["apple","mango","banana"]
print(fruits[2])
print(fruits)
fruits[1]="pineapple"
print(fruits[1])
print(fruits)


x=["harish","naresh","suresh","mahesh"]
print(id(x))
x[2]="kiran"
print(x[2])
print(x)
print(id(x))


date=[1,2,[4,5],[6,7],8,["something"]]
print(date[2][0])
print(date[3][0])
print(date[5][0][2])

mixed=[1,2,"hi",12.5,True]
print(mixed)
print(type(mixed))
print(type(mixed[0]))
print(type(mixed[2]))
