import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://192.168.0.104:8000')
print(s.pow(2,7))  # Returns 2**3 = 8
print(s.add(2,10))  # Returns 5
print(s.mul(5,25))  # Returns 5*2 = 10


d = xmlrpc.client.ServerProxy('http://192.168.0.104:11290')

print(d.zero(12,4))

# Print list of available methods
print(s.system.listMethods())