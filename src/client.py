import redis
import time,os
from rq import Queue, Connection
from helpers import print_response
from threading import Thread

listen = ['default']

WAIT = 1

def add():
    redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379/1')
    conn = redis.from_url(redis_url)
    with Connection(conn):
        q = Queue()
        q.enqueue(print_response,"Hello World")
        time.sleep(WAIT)
        print "Added task to queue"

if __name__ == '__main__':
    num_threads = int(os.getenv('CLIENTS', 1))
    #Continuously loop and create the threads to add to the queue.
    while True:
        for i in range(num_threads):
            t = Thread(target=add)
            t.start()
        time.sleep(WAIT)


