from machine import Pin, Timer
import utime

# Initialize the relay control pin (Assuming it's connected to GPIO 15)
relay = Pin(15, Pin.OUT)

# Initialize timer for hourly tasks
timer = Timer()

# Function to toggle power to the Raspberry Pi
def toggle_power(timer):
    relay.value(not relay.value())

# Set up the timer to call toggle_power every hour
timer.init(period=3600000, mode=Timer.PERIODIC, callback=toggle_power)

# Main loop
try:
    while True:
        # add code to monitor voltage/current sensors
        # and manage power from solar panel and battery
        utime.sleep(1)
except KeyboardInterrupt:
    timer.deinit()  # Clean up the timer when stopping the script
