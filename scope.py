

def sample():
    x=5
    print("hello")
sample()
        


x=5
def sample():
    global x
    x=10
sample()
print(x)

def func1():
    global x
    x=10
func1()
print(x)

#x="hello"
#def func1():
    #x=5
#def func2():
    #x=10
#func2()
#print(x)
#func1()
#print(x)

def func1():
    print(x)
def func2():
      x=10
func2()
func1()


def greet():
  name="sneha"
  print(name)
greet()

#global
name="sunny"
def hello():
    print(name)
hello() 
#nonlocal keywords
def outer():
    x="outer"
    def inner():
        print(x)
    inner()
outer() 

name="sneha"
for i in name:
    print(i, end=" ")

x=10
def show():
    x=5
    print(x)
show()
print(x)  


x="global"
def outer():
    x="outer"
    def inner():
        x= "inner"
        print("outer:", x)
outer()
print("global:", x)        
