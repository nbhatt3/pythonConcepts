#Concept - Decorator

#There are two primary ways of creating generators: by using generator functions and generator expressions.
#A common use case of generators is to work with data streams or large files, like CSV files.

#Generator functions look and act just like regular functions, but with one defining characteristic. 
#Generator functions use the Python yield keyword instead of return. 

#def infinite_sequence():
#    num = 0
#    while True:
#        yield num
#        num += 1

#yield indicates where a value is sent back to the caller, but unlike return, you DO NOT exit the function afterward.
#Instead, the state of the function is remembered. That way, when next() is called on a generator object 
#(either explicitly or implicitly within a for loop),the previously yielded variable num is incremented, and then yielded again.


#Given a directory, find out the file Name having max size recursively

# OUTPUT is - 
#Profile called <function getMaxFileName at 0x000001EEC9B8FC10>
#Profile Exits  <function profile.<locals>._inner at 0x000001EEC9B8FCA0>
#_inner Enter  ('D:\\Nitin',) {}
#Time taken  0.028580188751220703  secs
#_inner Exits  D:\Nitin\GuruJi_newSwaroop_Setting_Satsang_1FEB2020.jpg.png
#D:\Nitin\GuruJi_newSwaroop_Setting_Satsang_1FEB2020.jpg.png

import glob,os.path,time

#creating a decorator, a decorator is a nested function
def profile(fun):       #fun = getMaxFileName
    print("Profile called", fun)
    def _inner(*args, **kwargs):        # args = (path,), kwargs = {}
        #Note: kwargs is keyword arguments stored as dictionary, we donot have any kwargs argument in this example
        print("_inner Enter ", args, kwargs)       
        st = time.time()
        res = fun(*args, **kwargs)      #calling getFileName(path)
        print("Time taken ", time.time()-st, " secs")
        print("_inner Exits ", res)
        return res
    print("Profile Exits ", _inner)
    return _inner


#Apply profile decorator, decorator has full control of function called (getMaxFilename)
@profile
def getMaxFileName(path):               #getMaxFileName = profile(getMaxFileName) = _inner
    def get_files(path, ed={}):         # get_files() is a Nested function
        files = glob.glob(os.path.join(path,"*"))
        for file in files:
            if os.path.isfile(file):
                ed[file] = os.path.getsize(file)
        for file in files:
            if os.path.isdir(file):
                get_files(files,ed)
            return ed
    #st = time.time()        
    allfiles = get_files(path)
    sted = sorted(allfiles,key=lambda k: allfiles[k])   #Sorted in ascending order
    #print("Time taken ", time.time()-st, " secs");
    return sted[-1] if sted else ''         #retun last ,max size file from sted lsit

if __name__ == '__main__':
    path = r"D:\Nitin"      #raw string,  should not care about escape sequence
    print(getMaxFileName(path))     #calling _inner
