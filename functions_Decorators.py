#Concept -functions and Decorators 

#Assigning functions to variable
def plus_one(number):
    return number + 1

add_one = plus_one
print(add_one(4))       #output - 5


#Defining Functions Inside other Functions
def plus_one(number):
    def add_one(number):
        print("In add_one")
        return number + 1
    
    result = add_one(number)
    return result

print(plus_one(4))      #output - 5


#Passing Functions as arguments to other functions
def plus_one(number):
    return number + 1

def function_call(function):
    print("Function plus_one passed as argument")
    number_to_add = 4
    return function(number_to_add)

print(function_call(plus_one))      
# Output 
# Function plus_one passed as argument
# 5


#Function(s) returning other Function(s)
def hello_function():
    print("In function hello_function()")
    def say_hi():
        #print("In function say_hi()")
        return "Hi"
    return say_hi       #returning a function say_hi

hello = hello_function()
print(hello)      #output is  <function hello_function.<locals>.say_hi at 0x000002CC9896C3A0>
print(hello())    #calling the returned function, output is  Hi

#OUTPUT
#In function hello_function()
#<function hello_function.<locals>.say_hi at 0x01F9B190>
#Hi


#Python allows a Nested function to access the outer scope of the enclosing function
# This is called   - CLOSURE
def outer_message(message):
    "Enclosing Function"
    def message_sender():
        "Nested Function"
        #print("Nested function")
        print(message)

    message_sender()    #call to message_sender() func
    
outer_message("Some random message")    #output "Some random message"   
#Note: In above function, message string passed is available to nested function message_sender,
#  from outer_message function. 


#Creating a decorator and using it traditional way - by calling using passing function as argument
def uppercase_decorator(function):
    def wrapper():
       
        func = function()
        print("Inside wrapper ",function)
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper  # returning function wrapper

def say_hi():
    return "hello string"

decorator1 = (uppercase_decorator(say_hi))      
print(decorator1)       #getting function uppercase_decorator as return
print(decorator1())     #calling returned function
#OUTPUT is 
#<function uppercase_decorator.<locals>.wrapper at 0x000002CC9896C280>
#Inside wrapper  <function say_hi at 0x000002CC98943C10>
#HELLO STRING


########## Using decorator via @ SYMBOL and not the traditional way of calling ###############
def uppercase_decorator(function):
    def wrapper():
        func = function()
        print(function)
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper  # returning function wrapper

#USE @ symbol before the function we'd like to decorate, here function 'say_hi()' is decorated
@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi())
#OUTPUT
#<function say_hi at 0x000002CC9896C8B0>
#'HELLO THERE'


#Using multiple decoraters to single function
def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

def uppercase_decorator(function):
    def wrapper():
        func = function()
        print(function)
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper  # returning function wrapper

@split_string           #decorator 1 - splits the string and returns list of splitted items - ['hello', 'there']
@uppercase_decorator    #decorator 2 - makes upper case
#Notice that the application of decorators is from the bottom up
#first decorator called is uppercase_decorator and then split_string decorator
#i.e. first convert string to uppercase and then split into a list
def say_hi():
    return 'hello there'

print(say_hi())
#OUTPUT 
#<function say_hi at 0x000002CC9896C040>
#['HELLO', 'THERE']



#Accepting arguments in Decorator functions
#Pass the arguments to the wrapper function first,
#and then the arguments are passed to function that is decorated (cities)
def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("function passed is ",function)
        print("My arguments are: {0}, {1}".format(arg1,arg2))
        function(arg1, arg2)    #arguments are passed to function that is decorated (cities)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))

cities("Nairobi", "Accra")
#OUTPUT -
#My arguments are: Nairobi, Accra
#Cities I love are Nairobi and Accra


#Defining General Purpose Decorators
#To define a general purpose decorator that can be applied to any function, we use args and **kwargs.
#args and **kwargs collect all positional & keyword arguments, stores them in the args & kwargs variables.
#args and kwargs allow us to pass as many arguments as we would like during function calls.

#Create a decorator that can accept any no. of arguments using wrapper function
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are',kwargs)
        function_to_decorate(*args)

    return a_wrapper_accepting_arbitrary_arguments

#Using decorator with no arguments passed to it
@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("No arguments here. ")

function_with_no_argument()
#OUTPUT - 
#The positional arguments are ()
#The keyword arguments are {}
#No arguments here. 

#Use decorator with Positional arguments passed to it
@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)

function_with_arguments(1,2,3)
#OUTPUT - 
#The positional arguments are (1, 2, 3)
#The keyword arguments are {}
#1 2 3

##Use decorator with keyword arguments passed to it
#Keyword arguments are passed using keywords. In pairs, e.g. - first_name="Derrick", last_name="Mwiti"
@a_decorator_passing_arbitrary_arguments
def function_with_keyword_arguments():
    print("This has shown keyword arguments")

function_with_keyword_arguments(first_name="Derrick", last_name="Mwiti")
#OUTPUT - 
#The positional arguments are ()
#The keyword arguments are {'first_name': 'Derrick', 'last_name': 'Mwiti'}
#This has shown keyword arguments


#Passing Arguments to the Decorator
#Now let's see how we'd pass arguments to the decorator itself. 
#We define a decorator maker that accepts arguments then define a decorator inside it. 
#We then define a wrapper function inside the decorator as we did earlier.
def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
    def decorator(func):
        def wrapper(function_arg1, function_arg2, function_arg3) :
            "This is the wrapper function"
            print("The wrapper can access all the variables\n"
                  "\t- from the decorator maker: {0} {1} {2}\n"
                  "\t- from the function call: {3} {4} {5}\n"
                  "and pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2,decorator_arg3,
                          function_arg1, function_arg2,function_arg3))
            return func(function_arg1, function_arg2,function_arg3)

        return wrapper

    return decorator


pandas = "Pandas"
@decorator_maker_with_arguments(pandas, "Numpy","Scikit-learn")
def decorated_function_with_arguments(function_arg1, function_arg2,function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
           " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))

decorated_function_with_arguments(pandas, "Science", "Tools")
#OUTPUT - 
#The wrapper can access all the variables
#	- from the decorator maker: Pandas Numpy Scikit-learn
#	- from the function call: Pandas Science Tools
#and pass them to the decorated function
#This is the decorated function and it only knows about its arguments: Pandas Science Tools
