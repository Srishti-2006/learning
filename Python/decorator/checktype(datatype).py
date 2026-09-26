#decorator to check datatype of input
def sanity_check(data_type):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            if type(args[0])==data_type:
                func(*args)
            else:
                raise TypeError("ye data type nh chalega")
        return inner_wrapper
    return outer_wrapper

@sanity_check(int)
def square(num):
    print(num**2)

@sanity_check(str)
def greet(name):
    print('hello',name)

square(2)
greet('neeraj')
