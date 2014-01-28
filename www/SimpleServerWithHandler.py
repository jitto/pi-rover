
import SocketServer
import MyHandler
from MyHandler import initMotor

PORT = 80

Handler = MyHandler.MyHandler
initMotor()

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
