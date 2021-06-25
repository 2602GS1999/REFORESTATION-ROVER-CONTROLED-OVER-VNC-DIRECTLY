from os import system
from PEOPLE import *
def next_line():
    print('\r\n\r\n')
    
def prsn_recog():
    system("espeak -s 150 'hello i am Cosmos! Who are you?'")
    q1=input("HELLO! I'M COSMOS. WHO ARE YOU?")
    q1=q1.upper()
    Q1= q1.split()
    if any(x in Q1 for x in me) == True:
        next_line()
        system("espeak -s 150 ' USER IDENTIFIED AS GAENESH SHREEDHAR'")
        q2=input(" USER IDENTIFIED AS GANESH SREEDHAR ")
    elif any(x in Q1 for x in sih) == True :
        next_line()
        system("espeak -s 150 'Access granted for team FORBOTS'")
        q2=input("ACCESS GRANTED FOR TEAM FORBOTS ")
    elif any(x in Q1 for x in dr_sl) == True:
        next_line()
        system("espeak -s 150 'USER IDENTIFIED AS Dr. P. SOOJAN LAAL , PRICIPAL OF MBITS'")
        q2=input( "USER IDENTIFIED AS Dr. P. SOJAN LAL , PRICIPAL OF MBITS")
    elif any(x in Q1 for x in hod)== True:
        next_line()
        system("espeak -s 150 'USER IDENTIFIED AS Dr ROY MATHEW, HEAD OF DEPARTMENT, MECHANICAL ENGINEERING!'")
        q2=input('USER IDENTIFIED AS Dr ROY MATHEW, HEAD OF DEPARTMENT, MECHANICAL ENGINEERING!')
    elif any(x in Q1 for x in prof) == True:
        next_line()
        system("espeak -s 150 'HELLO PROFESSOR, I KNOW YOU!'")
        q2=input("HELLO PROFESSOR, I KNOW YOU!")
    elif any(x in Q1 for x in stud)== True:
        next_line()
        system("espeak -s 150 'YOU ARE AN ENGINEERING STUDENT , RIGHT?'")
        q2=input("YOU ARE AN ENGINEERING STUDENT RIGHT?")
    else:
        next_line()
        system("espeak -s 150 'I DO NOT KNOW WHO YOU ARE. BUT THAT IS OKAY!'")
        q2=input("I DO NOT KNOW WHO YOU ARE. BUT THAT IS OKAY!")

    q2.upper()
    Q2=q2.split()

def chat_mode():
    next_line()
    system("espeak -s 150 s'I CAN PERFORM VARIOUS TASKS. WHAT ARE YOU LOOKING FOR?'")
    r=input('I CAN PERFORM VARIOUS TASKS. WHAT ARE YOU LOOKING FOR?')
    

    
    
