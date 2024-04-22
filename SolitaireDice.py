# Packages
import sys
from copy import deepcopy
from random import randint
import re

# Text assets
import tutorial
import info_screens


# The main menu for the program
def main():
    while True: 
        print(info_screens.main_menu)
        user_input = g_input("What would you like to do? ")
        # Start a new game
        if user_input == "new game":
            print(info_screens.new_game)
            try:
                names = get_names("Input one or more players separated by commas: ")
                game = Solitaire_dice(names)
                game.game()
                del game
                g_input("Enter to return to menu.")
            except SystemExit:
                continue
        # Start a new game with tutorial
        if user_input == "tutorial":
            print(info_screens.new_game)
            try:
                while True:
                    try:
                        name = get_names("Welcome! What's your name? ")
                        if len(name) != 1:
                            raise ValueError
                        break
                    except ValueError:
                        print("Input one name, please. Don't use a comma in your name.")
                print(f"name: {name}{type(name)}")
                game = Solitaire_dice(name, True)
                game.game()
                del game
                g_input("Enter to return to menu.")
            except SystemExit: 
                continue
        # Credits
        if user_input == "credits":
            print(info_screens.credits)
            try:
                g_input("Enter to return to menu.")
            except SystemExit:
                continue

# General input, allows the user to type basic commands, returns the input
def g_input(prompt="Enter to Continue: ", lower=True):
    while True:
        try: 
            user_input = input(prompt).strip()
            if user_input == "help":
                input(info_screens.game_help)
            else:
                raise Help
        except Help:
            break
    if user_input.lower() == "exit":
        sys.exit()
    else:
        if lower == True:
            return user_input.lower()
        else:
            return user_input

# Confirmation input, raises an error if the user inputs 'no', does nothing if 'yes'
def c_input(message="Conintue with this selection? y/n: "):
    while True:
        confirm = g_input(message)
        if confirm in ["n", "no"]:
            raise PlayerReject
        elif confirm in ["y", "yes", ""]:
            break
        else:
            continue

# Gets names of players and returns them as a tidy list
def get_names(message):
    user_input = g_input(message, lower=False)
    names = user_input.split(",")
    for name in names:
        name = name.strip()
    return names


# Stores the rules of the game
class Game_rules:
    def __init__(self):
        self.rules = {
            # v is value, p is acceptable range of parameters, d is default
            # messing with values will likely result in an unwinable game
            "max_throwaway_marks": {"v": 8, "p": [1,16], "d": 8},
            "max_throwaway_dice": {"v": 3, "p": [1,6], "d": 3},
            "max_point_marks": {"v": 5, "p": [1,10], "d": 5},
            "zero_threshold": {"v": 5, "p": [1,10], "d": 5},
            "point_factor": {"v": 10, "p": [1,100], "d": 10},
            "penalty": {"v": -200, "p": [-1000,0], "d": -200},
            "win_score": {"v": 500, "p": [0,67000], "d": 500}
        }
    
    # Adjusts the rules for the game
    def set_rule(self):
        while True:
            print(self.ui())
            rule_input = g_input("What rule to change? ")
            # Done to continue to game
            if rule_input == "done":
                g_input("Starting game.")
                break
            # resets values to default
            elif rule_input == "default":
                for rule in self.rules:
                    self.rules[rule]["v"] = self.rules[rule]["d"]
                    g_input("Rules returned to default values.")
            # checks if the input is a valid rule
            elif rule_input in self.rules:
                while True:
                    try:
                        parameter_input = g_input(f"{rule_input} selected. \nChoose new value or type 'info': ").strip().replace("'", "")
                        # hints if user inputs 'info'
                        if parameter_input == "info":
                            print(info_screens.rule_hint[rule_input])
                        else:
                            parameter_input = int(parameter_input)
                            break
                    except ValueError:
                        print("Please enter the parameter as a number.")
                        continue
                # check if parameter is within accepted values
                if self.rules[rule_input]["p"][0] <= int(parameter_input) <= self.rules[rule_input]["p"][1]:
                    self.rules[rule_input]["v"] = int(parameter_input)
                    g_input(f"{rule_input} adjusted to {self.rules[rule_input]['v']} ")
                else:
                    g_input("Chosen value is not within accepted values. Please try again.")
            else: 
                g_input("Rule not recognized. Please try again.")
        
    # Returns a table of rules and data
    def ui(self):
        s = info_screens.rule_adjust_top
        for rule in self.rules.keys():
            white_space = (22 - len(rule)) * " "
            current = f"{self.rules[rule]['v']:9}"
            minimum = f"{self.rules[rule]['p'][0]:9}"
            maximum = f"{self.rules[rule]['p'][1]:9}"
            default = f"{self.rules[rule]['d']:9}"
            s += f"{rule}{white_space}{current}{minimum}{maximum}{default}\n"
        s += info_screens.rule_adjust_bottom
        return s


