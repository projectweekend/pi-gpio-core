import zmq
from .zmq_client import ZmqClient, ZmqClientError


class SubClient(ZmqClient):

    def __init__(self, server_addr):
        context = zmq.Context()
        super().__init__(context=context, server_addr=server_addr)

    def _connect(self):
        self._socket = self._context.socket(zmq.SUB)
        self._socket.connect(self._server_addr)

    def _disconnect(self):
        self._socket.setsockopt(zmq.LINGER, 0)
        self._socket.close()

    def messages(self):
        yield self._socket.recv_json()