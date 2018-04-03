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
            data = json.loads(payload.decode('utf8'))
            from server.endpoints.agent_endpoints import endpoints
            endpoints[data[u'endpoint']](data)
        except Exception as ex:
            self.sendMessage(str(ex))

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {}".format(reason))


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
