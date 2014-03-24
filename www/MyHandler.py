import SimpleHTTPServer
import urlparse
from webiopi import GPIO
import time
from subprocess import call

def initMotor():
    GPIO.setFunction(17, GPIO.PWM)
    GPIO.setFunction(22, GPIO.PWM)
    GPIO.setFunction(23, GPIO.PWM)
    GPIO.setFunction(24, GPIO.PWM)
    motorTurn(0.2, 0, 0.2, 0)
    time.sleep(.1)
    motorTurn(0, 0, 0, 0)

def motorTurn(right1, right2, left1, left2):
    GPIO.pulseRatio(17, right1)
    GPIO.pulseRatio(22, right2)
    GPIO.pulseRatio(23, left1)
    GPIO.pulseRatio(24, left2)


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
      motorTurn(0.8, 0, 0.9, 0)
    elif ( 'backward' in self.path ):     
      motorTurn(0, 0.4, 0, 0.5)
    elif ( 'left' in self.path ):
      motorTurn(0.4, 0, 0.8, 0)
    elif ( 'right' in self.path):
      motorTurn(0.8, 0, 0.4, 0)
    elif ( 'stop' in self.path):
      motorTurn(0, 0, 0, 0)
    elif ( 'camera' in self.path ):
      call(["raspistill", "-t", "10", "-o", "test.jpg"])
 
