for x in range(1,10):
    print(x)
    if(x==5):
        break

for x in range(1,10):
    if(x==5):
        continue
    x+=1
    print(x) 

stop=["kphb","sranagar","ameerpet","paradeground","paradise","sec"]
for stop in stop:
    if(stop=="ameerpet"):
        continue
    print(stop)

list=[4,6,8,912,34,56]
for x in list:
    print(x)
    if(x==34):
        break
        