This program works as the “server” or auctioneer for the auction game. 

To start the auction game, please follow the steps below:

1. Put all necessary files in the same directory, including the server.py,
setup.txt, and all bidder programs to join.

2. Start the game using command “python server.py #N #ID1 #ID2 …”, where #N is
the number of rounds, followed by IDs of the target bidders.

3. Wait until the program exits.

Three Output files:

“log.txt” - This shows everything happened during the bidding process.

“result.txt” - This includes the winner’s and probably the others’ bidding
information for every round. All bidder programs are allowed to read this file
to react correspondingly during the game.

“scores.txt” - This shows the final scores for each bidder.

Some examples: 

“python server.py 100 10032976 09632866” - start a game for 2 bidders(if no
random bidder indicated in the setup.txt): a bidder with ID “10032976” and a
bidder with ID “09632866”, for 100 rounds.

“python server.py 100 99 075” - you may want to try this command when the
bidding option is {0.3,0.6}.

“python server.py 0 tft” - when the number of rounds is already specified in the
setup, also with the presence of a random bidder, so no need to include 00 in
this command.

Note: On lab2 machines, the default version of python for command “python” does
not support the server, and it’s required to use python2.6 or above. To do so,
please first type “whereis python”, which shows all the installed version on
that computer, and then copy the path for 2.6 or above and replace the word
“python” with it to indicate which version you want to use.


Bidder programs given (you can use these to play against your own program for
testing):

```
00 - random bidder
99 - timeout bidder
05 - always bids 0.5
075 - always bids 0.75
tft - tit-for-tat
```
