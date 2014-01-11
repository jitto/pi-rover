import SimpleHTTPServer
import urlparse
import RPi.GPIO as GPIO

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

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
      GPIO.setmode(GPIO.BOARD)
      GPIO.setup(16, GPIO.OUT)
      GPIO.output(16,True)
      GPIO.setup(18, GPIO.OUT)
      GPIO.output(18, False)
    else:
      GPIO.setmode(GPIO.BOARD)
      GPIO.setup(16, GPIO.OUT)
      GPIO.output(16,False)
      GPIO.setup(18, GPIO.OUT)
      GPIO.output(18, True)
 
    
 
