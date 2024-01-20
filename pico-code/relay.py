from machine import Pin
import utime

relay_pin = Pin(16, Pin.OUT)

def activate_relay(duration):
    print("Relay ON")
    relay_pin.high()
    utime.sleep(duration)
    print("Relay OFF")
    relay_pin.low()

activate_relay(15)