# Dictates who is playing the game, manages turns, stores current hand and available dice.
class Solitaire_dice:
    # Initializes game and creates player classes
    def __init__(self, names,  t=False):
        self.active_players = []
        self.out_players = []
        self.round_count = 0
        self.hand = []
        self.available_dice = []
        self.selection = {}
        self.Game_rules = Game_rules()
        # check for tutorial, if not ask for game rules
        self.t = t
        self.tutorial_dict = {}
        if self.t == True: 
            self.tutorial_dict = tutorial.tutorial
        # set game rules:
        else:
            while True:
                try:
                    # yes simply passes, no raises PlayerReject
                    print(info_screens.game_setup)
                    c_input("Standard rules? y/n: ")
                    break
                except PlayerReject:
                    self.Game_rules.set_rule()
                    break
        # copy rules dictionary from Game_rules to self
        self.rules = self.Game_rules.rules
        #initialize players
        for name in names:
            self.active_players.append(Player(name, self))
    
    # Expects list of active players
    # Manages who is playing, ends the game when there are no more players
    def game(self):
        while len(self.active_players) > 0:
            if self.t == True and self.round_count == 0:
                self.available_dice = [2,4,4,5,6]
                example_player = tutorial.Player("Sid", self)
                self.ui_print(example_player, 0)
                del example_player
            self.round_count += 1
            self.round()
            for player in self.active_players[:]:
                if player.out == True:
                    self.out_players.append(player)
                    self.active_players.remove(player)
        g_input(self.end_game_ui(self.out_players))
        for player in self.out_players:
            del player

    # Expects list of active players, updates players
    # Manages full round of all players
    def round(self):
        # Tutorial dictates the hand if enabled (and hand is present)
        if self.tutorial_check("hand", h=True) == True:
            self.hand = self.tutorial_dict[self.round_count]["hand"]
        # hand is constant for all players
        else:
            self.hand = self.die_roll()
        for player in self.active_players:
            while True:
                self.available_dice = deepcopy(self.hand)
                # checks for free ride and updates player
                player.free_ride_update(self)
                try:
                    # user selects pairs and throwaway
                    self.select(player)
                    # user confirms choice
                    self.accept_selection(player)
                    break
                except FormatError:
                    g_input(info_screens.format_error)
                    continue
                except DieNotAvailableError:
                    g_input(info_screens.die_error)
                    continue
                except InvalidThrowawayError:
                    g_input(info_screens.throwaway_error)
                    continue
                except PlayerReject:
                    g_input(info_screens.reject_error)
                    continue
                except TutorialError:
                    g_input(info_screens.tutorial_error)
            player.update_scorecard(self)

    # Player selects two pairs from available die
    # selection is validated and returned as a dict
    def select(self, player):
        self.selection = {}
        # player picks two pairs from available die
        for pick in range(0,2):
            self.ui_print(player, pick)
            s_pair = []
            # must be a pair of integers
            try:
                message = ["First", "Second"]
                user_input = g_input(f"{message[pick]} pair: ").strip()
                matches = re.search(r"^(\d{1})[, .]?(\d{1})$", user_input)
                if matches:
                    for match in [matches.group(1), matches.group(2)]:
                        s_pair.append(int(match))
                else: 
                    raise ValueError
            except ValueError:
                raise FormatError
            # selected dice must be available
            try:
                for die in s_pair:
                    self.available_dice.remove(die)
            except ValueError:
                raise DieNotAvailableError
            # at least one available die must be a valid throwaway
            # unless it's a free ride
            if player.free_ride == False:
                matches = 0
                for die in self.available_dice:
                    if die in player.valid_throwaway:
                        matches += 1
                if matches == 0:
                    raise InvalidThrowawayError
            # tutorial only: validates that pairs match tutorial selection
            if self.tutorial_check(pick, "selection") == True:
                if sorted(s_pair) != self.tutorial_dict[self.round_count][pick]["selection"]:
                    raise TutorialError
            # stores pair with key 1 or 2
            self.selection[f"pair_{pick+1}"] = s_pair
        # Throwaway (the leftover die) stored in selection dict
        self.selection["throwaway"] = (self.available_dice[0])
        # available_dice cleared to properly display dice in UI
        self.available_dice = []

    # Instantiates, prints and deletes the UI class
    def ui_print(self, player, pick):
        ui = UI(player, self)
        print_list = ui.main_ui()
        # Check if tutorial applies
        if self.tutorial_check(pick, 0) == True:
            g_input(self.tutorial_dict[self.round_count][pick][0])
        for i in range(0, len(print_list)):            
            print(print_list[i], end="")
            # tutorial_check[0] is reserved, so tutorial positions start at 1
            if self.tutorial_check(pick, i+1) == True:
                g_input(self.tutorial_dict[self.round_count][pick][i+1])
        del ui

    # Collects the round number and a position number, returns the tutorial
    # if h==True, pick is a hand of dice
    def tutorial_check(self, pick, position="", h=False):
        if self.t == True:
            if self.round_count in self.tutorial_dict:
                # pick can be a tutorial position or a hand
                if pick in self.tutorial_dict[self.round_count]:
                    # if pick is a hand
                    if h == True:
                        return True
                    # if pick is a position
                    elif position in self.tutorial_dict[self.round_count][pick]:
                        return True
        return False

    # Returns a sorted list of 5 random integers representing dice
    def die_roll(self):
        hand = []
        for _ in range(0,5):
            hand.append(randint(1,6))
        hand.sort()
        return hand

    # Displays the resulting scorecard of the player's selection and asks to confirm
    def accept_selection(self, player):
        player_copy = deepcopy(player)
        player_copy.update_scorecard(self)
        self.ui_print(player_copy, "c")
        if player_copy.out == True:
            print(
                "\nWarning! This selection will use your last throwaway die.\n"
                "This will end your run."
                "\n"
            )
        # raises an error if choice is no
        c_input()
        if player_copy.out == True:
            g_input(
                f"\n{player.name} has ended their run."
                "\n"
                "Enter to continue: "
                )
            
    # returns the final scoreboard
    def end_game_ui(self, out_players):
        # sort players by score
        out_players.sort(key=lambda player: player.score, reverse=True)
        # split player list into winners and others
        winners =  []
        others = []
        for player in out_players: 
            if player.score >= self.rules["win_score"]["v"]:
                winners.append(player)
            else:
                others.append(player)
        s = info_screens.end_game
        if len(winners) > 0:
            s += "Winners:\n\n"
            for player in winners:
                s += f"{    player.score:>7}: {player.name}\n"
        if len(others) > 0:
            s += "\n\nAttempts:\n\n"
            for player in others: 
                s += f"{    player.score:>7}: {player.name}\n"
        s += "\n\n"
        return s

