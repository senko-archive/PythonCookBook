import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

class MyThread(threading.Thread):
    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name

    def run(self):
        logging.info("Thread %s: starting", self.name)
        time.sleep(2)
        logging.info("Thread %s: finishing", self.name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    threads = list()
    for index in range(10):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index, ))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)

    print("----------------------------------")

    classThreads = list()
    for index in range(5):
        logging.info("Main    : create and start thread %d.", index)
        x = MyThread(index)
        classThreads.append(x)
        x.start()

    for index, classThread in enumerate(classThreads):
        logging.info("Main    : before joining thread %d.", index)
        classThread.join()
        logging.info("Main    : thread %d done", index)
