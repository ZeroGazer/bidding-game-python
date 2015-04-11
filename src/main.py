#!/usr/local/bin/python

import re

def count_rounds():
    global current_round
    current_round = 1
    with open('result.txt', 'r') as input:
        if not input.readline().strip():
            return current_round
        else:
            while True:
                for i in range(6):
                    temp = input.readline()
                current_round += 1
                if not temp.strip():
                    return current_round

def initialize():
    global bidders_num
    global has_random_bidder
    global rounds
    global all_bids_are_announced
    global are_discrete_bids
    global bids
    with open('setup.txt', 'r') as input:
        bidders_num = input.readline().strip()
        has_random_bidder = (input.readline().strip() == '1')
        rounds = input.readline().strip()
        all_bids_are_announced = (input.readline().strip() == '1')
        bids_string = input.readline().strip()
        are_discrete_bids = bool(re.compile('^\{.+\}$').match(bids_string))
    bids = bids_string[1:len(bids_string)-1].split(',')
    for i in range(len(bids)):
        if re.compile('^\d+\/\d+$').match(bids[i]):
            bids[i] = float(bids[i].split('/')[0]) / float(bids[i].split('/')[1])
        bids[i] = float(bids[i])
    bids.sort()
       
def main():
    initialize()

if __name__ == '__main__':
    main()
