######################################### CONCEPT - GENERATOR ############################################

#There are two primary ways of creating generators: by using generator functions and generator expressions.
#A common use case of generators is to work with data streams or large files, like CSV files.

#Generator functions look and act just like regular functions, but with one defining characteristic. 
#Generator functions use the Python yield keyword instead of return. 

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

#yield indicates where a value is sent back to the caller, but unlike return, you DO NOT exit the function afterward.
#Instead, the state of the function is remembered. That way, when next() is called on a generator object 
#(either explicitly or implicitly within a for loop),the previously yielded variable num is incremented, and then yielded again.

#Create generator using expression
nums_squared_lc = [num**2 for num in range(5)]
nums_squared_gc = (num**2 for num in range(5))

#Both nums_squared_lc and nums_squared_gc look basically the same, but there’s one key difference. 
# what happens when you inspect each of these objects:
#The first object used brackets to build a list, while the second created a generator expression by using parentheses. 
#The output confirms that you’ve created a generator object and that it is distinct from a list.

nums_squared_lc
#Output - [0, 1, 4, 9, 16]
nums_squared_gc
#Output - <generator object <genexpr> at 0x107fbbc78>

#Note: There is one thing to keep in mind, though. If the list is smaller than the running machine’s available memory
# ,then list comprehensions can be faster to evaluate than the equivalent generator expression.

#Remember, list comprehensions return full lists, while generator expressions return generators. 
#Generators work the same whether they’re built from a function or an expression. 
#Using an expression just allows you to define simple generators in a single line, with an assumed yield at the end of each inner iteration.

