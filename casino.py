import random
import chipcount
import time

#INITIALIZE function
def __init__():
    print("______________________________________________________________________________________________".center(100))
    print("|                                                                                              |".center(100))
    print("|        /$$           /$$$$$$                      /$$                              /$$       |".center(100))
    print("|      /$$$$$$        /$$__  $$                    |__/                            /$$$$$$     |".center(100))
    print("|     /$$__  $$      | $$  \__/  /$$$$$$   /$$$$$$$ /$$ /$$$$$$$   /$$$$$$        /$$__  $$    |".center(100))
    print("|    | $$  \__/      | $$       |____  $$ /$$_____/| $$| $$__  $$ /$$__  $$      | $$  \__/    |".center(100))
    print("|    |  $$$$$$       | $$        /$$$$$$$|  $$$$$$ | $$| $$  \ $$| $$  \ $$      |  $$$$$$     |".center(100))
    print("|     \____  $$      | $$    $$ /$$__  $$ \____  $$| $$| $$  | $$| $$  | $$       \____  $$    |".center(100))
    print("|     /$$  \ $$      |  $$$$$$/|  $$$$$$$ /$$$$$$$/| $$| $$  | $$|  $$$$$$/       /$$  \ $$    |".center(100))
    print("|    |  $$$$$$/       \______/  \_______/|_______/ |__/|__/  |__/ \______/       |  $$$$$$/    |".center(100))
    print("|     \_  $$_/                                                                    \_  $$_/     |".center(100))
    print("|       \__/                                                                        \__/       |".center(100))
    print("|______________________________________________________________________________________________|".center(100))                                                                            
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




def invalid():
    print('\n'+"Invalid response, please try again.".center(100)+'\n')
    time.sleep(1)

def cashout(balance, name):
    print("You have decided to cashout.".center(100))
    while True:
        print("You currently have {} chips. Are you sure you want to stop now? (Y/N)".format(balance).center(100))
        y_n = input()
        if y_n.startswith('y') or y_n.startswith('Y'):
            print("Cashed out {} chips!".format(balance).center(100))
            chipcount.save_score(balance, name)
            main()
        elif y_n.startswith('n') or y_n.startswith('N'):
            print("Yay! You decided to keep playing!".center(100))
            break
        else:
            invalid()
    return balance, name



