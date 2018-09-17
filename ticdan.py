import time
import serial
#create an array for board positions 
board= [' ',' ',' ',' ',' ',' ',' ',' ',' ']
#starting player and mark
player = 1
mark = 'X'
#winning flags
win = 1
draw = -1
running = 0
stop = 1

game = running
def drawboard():
	print("%c | %c | %c") %(board[0],board[1],board[2])
	print("__|__ |__")
	print("%c | %c | %c") %(board[3],board[4],board[5])
	print("__|__ |__")
	print("%c | %c | %c") %(board[6],board[7],board[8])
	print("  |   |  ")

#function to check if a position is empty
def checkPosition(x):
	if(board[x]==' '):
		return True
	else:
		return False
	
def checkWin():
	global game
	#horizontal winning combo
	if(board[0]==board[1] and board[1]==board[2] and board[0] !=' '):
		game = win
	elif(board[3]==board[4] and board[4]==board[5] and board[4] !=' '):
		game = win
	elif(board[6]==board[7] and board[7]==board[8] and board[6] !=' '):
		game = win
	#vertical winning combo
	elif(board[0]==board[3] and board[3]==board[6] and board[0] !=' '):
		game = win
	elif(board[1]==board[4] and board[4]==board[7] and board[1] !=' '):
		game = win
	elif(board[2]==board[5] and board[5]==board[8] and board[2] !=' '):
		game = win
	#diagonal winning conditions
	elif(board[0]==board[4] and board[4]==board[8] and board[0] !=' '):
		game = win
	elif(board[2]==board[4] and board[4]==board[6] and board[2] !=' '):
		game = win
	#draw
	elif(board[0]!=' ' and board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!='' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' '):
		game = draw
	else:
		#game is still on
		game = running
		
		
print ("Tic - Tac -Toe ")
print ("Dan the shitty programmer\t")
print("player 1[X] and player 2[O]\n")
print()
print()
print("Please wait.........")
time.sleep(2)
#drawboard()
while(game == running):
	drawboard()
	#check for player 
	if (player %2 !=0):
		print("player 1's turn")
		mark = 'X'
	else:
		print("player 2's turn")
		mark = 'O'
	#check for user input
	choice = int(input("Enter the position between [1-9] where you want to mark: ")-1)
	#user inputvalidation
	if (choice >9 or choice <0):
		print("please enter a valid integer choice [1-9]")
		break
	else:
		if (checkPosition(choice) == True):
			board[choice] = mark
			player+=1
			checkWin()
drawboard()
if (game == win):
	if(player%2!=0):
		print("player 2 won")
	else:
		print("player 1 won")
elif(game == draw):
	print ("game ended as a draw")
		
		