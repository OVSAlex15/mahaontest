v0 = input('enter start ')
v= input('enter end ')
t = input('enter time ')
def decorator(func):
    def wrapper(v0,v,t):
        usk = func(v0,v,t)
        S = (v**2 - v0**2)/(2*usk)
        
        print(S,' это расстояние')
        
    return wrapper

@decorator
def uskkorenie(v0,v,t):
    a = (v - v0)/t
    return a
try:
    uskkorenie(v0,v,t) 
except ZeroDivisionError:
    print("Нельзя делить на ноль ")
except TypeError:
    print("Делить можно только числа ") 
  
