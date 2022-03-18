#Write a Python program that invoke square root function after specific milliseconds
from time import sleep
import math
def fun(fn, ms, *args):
  sleep(ms / 1000)
  return fn(*args)
print("Square root after specific miliseconds:") 
print(fun(lambda x: math.sqrt(x), 100, 16))
print(fun(lambda x: math.sqrt(x), 1000, 100))
print(fun(lambda x: math.sqrt(x), 2000, 25100))