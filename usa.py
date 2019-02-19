import time

def beginUSA():
	print "You're name is James Webb, Chief Administrator of NASA"
	time.sleep(4)
	print "You have just recieved word that the Soviets have sucessfully sent a man into orbit"
	time.sleep(4)
	print "You are set to launch the Freedom 7 in a month, but it has already been delayed several times"
	time.sleep(4)
	print "You don't want to be humiliated by the Soviets any more."
	time.sleep(4)
	print "Do you 1. Move up the launch date of Freedom 7 to keep up with the Soviets?"
	time.sleep(4)
	print "Or 2. Keep the scheduled launch date. (1/2)"

	while True:
		firstChoice = raw_input()
		if "1" in firstChoice:
			print "The most you can move the date up is to is April 30th, 5 days before what was scheduled."
			time.sleep(4);
			earlyDate();
		elif "2" in firstChoice:
			print "It would be too dangerous to move the date up sooner"
			time.sleep(4);
			normalDate();
		else:
        	       	print "Type either 1 or 2"
  	        	continue
	return


def earlyDate():
	print "It is strongly suggested that you do not do this as you could put the mission in danger."
	time.sleep(4)
	print "Would you still like to continue? (yes/no)"
	
	while True: 
		sureDecision = raw_input()
		if "yes" in sureDecision:
			print "OK. You're the boss. April 30th it is."
		elif "no" in sureDecision:
			print "I think that was the right decision"
		else:
			print "Type yes or no"
			


def normalDate():
	print "There is still a lot to be done before the launch date."
	print "Everything will proceed as planned"
