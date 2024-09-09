"""
Imports color program, allows us to add color in terminal
"""
import colorama
from colorama import Back, Fore, Style

colorama.init(autoreset=True)

pickaxe = 1
bank = 0


def shop():
    """
    Displays prices for items and determines if you can buy them
    changes global variables bank and pickaxe if items are bought
    :return:
    """
    global pickaxe
    global bank
    print(f"You have {Fore.GREEN}${bank} {Fore.RESET}in you bank account")
    print(f"""{Fore.YELLOW} Your Current Pickaxe is LVL {pickaxe}
        
    {Fore.RESET}Welcome To The Item Shop!
    {Fore.CYAN}Pickaxe 2{Fore.RESET}: {Fore.GREEN}$1000
    {Fore.BLUE}Pickaxe 3{Fore.RESET}: {Fore.GREEN}$2500
    {Fore.MAGENTA}Pickaxe 4{Fore.RESET}: {Fore.GREEN}$5000
    {Fore.RED}P{Fore.YELLOW}i{Fore.GREEN}c{Fore.BLUE}k{Fore.MAGENTA}a{Fore.RED}x{Fore.YELLOW}e {Fore.GREEN}5{Fore.RESET}: {Fore.GREEN}$10000
    
    {Fore.RESET}Luxury Shop:
    {Fore.YELLOW}Macbook: {Fore.GREEN}15,000
    {Fore.YELLOW}Ferrari: {Fore.GREEN}50,000
    {Fore.YELLOW}Villa: {Fore.GREEN}100,000
    {Fore.YELLOW}Mansion: {Fore.GREEN}500,000
    """)
    buy = input(
        f"What would you like to buy?({Fore.CYAN}2{Fore.RESET}, {Fore.BLUE}3{Fore.RESET}, {Fore.MAGENTA}4{Fore.RESET}, {Fore.RED}5{Fore.RESET}, {Fore.YELLOW}etc{Fore.RESET}) ")
    if buy == "2":
        if bank >= 1000:
            if pickaxe != 1:
                print(f"{Fore.YELLOW}Why would you want to downgrade?")
                return
            pickaxe = 2
            bank = bank - 1000
        else:
            print(Fore.RED + "You do not have enough money!")
    elif buy == "3":
        if bank >= 2500:
            if pickaxe < 2:
                print(f"{Fore.RED}Slow Down! {Fore.YELLOW}You need to buy the Second upgrade")
                return
            elif pickaxe > 2:
                print(f"{Fore.YELLOW}Why would you want to downgrade?")
                return
            pickaxe = 3
            bank = bank - 2500
        else:
            print(Fore.RED + "You do not have enough money!")
    elif buy == "4":
        if bank >= 5000:
            if pickaxe < 3:
                print(f"{Fore.RED}Slow Down! {Fore.YELLOW}You need to buy the Third upgrade")
                return
            elif pickaxe > 3:
                print(f"{Fore.YELLOW}Why would you want to downgrade?")
                return
            pickaxe = 4
            bank = bank - 5000
        else:
            print(Fore.RED + "You do not have enough money!")
    elif buy == "5":
        if bank >= 10000:
            if pickaxe < 4:
                print(f"{Fore.RED}Slow Down! {Fore.YELLOW}You need to buy the Fourth upgrade")
                return
            elif pickaxe > 4:
                print(f"{Fore.YELLOW}Why would you want to downgrade?")
                return
            pickaxe = 5
            bank = bank - 10000
    elif buy == "Macbook":
        if bank >= 15000:
            print(f"{Fore.YELLOW}nice upgrade!!!")
            bank = bank - 15000
        else:
            print(Fore.RED + "You do not have enough money!")
    elif buy == "Ferrari":
        if bank >= 50000:
            print(f"{Fore.YELLOW}Congrats, now you can get to work even faster!!!")
            bank = bank - 50000
        else:
            print(Fore.RED + "You do not have enough money!")
    elif buy == "Villa":
        if bank >= 100000:
            print(f"{Fore.YELLOW}Congrats on the new villa!!!")
            bank = bank - 100000
        else:
            print(Fore.RED + "You do not have enough money!")
    elif buy == "Mansion":
        if bank >= 500000:
            print(f"{Fore.YELLOW}Congrats baller you bought the mansion!!!")
            bank = bank - 500000
        else:
            print(Fore.RED + "You do not have enough money!")
    return pickaxe


def orePercentage(gold, silver, bronze):
    """
    Determines the chances of mining ores based off of the pickaxe level
    gold gives 1000, silver gives 500, bronze gives 250
    """
    from random import randint
    global bank

    r = randint(0, 100)

    if r >= gold:
        print(f"You got {Fore.YELLOW}gold")
        print(f"{Fore.GREEN}+ $1000")
        bank += 1000
    elif r >= silver:
        print(f"You got {Fore.LIGHTWHITE_EX}silver")
        print(f"{Fore.GREEN}+ $500")
        bank += 500
    elif r >= bronze:
        print(f"You got  {Fore.RED}bronze")
        print(f"{Fore.GREEN}+ $250")
        bank += 250
    return bank


def mine():
    """
    calls ore percentage function depending on the pickaxe level, changing the parameters
    :return:
    """
    global pickaxe
    mine = input(f"Do you want to mine? ({Fore.GREEN}Y{Fore.RESET}/{Fore.RED}N{Fore.RESET})").lower()
    if mine == "y":
        if pickaxe == 1:
            orePercentage(95, 60, 0)
        if pickaxe == 2:
            orePercentage(80, 45, 0)
        if pickaxe == 3:
            orePercentage(65, 30, 0)
        if pickaxe == 4:
            orePercentage(50, 15, 0)
        if pickaxe == 5:
            orePercentage(35, 5, 0)
    else:
        wantToShop = input(f'Do you want to shop? ({Fore.GREEN}Y{Fore.RESET}/{Fore.RED}N{Fore.RESET})').lower()
        if wantToShop == "y":
            shop()
        else:
            return


while True:
    print(f"\nYour Pickaxe is LVL {pickaxe}")
    print(f"You have {Fore.GREEN}${bank}{Fore.RESET} in your bank account")
    mine()

# shop is an area where players can buy different pickaxes
# so the chance of getting better ores increases
#
# the first pickaxe is free
# the second pickaxe costs 1000
# the third pickaxe costs 2500
# the fourth pickaxe costs 5000
# the fifth pickaxe costs 10000
#
# the pickaxe starts at 1 and the player will have the
# option to buy a different pickaxe at anypoint
# when that happens we have to change the value of pickaxe
# to correspond so that the orePercentage function will
# give accurate amounts of ore depending on the pickaxe
