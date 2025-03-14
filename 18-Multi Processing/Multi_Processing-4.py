import time
import multiprocessing

def task_1(num):
    print(f"task_one-{num} # <== 1")
    print(f"task_one-{num} # <== 2")
    print(f"task_one-{num} # <== 3")
    time.sleep(num) ###
    print(f"task_one- ready for : {num}")


if __name__ == "__main__":

    start = time.time()


    processes = []
    #for i in range(10):
    for i in range(10 , 1 ,-1):
        p = multiprocessing.Process(target=task_1, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    
    end = time.time()
    
    print(f"Took: {round(end - start, 2)} second(s).")