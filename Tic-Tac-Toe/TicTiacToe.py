from p5 import *

board = 9*[None]
turn = 1
paused = False

def draw_p1(x,y):
	push_matrix()
	translate((x+0.5)*200,(y+0.5)*200)
	rect_mode('CENTER')
	rotate(PI/4)
	fill(255)
	rect((0,0),100, 10)
	rotate(PI/2)
	rect((0,0),100, 10)
	reset_matrix()
	rect_mode('CORNER')

def draw_p2(x,y):
	push_matrix()
	translate((x+0.5)*200,(y+0.5)*200)
	fill(255)
	circle((0,0),100)
	fill(0)
	circle((0,0),80)
	reset_matrix()

def draw_blank(x,y):
	push_matrix()
	translate((x+0.5)*200,(y+0.5)*200)
	rect_mode('CENTER')
	fill(0)
	rect((0,0),150,150)
	reset_matrix()
	rect_mode('CORNER')

def draw_board():
	global board
	for i in range(3):
		for j in range(3):
			fill(0)
			rect((i*200+2,j*200+2),196,196)
	for i in range(3):
		for j in range(3):
			index = j*3 + i
			if board[index] == 'X':
				draw_p1(i,j)
			elif board[index] == 'O':
				draw_p2(i,j)
			else:
				draw_blank(i,j)

def check_winner():
	global board
	for i in range(3):
		if board[i] == board[i+3] == board[i+6] == 'X':
			return 1
		elif board[i] == board[i+3] == board[i+6] == 'O':
			return 2
	for i in [0,3,6]:
		if board[i] == board[i+1] == board[i+2] == 'X':
			return 1
		elif board[i] == board[i+1] == board[i+2] == 'O':
			return 2
	if board[0] == board[4] == board[8] == 'X':
		return 1
	elif board[0] == board[4] == board[0] == 'O':
		return 2
	if board[2] == board[4] == board[6] == 'X':
		return 1
	elif board[2] == board[4] == board[6] == 'O':
		return 2
	return 0

def mouse_pressed():
	global board, turn, paused
	if paused:
		turn = 1
		for i in range(9):
			board[i] = None
		paused = False
	else:
		i = mouse_x//200
		j = mouse_y//200
		index = j*3 + i
		if board[index] == None:
			if turn == 1:
				board[index] = 'X'
			elif turn == -1:
				board[index] = 'O'
			turn *= -1
		if check_winner() == 1:
			with push_style():
				fill(0)
				text('Player 1 wins',(10, height-39))
			paused = True
		elif check_winner() == 2:
			with push_style():
				fill(0)
				text('Player 2 wins',(10, height-39))
			paused = True
		elif None not in board:
			with push_style():
				fill(0)
				text('Game Draw',(10, height-39))
			paused = True

def setup():
	size(600,640)
	title('TicTacToe')
	rect_mode('CORNER')
	ellipse_mode('CENTER')
	no_stroke()
	background(255)
	font = create_font('calibri.ttf',38)
	text_font(font)

def draw():
	global turn
	if not paused:
		background(255)
	draw_board()
	with push_style():
		fill(0)
		if turn == 1 and paused == False:
			text('Player 1 Turn',(width-210,height-39))
		elif turn == -1 and paused == False:
			text('Player 2 Turn',(width-210,height-39))

run()