import machine
import utime
picoLED = machine.Pin(25, machine.Pin.OUT)
while True:
    picoLED.toggle()
    utime.sleep(1)