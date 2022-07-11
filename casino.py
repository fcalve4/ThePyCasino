import random
import chipcount
import time

#INITIALIZE function
def __init__():
    print(
    """
     ______________________________________________________________________________________________
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
    player_name = str(input("Welcome to the Casino! What is your name?".center(100)+'\n').lower().capitalize())
    time.sleep(0.5)
    balance = chipcount.get_score(1000, player_name)
    if balance <= 1000:
        print("Hello, {}! Here are 1000 chips to play with.".format(player_name).center(100))
        balance = 1000
        time.sleep(0.5)
    else:
        print("Good to see you again, {}! You left off with {} chips.".format(player_name, balance).center(100))
        time.sleep(0.5)
    return(balance, player_name)

#Run init and save playername and chip balance
BALANCE, NAME= __init__()


def invalid():
    print('\n' + "Invalid response, please try again.".center(100) + '\n')
    time.sleep(1)

def cashout(BALANCE, NAME):
    print("You have decided to cashout.".center(100))
    print("You currently have {} chips. Are you sure you want to stop now? (Y/N)".format(BALANCE).center(100))
    while True:
        y_n = input()
        if y_n.startswith('y') or y_n.startswith('Y'):
            print("Cashed out {} chips!".format(BALANCE).center(100))
            chipcount.save_score(BALANCE, NAME)
            main()
        elif y_n.startswith('n') or y_n.startswith('N'):
            print("Yay! You decided to keep playing!".center(100))
            break
        else:
            invalid()
    return BALANCE, NAME



def roulette(BALANCE=BALANCE, NAME=NAME):
    print("Welcome to Roulette!".center(100))
    dict = {0:'Green', 1:'Black', 2:'Red', 3:'Black', 4:'Red', 5:'Black', 6:'Red', 7:'Black', 8:'Red', 9:'Black', 10:'Red', 11:'Black', 12:'Red', 13:'Black', 14:'Red', 15:'Black', 16:'Red', 17:'Black', 18:'Red', 19:'Black', 20:'Red', 21:'Black', 22:'Red', 23:'Black', 24:'Red', 25:'Black', 26:'Red', 27:'Black', 28:'Red', 29:'Black', 30:'Red', 31:'Black', 32:'Red', 33:'Black', 34:'Red', 35:'Black', 36:'Red'}

    def spin():
        print("-Spinning-".center(100))
        time.sleep(0.5)
        print("-Spinning-".center(100))
        time.sleep(0.5)
        print("-Spinning-".center(100))
        time.sleep(0.5)
        roll = random.choice(list(dict.items()))
        return roll


    def win_mess():
        print("{} {}! You Win!".format(roll[0], roll[1]).center(100))
        print("You just won {} chips! They have been added to your balance.".format(winnings).center(100))
        print("Total Balance: {}".format(BALANCE).center(100))        
        while True:
            print("Would you like to place another wager? (Y/N)".center(100))
            y_n = input()
            if y_n.startswith('y') or y_n.startswith('Y'):
                break
            elif y_n.startswith('n') or y_n.startswith('N'):
                cashout(BALANCE, NAME)
            else:
                invalid()


    def lose_mess():
        print("{} {}. You lose :(".format(roll[0], roll[1]).center(100))
        print("Your wager, {}, has been subtracted from your balance.".format(wager).center(100))
        print("Total Balance: {}".format(BALANCE).center(100))
        while True:
            print("Would you like to place another wager? (Y/N)".center(100))
            y_n = input()
            if y_n.startswith('y') or y_n.startswith('Y'):
                break
            elif y_n.startswith('n') or y_n.startswith('N'):
                cashout(BALANCE, NAME)
            else:
                invalid()
        

    #Main roulette loop
    while True:
        print(
        """
                               ________________________________________
                              |                                        |
                              |     You have a couple options.         |
                              |     Press 'w' to make a wager.         |
                              |     Press 'o' to view the odds.        |
                              |     Press 'x' to quit and cash out.    |
                              |________________________________________|
        """
        )
        ans = input().lower()
        if ans == 'w':
            while True:
                print("Please enter the amount you would like to wager.".center(100))
                try: 
                    wager = int(input())
                except:
                    invalid()
                    continue 
                if wager <= BALANCE:
                    while True:
                        print("You have chosen to wager {} chips. Is this correct? (Y/N)".format(wager).center(100))
                        y_n = input('\n'.center(100)).lower()
                        if y_n == 'y':
                            print("Time to choose the conditions of your wager.".center(100))
                            while True:
                                print("Press 's' for Single Number".center(100))
                                print("Press 'r' for Red".center(100))
                                print("Press 'b' for Black".center(100))
                                print("Press 'e' for Even".center(100))
                                print("Press 'o' for Odd".center(100))
                                print("Press 'g' for Green".center(100))
                                print("Press 'd' for Dozen".center(100))
                                resp = input('\n'.center(100)).lower()
                                if resp.startswith('s'):
                                    while True:
                                        print("Input a number between 0 and 36.".center(100))  
                                        try:
                                            choice = int(input())
                                            if choice < 0 or choice > 36:
                                                invalid()
                                                continue
                                        except:
                                            invalid()
                                            continue
                                        roll = spin()
                                        if choice == roll[0]:
                                            winnings = wager*36
                                            BALANCE += winnings
                                            win_mess()
                                        else:
                                            BALANCE -= wager
                                            lose_mess()
                                elif resp.startswith('r'):
                                    print("Input 'red' or 'black'.".center(100))
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
                                    print("Input 'even' or 'odd'.".center(100))
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
                                    choice = resp.lower()
                                    roll = spin()
                                    if choice.startswith('g') and roll[1] == 'g':
                                        winnings = wager*50
                                        BALANCE += winnings
                                        win_mess()
                                    else:
                                        BALANCE -= wager
                                        lose_mess()
                                elif resp == 'd':
                                    print("Input 'first', 'second', or 'third'.".center(100))
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
                            print("Alright, let's fix that.".center(100))
                            break

                        else:
                            invalid()
                elif wager > BALANCE:
                    print("You don't have enough chips! Try placing a smaller wager.".center(100))

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
    print("Welcome to Slots!".center(100))
    bonanza = ["Diamond", "Cherry", "|BAR|", "[7]"]

    def spin():
        print("-Spinning-".center(100))
        time.sleep(0.5)
        print("-Spinning-".center(100))
        time.sleep(0.5)
        print("-Spinning-".center(100))
        time.sleep(0.5)      
        first = random.choice(bonanza)
        second = random.choice(bonanza)
        third = random.choice(bonanza)

        return first, second, third


    def win_mess():
        print(" {}  {}  {} ".format(output[0], output[1], output[2]).center(100))
        print("You just won {} chips! They have been added to your balance.".format(winnings).center(100))
        print("Total Balance: {}".format(BALANCE).center(100))
        while True:
            print("Would you like to place another wager? (Y/N)".center(100))
            y_n = input()
            if y_n.startswith('y') or y_n.startswith('Y'):
                break
            elif y_n.startswith('n') or y_n.startswith('N'):
                cashout(BALANCE, NAME)
            else:
                invalid()


    def lose_mess():
        print(" {}  {}  {} ".format(output[0], output[1], output[2]))
        print("You lost! Your wager, {}, has been subtracted from your balance.".format(wager).center(100))
        print("Total Balance: {}".format(BALANCE).center(100))
        while True:
            print("Would you like to place another wager? (Y/N)".center(100))
            y_n = input()
            if y_n.startswith('y') or y_n.startswith('Y'):
                break
            elif y_n.startswith('n') or y_n.startswith('N'):
                cashout(BALANCE, NAME)
            else:
                invalid()
        


    
    while True:    
        print(
        """
                               ________________________________________
                              |                                        |
                              |     You have a couple options.         |
                              |     Press 'w' to make a wager.         |
                              |     Press 'o' to view the odds.        |
                              |     Press 'x' to quit and cash out.    |
                              |________________________________________|
        """
        )
        ans = input(''.center(100)).lower()
        if ans == 'w':
            while True:
                print("Please enter the amount you would like to wager.".center(100))
                try: 
                    wager = int(input())
                except:
                    invalid()
                    continue 
                if wager <= BALANCE:
                    while True:
                        print("You have chosen to wager {} chips. Is this correct? (Y/N)".format(wager).center(100))
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
                            print("Alright, let's fix that.".center(100))
                            break
                        else:
                            invalid()

                elif wager > BALANCE:
                    print("You don't have enough chips! Try placing a smaller wager.".center(100))
                    

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
    print(
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
        """
        )
    while True:
        print("Please input a game from the choices above,".center(100))
        print("or Quit, to save your chips for later. You can".center(100))
        choice = input("also input Leaderboard to view the high rollers.".center(100)+'\n'.center(100)).lower()
        if choice.startswith('r'):
            roulette(BALANCE, NAME)
        elif choice.startswith('b'):
            pass
        elif choice.startswith('s'):
            slots(BALANCE, NAME)
        elif choice.startswith('q'):
            time.sleep(0.5)
            chipcount.save_score(BALANCE, NAME)
            time.sleep(0.5)
            print("Come back soon!".center(100))
            time.sleep(0.5)
            quit()
        elif choice.startswith('l'):
            time.sleep(0.5)
            chipcount.leaderboard()
            time.sleep(0.5)
        else:
            invalid()


#Run script
if __name__ == "__main__":
    main()


