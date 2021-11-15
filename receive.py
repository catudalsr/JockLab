from machine import Pin, UART
from time import sleep


uart = UART(0, 9600) # init with given baudrate

user_input = ""

while True:
    if uart.any():
        user_input = uart.readline()
        
        #cleanup transmission that was recieved with the 'decode' attribute
        print(user_input.decode("UTF-8"))
        
    else:
        sleep(.1) #sleep to allow uart to read full transmission
        
