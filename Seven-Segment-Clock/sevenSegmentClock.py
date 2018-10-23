#This is a python program to imitate a seven segment display clock.
#It displays current system time in seven segment format.
#The value from the dictionary corresponding to each digit to be displayed is passed to get_color() function.
#It determines the on/off state of a segment based on the values of corresponding bit from the value passed.
#The dictionary contains various 8-bit hexadecimal values that have states of the seven segments.
#Refer to https://en.wikipedia.org/wiki/Seven-segment_display to know more about virtual structure of seven segment display.

from p5 import *	#import everything from p5
from datetime import datetime	#import datetime function

#in this dictionary all values that are needed to display the digit is stored
#corresponding to numbers which are going to be dislpayed
nums = {0:0x7E,1:0x30,2:0x6D,3:0x79,4:0x33,5:0x5B,6:0x5F,7:0x70,8:0x7F,9:0x7B}

#setup function for p5
def setup():
	size(700, 200)	#creates a canvas of width 700 an height 200 in pixels
	title('Seven Segment Clock')

#function to determine the on/off state of a segment
def get_color(val,shift):
	a = 255*((val>>shift) & 1)
	return Color(255,0,0,a)

#this function draws the digit in seven segment font
def draw_digit(val):
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

#this functions draws blinking dots between hours, minutes and seconds
def draw_dots(s):
	fill(255,0,0,(s%2)*255)
	rect((20,45),10,10)
	rect((20,145),10,10)

#draw function of p5, which is called infinitly
def draw():
	background(0)
	h = datetime.now().hour		#gets system hour digit
	m = datetime.now().minute	#gets system minute digit
	s = datetime.now().second	#gets system second digit

	#this section determines positions of each digits and displays them accordingly
	with push_matrix():
		translate(0,0)
		draw_digit(nums[h//10])
	with push_matrix():
		translate(100,0)
		draw_digit(nums[h%10])
	with push_matrix():
		translate(200,0)
		draw_dots(s)
	with push_matrix():
		translate(250,0)
		draw_digit(nums[m//10])
	with push_matrix():
		translate(350,0)
		draw_digit(nums[m%10])
	with push_matrix():
		translate(450,0)
		draw_dots(s)
	with push_matrix():
		translate(500,0)
		draw_digit(nums[s//10])
	with push_matrix():
		translate(600,0)
		draw_digit(nums[s%10])

#calling the run function from p5 to start executing
run()
