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



