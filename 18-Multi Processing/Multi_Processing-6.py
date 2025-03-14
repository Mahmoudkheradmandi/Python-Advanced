import time
import concurrent.futures
 
def task_1(num):
    print(f"task_one-{num} # <== 1")
    print(f"task_one-{num} # <== 2")
    print(f"task_one-{num} # <== 3")
    time.sleep(num) ###
    return f"task_one- ready for : {num}"

if __name__ == "__main__":
    start = time.time()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(task_1, 2) for i in range(10)]
        
        for result in concurrent.futures.as_completed(results):
            print(result.result())

    end = time.time()
    print(f"Took: {round(end - start, 2)} second(s).")