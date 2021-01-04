import time
import logging
import consts
import socket
import time
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE
from urllib import parse

logger = logging.getLogger(__name__)
info = logger.info


class Event_loop:
    _instance = None
    _tasks = []
    _sector = DefaultSelector()
    _running = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def add_task(self, *task):
        self._tasks.extend(*task)

    def run_until_complete(self):
        self._running = True
        while self._running and self._tasks:
            for key, mask in self._sector.select(timeout=2):
                call = key.data
                call(key)
        self._running = False


class Fetcher:
    def __init__(self, url):
        self.url = url
        url = parse.urlparse(url)
        self.host = url.netloc
        self.path = url.path
        if self.path == '':
            self.path = '/'
        self.data = b''

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)
        current_loop = Event_loop()
        self.seltor = current_loop._sector
        self.loop_tasks = current_loop._tasks

        try:
            logger.debug(f"get {url.hostname} {url.port}")
            self.client.connect((url.hostname, url.port))
        except BlockingIOError:
            pass
        self.seltor.register(self.client.fileno(), EVENT_WRITE, self.send)

    def send(self, key):
        self.seltor.unregister(key.fd)
        self.client.send(f"GET {self.path} HTTP/1.1\r\nHost:{self.host}\r\nConnection:close\r\n\r\n"
                         .encode("utf8"))
        self.seltor.register(self.client.fileno(), EVENT_READ, self.read)

    def read(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            self.seltor.unregister(key.fd)
            data = self.data.decode('utf8')
            data = data.split('\r\n\r\n')[1]
            info(data)
            self.client.close()
            self.loop_tasks.remove(self)


# async def request():
#     url = f'http://127.0.0.1:5000/name_{random.randint(0, 1000)}'
#     info(f'Waiting for {url}', )
#     result = await get(url)
#     info(f'Get response from {url} Resul: {result}')


if __name__ == '__main__':
    start = time.time()
    # tasks = [asyncio.ensure_future(request()) for _ in range(5)]
    loop = Event_loop()
    loop.add_task([Fetcher(f"http://127.0.0.1:5000/name_{i}") for i in range(1, 20)])
    loop.run_until_complete()

    end = time.time()
    info(f'Cost time: {end - start}')
