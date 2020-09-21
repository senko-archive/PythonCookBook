import logging
import threading
import time

def do_something(name):
    logging.info("thread %s started", name)
    # do something
    time.sleep(3)
    logging.info("thread %s finished", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main     : before creating thread")
    x = threading.Thread(target=do_something, args=("thread_1", ))
    x.start()

    logging.info("Main     : Main is also working" )

    x.join()
    logging.info("Main     : I want to see this line after x is finished")
    logging.info("Main    : all done")

