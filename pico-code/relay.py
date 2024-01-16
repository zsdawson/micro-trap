from machine import Pin
import utime

# Set up the relay pin
relay_pin = Pin(16, Pin.OUT)

# Function to turn on the relay for a specified duration
def turn_on_relay(duration):
    relay_pin.high()  # Turn on the relay
    try:
        utime.sleep(duration)  # Keep the relay on for the specified duration
    except KeyboardInterrupt:
        print("Operation cancelled by user.")
    finally:
        relay_pin.low()  # Turn off the relay to ensure it is off


turn_on_relay(15)
