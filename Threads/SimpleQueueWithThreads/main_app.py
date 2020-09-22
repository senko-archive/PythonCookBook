import queue
import logging
import threading
import requests
import concurrent.futures

def producer(name, queue):
    base_url = "http://localhost:5001/api"
    logging.info(f"Producer Thread {name} started")
    response = requests.get(base_url)
    queue.put(response.text)

def consumer(name, queue):
    base_url = "http://localhost:5002/api/save"
    logging.info(f"Consumer Thread {name} started")
    while not queue.empty():
        data = queue.get()
        data_to_send = {'data': data}
        response = requests.post(base_url, data_to_send)
        if response.text == "OK":
            logging.info(f"for consumer thread {name} save is successful")

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    pipeline = queue.Queue(maxsize=50)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for index in range(20):
            executor.submit(producer, index, pipeline)
        for index in range(5):
            executor.submit(consumer, index, pipeline)


    x = pipeline.qsize()
    print(x)




