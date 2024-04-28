def firstfunction() :
    print("This is my first function")

# firstfunction()

# def add(a, b) :
#     return a + b

# print(add(3,6))


#                                Default Argument

def greet(name, massage="good morninig") :
    print(name, massage)

# greet("ms suraj")


#                                   keyword argument

def greet(name, age, message):
    print(message, name, "your age is ", age)

# greet(age = 33, message="Hello", name="Ms")           this is the interviw Questions



#                                   Possitional Arguments

def add_numbers(x, y) :
    print("x", x)
    print("y", y)
    print(x + y)
# add_numbers(5, 33)


# def sum_number(*args) :
#     print(type(args))
#     print(args)
#     sum = 0
#     for sum in args :
#         sum += args
#         return sum
# print(sum_number(1,2,3,4,5))


def fn(a, b, *args) :
    print(a)
    print(b)
    print(args)
    print(*args)
# fn(3,4,5,6,7,8,9)



#                           Kwargs in Python
def display_info(**kwargs) :
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key , "->", value)
# display_info(name="Vishwa",age=23, city="Gpj")

def func(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
# func(5,6,7,8,9, name="Ms", age=22)


#                           this is empliset Conversion

def add_numbers(a: int, b: int)->int:
    return a + b

# print(add_numbers(5.4, 33))
# print(type(add_numbers))


def outer():
    print("hellow from the outer")
    def inner():
        print("hellow from the inner")
    return inner
# fn = outer()
# fn()
# outer()()


#                           this is pass refrence/Value

# this is the pass by value

num = 5
def modify_num(num) :
    num +=1
    print(num)
# modify_num(num)
# print("original num ", num)


# this is the pass by reference 
my_list = [1,2,3,4]
def modify_list(li) :
    li.append(5)
    print(li)
# print("Before calling fun ", my_list)
# modify_list(my_list)

# print("after calling fun ", my_list)


#                       this is the lambda Function

funL = lambda x : x+10
print(funL(5))

add = lambda a, b : a+b
print(add(4,6))


def myfunL () :
    # return a new function
    return lambda msg : print(msg)
myfunL()("hellow lambda")
