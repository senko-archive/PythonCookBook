import concurrent.futures
import logging
import threading
import time
import random

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

def add(x, y):
    return x + y

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, range(5))

    futureList = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for index in range(50):
            future = executor.submit(add, random.randint(1,101), random.randint(1,101))
            futureList.append(future)

    for future in futureList:
        print(future.result())


