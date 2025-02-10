from machine import Pin 
import utime
led = Pin(7, Pin.OUT)
while True: 
    led.toggle() 
    utime.sleep(0.5)