from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from Hospedagens import Hospe

hos = []

hospe1 = Hospe.Hospe("Marceio", "Ibis", 5)
hospe2 = Hospe.Hospe("Sao Paulo", "Cabana o seu zé", 6)
hospe3 = Hospe.Hospe("Fernando de noronha", "", 7)
hospe4 = Hospe.Hospe("Belo Monte", "M", 8)

hos.append(hospe1) 
hos.append(hospe2)
hos.append(hospe3)
hos.append(hospe4)



# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('192.168.0.104', 11290),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    def barato(x):
        ho = []
        for i in hos:
            if(i.valor < x):
                r = (i.cidade, i.hotel, i.valor)
                ho.append(r)
        return ho

    server.register_function(barato, 'barato')

    server.serve_forever()