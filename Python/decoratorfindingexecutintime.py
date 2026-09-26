#decorator to detect the execution time of any function using time module
import time

def timer(func):
    def wrapper(*args):
        start=time.time()
        func(*args)
        print('time taken by',func.__name__,time.time()-start,'secs')
    return wrapper

# examples
@timer
def hello():
    print('hello world')
    time.sleep(2)

@timer
def display():
    print('displaying something')
    time.sleep(2)

@timer
def power(a,b):
    print(a**b)

@timer
def square(num):
    time.sleep(1)
    print(num**2)

hello()
display()
square(2)
power(2,3)