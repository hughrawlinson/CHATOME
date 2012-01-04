#!/usr/local/bin/python

# CHATOME
# A conversation simulator
# Written by Hugh Rawlinson

import sys, os, time, csv

lines = list()
print "|| SYSTEM UP ||"
print "|| WELCOME TO CHATOME ||"
print "|| BE AWARE THAT 'reset', 'save', 'load' AND 'quit' ARE RESERVED KEYWORDS ||"

def theLoop(input,lines):
	x = 0
	while x <= len(lines) :
		if input != lines[x][0]:
		 	x = x + 1
		else:
			if lines[x][1] != 0:
				lines[x][1] = input
				print lines[x][1]
			else:
				lines[x][0] = input
				print lines[x][0]
		return lines

def save(lines):
	file = csv.writer(open('wordDatabase.csv', 'rb'))
	x = 0
	for x in lines:
		y = 0
		line = []
		for y in lines[x]:
			line.append(lines[x][y])
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

while (1):
	input = raw_input()
	if (input == "reset"):
		os.system( [ 'clear', 'cls' ][ os.name == 'nt' ] )
		print "|| CHATTOME HAS BEEN RESET ||"
	
	elif (input == "quit"):
		print "|| DO YOU WANT TO SAVE? (Y or N) ||"
		input = raw_input()
		if (input == "Y") or (input == "y"):
			save(lines)
			print "|| DATABASE IS SAVING ||"
			time.sleep(1)
			print "|| DATABASE HAS BEEN SAVED ||"
		print "|| GOODBYE ||"
		sys.exit(0)
	
	elif (input == "save"):
		if save(lines) == 1:
			print "|| DATABASE HAS BEEN SAVED ||"
	
	elif (input == "load"):
		lines = load()
		print "|| DATABASE HAS LOADED ||"

	else:
		if (lines > 0):
			lines = theLoop(input,lines)
		
		else:
			lines[0] = [input]
			time.sleep(1)
			print "|| " + lines[0][0].capitalize() + " ||"