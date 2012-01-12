#!/usr/bin/python

# CHATOME
# A conversation simulator
# Written by Hugh Rawlinson

import sys, os, time, csv

def out(input):
	print "|| " + input.upper() + " ||"

def save(lines):
	file = csv.writer(open('wordDatabase.csv', 'w'), delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	x = 0
	while x < len(lines):
		y = 0
		line = []
		while y <  len(lines[x]):
			line.append(lines[x][y])
			y = y + 1
		x = x + 1
		file.writerow(line)
	return 1

def touch(filename):
    os.close(os.open(filename, os.O_WRONLY | os.O_CREAT, int("666", 8)))
    os.utime(filename, None)

def load(filename = 'wordDatabase.csv'):
    if not os.access(filename, os.F_OK):
        touch(filename)
    with open(filename, 'rb') as ifh:
        return list(list(row) for row in csv.reader(ifh))

lines = list()
first = 0
last = list([])
history = list([])
brkvar = 0
brkvar2 = 0
out("system up")
out("welcome to chatome")
out("BE AWARE THAT 'reset', 'save', 'load' AND 'quit' ARE RESERVED KEYWORDS")

while (1):
	input = raw_input()
	input = input.lower()
	if (input == "reset"):
		os.system( [ 'clear', 'cls' ][ os.name == 'nt' ] )
		out("chatome has been reset")
		last = []
	
	elif (input == "quit"):
		print "|| DO YOU WANT TO SAVE? (Y or N) ||"
		input = raw_input()
		if (input == "Y") or (input == "y"):
			out("database is saving")
			time.sleep(1)
			if save(lines) == 1:
				out("database has been saved")
		out("goodbye")
		sys.exit(0)
	
	elif (input == "save"):
		if save(lines) == 1:
			out("database has been saved")
	
	elif (input == "load"):
		lines = load()
		out("database has been loaded")

	else:
			isInLines = 0
			isInHistory = 0
			brkvar1 = 0
			brkvar2 = 0
			x = 0
			for row in lines:
				if isInLines == 0:
					if input == lines[x][0]:
						isInLines = 1
					else:
						x = x + 1
			if isInLines != 1:
				templist = list([input])
				lines.append(templist)
				x = len(lines) - 1

			if len(lines[x]) > 1:
				out(lines[x][1])
				this = [x,1]
			else:
				out(lines[x][0])
				this = [x,0]
			history.append(last)
			
			if first != 0 and len(last) != 0:
				z = 0
				for row in lines:
					if brkvar1 == 0:
						if lines[last[0]][last[1]] == lines[z][0]:
							c = 1
							isInRow = 0
							for column in range(0,len(lines[z])-1):
								if brkvar2 == 0:
									if lines[last[0]][last[1]] == lines[z][c]:
										brkvar2 = 1
										isInRow = 1
									else:
										c = c + 1
							if isInRow != 1:
								lines[z].append(input)
							brkvar1 = 1
						else:
							z = z + 1
			last = this
			if first != 1:
				first = 1