def roulette(balance, name):
    print("Welcome to Roulette!".center(100))
    wheel = {0:'Green', 1:'Black', 2:'Red', 3:'Black', 4:'Red', 5:'Black', 6:'Red', 7:'Black', 8:'Red', 9:'Black', 10:'Red', 11:'Black', 12:'Red', 13:'Black', 14:'Red', 15:'Black', 16:'Red', 17:'Black', 18:'Red', 19:'Black', 20:'Red', 21:'Black', 22:'Red', 23:'Black', 24:'Red', 25:'Black', 26:'Red', 27:'Black', 28:'Red', 29:'Black', 30:'Red', 31:'Black', 32:'Red', 33:'Black', 34:'Red', 35:'Black', 36:'Red'}

    def spin():
        print("-Spinning-".center(100))
        time.sleep(0.5)
        print("-Spinning-".center(100))
        time.sleep(0.5)
        print("-Spinning-".center(100))
        time.sleep(0.5)
        roll = random.choice(list(wheel.items()))
        return roll


    def win_mess():
        print("{} {}! You Win!".format(roll[0], roll[1]).center(100))
        print("You just won {} chips! They have been added to your balance.".format(winnings).center(100))
        print("Total balance: {}".format(balance).center(100))        
        while True:
            print("Would you like to place another wager? (Y/N)".center(100))
            y_n = input()
            if y_n.startswith('y') or y_n.startswith('Y'):
                break
            elif y_n.startswith('n') or y_n.startswith('N'):
                cashout(balance, name)
            else:
                invalid()


    def lose_mess():
        print("{} {}. You lose :(".format(roll[0], roll[1]).center(100))
        print("Your wager, {}, has been subtracted from your balance.".format(wager).center(100))
        print("Total balance: {}".format(balance).center(100))
        while True:
            print("Would you like to place another wager? (Y/N)".center(100))
            y_n = input()
            if y_n.startswith('y') or y_n.startswith('Y'):
                break
            elif y_n.startswith('n') or y_n.startswith('N'):
                cashout(balance, name)
            else:
                invalid()
        

    #Main roulette loop
    while True:
        print(" ________________________________________".center(100))       
        print("|                                        |".center(100))
        print("|     You have a couple options.         |".center(100))
        print("|     Press 'w' to make a wager.         |".center(100))
        print("|     Press 'o' to view the odds.        |".center(100))
        print("|     Press 'q' to quit and cash out.    |".center(100))
        print("|________________________________________|".center(100))
        ans = input().lower()
        if ans.startswith('w'):
            while True:
                print("Please enter the amount you would like to wager.".center(100))
                try: 
                    wager = int(input())
                except:
                    invalid()
                    continue 
                if wager <= balance:
                    while True:
                        print("You have chosen to wager {} chips. Is this correct? (Y/N)".format(wager).center(100))
                        y_n = input().lower()
                        if y_n.startswith('y'):
                            print("Time to choose the conditions of your wager.".center(100))
                            while True:
                                print("Press 's' for Single Number".center(100))
                                print("Press 'r' for Red".center(100))
                                print("Press 'b' for Black".center(100))
                                print("Press 'g' for Green".center(100))
                                print("Press 'd' for Dozen".center(100))
                                resp = input().lower()

                                #IF PLAYER CHOOSES SINGLE NUMBER
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
                                            balance += winnings
                                            win_mess()
                                        else:
                                            balance -= wager
                                            lose_mess()

                                #IF PLAYER CHOOSES RED
                                elif resp.startswith('r'):
                                    roll = spin()
                                    if resp.startswith('r') == roll[1][0].lower():
                                        winnings = wager
                                        balance += winnings
                                        win_mess()
                                    else:
                                        balance -= (wager)
                                        lose_mess()

                                #IF PLAYER CHOOSES BLACK
                                elif resp.startswith('b'):
                                    roll = spin()
                                    if resp.startswith('b') == roll[1][0].lower():
                                        winnings = wager
                                        balance += winnings
                                        win_mess()
                                    else:
                                        balance -= (wager)
                                        lose_mess()

                                #IF PLAYER CHOOSES GREEN
                                elif resp == 'g':
                                    roll = spin()
                                    if resp.startswith('g') and roll[1] == 'g':
                                        winnings = wager*50
                                        balance += winnings
                                        win_mess()
                                    else:
                                        balance -= wager
                                        lose_mess()

                                #IF PLAYER CHOOSES DOZEN
                                elif resp == 'd':
                                    print("Input 'first', 'second', or 'third'.".center(100))
                                    choice = str(input()).lower()
                                    roll = spin()
                                    if choice.startswith('f') and (roll[0] >= 1 and roll[0] <= 12):
                                        winnings = wager*2
                                        balance += winnings
                                        win_mess()
                                    elif choice.startswith('s') and (roll[0] >= 13 and roll[0] <= 24):
                                        winnings = wager*2
                                        balance += winnings
                                        win_mess()
                                    elif choice.startswith('t') and (roll[0] >= 25 and roll[0] <= 36):
                                        winnings = wager*2
                                        balance += winnings
                                        win_mess()
                                    else:
                                        balance -= wager
                                        lose_mess()
                                       
                                else:
                                    invalid()
                                
                        elif y_n.startswith('n'):
                            print("Alright, let's fix that.".center(100))
                            break

                        else:
                            invalid()
                elif wager > balance:
                    print("You don't have enough chips! Try placing a smaller wager.".center(100))

        elif ans.startswith('o'):

            print("_______________________________________".center(100))           
            print("|                                       |".center(100))
            print("|       Single Number pays 36 to 1      |".center(100))
            print("|        Red or Black pays 1 to 1       |".center(100))
            print("|        Even or Odd pays 1 to 1        |".center(100))
            print("|       Green or Zero pays 50 to 1      |".center(100))
            print("|   1st, 2nd, or 3rd Dozen pays 2 to 1  |".center(100))
            print("|                                       |".center(100))
            print("|     (Press any key to move on)        |".center(100))
            print("|_______________________________________|".center(100))

            x = input()
        elif ans.startswith('q'):
            cashout(balance, name)
        else:
            invalid()


