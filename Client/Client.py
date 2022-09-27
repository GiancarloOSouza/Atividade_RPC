import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://192.168.0.191:8000')

print(s.maisBarato(8))  # Returns 2**3 = 8



# Print list of available methods
print(s.system.listMethods())