# Stores and updates information related to player score, marks and throwaway dice
class Player:
    # Initializes player
    def __init__(self, name, game):
        self.name = name.strip()
        self.score = 0
        self.out = False
        self.pairs = {
            2: {"marks": 0, "multiplier": (10 * game.rules["point_factor"]["v"])},
            3: {"marks": 0, "multiplier": (7 * game.rules["point_factor"]["v"])},
            4: {"marks": 0, "multiplier": (6 * game.rules["point_factor"]["v"])},
            5: {"marks": 0, "multiplier": (5 * game.rules["point_factor"]["v"])},
            6: {"marks": 0, "multiplier": (4 * game.rules["point_factor"]["v"])},
            7: {"marks": 0, "multiplier": (3 * game.rules["point_factor"]["v"])},
            8: {"marks": 0, "multiplier": (4 * game.rules["point_factor"]["v"])},
            9: {"marks": 0, "multiplier": (5 * game.rules["point_factor"]["v"])},
            10: {"marks": 0, "multiplier": (6 * game.rules["point_factor"]["v"])},
            11: {"marks": 0, "multiplier": (7 * game.rules["point_factor"]["v"])},
            12: {"marks": 0, "multiplier": (10 * game.rules["point_factor"]["v"])}
        }
        self.throwaway_dice = {}
        self.free_ride = False
        self.valid_throwaway = [1,2,3,4,5,6]

    # Takes the game state and updates the player's scorecard
    def update_scorecard(self, game):
        s_pairs = [game.selection["pair_1"], game.selection["pair_2"]]
        self.update_pairs(s_pairs, game)
        self.calculate_score(game)
        if self.free_ride == False:
            self.update_throwaway(game.selection["throwaway"])
        self.update_valid_throwaway(game)
        self.update_out(game)

    # receives one of the players selections (a list of 2 ints) and updates the pairs dict
    def update_pairs(self, s_pairs, game):
        max_marks = game.rules["max_point_marks"]["v"] + game.rules["zero_threshold"]["v"]
        for s_pair in s_pairs:
            s_pair_total = s_pair[0] + s_pair[1]
            for pair in self.pairs:
                if s_pair_total == pair and self.pairs[pair]["marks"] < max_marks:
                    self.pairs[pair]["marks"] += 1
                    break

    # Refreshes the score by totalling the pair scores.
    def calculate_score(self, game):
        self.score = 0
        for pair in self.pairs:
            self.score += self.pair_score(pair, game)

    # Calculates and returns the score for a pair
    def pair_score(self, pair, game):
        # zero threshold is worth zero
        if self.pairs[pair]["marks"] in (0, game.rules["zero_threshold"]["v"]):
            return 0
        # Any marks under the zero threshold causes a total line score of rules["penalty"]
        elif self.pairs[pair]["marks"] < game.rules["zero_threshold"]["v"]:
            return game.rules["penalty"]["v"]
        # Reaching the zero threshold nullifies all marks under the zero threshod (removing the penalty)
        # Only marks above the zero threshold are counted for points
        elif self.pairs[pair]["marks"] > game.rules["zero_threshold"]["v"]:
            scoring_marks = self.pairs[pair]["marks"] - game.rules["zero_threshold"]["v"]
            return scoring_marks * self.pairs[pair]["multiplier"]

    # Compares the current hand to the list of valid throwaway die
    def free_ride_update(self, game):
        for die in game.hand:
            # if any die in the hand is a valid throwaway, no free ride
            if die in self.valid_throwaway:
                self.free_ride = False
                break
            # if no die in the hand is a valid throwaway, it's a free ride
            self.free_ride = True

    # Takes the dict of throwaway_dice and determines which die are valid to throw away
    def update_valid_throwaway(self, game):
        # if there are less than the maximum throwaway die already chosen, all die are valid
        self.valid_throwaway = []
        if len(self.throwaway_dice) < game.rules["max_throwaway_dice"]["v"]:
            for i in range(1, 7):
                self.valid_throwaway.append(i)
        # otherwise, the user may only choose throwaway die that have already been chosen
        else:
            for die in self.throwaway_dice:
                self.valid_throwaway.append(die)

    # Creates or updates the throwaway_dice dictionary
    def update_throwaway(self, die):
        if die not in self.throwaway_dice:
            self.throwaway_dice[die] = 1
        else:
            self.throwaway_dice[die] += 1

    # Marks the player as out if they reach the maximum count in any throwaway die
    def update_out(self, game):
        for die in self.throwaway_dice:
            if self.throwaway_dice[die] == game.rules["max_throwaway_marks"]["v"]:
                self.out = True
                break


