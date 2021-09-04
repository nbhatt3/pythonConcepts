
#suitable for I/O bound tasks
# see https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing

import time
import multiprocessing


def worker(sleeptime):
    print(multiprocessing.current_process().name, "Entering Multiprocessing sleep  ")
    time.sleep(sleeptime)
    print(multiprocessing.current_process().name, "Exiting Multiprocessing sleep ")

if __name__ == '__main__':
    print("Sequentially ")
    worker(5)   #MainProcess
    print("Parallely")
    ths = []
    st=time.time()
    for i in range(10):         #Create 10 Processes
        th = multiprocessing.Process(target=worker,args=(5,))      #create the thread
        ths.append(th)
    [th.start() for th in ths]      #start the process
    [th.join() for th in ths]       #join == wait for end
    print("Total Time taken", time.time()-st," secs")
