for x in range(5):
    str=" "
    for y in range(x+1):
        str+="*"
    print(str) 

for i in range(6):
    str=0
    for j in range(i):
        str=str*10+i
    print(str)

print(chr(97))

for x in range(5):
    str=0
    for y in range(x+1):
        str=str*10+y 
    print(str)

for i in range(97,102):
    str=" "
    for j in range(97,i+1):
        str+=chr(i)
    print(str) 


for i in range(97,102):
    str=""
    for j in range(97,i+1):
        str+=chr(j)
    print(str)

for i in range(5):
    str=" "
    for j in range(i-1):
        str+="e"
    print(str)           