# Creates and returns the main game UI
class UI:
    # Instantiates the class and stores variables for UI creation
    def __init__(self, player, game):
        self.name = player.name
        self.round_count = game.round_count
        self.score = player.score
        self.pairs = player.pairs
        self.rules = game.rules
        self.throwaway_dice = player.throwaway_dice
        self.selection = game.selection
        self.available_dice = game.available_dice
        self.valid_throwaway = player.valid_throwaway
        self.free_ride = player.free_ride
        self.t = game.t
        self.tutorial_dict = {}
        if self.t == True:
            self.tutorial_dict = game.tutorial_dict

    # Aggregates pieces of the main UI and returns them as a string
    def main_ui(self):
        # new lines separate ui instances
        return [
            f"{"\n" * 8}"
            f"{self.header()}\n",
            f"{self.score_board()}\n",
            f"{self.throwaway_meters()}\n",
            f"{self.dice()}\n"
            "\n"
        ]

    # Creates a header with a border, returns it as a string
    def header(self):
        # flexible divider whose width matches the score board
        # 6 is the number of mandatory blocks on the board (columns, etc);
        # the 10 "=" string is equal to the width of the multiplier and total columns
        divider = "===" * (self.rules["zero_threshold"]["v"] + self.rules["max_point_marks"]["v"] + 6) + "=========="
        s = f"{divider}\n\n"
        # adds name as N A M E
        for character in self.name.upper():
            s += f"{character} "
        s += (
            f"\n{divider}\n"
            f"Round: {self.round_count}\n"
            f"Total score: {self.score}\n"
        )
        return s

    # Creates a scoreboard based on the instance and returns it as a string
    # Scoreboard is flexible and generated based on game rules
    # All string lengths must be preserved to keep alignment
    def score_board(self):
        blocks = {
            "debt": " ■ ",
            "null": " ø ",
            "point": " £ ",
            "blank": "   ",
            "notch": " . ",
            "times": " × ",
            "equals": " = ",
            "s_rule": " | ",
            "l_rule": " ║ ",
        }
        # Creates row of column labels that align with column widths
        s = (
            # margin + label + flexible white space
            f"{blocks['blank']}{blocks['s_rule']}Debt  {(blocks['blank'] * (self.rules['zero_threshold']["v"] - 3))}"
            # column + zero threshold label "■»ø" + column
            f"{blocks['s_rule']}{blocks['debt'].strip()}»{blocks['null'].strip()}{blocks['l_rule']}"
            # label + flexible white space
            f"Points{(blocks['blank'] * (self.rules['max_point_marks']["v"] - 2))}"
            # end labels
            f"{blocks['times']}Bonus{blocks['equals']}Total\n"
        )
        # Appends a display of marks for each scoring pair and total score for that pair.
        for pair in self.pairs:
            s += (
                # marks and dividers for first 4 columns
                f"{self.line_printer(pair, blocks)}"
                # multiplier and line total
                f"{blocks['times']}{self.pairs[pair]['multiplier']:<5}{blocks['equals']}{self.pair_score(pair):5}\n"
            )
        # Appends a final row of notches to help player read column width
        s += (
            # margin + flexible number of notches
            f"{blocks['blank'] * 2}{(blocks['notch'] * (self.rules['zero_threshold']["v"] - 1))}"
            # space for column + notch + space for column
            f"{blocks['blank']}{blocks['notch']}{blocks['blank']}"
            # flexible amount of notches
            f"{(blocks['notch'] * (self.rules['max_point_marks']["v"]))}\n"
        )
        return s

    # copy of Player.pair_score(); avoids passing in player
    # Calculates and returns the score for a pair
    def pair_score(self, pair):
        # zero threshold is worth zero
        if self.pairs[pair]["marks"] in (0, self.rules["zero_threshold"]["v"]):
            return 0
        # Any marks under the zero threshold causes a total line score of rules["penalty"]
        elif self.pairs[pair]["marks"] < self.rules["zero_threshold"]["v"]:
            return self.rules["penalty"]["v"]
        # Reaching the zero threshold nullifies all marks under the zero threshod (removing the penalty)
        # Only marks above the zero threshold are counted for points
        elif self.pairs[pair]["marks"] > self.rules["zero_threshold"]["v"]:
            scoring_marks = self.pairs[pair]["marks"] - self.rules["zero_threshold"]["v"]
            return scoring_marks * self.pairs[pair]["multiplier"]

    # Takes a pair and generates blocks to display columns and icons; returns scorecard row
    def line_printer(self, pair, blocks):
        total_blocks = self.rules["zero_threshold"]["v"] + self.rules["max_point_marks"]["v"]
        # row label; leading digits on die must be equal to the length of any block
        s = f"{pair:3}{blocks['s_rule']}"
        # creates one block per column based on the number of marks for a pair
        for i in range(0, total_blocks):
            # places a blank block if that number of marks has not been reached
            if i >= self.pairs[pair]["marks"]:
                if i == self.rules["zero_threshold"]["v"] - 1:
                    # zero threshold column has dividers
                    s += f"{blocks['s_rule']}{blocks['blank']}{blocks['l_rule']}"
                else:
                    s += blocks["blank"]
            # creates an icon in the column if that mark has been reached
            else:
                # place a debt icon for every mark if the zero threshold has not been reached
                if self.pairs[pair]["marks"] < self.rules["zero_threshold"]["v"]:
                    s += blocks["debt"]
                else:
                    # debt icons are "converted" to null icons when zero threshold is reached
                    if i < self.rules["zero_threshold"]["v"] - 1:
                        s += blocks["null"]
                    # place a null icon if it is at the zero threshold
                    if i == self.rules["zero_threshold"]["v"] - 1:
                        # zero threshold column has dividers
                        s += f"{blocks['s_rule']}{blocks['null']}{blocks['l_rule']}"
                    # place point icons for every mark above the zero threshold
                    if i > self.rules["zero_threshold"]["v"] - 1:
                        s += blocks["point"]
        return s

    # returns an image of 5 dice based on available dice and player selections
    def dice(self):
        # '#' indicates where the number will display
        dice_image = [
            " +---+ ",
            " | # | ",
            " +---+ ",
            "       "
            ]
        label = [
            "   Pair 1:",
            "   Pair 2:"
            ]
        spacer = " | "
        throwaway_label = "   T   "
        blank = "       "
        # labels die if it is a valid throwaway
        s = f" {self.dice_row(blank, spacer, throwaway_label)}\n"
        # iterates through dice_image, creating a new row each time
        for line in dice_image:
            s += f" {self.dice_row(line, spacer)}\n"
        # labels for selected and available dice
        for i in self.selection:
            if type(self.selection[i]) == list:
                # labels selected pairs and their sum if they exist; ignores throwaway die
                s += f"   {i.replace('_', ' ').capitalize()}: {(self.selection[i][0] + self.selection[i][1]):2}   |"
            else:
                # labels the throwaway die
                if self.free_ride == False:
                    s += "  Throwaway"
                else:
                    s += "  Free Ride!"
        # the game only identifies available dice after first selection
        if len(self.available_dice) == 3:
            s += "  Available"
        return s

    # Expects selection, available dice, dice and spacer graphics, returns a row of the dice graphic
    # Optional flag 't' indicates if the row is the label for throwaway die; expects a label if so
    def dice_row(self, graphic, spacer, throwaway_label=""):
        s= ""
        # iterates through the selected dice if present
        # i can be a pair (as a list) or a single die (as an int)
        for i in self.selection:
            # if i is a pair of dice
            if type(self.selection[i]) == list:
                for die in self.selection[i]:
                    # replaces '#' (if present) with die number
                    if "#" in graphic:
                        s += graphic.replace("#", str(die))
                    else:
                        s += graphic
                s += spacer
            # if i is the throwaway die
            else:
                # replaces '#' (if present) with die number
                if "#" in graphic:
                    s += graphic.replace("#", str(self.selection[i]))
                else:
                    s += graphic
        # iterates through available dice if present
        for die in self.available_dice:
            if "#" in graphic:
                s += graphic.replace("#", str(die))
            # adds throwaway labels if the label is provided
            elif throwaway_label != "":
                if die in self.valid_throwaway:
                    s += throwaway_label
                elif self.free_ride == True:
                    s += throwaway_label
                else:
                    s += graphic
            # or simply prints the graphic
            else:
                s += graphic
        return s

    # Expects throwaway_dice dict, returns a graphic of said dict
    def throwaway_meters(self):
        blocks = {
            "available": "o",
            "used": "×"
        }
        lines = 0
        s = f"Throwaway Dice:\n"
        # prints a meter for each used throwaway die
        for die in self.throwaway_dice:
            lines += 1
            if lines == 4:
                s += "\n"
            s += f"   {die}:"
            for i in range(0, self.rules["max_throwaway_marks"]["v"]):
                if i >= self.throwaway_dice[die]:
                    s += blocks["available"]
                else:
                    s += blocks["used"]
            # space between meters
            s += "     "
        s += "\n"
        return s

class PlayerReject(Exception):
    pass

class FormatError(Exception):
    pass

class DieNotAvailableError(Exception):
    pass

class InvalidThrowawayError(Exception):
    pass

class TutorialError(Exception):
    pass

class Help(Exception):
    pass

if __name__ == "__main__":
    main()
