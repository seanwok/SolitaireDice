# Structure:
# # Not all keys/values need be present.
# tutorial = {
#     [round_count]: {
#         "hand": [i,i,i,i,i],
#         # every round has two picks       
#         [pick]: {
#             "selection": [i,i],
#             [location]: ["tutorial message"]
#         }
#     }
# }

tutorial = {
    # round
    0: {       
        # pick
        0: {
            #location
            0: (
                "\n\n\n\n\n\n\n\n\n\n\n\n\n"
                "==========================================================\n"
                "\n"
                "Welcome to Solitaire Dice!\n"
                "==========================================================\n"
                "\n"
                "Tutorial 'screens' are taller than normal game screens. \n"
                "You may have to scroll up or make your terminal taller.\n"
                "\n"
                "The object of this game is to score as many points as\n" 
                "possible. 500 points is considered a win.\n"
                "\n"
                "To collect points select pairs from a hand of five dice.\n"
                "\n"
                "Let's get started!\n"
                "\n\n"
                "Press Enter.\n"
                "==========================================================\n"
            ),
            1: (
                "\n"
                "First let's take a look at an example scorecard. This \n"
                "header contains general info about you. Well, about Sid, \n"
                "who is quite far in his run.\n"
                "\n\n"
                "Press Enter.\n"
                "==========================================================\n"
            ),
            2: (
                "\n"
                "This table tracks your marks and score.\n"
                "\n"
                "Notice that there is a row for each possible sum of two\n" 
                "dice. These sums are your scoring pairs.\n"
                "\n"
                "Each row might have three kinds of marks: ■, ø and £.\n"
                "These marks determine the score for that pair.\n"
                "\n"
                "At the end of each row, you will find the bonus and the\n"
                "current score for that row. Scoring will be covered soon.\n"
                "\n\n"
                "Press Enter.\n"
                "==========================================================\n"
            ),
            3: (
                "\n"
                "These meters indicate your throwaway dice. Every turn you\n"
                "will select two pairs from five dice.\n"
                "\n"
                "The remaining die, your throwaway die, will go here.\n"
                "\n"
                "When any meter is full your run will end.\n"
                "\n\n"
                "Press Enter.\n"
                "==========================================================\n"
            ),
            4: (
                "And finally, the stars of the show: the dice!\n"
                "\n"
                "Every round five dice will be rolled and you can select\n"
                "two pairs from those dice.\n" 
                "\n"
                "These pairs are added and your scoreboard is marked in\n"
                "the row matching the sum of your pair.\n"
                "\n\n"
                "Press Enter.\n"
                "==========================================================\n"
            ),
        },
    },
    1: {
        "hand": [1,2,3,5,6],       
        0: {
            "selection": [1,6],
            0: (
                "\n"
                "Let's try a few rounds. To move along the tutorial, I'll\n"
                "let you know which dice to pick.\n"
                "\n\n"
                "Press Enter.\n"
                "==========================================================\n"
            ),
            4: (
                "You've been rolled your first hand!\n"
                "\n"
                "Your goal is to collect scoring pairs so you can start\n"
                "gathering points. Each turn five dice are rolled. You can\n" 
                "pick two pairs from those dice.\n"
                "\n"
                "Many combinations of dice add up to 7--including two pairs\n" 
                "of available dice. Start by focusing there.\n"
                "\n\n"
                "Press Enter then choose dice 1 and 6 by typing 1,6"
            ),
        },
        1: {
            "selection": [2,5],
            4: (
                "\n\n"
                "Great job! Notice that your selection has been marked in\n"
                "the dice area. You can't pick these dice again this round.\n"
                "\n"
                "2 and 5 also make 7, so it makes sense to choose them."
                "\n"
                "You don't have to use the format 2,5 to input dice.\n"
                "These also work:\n"
                "    2.5\n"
                "    2 5\n"
                "    25\n"
                "\n\n"
                "Press Enter then choose dice 2 and 5."
            )
        },
        "c": {
            4: (
                "\n\n"
                "Since you picked two pairs that add up to 7, two ■ have\n"
                "been marked in the 7 column.\n"
                "\n"
                "But oh no! Your score has somehow gone down?\n"
                "\n"
                "The ■ are debt marks. Having any number of them in a row\n"
                "makes the entire row worth -200 points. Press Enter."
            )
        }
    },
    2: {
        "hand": [1,1,3,4,4],       
        0: {
            "selection": [3,4],
            4: (
                "With a new round you get a new hand. Luckily, you can \n"
                "collect another pair of 7.\n"
                "\n\n"
                "Press Enter then choose dice 3 and 4 by typing 3,4"
            ),
        },
        1: {
            "selection": [1,1],
            4: (
                "\n\n"
                "You unfortunately have run out of pairs that make 7 so \n"
                "you'll have to choose something else.\n"
                "\n"
                "Another attractive option is 1,1. That pair has a very \n"
                "large bonus (found on the right of the scoring board).\n"
                "\n\n"
                "Press Enter then choose dice 1 and 1 by typing 1,1"
            )
        },
        "c": {
            4: (
                "\n\n"
                "It looks like you've picked up another two ■, one in the 7\n"
                "row and one in the 2 row. Since any number of ■ in a row \n"
                "equals -200, both rows total the same.\n"
                "\n\n"
                "The Total score is the sum of the row scores. Press Enter."
            )
        }
    },
    3: {
        "hand": [2,3,5,5,6],       
        0: {
            "selection": [2,5],
            3: (
                "You maybe noticed these meters that appeared after the \n"
                "last two turns. When you select two pairs, one die must \n"
                "remain. (Almost) every turn, that last die is counted in \n"
                "these meters.\n"
                "\n"
                "On the first turn, you threw away a 3, and last turn, you \n"
                "threw away a 4. Now you have two meters for those dice \n"
                "and each of those meters has one used mark and seven \n"
                "available marks. Press Enter.\n"
            ),
            4: (
                "Graciously, you have another 7 pair available.\n"
                "\n\n"
                "Press Enter then choose dice 2 and 5 by typing 2,5"
            ),
        },
        1: {
            "selection": [3,6],
            4: (
                "\n\n"
                "Notice that every available die has a T over it. This is \n"
                "important and will be explained soon.\n"
                "\n\n"
                "Press Enter then choose dice 3 and 6 by typing 3,6"
            )
        },
        "c": {
            4: (
                "\n\n"
                "You've collected another row with a ■ so your total \n"
                "score has decreased by 200 points.\n"
                "\n"
                "The remaining die was a 5, making it your throwaway die. \n"
                "Another Throwaway meter has been added.\n"
                "\n\n"
                "Press Enter."
            )
        }
    },
    4: {
        "hand": [1,3,5,6,6],       
        0: {
            "selection": [1,6],
            4: (
                "This is strange! Suddenly only some dice have a T.\n"
                "\n"
                "The T indicates that a die can be thrown away. Previously\n"
                "you could throw away any die, but in this hand, you can \n"
                "only throw away 3 and 5.\n"
                "\n"
                "Once you accumulate three Throwaway meters, you can only \n"
                "throw away those dice. Here, you have a meter for 3, 4 and\n"
                "5. From now on, you must plan your selections so that one \n"
                "of these dice is left.\n"
                "\n\n"
                "Press Enter, then choose dice 1 and 6 by typing 1,6"
            ),
        },
        1: {
            "selection": [5,6],
            4: (
                "\n\n"
                "Of the remaining die, you cannot leave the 6 because it is\n"
                "not a valid throwaway die. The die you leave will be added\n" 
                "to the meter.\n"
                "\n"
                "Once you have selected the same throwaway die eight times,\n"
                "the meter is full and your run will end. This does not \n"
                "mean you lose; your score is tallied and if it is 500 or \n"
                "more points, you win.\n"
                "\n\n"
                "Press Enter then choose dice 5 and 6 by typing 5,6"
            )
        },
        "c": {
            4: (
                "\n\n"
                "Great news! The ■ in row 7 have changed and that row is \n"
                "no longer detracting points!\n"
                "\n"
                "Once you reach the zero threshold (■»ø), all ■ in that row\n"
                "become ø which are worth zero points.\n"
                "\n"
                "Since you left a 3, there are now three throwaway marks in\n"
                "that meter. \n"
                "\n\n"
                "Press Enter."
            )
        }
    },
    5: {
        "hand": [3,3,4,4,5],       
        0: {
            "selection": [3,4],
            4: (
                "Your luck is fantastic! There are not one, but two more 7\n"
                "pairs AND you're free to pick them because the remaining \n"
                "die is marked with a T.\n"
                "\n\n"
                "Press Enter then choose dice 3 and 4 by typing 3,4"
            ),
        },
        1: {
            "selection": [3,4],
            4: (
                "\n\n"
                "Go for a second 7 mark!\n"
                "\n\n"
                "Press Enter then choose dice 3 and 4 by typing 3,4"
            )
        },
        "c": {
            4: (
                "\n\n"
                "More fantastic news: now that you have reached the ■»ø in\n"
                "the 7 row, you can start accumulating (postive!) points in\n"
                "that row.\n"
                "\n"
                "Each £ is added together and multiplied by the bonus at \n"
                "the end of the row. You selected two 7's, meaning two £. \n"
                "Each £ is worth 30 points, making the row's new total 60.\n"
                "\n"
                "You cannot achieve more than five £ in any row. You may \n"
                "select that pair again but it will not be scored.\n"
                "\n\n"
                "Press Enter."

            )
        }
    },
    6: {
        "hand": [1,1,2,6,6],       
        0: {
            4: (
                "Notice that every die has a T over it this round even \n"
                "though none of them should be a valid throwaway die. \n"
                "You're already using the maximum three Throwaway meters!\n"
                "\n"
                "When none of the dice are a valid throwaway, you are given\n"
                "a Free Ride. This means you can leave any die you would \n"
                "like. That die will simply vanish.\n"
                "\n"
                "A Free Ride is only possible when you are using all your \n"
                "Throwaway meters.\n"
                "\n\n"
                "That's it! The game is now yours! Try to score 500 points.\n"
                "Press Enter."
            ),
        },
    },
}


