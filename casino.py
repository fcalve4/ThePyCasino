import random
import chipcount
import time



#INITIALIZE function
def __init__():
    print(
        """     ______________________________________________________________________________________________
    |                                                                                              |
    |        /$$           /$$$$$$                      /$$                              /$$       |
    |      /$$$$$$        /$$__  $$                    |__/                            /$$$$$$     |
    |     /$$__  $$      | $$  \__/  /$$$$$$   /$$$$$$$ /$$ /$$$$$$$   /$$$$$$        /$$__  $$    |
    |    | $$  \__/      | $$       |____  $$ /$$_____/| $$| $$__  $$ /$$__  $$      | $$  \__/    |
    |    |  $$$$$$       | $$        /$$$$$$$|  $$$$$$ | $$| $$  \ $$| $$  \ $$      |  $$$$$$     |
    |     \____  $$      | $$    $$ /$$__  $$ \____  $$| $$| $$  | $$| $$  | $$       \____  $$    |
    |     /$$  \ $$      |  $$$$$$/|  $$$$$$$ /$$$$$$$/| $$| $$  | $$|  $$$$$$/       /$$  \ $$    |
    |    |  $$$$$$/       \______/  \_______/|_______/ |__/|__/  |__/ \______/       |  $$$$$$/    |
    |     \_  $$_/                                                                    \_  $$_/     |
    |       \__/                                                                        \__/       |
    |______________________________________________________________________________________________|                                                                            
    """)
    time.sleep(0.5)
    player_name = input("Welcome to the Casino! What is your name?\n").lower().capitalize()
    time.sleep(0.5)
    balance = chipcount.get_score(1000, player_name)
    if balance == 1000:
        print("Hello, {}! Here are 1000 chips to play with.".format(player_name))
        time.sleep(0.5)
    else:
        print("Good to see you again, {}! You left off with {} chips.".format(player_name, balance))
        time.sleep(0.5)
    return(balance, player_name)

#Run init and save playername and chip balance
BALANCE, NAME= __init__()


def invalid():
    "Invalid response, please try again."
    time.sleep(1)

def cashout(BALANCE, NAME):
    print("You have decided to cashout.")
    print("You currently have " + str(BALANCE) + " chips. Are you sure you want to stop now? {y/n}")
    while True:
        y_n = input()
        if y_n == 'y':
            print("Cashed out {} chips!".format(BALANCE))
            chipcount.save_score(BALANCE, NAME)
            main()
        elif y_n == 'n':
            print("Yay! You decided to keep playing!")
            break
        else:
            invalid()
    return BALANCE, NAME



