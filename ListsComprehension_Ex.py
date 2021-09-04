#LIST COMPREHENSION

#list_variable = [expression for item in collection] 
# The expression generates elements in the list followed by a for 
# loop, over some collection of data which would evaluate the expression for every item in the collection.

#Note: List comprehensions are good alternatives to for loops, as they are more compact.

#Traditional FOR Loop in python 
numbers = range(9)
new_list = []

# Add values to `new_list`
for n in numbers:
    if n%2==0: #check if the element is even
        new_list.append(n**2) #raise that element to the power of 2 and append to the list

print(new_list) #

#Using List comprehension to replace big code above, get same result [0, 4, 16, 36, 64]
numbers = range(9)
new_list = [n**2 for n in numbers if n%2==0]     #expression followed by for loop, followed by the conditional clause if any
#OUTPUT     [0, 4, 16, 36, 64]
#############################################################

#You can replace lambda, map(), filter(), reduce() and use list comprehension in place of lambda
kilometer = [39.2, 36.5, 37.3, 37.8]
# Construct `feet` with `map()`
feet = map(lambda x: float(3280.8399)*x, kilometer)
# Print `feet` as a list
print(list(feet))  # [128608.92408000001, 119750.65635, 122375.32826999998, 124015.74822]

#Use list comprehension in place of lambda - Convert kilometer to feet
kilometer = [39.2, 36.5, 37.3, 37.8]
feet = [float(3280.8399)*x for x in kilometer]
print(feet)     # [128608.92408000001, 119750.65635, 122375.32826999998, 124015.74822]

#############################################################

#USE OF if condition - more than one condition can be used in list comprehension
#Add two(or more) if conditions one followed by another. 
# Only when both conditions are satisfied, the expression will be added to the list
divided = [x for x in range(100) if x % 2 == 0 if x % 6 == 0]
print(divided)

#############################################################

#If-Else Conditions - convert to list comprehension
kilometer = [39.2, 36.5, 37.3, 37.8]
feet = [float(3280.8399)*x for x in kilometer]
for x in feet:  
    if x >= 120000:
        x + 1
    else:
        x+5
#OUTPUT [128609.92408000001, 119755.65635, 122376.32826999998, 124016.74822]

#The if-else condition can be changed to use list comprehension as below:
kilometer = [39.2, 36.5, 37.3, 37.8]
feet = [float(3280.8399)*x for x in kilometer]
[x+1 if x >= 120000 else x+5 for x in feet]
#OUTPUT [128609.92408000001, 119755.65635, 122376.32826999998, 124016.74822]

#There are two expressions in above usage :
#The first expression (x+1) is dependent on the if statement;
#While the second expression (x+5) is dependent on the else statement.

#############################################################

#Nested List Comprehension
list_of_list = [[1,2,3],[4,5,6],[7,8]]

# Flatten `list_of_list`
[y for x in list_of_list for y in x]
#OUTPUT [1, 2, 3, 4, 5, 6, 7, 8]

#Another example
matrix = [[1,2,3],[4,5,6],[7,8,9]]
[[row[i] for row in matrix] for i in range(3)]
#OUTPUT [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

#############################################################


#############################################################


#############################################################


lst = [1,2,3,4,5]
#when output data type required is list
o=[e*e for e in lst]
print(o)

#when output data type required is set
o={e*e for e in lst}
print(o)

#when output data type required is dict
o={e:e*e for e in lst}
print(o)


o=[]
for e1 in lst:
    if e1%2 == 0:
        for e2 in lst:
            if e2%2 ==0:
                o.append((e1,e2))
print(o)
#Output - [(2, 2), (2, 4), (4, 2), (4, 4)]