class Player:
    # A dummy player class for round 0 tutorial
    def __init__(self, name, game):
        self.name = name.strip()
        self.score = -210
        self.out = False
        self.pairs = {
            2: {"marks": 0, "multiplier": (10 * game.rules["point_factor"]["v"])},
            3: {"marks": 2, "multiplier": (7 * game.rules["point_factor"]["v"])},
            4: {"marks": 0, "multiplier": (6 * game.rules["point_factor"]["v"])},
            5: {"marks": 7, "multiplier": (5 * game.rules["point_factor"]["v"])},
            6: {"marks": 0, "multiplier": (4 * game.rules["point_factor"]["v"])},
            7: {"marks": 8, "multiplier": (3 * game.rules["point_factor"]["v"])},
            8: {"marks": 4, "multiplier": (4 * game.rules["point_factor"]["v"])},
            9: {"marks": 5, "multiplier": (5 * game.rules["point_factor"]["v"])},
            10: {"marks": 0, "multiplier": (6 * game.rules["point_factor"]["v"])},
            11: {"marks": 0, "multiplier": (7 * game.rules["point_factor"]["v"])},
            12: {"marks": 0, "multiplier": (10 * game.rules["point_factor"]["v"])}
        }
        self.throwaway_dice = {
            1: 6,
            2: 4,
            5: 3
        }
        self.free_ride = False
        self.valid_throwaway = [1,2,5,]
