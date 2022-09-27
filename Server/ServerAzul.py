from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from Hospedagens import Hospe

hospe = []

hospe1 = Hospe("Marceio", "Ibis", 500)
hospe2 = Hospe("Sao Paulo", "Cabana o seu zé", 600)
hospe3 = Hospe("Fernando de noronha", "", 700)
hospe4 = Hospe("Belo Monte", "M", 800)

hospe.append(hospe1) 
hospe.append(hospe2)
hospe.append(hospe3)
hospe.append(hospe4)




# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('192.168.0.104', 11290),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    def barato(valor):
        for i in hospe:
            if(i.valor < valor):
                print
                print("Na cidade " + i.cidade + "\n, O hotel "+ i.hotel+ "esta com o valor de: " +i.valor)


    
    
    server.register_function(barato, 'barato')

    server.serve_forever()