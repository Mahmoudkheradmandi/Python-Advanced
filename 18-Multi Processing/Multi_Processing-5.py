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
        process = executor.submit(task_1, 1)
        print(process.result())

    end = time.time()
    print(f"Took: {round(end - start, 2)} second(s).")