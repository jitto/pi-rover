import time
import RPi.GPIO as GPIO

#10kbps to 100kbps - 100us to 10us
#needs pull up resister

#standby pulse - set to out and high for 600ms - back to low
#start header - short low pulse followed by header byte - 0x55 - followed by acknowledge sequence (MAK and SAK) - no slave responds during SAK time
#device address - 8 or 12 bit - 4 bits family code and 4 or 8 device code (no SAK for first device address byte - if using 2 byte address)
#command READ 0x03
#eeprom memory address - 16 bit - high byte first

class Unio:
  UNIO_STARTHEADER = 0x55
  UNIO_READ = 0x03
  UNIO_RDSR = 0x05
  UNIO_TSS = 0.000010
  UNIO_THDR = 0.000005
  UNIO_TSTBY = 0.000600
  UNIO_FUDGE_FACTOR = 0.000005
  UNIO_QUARTER_BIT = 0.000010
  gpioPin = 18
  addr = 0xa0

  def __init__(self):
    GPIO.setmode(GPIO.BCM)

  def readBytes(self, start, length):
    startClock = time.clock()
    self.standbyPulse()
    stbyClock = time.clock()
    self.startHeader()
    hdrClock = time.clock()
    self.send([self.addr, self.UNIO_READ, start >> 8, start & 0xff], False)
    sndClock = time.clock()
    result = self.read(length)
    readClock = time.clock()
    print startClock
    print "start %f, stby %f, hdr %f, snd %f, read %f" % (startClock, stbyClock, hdrClock, sndClock, readClock)
    return result

  def standbyPulse(self):
    self.setOutput()
    self.setBus(0)
    time.sleep(self.UNIO_TSS + self.UNIO_FUDGE_FACTOR)
    self.setBus(1)
    time.sleep(self.UNIO_TSTBY + self.UNIO_FUDGE_FACTOR)

  def startHeader(self):
    self.setBus(0)
    time.sleep(self.UNIO_THDR + self.UNIO_FUDGE_FACTOR)
    self.send([self.UNIO_STARTHEADER], True)

  def send(self, bytes, end):
    for byteIndex in range (0, len(bytes)):
      byte = bytes[byteIndex]
      for bitIndex in range(0, 8):
        self.writeBit(byte & 0x80)
        byte << 1
      self.writeBit(not (end and ((byteIndex + 1) == len(bytes))))
      sak = self.readBit() #check SAK for each byte sent
      print "send index %d with sak %d" % (byteIndex, sak)

  def read(self, length):
    result = []
    for byteIndex in range (0, length):
      data = 0
      self.setInput()
      for bitIndex in range (0, 8):
        data = (data << 1) | self.readBit()
      self.writeBit(not (byteIndex + 1 == length))
      sak = self.readBit() #check SAK after each byte read
      print "index %d with sak %d" % (byteIndex, sak)
      self.setOutput()
      result.append(data)
    return result

  def writeBit(self, bit):
    self.setBus(not bit)
    time.sleep(self.UNIO_QUARTER_BIT)
    time.sleep(self.UNIO_QUARTER_BIT)
    self.setBus(bit)
    time.sleep(self.UNIO_QUARTER_BIT)
    time.sleep(self.UNIO_QUARTER_BIT)

  def readBit(self):
    self.setInput()
    time.sleep(self.UNIO_QUARTER_BIT)
    a = self.readBus();
    time.sleep(self.UNIO_QUARTER_BIT)
    time.sleep(self.UNIO_QUARTER_BIT)
    b = self.readBus()
    time.sleep(self.UNIO_QUARTER_BIT)
    self.setOutput()
    return b and not a

  def readBus(self):
    return GPIO.input(17) 

  def setBus(self, state):
    GPIO.output(17, state)

  def setOutput(self):
    GPIO.setup(17, GPIO.OUT)

  def setInput(self):
    GPIO.setup(17, GPIO.IN)
