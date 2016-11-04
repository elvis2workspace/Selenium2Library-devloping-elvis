#coding=utf-8
'''
Created on 2015年1月31日

@author: Elvis
'''

from twisted.internet import protocol, reactor, endpoints

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)
        
class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()
    
endpoints.serverFromString(reactor, "tcp:1234").listen(EchoFactory())
reactor.run()