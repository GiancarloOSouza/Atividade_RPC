from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from Hospedagens import Hospe

hos = []

hospe1 = Hospe.Hospe("Marceio", "Ibis", 800)
hospe2 = Hospe.Hospe("Sao Paulo", "Ibis", 700)
hospe3 = Hospe.Hospe("Fernando de noronha", "Ibis", 600)
hospe4 = Hospe.Hospe("Belo Monte", "Ibis", 500)

hos.append(hospe1) 
hos.append(hospe2)
hos.append(hospe3)
hos.append(hospe4)




# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('192.168.0.104', 12000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    def baratoIbis(x):
        ho = []
        for i in hos:
            if(i.valor < x):
                r = (i.cidade, i.hotel, i.valor)
                ho.append(r)
        return ho


    
    
    server.register_function(baratoIbis, 'baratoIbis')

    server.serve_forever()