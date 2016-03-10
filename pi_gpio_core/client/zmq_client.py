import abc


class ZmqClientError(Exception):
    pass


class ZmqClient(metaclass=abc.ABCMeta):

    def __init__(self, context, server_addr):
        self.server_addr = server_addr
        self.context = context

    @abc.abstractmethod
    def _connect(self):
        pass

    @abc.abstractmethod
    def _disconnect(self):
        pass
