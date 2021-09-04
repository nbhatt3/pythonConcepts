
#suitable for CPU Bound tasks, where Input/Output tasks are not involved
#Note: generally thread or process do not return anything

# see https://docs.python.org/3/library/threading.html

import time
import threading

#a thread is a function in python
def worker(sleeptime):
    print(threading.current_thread().getName(), "Entering sleep ")
    time.sleep(sleeptime)
    print(threading.current_thread().getName(), "Exiting  sleep ")

if __name__ == '__main__':
    print("Sequentially ")
    worker(5)   #MainThread
    print("Parallely")
    ths = []
    st=time.time()
    for i in range(10):         #Create 10 threads
        th = threading.Thread(target=worker,args=(5,))      #create the thread
        ths.append(th)
    [th.start() for th in ths]      #start the thread
    [th.join() for th in ths]       #join == wait for end
    print("Total Time taken", time.time()-st," secs")