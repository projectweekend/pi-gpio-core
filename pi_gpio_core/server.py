from jsonrpc import JSONRPCResponseManager, dispatcher
import zmq


class Server:

    def __init__(self, addr):
        self.addr = addr
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind(self.addr)

    def run(self):
        while True:
            message = self.socket.recv_string()
            response = JSONRPCResponseManager.handle(message, dispatcher)
            self.socket.send_string(response.json)
