from jsonrpc import JSONRPCResponseManager
import zmq
from .gpio import gpio_dispatcher


class Server:

    def __init__(self, port):
        self.port = port
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind('tcp://127.0.0.1:{0}'.format(self.port))

    def run(self):
        while True:
            message = self.socket.recv_string()
            response = JSONRPCResponseManager.handle(message, gpio_dispatcher)
            self.socket.send_string(response.json)
