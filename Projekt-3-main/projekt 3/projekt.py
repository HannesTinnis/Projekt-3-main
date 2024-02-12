#Projekt 3 - Sten-Sax-Påse

__Author__ = "Hannes"
__version__ = "1.0.0"
__email__ = "hannes.tinnis@elev.ga.ntig.se"


import random
import os
from time import sleep
from colors import bcolors
os.system("cls")
print(bcolors.BOLD+"""
██████╗ ██████╗ ███████╗
██╔══██╗██╔══██╗██╔════╝
██████╔╝██████╔╝███████╗
██╔══██╗██╔═══╝ ╚════██║
██║  ██║██║     ███████║
╚═╝  ╚═╝╚═╝     ╚══════╝""")


while True:

    def user():
        user_choice = input("Välj sten, sax eller påse: ").lower()
        while user_choice not in ['sten', 'sax', 'påse', "exit"]:
            print("Ogiltigt val. Försök igen.")
            user_choice = input("Välj sten, sax eller påse: ").lower()
        return user_choice

    def get_computer_choice():
        return random.choice(['sten', 'sax', 'påse'])

    def result(user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Det blev lika!"
        elif (user_choice == 'sten' and computer_choice == 'sax') or \
             (user_choice == 'sax' and computer_choice == 'påse') or \
             (user_choice == 'påse' and computer_choice == 'sten'):
            return "Grattis! Du vinner!"
        else:
            return "Tyvärr, datorn vinner!"

    def main():
        print("Välkommen till sten, sax, påse!")
        while True:
            user_choice = user()
            computer_choice = get_computer_choice()
            print(f"Datorn valde: {computer_choice}")
            print(result(user_choice, computer_choice))
            if user_choice == "exit":
                print ("tack för att du spelade!")
                sleep(1)
                exit()
            

    if __name__ == "__main__":
        main()








