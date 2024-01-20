# micro-trap

### a 3d printed housing for the eletronics will hold a rpi-02w to take the pictures then the power will be managed by a arduino nano that will also send a signal to take the picture and the rpi-02w will have rtc to keep the corect time and send the pictures to a thumb drive and this will be all in one contained unit that will be make to be somewhat water proof.

##setup and install instructions 
needed to make 



lits of notes needed  
wiring for relay 
wiring for relay-diagram
wiring for rtc (done)
wiring for rtc-diagram
initialise rtc to the pico instructions
set time rtc instructions



##librarys needed 
micropython_DS3231

not nessicary but if you need incresed web functionality of the rpi-02w you can do a series of comands in the rerminal to help with the low ram but this can make hte sd card wear out faster so up to you  but jsut exciute the code is i have below and it should make it 2-3 times faster 

step 1:sudo nano dphys-swapfile swapoff 
step 2:sudo nano /etc/dphys-swapfile
step 3:change the number in there from 100 to 2048
step 4:sudo dphys-swapfile setup
step 5:sudo nano dphys-swapfile swapon

that should fix it and help a bit 
