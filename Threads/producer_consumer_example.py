import random
import logging
import threading
import concurrent.futures

''' in this code i will try to demonstrate one producer and one consumer trying to use
one pipeline object with locks.'''

SENTINEL = object()

def producer(pipeline):
    for index in range(10):
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        pipeline.setMessage(message, "Producer")
    # send sentinel to say pipeline producer is finished
    pipeline.setMessage(SENTINEL, "producer")

def consumer(pipeline):
    message = 0
    while message is not SENTINEL:
        message = pipeline.getMessage("Consumer")
        if message is not SENTINEL:
            logging.info("Consumer storing message: %s", message)

class Pipeline:
    """
    Class to allow a single element pipeline between producer and consumer.
    """
    def __init__(self):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire() # when beginning we need to acquire consumer lock because there is no message, and
                                     # get_message should not be allowed to work

    def getMessage(self, name):
        logging.debug("%s:about to acquire getlock", name)
        self.consumer_lock.acquire()
        logging.debug("%s:have getlock", name)
        message = self.message
        logging.debug("%s:about to release setlock", name)
        self.producer_lock.release()
        logging.debug("%s:setlock released", name)
        return message


    def setMessage(self, message, name):
        logging.debug("%s:about to acquire setlock", name)
        self.producer_lock.acquire()
        logging.debug("%s:have setlock", name)
        self.message = message
        logging.debug("%s:about to release getlock", name)
        self.consumer_lock.release()
        logging.debug("%s:getlock released", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    #logging.getLogger().setLevel(logging.DEBUG)

    pipeline = Pipeline()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(producer, pipeline)
            executor.submit(consumer, pipeline)