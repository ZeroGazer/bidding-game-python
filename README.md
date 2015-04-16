COMP3211 Project
================

HKUST COMP3211 Fundamentals of Artificial Intelligence (2015 Spring) Project

In this project, you are going to design a program to compete in a series of
auctions.

General setting

1. Each auction is a single item best price auction.

2. If your program wins the auction, it'll be rewarded with 1-b points, where b
is its bid. If it lose, then it gets 0 point.

3. Your program's score will be the sum of all auctions that it participated in.

4. You will be told at the beginning:

  a) whether the auctions will be held for exactly K times, for a given K, or
     for an unknown number of times;
     
  b) whether there is a bidder RANDOM who will bid randomly;
  
  c) whether the number of bidders is known;
  
  d) whether all bidders and their bids will be announced after each auction
     or just the winner and the winning bid would be announced;

  e) the set of allowable bids;

5. Your program has up to 10 seconds to send in its bid.

Specifically, you can assume that the current directory has the following files,
which you can access at runtime:

setup.txt: 

line 1: a number denoting the number of bidders. 0 means unknown.

line 2: 1 or 0. 1 means there is a random bidder;

line 3: a number denoting the number of auctions. 0 means unlimited;

line 4: 1 or 0. 1 means that all bids are announced, and 0 means only the winner
and its bid is announced;

line 5: either [0,1], meaning all numbers between 0 and 1 are allowed, or
{a,b,c,...,d}, meaning that only elements in the sets are allowed as bids;

result.txt:

initially empty, after each round, it will be appended with the following
information:

```
round $X
$ID1, $Bid1
$ID2, $Bid2
...
end of round $X
```

where $X is a number, $IDk is bidder k's ID, and $Bidk its bid.

The first bidder, $ID1, is the winner of the round.

The ID for RANDOM will be 00. We will use your student number as the ID of your
program. If a bidder sends in an illegal bid, like bids 0 when the set of
allowable bids is {0.3,0.6}, then its bid will be recorded as "-1". If a program
does not send in any bid, then its bid will be recorded as "-". If all bidders
in a round either sent in illegal bids or did not send in any bid, then there
will be no winner in the round, and this will be indicated by "-" on the first
line. For example, the following entries:

```
round 2
01, 0.3
02, 0.2
03, -
04, -1
end of round 2

round 3
-
01, -
02, -
03, -
04, -1
end of round 3
```

mean that at round #2, bidder 01 was the winner with the winning bid 0.3, bidder
02 bid 0.2, bidder 03 did not sent in any bid, and bidder 04 sent in an illegal
bid. However, at round #3, there is no winner as the only bid received was from
bidder 04, but the bid was illegal.

On each run, your program needs to return with your bid by writing to standard
output (e.g. "cout << " in C++). It needs to do so in 10 seconds, otherwise, it
will be aborted. 

In addition to the above two files, your program can create and access your own
files. For example, you may want to have a file to record historic bids by other
programs. To avoid conflicts, name these files as: my_file1_ID, my_file2_ID,
etc., where ID is your student number. However, your program is not allowed to
alter other people's files. Furthermore, your program will not have access to
files in other directories and have no access to internet.
