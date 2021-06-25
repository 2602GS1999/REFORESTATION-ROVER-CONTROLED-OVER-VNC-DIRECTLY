
#                                                COSMOS  MAIN  PROGRAM  MODULE

#=============================================================================================
import tkinter as T
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
    #system("espeak 'NOW , I AM MOVING BACKWARD'")

def FORWARD():
    next_line()
    print("GOING FORWARD")
    GPIO.output(7,1)
    GPIO.output(11,0)
    GPIO.output(13,0)
    GPIO.output(15,0)
    GPIO.output(37,0)
    #system("espeak 'NOW , I AM MOVING FORWARD'")

def LEFT ( ):
    next_line()
    print("NOW , I AM TURNING LEFT")
    GPIO.output(7,0)
    GPIO.output(11,0)
    GPIO.output(13,0)
    GPIO.output(15,1)
    GPIO.output(37,0)
    #system("espeak 'NOW , I AM TURNING LEFT'")
    

def RIGHT():
    print("GOING 'NOW , I AM TURNING RIGHT'")
    next_line()
    GPIO.output(7,0)
    GPIO.output(11,0)
    GPIO.output(13,1)
    GPIO.output(15,0)
    GPIO.output(37,0)
    #system("espeak 'NOW , I AM TURNING RIGHT'")

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

#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

FORBOTS= T.Tk()
FORBOTS.title(' COSMOS  UGV')
FORBOTS.geometry("600x700")
FORBOTS.configure(background='black')

#________________________________________________________________________________________________________________________________________
#                      MOVEMENT  CONTROL BUTTONS
#________________________________________________________________________________________________________________________________________

FWD=T.Button(FORBOTS, width=20,bg="blue",fg="white",height=3,text=' FORWARD', command =FORWARD)
FWD.place(x=210,y=300)

BCK=T.Button(FORBOTS, width=20,bg="blue",fg="white",height=3,text=' BACKWARD', command =BACKWARD)
BCK.place(x=210,y=420)

RHT=T.Button(FORBOTS, width=20,bg="blue",fg="white",height=3,text=' RIGHT', command =RIGHT)
RHT.place(x=400,y=360)

LFT=T.Button(FORBOTS,width=20,bg="blue",fg="white",height=3, text=' LEFT', command =LEFT)
LFT.place(x=20,y=360)

STP=T.Button(FORBOTS, width=20,bg="red",fg="white",height=3,text=' STOP', command =STOP)
STP.place(x=210,y=360)
#________________________________________________________________________________________________________________________________________
#                      ROVER FEATURE  BUTTONS
#________________________________________________________________________________________________________________________________________

SCM=T.Button(FORBOTS, width=20,height=2,bg="green",fg="white",text=' DEPLOY SEED CARE MODULE')
SCM.place(x=4,y=4)

DSB=T.Button(FORBOTS, width=20,bg="blue",fg="white",height=2,text=' DROP SEED BOMBS')
DSB.place(x=200,y=4)

LGT=T.Button(FORBOTS,width=20,height=2,bg="yellow",fg="black",text=' LIGHT ')
LGT.place(x=400,y=4)

LUK_LFT=T.Button(FORBOTS,width=20,height=2,text=' LOOK LEFT ')
LUK_LFT.place(x=4,y=60)

CAM=T.Button(FORBOTS,width=20,height=2,text='CAMERA')
CAM.place(x=200,y=60)

LUK_RHT=T.Button(FORBOTS,width=20,height=2,text=' LOOK RIGHT ')
LUK_RHT.place(x=400,y=60)

HBR= T.Button(FORBOTS,width=10,height=1,bg="red",fg="white",text='HIBERNATE')
HBR.place(x=4, y= 230)
#________________________________________________________________________________________________________________________________________
#                  OTHER STUFF
#________________________________________________________________________________________________________________________________________

FOR_TXT=T.Label(FORBOTS,text=':::::::::::::::::::::::::::::::::::::::::     COSMOS UGV   BY   TEAM   FORBOTS   :::::::::::::::::::::::::::::::::::::::::')
FOR_TXT.place(x=4, y=123)


ANC=T.Entry(FORBOTS, width=48,bg="white",fg="blue",bd=2,font=5)
ANC.place(x=2,y=180)

SPK=T.Button(FORBOTS,width=8,bg="blue",fg="white",height=1,text='ANNOUNCE')
SPK.place(x=505,y=180)

FORBOTS.mainloop()

