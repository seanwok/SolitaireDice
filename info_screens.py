# Errors

format_error = (
    "==========================================================\n"
    "Format Error: Please input a dice pair (not its sum) as \n"
    "'x,y', 'x y' 'xy' 'x.y'\n"
    "\n"
    "Example:\n"
    "    First pair: 1,5\n"
    "    First pair: 1 5\n"
    "    First pair: 1.5\n"
    "\n"
    "Press Enter to reselect pairs: "
)

die_error = (
    "==========================================================\n"
    "Selection not available: Please select a pair from the \n"
    "available dice. A die may not be picked more than once.\n"
    "\n"
    "Press Enter to reselect pairs: "
)

throwaway_error = (
    "==========================================================\n"
    "Invalid throwaway die: You may not select all valid throw-\n"
    "away dice; one must remain.\n"
    "\n"
    "Valid throwaway dice are marked with a T.\n"
    "\n"
    "Press Enter to reselect pairs: "
)

reject_error = (
    "==========================================================\n"
    "The world forgets.\n"
    "\n"
    "Press Enter to reselect pairs: "
)

tutorial_error = (
    "==========================================================\n"
    "For tutorial purposes, please choose the requested pair.\n"
    "\n"
    "Press Enter to reselect pairs: "
)

# Credits, help, title and win/lose screens
# All screens should be 31 lines tall and 58 characters wide

credits = (
    "\n\n\n\n\n\n\n\n"
    "==========================================================\n"
    "\n"
    "C R E D I T S\n"
    "==========================================================\n"
    "\n"
    "\n"
    "Original game designed by Sid Sackson and described in his\n"
    "book: A Gamut of Games.\n"
    "   https://sacksonportal.museumofplay.org\n"
    "   https://www.ludism.org/scwiki/SolitaireDiceRules\n"
    "\n"
    "\n"
    "Title ASCII word art genrated by Text to ASCII Art \n"
    "Generator by Patrick Gillespie. \n"
    "   Font: Double from FIGlet\n"
    "   http://patorjk.com/software/taag/\n"
    "   http://www.figlet.org/\n"
    "\n"
    "\n"
    "Game coded in 2024 by Sean O'Kelley for CS50P as part of \n"
    "the Open Source Society University curriculum.\n"
    "   https://cs50.harvard.edu/python/2022/\n"
    "   https://github.com/ossu/\n"
    "\n"
    "\n"
    "Many thanks to the OSSU discord.\n"
    "\n"
    "\n"
    "\n"
    "\n"
)

game_help = (
    "==========================================================\n"
    "Accepted pair selection inputs: 'x,y' 'x x' 'x.y' 'xy'\n"
    "Input 'exit' to exit\n"
    "Game rules can be found in the tutorial or readme.txt\n"
    "=========================================================="
    
)

main_menu = (
    "\n\n\n\n\n\n\n\n"
    "==========================================================\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "          __    ___   __    __ ______  ___  __ ____   ____\n"
    "         (( \\  // \\\\  ||    || | || | // \\\\ || || \\\\ ||   \n"
    "          \\\\  ((   )) ||    ||   ||   ||=|| || ||_// ||== \n"
    "         \\_))  \\\\_//  ||__| ||   ||   || || || || \\\\ ||___\n"
    "                                     ____   __   ___  ____\n"
    "                                     || \\\\  ||  //   ||   \n"
    "                                     ||  )) || ((    ||== \n"
    "                                     ||_//  ||  \\\\__ ||___\n"
    "\n"
    "\n"
    "==========================================================\n"
    "\n"
    "Original game by Sid Sakson. Coded for OSSU.\n"
    "\n"
    "Accepted input:\n"
    "   new game\n"
    "   tutorial\n"
    "   credits\n"
    "   help (available any time)\n"
    "   exit (available any time)\n" 
    "\n"
    "Please ensure the terminal window is tall and wide enough \n"
    "to see both the input cursor and the bar above the title.\n"
    "\n"
    "\n"
    
)

new_game = (
    "\n\n\n\n\n\n\n\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "==========================================================\n"
    "\n"
    "\n"
    "N E W   G A M E\n"
    "==========================================================\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
)

rule_adjust_top = (
    "\n\n\n\n\n\n\n\n"
    "==========================================================\n"
    "\n"
    "G A M E   S E T U P\n"
    "==========================================================\n"
    "\n"
    "\n"   
    "Rule                  Current  Minimum  Maximum  Default\n"
)

rule_adjust_bottom = (
    "\n"
    "\n"
    "To change a game rule, input the rule (exactly), then\n"
    "follow the prompt. \n"
    "\n"
    "Values must be within minimum and maximum values. \n"
    "\n"
    "\n"
    "Enter 'done' to start the game.\n"
    "Enter 'default' to return all rules to default.\n"
    "\n"
    "\n"
    "Adjust values with purpose. It is entirely possible to \n"
    "create a game that cannot be won or even enjoyed.\n"
    "\n"
    "Changing values could necessitate a wider terminal.\n"
    "\n"
    "\n"
    "\n"
  
)

game_setup = (
    "\n\n\n\n\n\n\n\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "==========================================================\n"
    "\n"
    "G A M E   S E T U P\n"
    "==========================================================\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
)

end_game = (
    "\n\n\n\n\n\n\n\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "==========================================================\n"
    "\n"
    "G A M E   C O M P L E T E\n"
    "==========================================================\n"
    "\n"
    "\n"
)


rule_hint = {
    "max_throwaway_marks": "\nThe number of times you can throw away a die before ending the game.\n",
    "max_throwaway_dice": "\nThe maximum number of throwaway meters.\n",
    "max_point_marks": "\nThe maximum number of times a £ can be earned for a pair.\n",
    "zero_threshold": "\nThe point at which ■ becomes ø.\n",
    "point_factor": (
        "\nMultiplied by the bonus to determine how much £ are worth.\n"
        "Numbers lower than 10 reduce the bonus.\n"
    ),
    "penalty": "\nNumber of points deducted for ■.\n",
    "win_score": "\nPoints needed to win.\n" 
}
