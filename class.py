class person:
    name="sneha"
    age=21
    gender="female"
obj1=person()
obj2=person()
print(obj1)
print(obj2)
print(obj1.name)
print(obj1.age)
print(obj2.name)
obj1.name="motupalli sneha"
print(obj1.name)
print(obj2.name)
print(person().name)

class details:
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age


obj_sneha=details("sneha","female",21)
obj_prashanth=details("prashanth","male",39)


print(obj_prashanth.name)
print(obj_sneha.name)

class Application:
    def __init__(app,name,color,category):
        app.name=name
        app.color=color
        app.category=category
insta=Application("insta","pink","social media")
youtube=Application("youtube","red","enteratiment")
ola=Application("ola","black","travalling")
zomato=Application("zomato","red","food")
print(insta.name,insta.color,insta.category)
print(youtube.name,youtube.color,youtube.category)
print(ola.name,ola.color,ola.category)
print(zomato.name,zomato.color,zomato.category)

class Application:
    def __init__(app,name,color,category):
        app.name=name
        app.color=color
        app.category=category
    def purpose(self):
        print("social media")

insta=Application("insta","pink","social media")
insta.purpose()
print(insta.name,insta.color,insta.category)

class Application:
    def __init__(app,name,color,category):
        app.name=name
        app.color=color
        app.category=category
    def purpose(self,app_name,purpose):
        print(f"{app_name} is used for {purpose}")
insta=Application("insta","pink","social media")
youtube=Application("youtube","red","enteratiment")
ola=Application("ola","black","travalling")
zomato=Application("zomato","red","food")

insta.purpose("insta","social media")
youtube.purpose("youtube","enteratiment")
ola.purpose("ola","travalling")
zomato.purpose("zomato","food")        


class student():
    def __init__(self,name,study):
        self.name=name
        self.study=study
    def display(self):
        print("name",  self.name)
        print("study", self.study)   

s1=student("sneha","inter")
s1.display()

class student():
    def __init__(self,name,study):
        self.name=name
        self.study=study
    def purpose(self):
        print(f"my name is {self.name} i study {self.study} ")    
sneha = student("sneha","inter")
sneha.purpose() 

class details():
    def __init__(self,name,age,category):
        self.name=name
        self.age=age
        self.category=category
    def purpose(self):
        print(f"my name is {self.name} my age {self.age} my category {self.category}")    
sneha = details("sneha",21,"student")
prashant = details("prashanth",27,"van driver")
nani = details("srinivasarao",45,"farmor")
sneha.purpose()
prashant.purpose()
nani.purpose()

'''print(sneha.name,sneha.age,sneha.category)
print(prashant.name,prashant.age,prashant.category)
print(nani.name,nani.age,nani.category)
'''

class numbercheck:
    def __init__(self, num):
        self.num=num
    def check(self):
        if self.num%2==0:
            print("even")
        else:
            print("odd")  
n=numbercheck(4)
n.check() 

class add():
    def __init__(self,num):
        self.num=num
        if num%2!=0:
            print("prime")
        else:
            print("not a prime")
s=add(6)  

class name():
    def __init__(self,name):
        self.name=name
s = name("sneha")
print(sneha.name)

class bankaccount:
    def __init__(acnt,name,email,ph,balence):
        acnt.name=name
        acnt.email=email
        acnt.ph=ph
        acnt.balence=balence
    def deposit(acnt,d_amnt):
        acnt.balence+=d_amnt
    def withdrawl(acnt,w_amnt):
        acnt.balence-=w_amnt    
    def checkbalance(acnt):
        print(acnt.balence)    
sneha_acnt=bankaccount("sneha","dokkasneha@gmail.com",8639778548,500)
sneha_acnt.deposit(100)
sneha_acnt.checkbalance()
sneha_acnt.withdrawl(50)
sneha_acnt.checkbalance()


class details:
    def __init__(self,name,roll_num,section):
        self.name=name
        self.roll_num=roll_num
        self.section=section
    def display(self):
        print(f"my na me is {self.name} my roll number is{self.roll_num} and {self.section} section")
student1=details("sneha","21nd1a5424","B") 
student1.display()

class details():
    def __init__(self,name,village):
        self.name=name
        self.village=village
    def cal(self):
        print(f"what is your name?")
        print(f"where are you from?")
    def response(self):
        print(f"my name is {self.name}")
        print(f"i am from {self.village}")    
        
pepoles = details("sneha","bodagunta")
pepoles.cal()
pepoles.response() 

class a:
    def methoda(self):
        print("a")
class b(a):
    def methodb(self):
        print("b")
obj=b()
obj.methoda()


class Animal:
    def sound(self):
        print("Animal sound")
class Dog(Animal):
    def brak(self):
        print("Dog Baeks")
class Puppy(Dog):
    def cute(self):
        print("puppy is cute")
p=Puppy()
p.sound()
p.brak()
p.cute() 

