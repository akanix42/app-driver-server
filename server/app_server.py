import json

from autobahn.twisted.websocket import WebSocketServerProtocol


# or: from autobahn.asyncio.websocket import WebSocketServerProtocol


class MyServerProtocol(WebSocketServerProtocol):

    def onConnect(self, request):
        print("Client connecting: {}".format(request.peer))

    def onOpen(self):
        print("WebSocket connection open.")

    def onMessage(self, payload, isBinary):
        try:
            print 'payload ' + payload
            print 'isBinary ' + str(isBinary)
            data = json.loads(payload.decode('utf8'))
            from endpoints import endpoints
            endpoints[data[u'endpoint']](self, data)
        except Exception as ex:
            print('error')
            print str(ex)
            self.send_message({'error': str(ex)})

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {}".format(reason))

    def send_message(self, data):
        self.sendMessage(json.dumps(data))


# if __name__ == '__main__':
import sys

from twisted.python import log
from twisted.internet import reactor

log.startLogging(sys.stdout)

from autobahn.twisted.websocket import WebSocketServerFactory

factory = WebSocketServerFactory()
factory.protocol = MyServerProtocol
factory.setProtocolOptions(autoPingInterval=5,
                           autoPingTimeout=2)

reactor.listenTCP(9000, factory)
reactor.run()
