import json
import zmq
from .zmq_client import ZmqClient, ZmqClientError


class ReqRepClient(ZmqClient):

    def __init__(self, server_addr, max_retries=3, timeout=3000):
        context = zmq.Context()
        super().__init__(context=context, server_addr=server_addr)
        self.max_retries = max_retries
        self.remaining_retries = self.max_retries
        self.timeout = timeout
        self._connect()

    def _connect(self):
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect(self.server_addr)
        self.poll = zmq.Poller()
        self.poll.register(self.socket, zmq.POLLIN)

    def _disconnect(self):
        self.socket.setsockopt(zmq.LINGER, 0)
        self.socket.close()
        self.poll.unregister(self.socket)

    def request(self, obj):
        while self.remaining_retries:
            json_data = json.dumps(obj=obj)
            self.socket.send_string(json_data)
            expect_reply = True
            while expect_reply:
                socks = dict(self.poll.poll(self.timeout))
                if socks.get(self.socket) == zmq.POLLIN:
                    response = self.socket.recv_string()
                    if not response:
                        break
                    else:
                        self.remaining_retries = self.max_retries
                        expect_reply = False
                        return json.loads(response)
                else:
                    self._disconnect()
                    self.remaining_retries -= 1
                    if self.remaining_retries == 0:
                        # server is not online so stop trying
                        break
                    self._connect()
                    self.socket.send_string(json_data)
        else:
            self.context.term()
            raise ZmqClientError('Max reconnect attempts exceeded')