class person:
    def method(self):
        print("name:" ,"sneha")
class person1(person):
    def method(self):
        print("age:", 21)
person = person1()
person.method()


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def purspose(self):
        print(f"{self.name}")
        print(f"{self.age}")
obj=person("sneha",21)
obj.purspose()

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"{self.name}")
        print(f"{self.age}")
class student(person):
    def __init__(self, name,age,roll_number,course):
        super().__init__(name,age)
        self.roll_number=roll_number
        self.course=course
    def display(self):
        print(f"{self.roll_number}")
        print(f"{self.course}") 
person =student("sneha",21,108,"python fullstack")
person.display() 


class singer:
    def __init__(self,sang):
        self.sang=sang
    def display(self):
        print(f"geetha is {self.sang}")
class dancer(singer):
    def __init__(self,name,sang):
        super().__init__(sang)
        self.name=name
    def display(self):   
        print(f"mahaseh is {self.name}")
perfomer =dancer("singer","dancer")
perfomer.display()

#encapsulation:
class student:
    def __init__(self,name,markes):
        self.name =name
        self.__markes=markes
    def get_markes(self):
        return self.__markes
s= student("sneha",90)
print(s.name)
print(s.get_markes())

class parent:
    def geet(self):
        print("i am a parent")
class child(parent):
    def geet(self):
        print("i am a child")
obj=child()
obj.geet()

#polymorphrism:
class dog():
    def speak(self):
        return "woof!!"
class cat():
    def speak(self):
        return "meow!!"
class tiger():
    def speak(self):
        return "roars"
def animal_sounds(animal):
    print(animal.speak())
dog=dog()
cat=cat()
tiger=tiger()
animal_sounds(dog)
animal_sounds(cat)
animal_sounds(tiger)

class Circle:
    def area(self):
        return 3.14*5*5
class Square:
    def area(self):
        return 4*4
class Rectangle:
    def area(self):
        return 4*6
def print_area(shape):
    print(shape.area())
Circle = Circle() 
Square = Square()
Rectangle = Rectangle()
print_area(Circle)
print_area(Square)
print_area(Rectangle) 

class book:
    def __init__(self,pages):
        self.pages = pages
    def __add__(self,other):
        return self.pages + other.pages
book1 = book(100)
book2 = book(150)
print(book1+book2)

class vehicle:
    def run(self):
        print("vechical is running")
class bike(vehicle):
    def run(self):
        print("bike is running")
class car(vehicle):
    def run(self):
        print("car is running")                
vehicles=[vehicle(),bike(),car()]
for v in vehicles:                                
    v.run() 



        

class pen:
    def use(self):
        print("pen is use 6th class studentes")
class pencil:
    def use(self):
        print("pencil is use childesns") 
def using(obj):
    obj.use()
pen = pen()
pencil=pencil()
using(pen)
using(pencil)


class broom:
    def clean(self):
        print("sweeping the floorwith a broom")
class mop:
    def clean(self):
        print("mopping the floor with water")
class vacuuming:
    def clean(self):
        print("vacuuming dust from carpet")
def start_cleaning(obj):
    obj.clean()
broom = broom() 
mop =mop()
vacuuming = vacuuming()
start_cleaning(broom)
start_cleaning(mop)
start_cleaning(vacuuming) 

class Mobile:
    def feature(self):
        return "used for calling and messaging"
class Laptop:
    def feature(self):
        return "used for coding and work"
class SmartWacth:
    def feature(self):
        return "used for tracking fitness" 
def show_feature(gadget):
    print(gadget.feature())
m = Mobile()
l = Laptop()
s = SmartWacth()
show_feature(m) 
show_feature(l)
show_feature(s)                          

class gadent:
    def __init__(self,brand,price):
        self.__brand = brand #encapsulated
        self.price = price
    def get_brand(self):
        return self.__brand

    def feature(self):
        return "basic gadget feature" 
class Mobile(gadent):
    def __init__(self,brand,price,camera):
        super().__init__(brand,price)
        self.camera=camera
    def feature(self):
        return f"Mobile from {self.get_brand()} with {self.camera}mp"
    def show_feature(gadgent):
        print(gadgent.feature())
m=Mobile("samsung",1700,67) 
show_feature(m)

#encapsulation:
class Student:
    def __init__(self):
        self.__name = None
    def set_name(self,name):
        self.__name =name
    def get_name(self):
        return self.__name
s=Student()
s.set_name("sneha") 
print(s.get_name())

class BankAccount:
    def __init__(self):
        self.__balance =0
    def deposit(self,amount):
        if amount >0:
            self.__balance +=amount
        else:
            print("invalid amount")
    def Withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance-= amount
        else:
            print("insufficient balance")
    def get_balance(self):
       return self.__balance
acc = BankAccount()
acc.deposit(5000)
acc.Withdraw(2000)
print(acc.get_balance())                                    









       
       
 