import logging
import threading
import time

def do_something(name):
    logging.info("thread %s started", name)
    # do something
    time.sleep(3)
    logging.info("thread %s finished", name)

def do_something_daemon(name):
    logging.info("thread %s started", name)
    # do something
    time.sleep(6)
    logging.info("thread %s finished", name)

# Another way to create thread with using Class
class MyThread(threading.Thread):
    def __init__(self, name):
        # we need to execute super -> threading.Threads init
        #threading.Thread.__init__(self)
        super(MyThread, self).__init__()
        self.name = name

    def run(self):
        logging.info("thread %s started", self.name)
        # do something
        time.sleep(3)
        logging.info("thread %s finished", self.name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main     : before creating thread")
    x = threading.Thread(target=do_something, args=("thread1", ))
    x.start()
    y = threading.Thread(target=do_something_daemon, args=("damoen_1", ), daemon=True)
    y.start()

    z = MyThread("thread_2")
    z.start()

    logging.info("Main    : wait for the thread to finish")
    logging.info("Main    : all done")