def roulette(BALANCE=BALANCE, NAME=NAME):
    print("Welcome to Roulette!")
    dict = {0:'Green', 1:'Black', 2:'Red', 3:'Black', 4:'Red', 5:'Black', 6:'Red', 7:'Black', 8:'Red', 9:'Black', 10:'Red', 11:'Black', 12:'Red', 13:'Black', 14:'Red', 15:'Black', 16:'Red', 17:'Black', 18:'Red', 19:'Black', 20:'Red', 21:'Black', 22:'Red', 23:'Black', 24:'Red', 25:'Black', 26:'Red', 27:'Black', 28:'Red', 29:'Black', 30:'Red', 31:'Black', 32:'Red', 33:'Black', 34:'Red', 35:'Black', 36:'Red'}

    def spin():
        print("-Spinning-")
        time.sleep(0.5)
        print("-Spinning-")
        time.sleep(0.5)
        print("-Spinning-")
        time.sleep(0.5)
        roll = random.choice(list(dict.items()))
        return roll


    def win_mess():
        print("{} {}! You Win!".format(roll[0], roll[1]))
        print("You just won {} chips! They have been added to your balance.\nTotal Balance: {}".format(winnings, BALANCE))
        print("Would you like to place another wager? {y/n}")
        while True:
            y_n = input()
            if y_n == 'y':
                break
            elif y_n == 'n':
                cashout(BALANCE, NAME)
            else:
                invalid()


    def lose_mess():
        print("{} {}. You lose :(".format(roll[0], roll[1]))
        print("Your wager, {}, has been subtracted from your balance.\nTotal Balance: {}".format(wager, BALANCE))
        print("Would you like to place another wager? {y/n}")
        while True:
            y_n = input()
            if y_n == 'y':
                break
            elif y_n == 'n':
                cashout(BALANCE, NAME)
            else:
                invalid()
        

    #Main roulette loop
    while True:
        print("You have a couple options.")
        print("Press 'w' to make a wager.")
        print("Press 'o' to view the odds.")
        print("Press 'x' to quit and cash out.")
        ans = input()
        if ans == 'w':
            while True:
                print("Please enter the amount you would like to wager.")
                wager = int(input())
                if wager <= BALANCE:
                    while True:
                        print("You have chosen to wager " + str(wager) + " chips. Is this correct? {y/n}")
                        y_n = input()
                        if y_n == 'y':
                            print("Time to choose the conditions of your wager.")
                            while True:
                                print("Press 's' for Single Number\nPress 'rb' for Red or Black\nPress 'eo' for Even or Odds\nPress 'g' for Green\nPress 'd' for Dozen")
                                resp = input() 
                                if resp == 's':
                                    print("Input a number between 0 and 36.")
                                    choice = int(input())
                                    roll = spin()
                                    if choice < 0 or choice > 36:
                                        invalid()
                                        continue
                                    elif choice == roll[0]:
                                        winnings = wager*36
                                        BALANCE += winnings
                                        win_mess()
                                    else:
                                        BALANCE -= wager
                                        lose_mess()
                                elif resp == 'rb':
                                    print("Input 'red' or 'black'.")
                                    choice = str(input()).lower()
                                    roll = spin()
                                    if not choice.startswith('r') or not choice.startswith('b'):
                                        invalid()
                                        continue
                                    elif choice.startswith('r') == roll[1][0].lower() or choice.startswith('b') == roll[1][0].lower():
                                        winnings = wager
                                        BALANCE += winnings
                                        win_mess()
                                    else:
                                        BALANCE -= (wager)
                                        lose_mess()
                                elif resp == 'eo':
                                    print("Input 'even' or 'odd'.")
                                    choice = str(input()).lower()
                                    roll = spin()
                                    if choice.startswith('e') and roll[0] % 2 == 0:
                                        winnings = wager
                                        BALANCE += winnings
                                        win_mess()
                                    elif choice.startswith('o') and roll[0] % 2 == 1:
                                        winnings = wager
                                        BALANCE += winnings
                                        win_mess()
                                    else:
                                        BALANCE -= wager
                                        lose_mess()
                                elif resp == 'g':
                                    choice = str(input()).lower()
                                    roll = spin()
                                    if choice.startswith('g') and roll[1] == 'g':
                                        winnings = wager*50
                                        BALANCE += winnings
                                        win_mess()
                                    else:
                                        BALANCE -= wager
                                        lose_mess()
                                elif resp == 'd':
                                    print("Input 'first', 'second', or 'third'.")
                                    choice = str(input()).lower()
                                    roll = spin()
                                    if choice.startswith('f') and (roll[0] >= 1 and roll[0] <= 12):
                                        winnings = wager*2
                                        BALANCE += winnings
                                        win_mess()
                                    elif choice.startswith('s') and (roll[0] >= 13 and roll[0] <= 24):
                                        winnings = wager*2
                                        BALANCE += winnings
                                        win_mess()
                                    elif choice.startswith('t') and (roll[0] >= 25 and roll[0] <= 36):
                                        winnings = wager*2
                                        BALANCE += winnings
                                        win_mess()
                                    else:
                                        BALANCE -= wager
                                        lose_mess()
                                else:
                                    invalid()
                                
                        elif y_n == 'n':
                            print("Alright, let's fix that.")
                            break
                        else:
                            invalid()
                elif wager > BALANCE:
                    print("You don't have enough chips! Try placing a smaller wager.")
                    continue
        elif ans == 'o':
            print(
                """
                 _______________________________________
                |                                       |
                |       Single Number pays 36 to 1      |
                |        Red or Black pays 1 to 1       |
                |        Even or Odd pays 1 to 1        |
                |       Green or Zero pays 50 to 1      |
                |   1st, 2nd, or 3rd Dozen pays 2 to 1  |
                |                                       |
                |     (Press any key to move on)        |
                |_______________________________________|
                """
            )
            x = input()
        elif ans == 'x':
            cashout(BALANCE, NAME)
        else:
            invalid()


