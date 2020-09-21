import threading
import logging
import time


def thread1(event):
    logging.info("wait for the event to start")
    event_is_set = event.wait()
    if event_is_set:
        logging.info('Im doing someting because event is set')
    logging.info('event set: %s', event_is_set)


def thread2(event, timeout):
    while not event.is_set(): # event set olmadigi surece while'da kal
        logging.info("wait for the event to start")
        event_is_set = event.wait(timeout)
        logging.info('event set: %s', event_is_set)
        if event_is_set:
            logging.info('processing event')
        else:
            logging.info('doing something else')

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='(%(threadName)-9s) %(message)s', )

    e = threading.Event()
    t1 = threading.Thread(name="blocking", target=thread1, args=(e, ))
    t1.start()

    t2 = threading.Thread(name="non-blocking", target=thread2, args=(e, 2))
    t2.start()

    logging.info('Waiting before calling Event.set()')
    time.sleep(3)
    e.set()
    logging.info('Event is set')




