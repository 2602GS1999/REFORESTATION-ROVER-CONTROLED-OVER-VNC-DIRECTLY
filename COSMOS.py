
#                                                COSMOS  MAIN  PROGRAM  MODULE

#=============================================================================================
import time
import random

import RPi.GPIO as GPIO

from os import system
from subprocess import call

from INPUT import *
from OUTPUT import *
from OUTPUT_SPECIAL  import *
from PEOPLE import *
from TOPICS import *

from CHAT_ALGORITHMS import *

GPIO.setmode( GPIO.BOARD )
GPIO.setwarnings(False)

#============================================================================================
GPIO.setup(7 , GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def BACKWARD():
    next_line()
    print("GOING BACKWARD")
    GPIO.output(7,0)
    GPIO.output(11,1)
    GPIO.output(13,0)
    GPIO.output(15,0)
    GPIO.output(37,0)
    system("espeak 'NOW , I AM MOVING BACKWARD'")

def FORWARD():
    next_line()
    print("GOING FORWARD")
    GPIO.output(7,1)
    GPIO.output(11,0)
    GPIO.output(13,0)
    GPIO.output(15,0)
    GPIO.output(37,0)
    system("espeak 'NOW , I AM MOVING FORWARD'")

def LEFT ( ):
    next_line()
    print("NOW , I AM TURNING LEFT")
    GPIO.output(7,0)
    GPIO.output(11,0)
    GPIO.output(13,0)
    GPIO.output(15,1)
    GPIO.output(37,0)
    system("espeak 'NOW , I AM TURNING LEFT'")
    

def RIGHT():
    print("GOING 'NOW , I AM TURNING RIGHT'")
    next_line()
    GPIO.output(7,0)
    GPIO.output(11,0)
    GPIO.output(13,1)
    GPIO.output(15,0)
    GPIO.output(37,0)
    system("espeak 'NOW , I AM TURNING RIGHT'")

def STOP():
    next_line()
    print("STOPPING BOTH MOTORS ")
    GPIO.output(7,0)
    GPIO.output(11,0)
    GPIO.output(13,0)
    GPIO.output(15,0)
    GPIO.output(37,1)
    system("espeak 'STOPPING BOTH MOTORS' ")

def STAND_STILL():   # ROBOT IS ALWAYS STATIONARY WHILE IN INTERACTIVE MODE

    GPIO.output(7,0)
    GPIO.output(11,0)
    GPIO.output(13,0)
    GPIO.output(15,0)
    GPIO.output(37,1)
    system("espeak -s 150 'STANDBY!'")

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# PERMISSION  TO  MOVE  THE  ROBOT  GRANTED!

def MOVEMENT_GRANT():
    
    print(WARNING)
    system(warning)
    time.sleep(2)
    print(LA_GRANDED)
    system(la_granded)
    
    while(1):
        qstn=input(COMMAND_REQUEST)
        qstn=qstn.upper()
        QSTN=qstn.split()

        if any(x in QSTN for x in fwd) == True :
            FORWARD()
            time.sleep(10)
            STOP()
            
        elif any(x in QSTN for x in bak) == True :
            BACKWARD()
            time.sleep(10)
            STOP()
            
        elif any(x in QSTN for x in rit) == True :
            RIGHT()
            time.sleep(1)
            STOP()
            
        elif any(x in QSTN for x in lft) == True :
            LEFT()
            time.sleep(1)
            STOP()
        elif any(x in QSTN for x in stp) == True :
            STOP()
            
        elif any(x in QSTN for x in shutdown) == True :
            STAND_STILL()
            next_line()
            print('SHUTTING DOWN...')
            system("espeak 'Shutting down!' ")
            system("sudo shutdown")
        else :
            STAND_STILL()
            pass


            
 #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

STAND_STILL()
prsn_recog()
chat_mode()
MOVEMENT_GRANT()


