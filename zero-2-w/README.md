first thing to do is set up the raspberry pi and also probbly set the password to password to keep things simple. the next thing to do is to go and do some comands that i will show below and then and after your raspberry pi is in position then activate the cron job and every time its powered on it will take a picture on boot.

first terminal comands  

sudo apt-get update  
sudo apt-get upgrade  

then after both work create/run this code   
nano ~/capture_image.sh  

then add this code to the file  
#!/bin/bash  
DATE=$(date +"%Y-%m-%d_%H%M")  
mkdir -p /home/pi/Desktop/photos-pi  
raspistill -o /home/pi/Desktop/photos-pi/image_$DATE.jpg  

