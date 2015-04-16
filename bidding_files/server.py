import os
import sys
import time
import re
import random
import signal
from random import choice
import subprocess
from subprocess import Popen
import fcntl
import operator

# Reading setup file
setupfile = open("setup.txt", "r")
players = int(setupfile.readline().strip())                             # Number of bidders - autodetect
randbidder = False if int(setupfile.readline().strip()) == 0 else True  # Is there a random bidder? 
auctions = int(setupfile.readline().strip())                            # Number of auctions
announceall = False if int(setupfile.readline().strip()) == 0 else True # Announce all bids?

bid_element = setupfile.readline().strip()                              # Fixed bidding price set?
if bid_element == "[0,1]":  # Continuous interval
        bid_option = 0
elif bid_element == "{0,1/100000,...,99999/100000,1}":
        bid_option = 1
        bid_options = []
        oc = 0          # Option Count
        while oc < 100001:
                bid_options.append(float(float(oc)/100000))
                oc += 1
else:
        bid_option = 1      # Discrete options
        bid_options = []     
        oc = 1          # Option Count
        num = ''
        while oc < len(bid_element):
                if bid_element[oc] == ',' or bid_element[oc] == '}':
                        bid_options.append(float(num))
                        #print num
                        num = ''
                else:
                        num += bid_element[oc]
                oc += 1
setupfile.close()

# Creating log file and result file
logfile = open("log.txt", "w")
resfile = open("result.txt", "w")
resfile.close
bidders = []
scores = {}

# Initializing bidders
if randbidder:
        bidders.append("00")
        scores["00"] = 0
        

for file in sys.argv[2:]:
        bidders.append(file)
        scores[file] = 0
        
print str(len(bidders)) + " bidders joined."

# Initializing variables
lastroundbids = {}
sorted_bids = {}
rc = 0  # Round Count
random.seed()
if auctions == 0:
	auctions = 100000000
	if sys.argv[1] > 0:
		auctions = int(sys.argv[1])
print "Running " + str(auctions) + " rounds..."

# Bidding loop
while rc < auctions:
	for bidder in bidders:
                print "Reading " + bidder + "'s bid"
                p = Popen("./"+bidder, stdout=subprocess.PIPE)
                fcntl.fcntl(p.stdout.fileno(), fcntl.F_SETFL, os.O_NONBLOCK)
                # Timeout for each bidder, if no bid is captured, terminate the bidder
                tc = 0  # Timeout Count
                while tc < 20:
                        time.sleep(0.5)
                        os.kill(p.pid,signal.SIGSTOP)
                        try:
                                out = p.stdout.read()
                                if len(out) > 0:
                                        lastroundbids[bidder] = float(out)
                                        break
                        except:
                                tc += 1
                                os.kill(p.pid,signal.SIGCONT)
                                if tc == 20:
                                        p.terminate()
                                        print "Timeout: " + bidder + " is terminated"
                                        lastroundbids[bidder] = -100
                        p.stdout.close
                # Checking whether the bid is legal if in the Discrete mode
                if bid_option == 1:     
                        legal = False
                        for option in bid_options:
                                if lastroundbids[bidder] == option:
                                        legal = True
                                        break
                        if legal == False:
				if not lastroundbids[bidder] == -100:
                                	print bidder + "'s bidding price is illegal"
                                	lastroundbids[bidder] = -1
                # Checking whether legal in Continuous mode
		else:
                        # the program may be stucking at the next line due to the number comparisons
                        # TODO: format the number in some ways before the comparison 
			if lastroundbids[bidder] < 0 or lastroundbids[bidder] > 1:
				if not lastroundbids[bidder] == -100:
					print bidder + "'s bidding price is illegal"
					lastroundbids[bidder] = -1

        print "Reading finished"
        rc += 1
        # Getting the winning bid            
        winner = max(lastroundbids.values())
        # Sorting the bids in descending order
        sorted_bids = sorted(lastroundbids.iteritems(), key = operator.itemgetter(1), reverse = True)
        if not winner < 0:
                winner_count = 0
                for uid, bid in sorted_bids:
                        if bid == winner:
                                winner_count += 1
               # print winner_count
                expected_payoff = (1 - winner)/winner_count
               # print expected_payoff
                # Updating the winners' scores
                for uid, bid in sorted_bids:
                        if bid == winner:
                                scores[uid] += expected_payoff                       

        # Writing logs, results and scores
        resfile = open("result.txt", "a")
        resfile.write("round " + str(rc) + "\n")
        logfile.write("round " + str(rc) + "\n")
        for uid, bid in sorted_bids:
                if bid == -1:
                        scores[uid] -= 1
                if bid == -100:
                        bid = "-"
                logfile.write(uid + ", " + str(bid) + "\n")
                if announceall:
                        resfile.write(uid + ", " + str(bid) + "\n")
                elif not winner < 0:
                        if bid == winner:
                                resfile.write(uid + ", " + str(bid) + "\n")
                        
        lastroundbids = {}
        sorted_bids = {}
        #time.sleep(1)
        resfile.write("end of round " + str(rc) + "\n\n")
        logfile.write("end of round " + str(rc) + "\n\n")
        with open("scores.txt", "w") as scorefile:
                for uid, value in scores.iteritems():
                        scorefile.write(uid + " -> " + str(value) + "\n")
        resfile.close
        resfile = open("result.txt", "r")
        resfile.close

logfile.close
