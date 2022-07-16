import random
import chipcount
import time
import os, psutil
process = psutil.Process(os.getpid())

#FIX BLACKAJCK


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

    #Get player name
    player_name = str(input("Welcome to the Casino! What is your name?".center(100)+'\n').lower().capitalize())
    time.sleep(0.5)

    #Get player balance from ledger.csv
    balance = chipcount.get_score(1000, player_name)
    if balance <= 1000:
        print("Hello, {}! Here are 1000 chips to play with.".format(player_name).center(100))
        balance = 1000
        time.sleep(0.5)
    else:
        print("Good to see you again, {}! You left off with {} chips.".format(player_name, balance).center(100))
        time.sleep(0.5)
    return(balance, player_name)



#Invalid response function
def invalid():
    print('\n'+"Invalid response, please try again.".center(100)+'\n')
    time.sleep(1)

#Cashout and return to main menu
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


#Main roulette function
def roulette(balance, name):
    print("Welcome to Roulette!".center(100))
    wheel = {0:'Green', 1:'Black', 2:'Red', 3:'Black', 4:'Red', 5:'Black', 6:'Red', 7:'Black', 8:'Red', 9:'Black', 10:'Red', 11:'Black', 12:'Red', 13:'Black', 14:'Red', 15:'Black', 16:'Red', 17:'Black', 18:'Red', 19:'Black', 20:'Red', 21:'Black', 22:'Red', 23:'Black', 24:'Red', 25:'Black', 26:'Red', 27:'Black', 28:'Red', 29:'Black', 30:'Red', 31:'Black', 32:'Red', 33:'Black', 34:'Red', 35:'Black', 36:'Red'}

    #Roulette spin function
    def spin():
        print("-Spinning-".center(100))
        time.sleep(0.5)
        print("-Spinning-".center(100))
        time.sleep(0.5)
        print("-Spinning-".center(100))
        time.sleep(0.5)
        roll = random.choice(list(wheel.items()))
        return roll

    #Roulette win message
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

    #Roulette lose message
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



#Main slots function
def slots(balance, name):
    print("Welcome to Slots!".center(100))
    bonanza = ["Diamond", "Cherry", "|BAR|", "[7]"]

    #Slots spin function
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

    #Slots win message
    def win_mess():
        print(" {}  {}  {} ".format(output[0], output[1], output[2]))
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

    #Slots lose message
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
        


    #Main slots loop
    while True:    
        print(" ________________________________________".center(100))       
        print("|                                        |".center(100))
        print("|     You have a couple options.         |".center(100))
        print("|     Press 'w' to make a wager.         |".center(100))
        print("|     Press 'o' to view the odds.        |".center(100))
        print("|     Press 'q' to quit and cash out.    |".center(100))
        print("|________________________________________|".center(100))
        ans = input().lower()
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


