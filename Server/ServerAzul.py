from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('192.168.0.104', 11290),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

 
    def tudoZero(x, y):
        m = (x*y) * 0
        return  m
    
    server.register_function(tudoZero, 'zero')

    server.serve_forever()