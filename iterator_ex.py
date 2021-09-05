#Concpet of using Iterators 
#Lazy computation in python is handled using Iterators - it consists of methods iter(obj), next(obj)
#Note: for loop is an example of iterator
#Given a directory, get all files recursively

#[1, 2, 3] and ['a', 'b', 'c'], like all lists, are iterable, which means they can return their elements one at a time. 
# Technically, any Python object that implements the .__iter__() or .__getitem__() methods is iterable.


#Simple example of making a iterator class 
#First setting up and retrieving the iterator object with an iter() call, 
# and then repeatedly fetching values from it via next().
class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value

repeater = Repeater('Hello')
for item in repeater:
    print(item)

#Output - Hello (Hello string will be printed unlimited times, will continuosly print Hello on console)

#Example - making a finite iterator class
class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value

#Iteration stops after the number of repetitions defined in the max_repeats parameter:
#Every time next() is called in this loop we check for a StopIteration exception and break the loop
repeater = BoundedRepeater('Hello', 3)
for item in repeater:
    print(item)

#Output - 
#Hello
#Hello
#Hello

#Same output can be achived using while loop, instead of for loop
repeater = BoundedRepeater('Hello', 3)
iterator = iter(repeater)
while True:
    try:
        item = next(iterator)
    except StopIteration:
        break
    print(item)


###########################################################################################

import glob,os.path,time

def get_files(path, lst):   #without iterator
        # get_files() is a Nested function
    files = glob.glob(os.path.join(path,"*"))
    print(files)    #print all files obtained with comma separated as list
    print("In First function")
    for file in files:
        if os.path.isfile(file):
          lst.append(file)
    for file in files:
        if os.path.isdir(file):
           get_files(file,lst)
    return lst

def get_files_itr(path):   #using iterator - generator function using Yield and Yield from
    files = glob.glob(os.path.join(path,"*"))
    for file in files:
        if os.path.isfile(file):
          yield file
    for file in files:
        if os.path.isdir(file):
           yield from get_files_itr(file)

#Iterator class using special method __iter__
class Files:
    def __init__(self, path):
        self.path = path
    def __iter__(self):
        files = glob.glob(os.path.join(path,"*"))
        for file in files:
            if os.path.isfile(file):
                yield file
        for file in files:
            if os.path.isdir(file):
                yield from Files(file)

if __name__ == '__main__':
    path = r"D:\Scrum"      #raw string,  should not care about escape sequence
    
    for file in get_files(path,[]):    #call function without iterator
        print(file)
    for file in get_files_itr(path):    #call function with iterator and use of yield
        print(file)
    
    #Using class 'Files' and yield
    for file in Files(path):
        print(file)
