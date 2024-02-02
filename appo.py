# from app_not import run_this_app
# if __name__ == "__main__":
#     run_this_app().run(port=5000, debug=True)

from functools import wraps
 


def jwt_required() :
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            # verify_jwt_in_request(optional, fresh, refresh, locations, verify_type)
            # return current_app.ensure_sync(fn)(*args, **kwargs)
            print("abc")
            return 

        return decorator

    return wrapper

def abc():
    # print("madang", func)
    def a_tdecorator(func ):
        print(func,"kok")
        @wraps(func)
        def wrapper(*args, **kwargs):
            """A wrapper function"""
    
            # Extend some capabilities of func
            func()
            func()
            return "komok"
        return wrapper
    return a_tdecorator

def a_decorator(func=None):
    print("func from ad decorator",func)
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("func wrapper",func)
        """A wrapper function"""
 
        # Extend some capabilities of func
        func()
        return "lll"
    return wrapper
 

@abc()
def first_function(cc="xc"):
    """This is docstring for first function"""
    print("first function")
 
@a_decorator
def second_function():
    """This is docstring for second function"""
    print("second function")
    return "abc"
    
def seconds_function():
    """This is docstring for second function"""
    print("secondyy function")
    
 
print(first_function())
print("lop", "demddddddddddddddddddddddddddddddddd")
# print(second_function())
# print("lop", "dem")
# ss = a_decorator(seconds_function)
# print("lop",ss(), "dem")
# print(first_function.__name__)
# print(first_function.__doc__)
# print(second_function.__name__)
# print(second_function.__doc__)
# ss = abc(seconds_function)
# ss
# print("x")
# ss()
# print("xx")
# ss()()
# print("xxx")

# df = a_decorator(seconds_function)
# df
# print("df")
# df()