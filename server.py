from jsonrpc import JSONRPCResponseManager, dispatcher
import zmq


context = zmq.Context(io_threads=3)
socket = context.socket(zmq.REP)
socket.bind('tcp://*:5555')


def main():

    while True:
        #  Wait for next request from client
        message = socket.recv_string()
        print('Received request: {0}'.format(message))

        response = JSONRPCResponseManager.handle(message, dispatcher)

        socket.send_string(response.json)


if __name__ == '__main__':
    main()