def slots(BALANCE=BALANCE, NAME=NAME):
    print("Welcome to Slots!")
    bonanza = ["Diamond", "Cherry", "|BAR|", "[7]"]

    def spin():
        print("-Spinning-")
        time.sleep(0.5)
        print("-Spinning-")
        time.sleep(0.5)
        print("-Spinning-")
        time.sleep(0.5)      
        first = random.choice(bonanza)
        second = random.choice(bonanza)
        third = random.choice(bonanza)

        return first, second, third


    def win_mess():
        print(" {}  {}  {} ".format(output[0], output[1], output[2]))
        print("You just won {} chips! They have been added to your balance.\nTotal Balance: {}".format(winnings, BALANCE))
        print("Would you like to place another wager? {y/n}")
        while True:
            y_n = input()
            if y_n == 'y':
                break
            elif y_n == 'n':
                cashout(BALANCE, NAME)
            else:
                invalid()


    def lose_mess():
        print(" {}  {}  {} ".format(output[0], output[1], output[2]))
        print("You lost! Your wager, {}, has been subtracted from your balance.\nTotal Balance: {}".format(wager, BALANCE))
        print("Would you like to place another wager? {y/n}")
        while True:
            y_n = input()
            if y_n == 'y':
                break
            elif y_n == 'n':
                cashout(BALANCE, NAME)
            else:
                invalid()
        


    
    while True:    
        print("You have a couple options.")
        print("Press 'w' to make a wager.")
        print("Press 'o' to view the odds.")
        print("Press 'x' to quit and cash out.")
        ans = input()
        if ans == 'w':
            while True:
                print("Please enter the amount you would like to wager.")
                wager = int(input())
                if wager <= BALANCE:
                    while True:
                        print("You have chosen to wager " + str(wager) + " chips. Is this correct? {y/n}")
                        y_n = input()
                        if y_n == 'y':
                            output = list(spin())
                            if output[0] == '[7]' and output[1] == '[7]' and output[2] == '[7]':
                                winnings = wager*500
                                BALANCE += winnings
                                win_mess()
                            elif output[0] == '|BAR|' and output[1] == '|BAR|' and output[2] == '|BAR|':
                                winnings = wager*250
                                BALANCE += winnings
                                win_mess()
                            elif output[0] == 'Cherry' and output[1] == 'Cherry' and output[2] == 'Cherry':
                                winnings = wager*100
                                BALANCE += winnings
                                win_mess()
                            elif output[0] == 'Diamond' and output[1] == 'Diamond' and output[2] == 'Diamond':
                                winnings = wager*50
                                BALANCE += winnings
                                win_mess()
                            elif output[0] == 'Diamond' and output[1] == 'Diamond' and output[2] != 'Diamond':
                                winnings = wager*10
                                BALANCE += winnings
                                win_mess()
                            elif output[0] == 'Diamond' and output[1] != 'Diamond' and output[2] == 'Diamond':
                                winnings = wager*10
                                BALANCE += winnings
                                win_mess()
                            elif output[0] != 'Diamond' and output[1] == 'Diamond' and output[2] == 'Diamond':
                                winnings = wager*10
                                BALANCE += winnings
                                win_mess()
                            elif 'Diamond' in output:   
                                winnings = wager*2
                                BALANCE += winnings
                                win_mess()
                            else:
                                BALANCE -= wager
                                lose_mess()
                        elif y_n == 'n':
                            print("Alright, let's fix that.")
                            break
                        else:
                            invalid()

                elif wager > BALANCE:
                    print("You don't have enough chips! Try placing a smaller wager.")
                    

        elif ans == 'o':
            print(
                """
                 _______________________________________
                |                                       |
                |        Diamond 1x | Pays 2 to 1       |
                |        Diamond 2x | Pays 10 to 1      |
                |        Diamond 3x | Pays 50 to 1      |
                |       Cherry  3x | Pays 100 to 1      |
                |        |BAR|  1x | Pays 250 to 1      |
                |         [7]   3x | Pays 500 to 1      |
                |                                       |
                |      (Press any key to move on)       |
                |_______________________________________|
                """
            )
            x = input()

        elif ans == 'x':
            cashout(BALANCE, NAME)
        else:
            invalid()  



#Main function
def main():
    choice = input(
        """
         _______________________________________________________________
        |      __  __         _          __  __                         |
        |     |  \/  |  __ _ (_) _ __   |  \/  |  ___  _ __   _   _     |
        |     | |\/| | / _` || || '_ \  | |\/| | / _ \| '_ \ | | | |    |
        |     | |  | || (_| || || | | | | |  | ||  __/| | | || |_| |    |
        |     |_|  |_| \__,_||_||_| |_| |_|  |_| \___||_| |_| \__,_|    |
        |                                                               |
        |                                                               |
        |       |Roulette|         |Blackjack|          |Slots|         |
        |_______________________________________________________________|

                  Please input a game from the choices above, 
                     or quit, to save your chips for later.\n"""

        ).lower()
    if choice.startswith('r'):
        roulette(BALANCE, NAME)
    elif choice.startswith('b'):
        pass
    elif choice.startswith('s'):
        slots(BALANCE, NAME)
    elif choice.startswith('q'):
        time.sleep(0.5)
        print("Come back soon!")
        time.sleep(0.5)
        quit()


#Run script
if __name__ == "__main__":
    main()

