class Person:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    def display(self):
        print(f"my name is {self.name} my grade is {self.grade}")
sneha = Person("sneha","B") 
sneha.display() 

class details:
    def __init__(self,name,ph):
        self.name=name
        self.ph=ph
class sub_details(details):
    def __init__(self,name,ph,email,course):
        super().__init__(name,ph)
        self.email=email
        self.course=course
    def alldetails(self):
        print(f"my name is {self.name} i am choosing course{self.course}")
s= sub_details("sneha",8639778548,"sneha@gmail.com","Btech")
s.alldetails()

class Animal:
    def __init__(self,name):
        self.name=name
class Dog(Animal):
    def __init__(self,name, breed):
        super().__init__(name) 
        self.breed=breed
    def add(self):
        print(f"{self.name} it is very cost becouse i am very cute {self.breed}")
pet = Dog("rocke","bulldog")                   
pet.add()

class A:
    def __init__(self,val):
        self.val =val
    def show(self):
        print("A:",self.val)
class B(A):
    def show(self):
        print("B:",self.val)
class C(A):
    def show(self):
        print("C:",self.val)
class D(B, C):
    pass
d =D(50)
d.show() 

class A:
    def __init__(self,a):
        print("class A:", a)
class B(A):
    def __init__(self,a,b):
        super().__init__(a)
        print("class B:",b) 
class C(B):
    def __init__(self,b,a,c):
        super().__init__(a,b)
        print("class C:",c)      
c=C(2,3,1)

class person:
    def __init__(self,name):
        self.name=name
p=person("sneha")
print(p.name)  

class A:
    def showA(self):
        print("A class")
class B:
    def show(self):
        print("B class")
obj = B()
obj.show()

class parent:
    name ="parent"
class child(parent):
    name="child" 
obj=child()
print(obj.name) 

class Base:
    def __init__(self):
        self.value =10
class Derived(Base):
    def __init__(self):
        super().__init__()
        self.value =20
d = Derived()
print(d.value)

class person:
    def __init__(self,name):
        self.name = name
class student(person):
    def __init__(self,name,roll):
        (super).__init__(name)
        self.roll =roll
s = student("sneha",24)
print(s.name)
print(s.roll)        





