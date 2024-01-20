# File: rtc_setup_and_use.py
import RTC_DS3231

# Initialize RTC with default SDA and SCL pins for I2C0
# GPIO 8 (SDA), GPIO 9 (SCL)
rtc = RTC_DS3231.RTC(sda_pin=8, scl_pin=9)

# Function to set the time on the DS3231
def set_time():
    # Set the time (modify the byte string to the current time)
    rtc.DS3231_SetTime(b'\x00\x32\x17\x05\x19\x01\x24')  # Example: # 4:30:00 PM, Fri, 19 January 2024

# Function to get the current time from the DS3231
def get_time():
    # Get the current time (mode 1 for formatted string)
    return rtc.DS3231_ReadTime(1)

# Set the time
set_time()

# Get and print the current time
current_time = get_time()
print("Current Time:", current_time)


