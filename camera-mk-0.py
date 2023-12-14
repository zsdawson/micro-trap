from picamera import PiCamera
from datetime import datetime
import os

# Initialize the camera
camera = PiCamera()

# Capture the image with a timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"/path/to/usb/drive/image_{timestamp}.jpg"
camera.capture(filename)


camera.led = False

# Reduce power consumption
# Turn off HDMI
os.system('sudo /usr/bin/tvservice -o')

# Add more commands to turn off other non-essential items
