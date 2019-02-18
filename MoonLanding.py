#import
import random
import usa
import soviet

#variables
#numList = [1, 2, 3, 4]

print "-" * 50
print "Welcome to the game"
print "-" * 50

def greeting():
	while True:
		print "Select a country: USA or Soviet Union?"
		country = raw_input()
		if "usa" in country:
			print "You have selected the USA"
			print "The date is April 13th, 1961."
			usa.beginUSA()
		elif "soviet union" in country:
			print "You have selected the Soviet Union"
		        print "The date is April 12th, 1961"
			soviet.beginSoviet()
		else:
			print "Try again"
			continue
		return

greeting()

