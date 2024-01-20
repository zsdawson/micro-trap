from machine import Pin
import utime

# Initialize Relay
relay_pin = Pin(15, Pin.OUT)

def toggle_relay():
    while True:
        relay_pin.value(1)  # Turn on relay
        utime.sleep(15)     # Wait for 15 seconds

        relay_pin.value(0)  # Turn off relay
        utime.sleep(15)     # Wait for 15 seconds

# Start toggling the relay
toggle_relay()
