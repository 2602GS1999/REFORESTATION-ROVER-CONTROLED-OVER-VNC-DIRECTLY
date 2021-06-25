def next_line():
    print('\r\n\r\n')
    
GREETING_SPEECH='''
Hello!

  I'm Cosmos, a machine  of a different kind!

  '''
greeting_speech='''espeak  -s 150 "Hello!
  I'm Cosmos, a machine  of a different kind!

  '''
TASK=['HOW CAN I HELP YOU?\r\n','NEXT TASK PLEASE\r\n',
'GIVE ME THE NEXT COMMAND, PLEASE\r\n','WAITING FOR COMMAND\r\n']

COMMAND_REQUEST='''
\r\n\r\n______________________________________ ENTER  COMMAND ______________________________________ \r\n '''

WARNING =""" DISCONNECT  VGA CABLE, MOUSE AND KEYBOARD, IF CONNECTED.
MAKE SURE THAT VNC SERVER IS ENABLED.
OPERATE WITH CARE!  """
warning ="""espeak  -s 150       '''  DISCONNECT  VGA CABLE, MOUSE AND KEYBOARD, IF CONNECTED.
MAKE SURE THAT VNC SERVER IS ENABLED!
OPERATE WITH CARE!   '''       """

LA_GRANDED =" \r\n\r\n  LOCOMATION ACCESS GRANTED!  \r\n\r\n "
la_granded ="espeak  -s 150 'Locomation access granted! ' "

#=======================================================================================

machine="""  espeak -s 150 "Machines who think like human beings doesn't really present a problem!
But people who think like machines are more than enough to cause chaos in society! "

"""
