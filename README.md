# Rock-Paper-Scissors
The classic game of Rock,Paper,Scissors in Python

Line 1-2 : This section imports the extra Python
functions we’ll need for the code – they’re
still parts of the standard Python libraries, just
not part of the default environment.

Line 4-12 : The initial rules of the game are created
here. The three variables we’re using and
their relationship is defined. We also provide a
variable so we can keep score of the games.

start() : We begin the game code by defining the
start of each round. The end of each play
session comes back through here, whether we
want to play again or not.

game() : The game is actually contained all in
here, asking for the player input, getting
the computer input and passing these on to get
the results. At the end of that, it then asks if you’d
like to play again.

move() : Player input is done here. We give the
player information on how to play this
particular version of the game and then allow
their choice to be used in the next step. We also
have something in place in case they enter an
invalid option.

result() : There are a few things going on when we
show the results. First, we’re putting in a
delay to add some tension, appending a variable
to some printed text, and then comparing what
the player and computer did. Through an if
statement, we choose what outcome to print,
and how to update the scores.

scores() : We now ask for text input on whether
or not someone wants to play again.
Depending on their response, we go back to the
start, or end the game and display the results.








