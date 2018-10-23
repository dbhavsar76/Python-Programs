from p5 import *

dictionary = {
	'0':0x7e, '1':0x30, '2':0x6d, '3':0x79, '4':0x33,
	'5':0x5b, '6':0x5f, '7':0x70, '8':0x7f, '9':0x7b,
	'a':0x77, 'b':0x1f, 'c':0x4e, 'd':0x3d, 'e':0x4f,
	'f':0x47, 'h':0x37, 'j':0x38, 'l':0x0e, 'n':0x15,
	'p':0x67, 'r':0x05, 's':0x5b, 't':0x0f, 'u':0x3e,
	'y':0x3b, ' ':0x00
}
forbidden = ['g','i','k','m','o','q','v','w','x','z']
text = ' '

class Seven_segment_text:
	def __init__(self, text):
		self.text = text
		self.x = 0
		self.y = 0

	def __call__(self, text):
		self.text = text
		self.x = 0
		self.y = 0
		return self

	def display(self):
		global dictionary
		for i in range(len(self.text)):
			val = dictionary[self.text[i]]
			if self.x > 2550:
				self.x = 0
				self.y += 200
			with push_matrix():
				scale(0.5)
				translate(self.x,self.y)
				no_stroke()
				fill(get_color(val,6))
				rect((20,25),60,10)
				fill(get_color(val,5))
				rect((80,35),10,60)
				fill(get_color(val,4))
				rect((80,105),10,60)
				fill(get_color(val,3))
				rect((20,165),60,10)
				fill(get_color(val,2))
				rect((10,105),10,60)
				fill(get_color(val,1))
				rect((10,35),10,60)
				fill(get_color(val,0))
				rect((20,95),60,10)
			self.x += 100
		self.x = 0
		self.y = 0

def get_input():
	string = input('Enter text : ')
	return str(string).lower()

def check_string(string):
	global forbidden
	for char in string:
		for char2 in forbidden:
			if char == char2:
				return False
	else:
		return True

def get_color(val,shift):
	a = 255*((val>>shift) & 1)
	return Color(255,0,0,a)

o = Seven_segment_text(text)

def setup():
	global text, o
	size(1300,600)
	title("seven segment text")
	rect_mode('CORNER')
	background(0)
	no_loop()
	print('Enter text to display it in seven segment display format.')
	print('Click anywhere on the canvas to enter text in console.')
	print('Following charecters are not supported: g, i, k, m, o, q, v, w, x, z')

def mouse_pressed():
	global o
	text = get_input()
	if check_string(text):	
		o.text = text
	else:
		o.text = 'error'
	redraw()

def draw():
	global o
	background(0)
	o.display()


run(frame_rate = 2)