def slots(balance, name):
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
        print("Total balance: {}".format(balance).center(100))
        while True:
            print("Would you like to place another wager? (Y/N)".center(100))
            y_n = input()
            if y_n.startswith('y') or y_n.startswith('Y'):
                break
            elif y_n.startswith('n') or y_n.startswith('N'):
                cashout(balance, name)
            else:
                invalid()


    def lose_mess():
        print(" {}  {}  {} ".format(output[0], output[1], output[2]))
        print("You lost! Your wager, {}, has been subtracted from your balance.".format(wager).center(100))
        print("Total balance: {}".format(balance).center(100))
        while True:
            print("Would you like to place another wager? (Y/N)".center(100))
            y_n = input()
            if y_n.startswith('y') or y_n.startswith('Y'):
                break
            elif y_n.startswith('n') or y_n.startswith('N'):
                cashout(balance, name)
            else:
                invalid()
        


    
    while True:    
        print(" ________________________________________".center(100))       
        print("|                                        |".center(100))
        print("|     You have a couple options.         |".center(100))
        print("|     Press 'w' to make a wager.         |".center(100))
        print("|     Press 'o' to view the odds.        |".center(100))
        print("|     Press 'q' to quit and cash out.    |".center(100))
        print("|________________________________________|".center(100))
        ans = input(''.center(100)).lower()
        if ans == 'w':
            while True:
                print("Please enter the amount you would like to wager.".center(100))
                try: 
                    wager = int(input())
                except:
                    invalid()
                    continue 
                if wager <= balance:
                    while True:
                        print("You have chosen to wager {} chips. Is this correct? (Y/N)".format(wager).center(100))
                        y_n = input().lower()
                        if y_n.startswith('y'):
                            output = list(spin())
                            if output[0] == '[7]' and output[1] == '[7]' and output[2] == '[7]':
                                winnings = wager*500
                                balance += winnings
                                win_mess()
                            elif output[0] == '|BAR|' and output[1] == '|BAR|' and output[2] == '|BAR|':
                                winnings = wager*250
                                balance += winnings
                                win_mess()
                            elif output[0] == 'Diamond' and output[1] == 'Diamond' and output[2] == 'Diamond':
                                winnings = wager*100
                                balance += winnings
                                win_mess()
                            elif output[0] == 'Bell' and output[1] == 'Bell' and output[2] == 'Bell':
                                winnings = wager*50
                                balance += winnings
                                win_mess()
                            elif output[0] == 'Cherry' and output[1] == 'Cherry' and output[2] == 'Cherry':
                                winnings = wager*10
                                balance += winnings
                                win_mess()
                            else:
                                balance -= wager
                                lose_mess()
                        elif y_n.startswith('n'):
                            print("Alright, let's fix that.".center(100))
                            break
                        else:
                            invalid()

                elif wager > balance:
                    print("You don't have enough chips! Try placing a smaller wager.".center(100))
                    

        elif ans.startswith('o'):
            print(" _______________________________________".center(100))                             
            print("|                                       |".center(100))
            print("|     Cherry   3x  | Pays 10 to 1       |".center(100))
            print("|      Bell    3x  | Pays 50 to 1       |".center(100))
            print("|     Diamond  3x  | Pays 100 to 1      |".center(100))
            print("|      |BAR|   3x  | Pays 250 to 1      |".center(100))
            print("|       [7]    3x  | Pays 500 to 1      |".center(100))
            print("|                                       |".center(100))
            print("|      (Press any key to move on)       |".center(100))
            print("|_______________________________________|".center(100))
            x = input()

        elif ans.startswith('q'):
            cashout(balance, name)
        else:
            invalid()  



#Main function
def main():

    print("_______________________________________________________________".center(100))
    print("|      __  __         _          __  __                         |".center(100))
    print("|     |  \/  |  __ _ (_) _ __   |  \/  |  ___  _ __   _   _     |".center(100))
    print("|     | |\/| | / _` || || '_ \  | |\/| | / _ \| '_ \ | | | |    |".center(100))
    print("|     | |  | || (_| || || | | | | |  | ||  __/| | | || |_| |    |".center(100))
    print("|     |_|  |_| \__,_||_||_| |_| |_|  |_| \___||_| |_| \__,_|    |".center(100))
    print("|                                                               |".center(100))
    print("|                                                               |".center(100))
    print("|       |Roulette|         |Blackjack|          |Slots|         |".center(100))
    print("|_______________________________________________________________|".center(100))

    while True:
        print("Please input a game from the choices above,".center(100))
        print("or Quit, to save your chips for later. You can".center(100))
        choice = input("also input Leaderboard to view the high rollers.".center(100)+'\n').lower()
        if choice.startswith('r'):
            roulette(balance, name)
        elif choice.startswith('b'):
            print("Coming Soon!")
            pass
        elif choice.startswith('s'):
            slots(balance, name)
        elif choice.startswith('q'):
            time.sleep(0.5)
            print("Come back soon!".center(100))
            time.sleep(0.5)
            break
        elif choice.startswith('l'):
            time.sleep(0.5)
            chipcount.leaderboard()
            time.sleep(0.5)
        else:
            invalid()


#Run script
if __name__ == "__main__":
    #Run init and save playername and chip balance
    balance, name= __init__()
    main()


