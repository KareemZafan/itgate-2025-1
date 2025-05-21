import math

def add(a,b):
 return a + b
 
def sub(a,b):
 return a - b
 
def mul(a,b):
 return a * b
 
def div(a,b):
if b == 0: 
	return None
 return a / b
 
 
def is_even(a):
 return a % 2 == 0 
 
 
 
def get_square_root(a):
 	return math.sqrt(a)
 
print(add(2,4))
print(sub(2,4))
print(mul(2,4))
print(div(2,4)) 
print(get_square_root(100)) # 10
print(is_even(100)) # True
 
