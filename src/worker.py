import redis
import os, time
from rq import Worker, Queue, Connection

listen = ['default']

redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379/1')

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()