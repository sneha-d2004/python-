op= lambda:"hello"
print(op)
print(op())


op=lambda x:x-3
print(op(4))

op=lambda x:x+2
print(op(3))

op=lambda x,y,z:x+z
print(op(1,2,3))

op=lambda x:"even" if x%2==0 else"odd"
print(op(7))

num=lambda x:x-5
print(num(4))

