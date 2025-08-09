class parent:
    def pmethod(self):
        print("i am a method from parent")
    def pmethod2(self):
        print("i am a method from parent2") 
class child(parent):
    def cmethod(self):
        print(" i a am a method from child")           
obj1=child()
obj1.cmethod()
obj1.pmethod()
obj1.pmethod2()

class parent:
    def pmethod(self):
        print("i am a method from parent")
    def pmethod2(self):
        print("i am a method from parent2") 
class child(parent):
    def cmethod(self):
        print(" i a am a method from child")
        super().pmethod2()
obj1=child()
obj1.cmethod()

#singleinheritene:-
class user:
    def __init__(self, name,email):
        self.name=name
        self.email=email
class student(user):
    def __init__(self,name,email,enrolledcourse):
        super().__init__(name,email) 
        self.enrolledcorse=enrolledcourse
    def getcouse(self):
        print(f"{self.name} is learning {self.enrolledcorse}")
class instrauctor(user):
    def __init__(self,name,email,courses_training):
        super().__init__(name,email)                   
        self.courses_training=courses_training
    def getcouse(self):
        print(f"{self.name} is teaching {self.course_training}")
student_obj=student("sneha","sneha@gmail.com",["html","css","python","js"])
student_obj.getcouse()
Trainer_obj=instrauctor("harish","harish@gmail.com",["frentend","backend","db","ai"])
Trainer_obj.getcouse  

class user:
    def __init__(self, name,email):
        self.name=name
        self.email=email
class student(user):
    def __init__(self,name,email,enrolledcourse):
        super().__init__(name,email) 
        self.enrolledcorse=enrolledcourse
    def getcouse(self):
        print(f"{self.name} is learning {self.enrolledcorse}")
    def removecourse(self,course):
        self.enrolledcorse .remove(course)
        self.getcouse()
    def addcourse(self,course):
        self.enrolledcorse. append(course)
        self.getcouse()    
student_obj=student("sneha","sneha@gmail.com",["html","css","python","js"])
student_obj.removecourse("html")
student_obj.addcourse("sql")
student_obj.getcouse() 

#multipleinhertance:-
'''class parent:
    def pmethod1(self):
        print("i am a metho from parent1")
    def pmethod2(self):
        print("i am a method from parent2")
class child(parent,parent):
    def cmethod(self):
        print("i am a method from child")
obj1=child
#obj1.cmethod()
#obj1.p1method()
obj1.pmethod2()

'''

class parentActor:
    def __init__(self,name,pworth):
        self.pname=name
        self.pworth=pworth
        print(f"{self.pname} is the parent")
    def passert(self):
        print(f"{self.pname} assert are {self.pworth} cr")
class childActor(parentActor):
    def __init__(self,pname,cname,pworth):
        super().__init__(pname, pworth)
        self.cname=cname
        print(f"{self.cname} is came by the referrence of {self.pname}")
    def Cassert(self,worth):
        self.cworth=worth
        print(f"{self.cname} is having worth of {self.cworth} cr")
    def TotalAssert(self):
        print(f"total assert of{self.cname} is {self.pworth+self.cworth}")
ramcharan=childActor("chiranjeevi","ramcharan",100) 
ramcharan.Cassert(75)
ramcharan.TotalAssert()       
ramcharan.passert()

#MULTIPLE INHERTANCE
class parent1:
    def p1method(self):
        print("i am a method from parent1")
class parent2:
    def p2method(self):
        print("i am a method from parent2")
class child(parent1,parent2):
    def cmethod(self):
        print("i am a method from child")
obj=child()
obj.cmethod()
obj.p1method()
obj.p2method()

class a:
    def __init__(self):
        print("class a constructor")
class b:
    def __init__(self):
        print("class b constructor")
class c(a,b):
    def __init__(self):
        super().__init__()
        print("class c constractor")
obj=c()

class father:
    def skills(self):
        print("dancer")
class mother:
    def skills(self):
        print("cooking")
class child(father,mother):
    def skills(self):
        print("acting")
obj=child()
obj.skills()

class e:
    def display(self):
        print("a class")
class r:
    def display(self):
        print("b class")
class s(e,r):
    def display(self):
        print("c class")
obj=s()
obj.display()
obj=r()
obj.display()
obj=e()
obj.display() 

#hybrid inheritance:
class a:
    def showa(self):
        print("a class")
class b(a):
    def showb(self):
        print("b class")
class c:
    def showc(self):
        print("c class")
class d(b,c):
    def showd(self):
        print("d class")
d=d()
d.showa()
d.showb()
d.showc()
d.showd()

class person:
    def info(self):
        print("i am a person")
class student(person):
    def student_info(self):
        print("i am a student")
class artist:
    def artist_info(self):
        print("i am an artist")
class allrounder(student,artist):
    def allrounder_info(self):
        print("i can study and do art") 
a=allrounder()
a.allrounder_info()
a.artist_info()
a.student_info()
a.info()

#hierarchical inheritance:
class animal:
    def sound(self):
        print("animals make sound")
class dog(animal):
    def bark(self):
        print("dog barks")
class cat(animal):
    def meow(self):
        print("cat meows")
d=dog()
d.sound()
d.bark()
c=cat()
c.sound()
c.meow()

#method overriding
class vehical:
    def speed(self):
        print("vechicle speed is normal")
class car(vehical):
    def speed(self):
        print("car spped is 120kmph")
class cycle(vehical):
    def speed(self):
        print("cycle speed is 20kmph")
car=car()
car.speed()
cycle=cycle()
cycle.speed()


class order:
    def __init__(self,customer,order_id):
        self.customer=customer
        self.order_id=order_id
    def deliver(self):
        print(f"{self.customer} will get him order  num {self.order_id} withd standard delivery")
class expressorder(order):
    def __init__(self,customer,order_id):
        super().__init__(customer,order_id)
    def deliver(self):
        print(f"{self.custmoer} will get him order num {self.order_id} with express delivery in one day /same day")
obj=order("sneha",521125)
#obj.deliver()
obj1=order("viny",50098)
obj2=expressorder("asha",54112)
print(obj.__dict__)
print(obj1.__dict__)
print(expressorder.__mro__)            

class parent:
    def greet(self):
        print("hello parent")
class child(parent):
    def greet(self):
        super().greet() 
        print("hello child")
parent=child()           
parent.greet()

class a:
    def show(self):
        print("class a")
class b(a):
    def show(self):
        print("class b")
class c(a):
    def show(self):
        super().show()
        print("class c")
c=c()
c.show()

#encapsulation:
class parent:
    def __init__(self):
        self._user="sneha"
class child(parent):
    def __init__(self):
        super().__init__()
        print(self._user)  
obj=child()

class sample:
    def __init__(self):
        self. __name="sneha"
    def getdetails(self):
        return self.__name
obj=sample()
print(obj.getdetails()) 

class demo:
    def __init__(self):
        self.name="prashanth"
obj=demo()
print(obj.__dict__)
obj.name="sneha"
print(obj.__dict__) 
obj=demo(),obj.name
print(obj.__dir__)      



