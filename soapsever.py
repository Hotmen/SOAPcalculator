import SOAPpy

def hello(x ,y):
    return x+y

server = SOAPpy.SOAPServer(("localhost", 8080))
server.registerFunction(hello)
server.serve_forever()
