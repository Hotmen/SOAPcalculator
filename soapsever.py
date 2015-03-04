import SOAPpy
import polishrecord


def calculate(expression):
    return polishrecord.polish(polishrecord.exptopolish(expression))


class MySoapServer(SOAPpy.SOAPServer):
    def __init__(self, host, port):
        SOAPpy.SOAPServer.__init__(self, (host, port))
        self.registerFunction(calculate)

if __name__ == '__main__':
    ser = MySoapServer('localhost', 8080)
    ser.serve_forever()