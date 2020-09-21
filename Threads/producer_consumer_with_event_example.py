import random
import logging
import threading
import concurrent.futures
import queue
import time

'''This code demonstrates usage of event and queue with consumer and producer thread'''
'''In this code producer and consumer does their job until they receive the event'''

def producer(event, queue):
    while not event.is_set(): # yani henuz event set edilmemisken bunlari yap
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        queue.put(message)

    logging.info("Producer received event. Exiting")

def consumer(event, queue):
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logging.info("Consumer storing message: %s (size=%d)", message, queue.qsize())

    logging.info("Consumer received event. Exiting")

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    pipeline = queue.Queue(maxsize=10)
    event = threading.Event()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(producer, event, pipeline)
            executor.submit(consumer, event, pipeline)

        time.sleep(0.1)
        logging.info("Main: about to set event")
        event.set()