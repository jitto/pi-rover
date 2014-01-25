import SimpleHTTPServer
import urlparse
import RPi.GPIO as GPIO

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

  def motorTurn(self, pin8, pin10, pin16, pin18):
    GPIO.output(16,pin16)
    GPIO.output(18, pin18)
    GPIO.output(11,pin8)
    GPIO.output(15, pin10)
      
  def __init__(self, request, client_address, server):
    SimpleHTTPServer.SimpleHTTPRequestHandler.__init__(self, request, client_address, server)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
  
  def do_GET(self):

    parsedParameters = urlparse.urlparse(self.path)
    queryParsed = urlparse.parse_qs(parsedParameters.query)

    if ( 'rover' in self.path ):
      self.processMyRequest(self.path)
    else:
      SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self);

  def processMyRequest(self, query):
    print query
    
    if ( 'forward' in self.path ):            
      self.motorTurn(True, False, True, False)
    elif ( 'backward' in self.path ):     
      self.motorTurn(False, True, False, True)
    elif ( 'left' in self.path ):
      self.motorTurn(False, True, True, False)
    elif ( 'right' in self.path):
      self.motorTurn(True, False, False, True)
    elif ( 'stop' in self.path):
      self.motorTurn(False, False, False, False)
      
  
      