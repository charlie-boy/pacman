import random

class Person(object):
	board = [35*["."] for i in range(0,15)]
	score = 0

	def __init__(self):
		self.board = board
		self.score = score

	def board_design(self):												# basic_board_design
		for i in range(3, 12):											# "X" represents wall
			for j in range(8, 9):										# "C" represents coin
				self.board[i][j] = "X"

			for j in range(15, 16):
				self.board[i][j] = "X"

			for j in range(18, 19):
				self.board[i][j] = "X"

			for j in range(25, 26):
				self.board[i][j] = "X"

		for i in [3]:
			for j in range(9, 15):
					self.board[i][j] = "X"

			for j in range(19, 25):
					self.board[i][j] = "X"

		for i in [8]:
			for j in range(10, 24):
					self.board[i][j] = "X"

		for i in range(3, 12):
			for j in range(5,7):
				self.board[i][j] = "C"


	def update_board(self, px, py, b_coords):
		self.px = px
		self.py = py
		self.b_coords = b_coords

		if self.checkCoin(self.px, self.py):
			self.collectCoin()												# increments the number of coin
			cx, cy = self.place_another_coin()								# places random coins on the board
			self.board[cx][cy] = "C"

		self.board[self.px][self.py] = "P"
		for i in range(0, len(b_coords)):
			self.board[b_coords[i][0]][b_coords[i][1]] = "G"

		self.previous_px = self.px 											# position of pacman at t-1
		self.previous_py = self.py

	def checkWall(self, x, y):												# mentioned in assignment
		if(self.board[x][y] == "X"):
			return True
		else:
			return False

	def checkCoin(self, x, y):
		if(self.board[x][y] == "C"):
			return True
		else:
			return False

	def checkPacman(self, x, y):												# mentioned in assignment
		if(self.board[x][y] == "P"):
			return True
		else:
			return False

	def checkGhost(self, x, y):
		if(self.board[x][y] == "G"):
			return True
		else:
			return False


	def collectCoin(self):												# mentioned in assignment
		self.score = self.score + 1

	def place_another_coin(self):
		cx = random.randrange(0, 15, 1)
		cy = random.randrange(0, 35, 1)

		while (self.checkWall(cx, cy) or self.checkCoin(cx, cy) or self.checkPacman(cx, cy) or self.checkGhost(cx, cy)):
			cx = random.randrange(0, 5, 1)
			cy = random.randrange(30, 35, 1)

		return cx, cy

	def replace_dots(self):												# replace dots again after change in position of pacman and ghosts
		self.board[self.previous_px][self.previous_py] = "."
		for i in range(0, len(b_coords)):
			self.board[b_coords[i][0]][b_coords[i][1]] = "."

	def print_board(self):
		for i in range(0,15):
			print(" ".join( str(x) for x in self.board[i]))


class Pacman(Person):
	def __init__(self, x=1, y=1):
		self.x = x
		self.y = y

	def new_position(self, p):											# returns the position of pacman according to the input(w,a,s,d)
		if p == "a":
			self.y = self.y - 1

		elif p == "s":
			self.x = self.x + 1

		elif p == "d":
			self.y = self.y + 1

		elif p == "w":
			self.x = self.x - 1

		if self.checkWall(self.x, self.y):								# to check the presence of wall at next position 
			self.x = self.previous_px									# if true, it allocates previous position to next position, therefore pacman stays as it is
			self.y = self.previous_py

		return self.x, self.y
		

class Ghost(Person):
	def __init__(self, x=2, y=31):
		self.x = x
		self.y = y

	def ghostPosition(self):											# mentioned in assignment. Returns the position of Ghost
		self.x = random.randrange(0, 15, 1)
		self.y = random.randrange(0, 35, 1)

		while (self.checkWall(self.x, self.y) or self.checkCoin(self.x, self.y) or self.checkGhost(self.x, self.y)):
			self.x = random.randrange(0, 5, 1)
			self.y = random.randrange(30, 35, 1)

		return self.x, self.y

def checkGhost(px, py, b_coords):											# mentioned in assignment
	for i in range(0, len(b_coords)):	
		if (px == b_coords[i][0] and py == b_coords[i][1]):
			exit()

if __name__ == "__main__":
	a = Pacman()
	b = [Ghost(), Ghost(), Ghost()]											# objects of three ghosts. to increase/decrease number of ghosts create/delete Ghost() and initialize their values in next line
	b_coords = [[0,3], [0,15], [0,33]]										# initial coordinates of three ghosts
	a.board_design()
	a.update_board(1, 1, b_coords)											# b_coords are the coordinates of ghosts
	print "*******Rules*********"
	print "1. use W, A, S, D for movements"
	print "2. use Q to quit the game"
	print "********HAPPY HUNTING********\n\n"
	a.print_board()
	a.replace_dots()

	p = "n"
	while(True):
		print ("Score: " + str(a.score))
		p = raw_input("Enter direction: ")
		if p == "":
			p = "n"
		px, py = a.new_position(p[0])
		for i in range(0, len(b_coords)):
			b_coords[i] = b[i].ghostPosition()
		checkGhost(px, py, b_coords)
		a.update_board(px, py, b_coords)
		a.print_board()
		a.replace_dots()
		if p == "q" or p == "Q":
			exit()


