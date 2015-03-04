from SOAPpy import SOAPProxy
import sys
import socket
import threading
from soapsever import MySoapServer


def startcalculate(host, port):
    sock = socket.socket()
    try:
        sock.connect((host, port))
    except socket.error:
        sys.stdout.write('Server is down, try later!')
        sock.close()
        return
    sock.close()
    url = str(host) + ':' + str(port)
    conn = SOAPProxy(url)
    # conn.config.dumpSOAPOut = 1        #Debug option for output connection
    # conn.config.dumpSOAPIn = 1         #Debug option for input connection

    data = ''
    sys.stdout.write('Welcome to calculator!\n')
    sys.stdout.write('Type expression to calculate or quit to exit\n')
    while data != 'quit':
        sys.stdout.write('>>')
        data = sys.stdin.readline().strip()
        if data != 'quit':
            sys.stdout.write('Result is ' + str(conn.calculate(data)) + '\n')

if __name__ == '__main__':
    srv = MySoapServer('localhost', 8080)
    th = threading.Thread(target=srv.serve_forever, args=())
    th.start()
    startcalculate('localhost', 8080)
    srv.shutdown()
    th.join()
