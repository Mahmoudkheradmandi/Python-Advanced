import time 
import multiprocessing

def task_1(name):
    print(f"task_one-{name} # <== 1")
    print(f"task_one-{name} # <== 2")
    print(f"task_one-{name} # <== 3")
    time.sleep(2)
    print(f"task_one- ready # <== 5")
    
    
if __name__ == '__main__': 
    
    start = time.time()

    p1 = multiprocessing.Process(target=task_1, args=(1,))
    p2 = multiprocessing.Process(target=task_1, args=(2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    end = time.time()
    print(f"Took: {round(end-start, 2)} second(s).")    