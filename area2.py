#! /usr/bin/python
#-*-coding: utf-8 -*-
# area2.py
# calculates the area of a given rectangle, square or circle.
# Z0MBiE 2014

def options():
	print ("Options:")
	print ("'C' to find the area of a circle")
	print ("'S' to find the area of a square")
	print ("'R' to find the area of a rectangle")
	print ("'Q' to Quit")
	print()

def area_rectangle(width, height):
	return width * height

def area_square(L):
	return L * L

def area_circle(radius):
	return 3.14 * radius ** 2

print()
print ("This program will calculate the area of a [S]quare, [C]ircle or [R]ectangle.")
print ()
choice = "x"
options()
while choice != "q":
	choice = input("Please enter your choice: ")
	if choice == 's':
		L = float(input("Length of squares side: "))
		print ("The area of the square is:", area_square(L))
		print()
		options()
	elif choice == 'r':
		width = float(input("Please enter the width of the rectangle: "))
		height = float(input("Please enter the height of the rectangle: "))
		print ("The area of the rectangle is:", area_rectangle(width, height))
		print()
		options()
	elif choice == 'c':
		radius = float(input("Please enter the radius of the circle: "))
		print ("The area of the circle is:", area_circle(radius))
		print()
		options()
	elif choice == 'q':
		print (" ",end="")
	else:
		print ("Unrecognised option.")
		print()
		options()