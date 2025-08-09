color="balck"
if(color=="red"):
  print("pless stop")
elif(color=="orange"):
  print("ready to go")
elif(color=="green"): 
  print("please go") 
else:
  print("invalid colour input")  


eamcet_rank= 4500
if(eamcet_rank<500):
    print("go sit in reddyclg") 
elif(eamcet_rank<7500):
    print("you sit in st marrys")
elif(eamcet_rank<3000):
    print("you sit in malareddy")
else:
    print("you are join in bcom") 

a=int(input("enter the value a:"))
b=int(input("enter the value b:"))
c=int(input("enter the valu c:"))
if(a==b==c):
    print("we conform equal triangle")
elif(a==b)or(b==c)or(c==a):
    print("we confome isosceles triangle")
elif(a!=b!=c):
    print("we conform scalene triangle") 
elif((a+b)>=c)or((b+c)>=a)or((c+a)>=b):
    print("inquality triangle") 
else:
    print("can not form a triangle")




