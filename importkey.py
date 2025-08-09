print("hello")

#ceil()
import math
print(math.ceil(2.3))
#floor function
print(math.floor(6.8))
#trunc
print(math.trunc(128.654))
#factorial
print(math.factorial(5))
#mathematical constant
print(math.pi)
print(math.e)
print(math.inf)
print(math.nan)
#exp()
print(pow(math.e,10))
print(math.exp(10))
print(math.pow(5,2))
#log()
print(math.log(8,2))
#sqrt()
print(math.sqrt(25))
#trignometric functions
a=math.degrees(90)
b=math.pi
print(round(math.sin(b/2)))
print(round(math.cos(b/2)))
#choice()
import random
a=[1,2,3,4,5,6,7,8,9,10]
print(random.choice(a))
#choices()
print(random.choices(a,k=5))
#sample()
print(random.sample(a,k=6))
#shuffle()
random.shuffle(a)
print(a)
print(max(a),min(a))

