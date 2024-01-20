# File: get_current_time.py
import RTC_DS3231

# Initialize RTC with default SDA and SCL pins for I2C0
# GPIO 8 (SDA), GPIO 9 (SCL)
rtc = RTC_DS3231.RTC(sda_pin=8, scl_pin=9)

# Function to get the current time from the DS3231
def get_time():
    # Get the current time (mode 1 for formatted string)
    return rtc.DS3231_ReadTime(1)

# Get and print the current time
current_time = get_time()
print("Current Time:", current_time)
