#!/usr/local/bin/python

import re

def count_rounds():
    global current_round
    current_round = 1
    with open('result.txt', 'r') as input:
        input_str = input.readline().strip()
        while input_str:
            while not(input_str.startswith('end')):
                input_str = input.readline().strip()
            input_str = input.readline().strip()
            input_str = input.readline().strip()
            current_round += 1

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

def read_previous_rounds():
    global last_bidders
    global last_last_bidders
    last_bidders = []
    last_last_bidders = []
    with open('result.txt', 'r') as input:
        if current_round == 2:
            input_str = input.readline().strip()
            input_str = input.readline().strip()
            while not(input_str.startswith('end')):
                if not(input_str == '-'):
                    input_list = input_str.split(', ')
                    if input_list[1] == '-':
                        last_bidders.append(Bidder(input_list[0], 0))
                    else:
                        last_bidders.append(Bidder(input_list[0], float(input_list[1])))
                    input_str = input.readline().strip()
        else:
            counter = 1
            input_str = input.readline().strip()
            while input_str and (counter != (current_round - 2)):
                while not(input_str.startswith('end')):
                    input_str = input.readline().strip()
                input_str = input.readline().strip()
                input_str = input.readline().strip()
                counter += 1
            input_str = input.readline().strip()
            while not(input_str.startswith('end')):
                if not(input_str == '-'):
                    input_list = input_str.split(', ')
                    if input_list[1] == '-':
                        last_last_bidders.append(Bidder(input_list[0], 0))
                    else:
                        last_last_bidders.append(Bidder(input_list[0], float(input_list[1])))
                input_str = input.readline().strip()
            input_str = input.readline().strip()
            input_str = input.readline().strip()
            input_str = input.readline().strip()
            while not(input_str.startswith('end')):
                if not(input_str == '-'):
                    input_list = input_str.split(', ')
                    if input_list[1] == '-':
                        last_bidders.append(Bidder(input_list[0], 0))
                    else:
                        last_bidders.append(Bidder(input_list[0], float(input_list[1])))
                input_str = input.readline().strip()

def main():
    initialize()

if __name__ == '__main__':
    main()
