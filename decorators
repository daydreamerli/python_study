import functools

def decorator_with_arguments(numbers):
    @functools.wraps(numbers)
    def my_decorator(func):
        @functools.wraps(func)
        def funcion_that_runs_func(*args,**kwargs):
            print('In the decorator!')
            if numbers == 56 or 100:
                func(*args,**kwargs)
            else :
                print("Not running the function!")
            print("After the decorator!")
        return funcion_that_runs_func
    return my_decorator

@decorator_with_arguments(56)
def my_function_One(x,y):
    """-----this is the first Docstring------"""
    print(int(x+y))

@decorator_with_arguments(100)
def my_function_two(x,y):
    """-----this is the first Docstring------"""
    print('100'+' this is my function_two')

my_function_One(44,56)
my_function_two(66,34)
print(my_function_One.__doc__)      # why you need the wrapper function
print(my_function_two.__doc__)
