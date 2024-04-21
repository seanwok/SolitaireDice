==========================================================
          __    ___   __    __ ______  ___  __ ____   ____
         (( \  // \\  ||    || | || | // \\ || || \\ ||   
          \\  ((   )) ||    ||   ||   ||=|| || ||_// ||== 
         \_))  \\_//  ||__| ||   ||   || || || || \\ ||___
                                     ____   __   ___  ____
                                     || \\  ||  //   ||   
                                     ||  )) || ((    ||== 
                                     ||_//  ||  \\__ ||___


==========================================================

What this is
==========================================================

This is a simple dice game for one or more players which 
runs in the terminal. Created for a class project.

This project was coded in Python 3.12.3.


==========================================================

How to Play
==========================================================

The game presents you with 5 dice. You pick two pairs of 
dice from them and leave one behind.

For each pair, a mark is added to the row on the score-
board corresponding with the sum of that pair. 

Any number of ■ in a row makes that row worth -200 points;
whether there is one or 6 ■, the row is worth -200.

Once you reach the ■»ø column, all ■ become ø, which are 
worth 0 points. 

After you reach ■»ø, you can accumulate £. Each £ is worth
the number of points in the bonus column on the board. 

There is a maximum number of £ you can earn in a row. 
After that, you may still collect that pair, but it will 
not add more points. 

Each time you select two pairs, you leave one throwaway 
die. This throwaway die is added to a meter; once that 
meter is full, your run is over and your final score is 
calculated.

You may only throw away three different throwaway dice. 
Once you have selected three different faces, you must 
plan your pairs so that one of those three is left.

If your roll contains no dice that can be thrown away, the
remaining die that round vanishes. This is called a Free
Ride.

In a standard game, ending with 500 or more points is 
considered a win. 


==========================================================

Valid inputs:
==========================================================

Pairs can be input in the following formats:
    x,y
    xy
    x.y
    x y

Other commands (available any time):
    exit
    help


==========================================================

Credits:
==========================================================

Original game designed by Sid Sackson and described in his
book: A Gamut of Games.
   https://sacksonportal.museumofplay.org
   https://www.ludism.org/scwiki/SolitaireDiceRules


Title ASCII word art genrated by Text to ASCII Art
Generator by Patrick Gillespie.
   Font: Double from FIGlet
   http://patorjk.com/software/taag/
   http://www.figlet.org/


Game coded in 2024 by Sean O'Kelley for CS50P as part of
the Open Source Society University curriculum.
   https://cs50.harvard.edu/python/2022/
   https://github.com/ossu/

Many thanks to the OSSU discord.