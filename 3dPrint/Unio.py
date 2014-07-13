import time
import RPi.GPIO as GPIO

#10kbps to 100kbps - 100us to 10us
#needs pull up resister

#standby pulse - set to out and high for 600ms - back to low
#start header - short low pulse followed by header byte - 0x55 - followed by acknowledge sequence (MAK and SAK) - no slave responds during SAK time
#device address - 8 or 12 bit - 4 bits family code and 4 or 8 device code (no SAK for first device address byte - if using 2 byte address)
#command READ 0x03
#eeprom memory address - 16 bit - high byte first

def usleep(microSeconds):
  time.sleep(microSeconds/1000000)

class Unio:
  UNIO_STARTHEADER = 0x55
  UNIO_READ = 0x03
  UNIO_RDSR = 0x05
  UNIO_TSS = 10
  UNIO_THDR = 5
  UNIO_TSTBY = 600
  UNIO_FUDGE_FACTOR = 5
  UNIO_QUARTER_BIT = 10
  gpioPin = 18
  addr = 0xa0

  def __init__(self):
    GPIO.setmode(GPIO.BCM)

  def readBytes(self, start, length):
    self.standbyPulse()
    self.startHeader()
    self.send([self.addr, self.UNIO_READ, start >> 8, start & 0xff], False)
    return self.read(length)

  def standbyPulse(self):
    self.setBus(0)
    self.setOutput()
    usleep(self.UNIO_TSS + self.UNIO_FUDGE_FACTOR)
    self.setBus(1)
    usleep(self.UNIO_TSTBY + self.UNIO_FUDGE_FACTOR)

  def startHeader(self):
    self.setBus(0)
    usleep(self.UNIO_THDR + self.UNIO_FUDGE_FACTOR)
    self.send([self.UNIO_STARTHEADER], True)

  def send(self, bytes, end):
    for byteIndex in range (0, len(bytes)):
      byte = bytes[byteIndex]
      for bitIndex in range(0, 8):
        self.rwbit(byte & 0x80)
        byte << 1
      self.rwbit(end and ((byteIndex + 1) == len(bytes)))
    return self.readBit()

  def read(self, length):
    result = []
    for byteIndex in range (0, length):
      data = 0
      self.setInput()
      for bitIndex in range (0, 8):
        data = (data << 1) | self.rwbit(1)
      self.setOutput()
      self.readBit()
      result.append(data)

  def rwbit(self, bit):
    self.setBus(not bit)
    usleep(self.UNIO_QUARTER_BIT)
    a = self.readBus();
    usleep(self.UNIO_QUARTER_BIT)
    self.setBus(bit)
    usleep(self.UNIO_QUARTER_BIT)
    b = self.readBus()
    usleep(self.UNIO_QUARTER_BIT)
    return b and not a

  def readBit(self):
    self.setInput()
    b = self.rwbit(1)
    self.setOutput()
    return b

  def readBus(self):
    return GPIO.input(17) 

  def setBus(self, state):
    GPIO.output(17, state)

  def setOutput(self):
    GPIO.setup(17, GPIO.OUT)

  def setInput(self):
    GPIO.setup(17, GPIO.IN)