#Main blackjack function
def blackjack(balance, name):
    print("Welcome to Blackjack!".center(100))

    deck = [
        [2,'Hearts'],[2,'Diamonds'],[2,'Clubs'],[2,'Spades'],
        [3,'Hearts'],[3,'Diamonds'],[3,'Clubs'],[3,'Spades'],
        [4,'Hearts'],[4,'Diamonds'],[4,'Clubs'],[4,'Spades'],
        [5,'Hearts'],[5,'Diamonds'],[5,'Clubs'],[5,'Spades'],
        [6,'Hearts'],[6,'Diamonds'],[6,'Clubs'],[6,'Spades'],
        [7,'Hearts'],[7,'Diamonds'],[7,'Clubs'],[7,'Spades'],
        [8,'Hearts'],[8,'Diamonds'],[8,'Clubs'],[8,'Spades'],
        [9,'Hearts'],[9,'Diamonds'],[9,'Clubs'],[9,'Spades'],
        [10,'Hearts'],[10,'Diamonds'],[10,'Clubs'],[10,'Spades'],
        ['Jack','Hearts'],['Jack','Diamonds'],['Jack','Clubs'],['Jack','Spades'],
        ['Queen','Hearts'],['Queen','Diamonds'],['Queen','Clubs'],['Queen','Spades'],
        ['King','Hearts'],['King','Diamonds'],['King','Clubs'],['King','Spades'],
        ['Ace','Hearts'],['Ace','Diamonds'],['Ace','Clubs'],['Ace','Spades']
        ]


    def init_deal():
        hand = []
        for i in range(2):
            random.shuffle(deck)
            card = deck.pop()
            hand.append(card)
        return hand

    def get_total(hand):
        for card in hand:
            if 'Ace' in card:
                ace = card
                hand.append(ace)

        total = 0
        for card in hand:
            if card[0] == "Jack" or card[0] == 'Queen' or card[0] == 'King':
                total += 10
            elif card[0] == 'Ace':
                if total >= 11:
                    total += 1
                else:
                    total += 11
            else:
                total += int(card[0])
        return total

    
    def add_card_dealer(dealer_hand):
        card = deck.pop()
        print("Dealer draws a card.")
        dealer_hand.append(card)
        print("It's the {} of {} for a new total of {}.".format(card[0], card[1], get_total(dealer_hand)))
        return dealer_hand

    def add_card_player(player_hand):
        card = deck.pop()
        print("You draw a card.")
        player_hand.append(card)
        print("It's the {} of {} for a new total of {}.".format(card[0], card[1], get_total(player_hand)))
        return player_hand

    def print_dealer_second_card(dealer_second_card, dealer_hand):
        print("Dealer reveals the {} of {} for a total of {}.".format(dealer_second_card[0], dealer_second_card[1], get_total(dealer_hand)))
            

                    



    def game():
        print("-Dealing-") 
        player_hand = init_deal()
        dealer_hand = init_deal()

        print("You have been dealt the {} of {} and the {} of {} for a total of {}.".format(player_hand[0][0], player_hand[0][1], player_hand[1][0], player_hand[1][1], get_total(player_hand)))
        print("The dealer is showing the {} of {}.".format(dealer_hand[0][0], dealer_hand[0][1]))
        dealer_second_card = (dealer_hand[1][0], dealer_hand[1][1])


        if get_total(player_hand) == 21 and get_total(dealer_hand) != 21:
            print("Blackjack! You win!")
            status = 'b'
            return status
        elif get_total(dealer_hand) == 21 and get_total(player_hand) != 21:
            print_dealer_second_card(dealer_second_card, dealer_hand)
            print("Dealer has blackjack! You lose!")
            status = 'l'
            return status
        elif get_total(player_hand) == 21 and get_total(dealer_hand) == 21:
            print_dealer_second_card(dealer_second_card, dealer_hand)
            print("Double blackjack! 10x Payout!!! (Fun fact, the probability of this happening is only 0.058%)")
            status = 'bb'
            return status

        while True:
            print("Would you like to hit or stand?")
            ans = input().lower()
            if ans.startswith('h'):
                add_card_player(player_hand)
                if get_total(player_hand) == 21:
                    print("21! Let's see what the dealer has.")
                    print_dealer_second_card(dealer_second_card, dealer_hand)
                    while get_total(dealer_hand) < 17:
                        add_card_dealer(dealer_hand)
                        if get_total(dealer_hand) > 21:
                            print("Dealer busts with {}.".format(get_total(dealer_hand)))
                    if get_total(dealer_hand) > get_total(player_hand) and get_total(dealer_hand) <= 21:
                        print("Dealer stands on {}.".format(get_total(dealer_hand)))
                        print("You lose!")
                        status = 'l'
                        break
                    elif get_total(dealer_hand) > 21:
                        print("You win!")
                        status = 'w'
                        break
                    elif get_total(player_hand) > get_total(dealer_hand) and get_total(dealer_hand) <= 21:
                        print("Dealer stands on {}.".format(get_total(dealer_hand)))
                        print("You win!")
                        status = 'w'
                        break
                    else:
                        print("Dealer stands on {}.".format(get_total(dealer_hand)))
                        print("Push! Nobody wins!")
                        status = 'p'
                        break

                elif get_total(player_hand) > 21:
                    print("You busted!")
                    status = 'l'
                    break
                else:
                    continue

            elif ans.startswith('s'):
                print("You have decided to stand on {}.".format(get_total(player_hand)))
                print_dealer_second_card(dealer_second_card, dealer_hand)
                
                while get_total(dealer_hand) < 17:
                    add_card_dealer(dealer_hand)
                    if get_total(dealer_hand) > 21:
                        print("Dealer busts with {}.".format(get_total(dealer_hand)))

                        
                if get_total(dealer_hand) > get_total(player_hand) and get_total(dealer_hand) <= 21:
                    print("Dealer stands on {}.".format(get_total(dealer_hand)))
                    print("You lose!")
                    status = 'l'
                    break
                elif get_total(dealer_hand) > 21:
                    print("You win!")
                    status = 'w'
                    break
                elif get_total(player_hand) > get_total(dealer_hand) and get_total(dealer_hand) <= 21:
                    print("Dealer stands on {}.".format(get_total(dealer_hand)))
                    print("You win!")
                    status = 'w'
                    break
                else:
                    print("Dealer stands on {}.".format(get_total(dealer_hand)))
                    print("Push! Nobody wins!")
                    status = 'p'
                    break
            else:
                invalid()
        return status
        

                    

    #Main blackjack loop
    while True:    
        print(" ________________________________________".center(100))       
        print("|                                        |".center(100))
        print("|     You have a couple options.         |".center(100))
        print("|     Press 'w' to make a wager.         |".center(100))
        print("|     Press 'h' to see how to play.      |".center(100))
        print("|     Press 'q' to quit and cash out.    |".center(100))
        print("|________________________________________|".center(100))


        ans = input().lower()

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
                            status = game()
                            print(status)
                            print("Would you like to play another hand? (Y/N)")
                            y_n = input().lower()
                            if y_n.startswith('y'):
                                continue
                            elif y_n.startswith('n'):
                                print("See you again soon!")
                                break
                        elif y_n.startswith('n'):
                            print("Alright, let's fix that.".center(100))
                            break
                        else:
                            invalid()

                elif wager > balance:
                    print("You don't have enough chips! Try placing a smaller wager.".center(100))




        elif ans.startswith('h'):
            print(" _______________________________________".center(100))                             
            print("|            Blackjack Rules            |".center(100))
            print("|                                       |".center(100))
            print("|     Draw cards against the dealer.    |".center(100))
            print("| Closest to 21 without going over wins.|".center(100))
            print("|   Face cards worth 10, Aces 1 or 11.  |".center(100))
            print("|       Dealer must stand on 17+.       |".center(100))
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
    print("|        |Roulette|         |Slots|          |Blackjack|        |".center(100))
    print("|_______________________________________________________________|".center(100))
    
    while True:
        print("Please input a game from the choices above,".center(100))
        print("or Quit, to save your chips for later. You can".center(100))
        choice = input("also input Leaderboard to view the high rollers.".center(100)+'\n').lower()
        if choice.startswith('r'):
            roulette(balance, name)
        elif choice.startswith('b'):
            blackjack(balance, name)
        elif choice.startswith('s'):
            slots(balance, name)
        elif choice.startswith('q'):
            time.sleep(0.5)
            print("Thanks for playing! Come back soon!".center(100))
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
    balance, name= __init__() #Run init and save playername and chip balance
    main() #run main


