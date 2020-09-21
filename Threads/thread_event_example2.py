import threading
import time
import logging
import concurrent.futures
import random

def generator1(event):
    logging.info("generator 1 started")
    event_status = event.is_set()
    logging.info("generator1 - event is: %s", event_status)
    while event_status:
        logging.info("generator1 generating %s", random.randint(1, 101))

    logging.info("generator1 event is not set, doing something else")

def generator2(event, end_event):
    logging.info("generator 2 started")
    while True:
        if event.is_set():
            logging.info("event icindeyim")
            time.sleep(0.1)
        else:
            logging.info("event disindayim")
            time.sleep(0.1)
            if end_event.is_set():
                break




if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='(%(threadName)-9s) %(message)s', )

    event = threading.Event()
    end_event = threading.Event()
    t1 = threading.Thread(name="gen2", target=generator2, args=(event, end_event))
    t1.start()
    time.sleep(1)
    event.set()
    time.sleep(1)
    event.clear()
    time.sleep(1)
    logging.info("main is finished now")
    end_event.set()

