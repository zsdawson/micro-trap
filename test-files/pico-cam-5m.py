import RTC_DS3231
from machine import Pin
import utime

# Initialize RTC with default SDA and SCL pins for I2C0
# GPIO 8 (SDA), GPIO 9 (SCL)
rtc = RTC_DS3231.RTC(sda_pin=8, scl_pin=9)

# Initialize Relay
relay_pin = Pin(15, Pin.OUT)

def control_relay():
    last_minute_checked = -1
    relay_state = False

    while True:
        current_time = rtc.DS3231_ReadTime(1)
        current_minute = int(current_time.split(':')[1])
        current_second = int(current_time.split(':')[2][:2])

        # Synchronize the check to happen at an even interval
        if current_second % 5 != 0:
            utime.sleep(5 - current_second % 5)
            continue

        print(f"Current Time: {current_time}, Relay State: {'ON' if relay_state else 'OFF'}")

        # Check if the minute has changed
        if current_minute != last_minute_checked:
            last_minute_checked = current_minute

            # Determine the 5-minute cycle (0-4, 5-9, 10-14, etc.)
            cycle_minute = current_minute % 5

            # Turn on the relay for the first 2 minutes of each cycle
            if cycle_minute < 2:
                if not relay_state:
                    relay_pin.value(1)  # Turn on relay
                    relay_state = True
                    print("Relay ON")

            # Turn off the relay for the last 3 minutes of each cycle
            else:
                if relay_state:
                    relay_pin.value(0)  # Turn off relay
                    relay_state = False
                    print("Relay OFF")

        # Wait for 5 seconds before the next check
        utime.sleep(5)

# Start controlling the relay
control_relay()

