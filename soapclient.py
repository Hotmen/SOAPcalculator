from SOAPpy import SOAPProxy

conn = SOAPProxy('localhost:8080')
conn.config.dumpSOAPOut = 1        #Debug option for output connection
conn.config.dumpSOAPIn = 1         #Debug option for input connection
print conn.hello(1, 5)