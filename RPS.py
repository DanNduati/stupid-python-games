import time 
import serial
import random
3

selection = {1:"Rock",2:"Paper",3:"Scissors"}
#print(len(selection))
print("|``|  |``|  |````")
print("|__|  |__|  |____")
print("|\    |         |")
print("| \   |     ____|")
print("Rock paper scissors")
print("Dan the shitty programmer")
print("Press ctrl+c to quit\n")

def play():
	global user
	user = int(input("Enter your choice [1-3] for: Rock ,Paper ,Scissors :\n"))
	print("please wait for computer to think :>)")
	
	time.sleep(1.5)
	global cpu_select
	print("Your choice is:\t%s")%selection[user]
	cpu_select = random.randrange(1,4)
	cpu = selection[cpu_select]
	print ("the computer chose: %s\n")%cpu
	
def checkWin():
	#user winning
	if( user == 1 and cpu_select ==3 ):
		print("you've won!!!")
	elif( user == 3 and cpu_select ==2):
		print("you've won!!!")
	elif(user == 2 and cpu_select == 1):
		print("you've won!!!")
	elif(user == cpu_select):
		print("You draw!!")
	else:
		print("you've lost!!!")
try:
	while(True):		
		play()
		checkWin()
except KeyboardInterrupt: 
	pass
