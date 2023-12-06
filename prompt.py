import time
import os
import sys

def prompt():
    print("---------------------------------------")
    print("""

⠀⠀⣴⣏⡦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⡇⠀⠀⢬⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠘⣇⠀⠀⠀⠱⣌⣁⡉⠲⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣹⣧⠀⠀⠀⢿⡀⠉⠂⣙⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠘⢤⡉⡀⠀⠀⢈⢻⣿⣆⠸⢾⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⢻⡄⠀⣾⠀⢧⡙⣇⠈⣿⣿⣿⣿⠿⠃⠀⠀⠀⠀
⠀⠀⠀⠠⣾⢿⠾⢻⣇⡆⣿⣎⡴⣿⡄⢻⣷⡦⠤⠀⠀⠀⠀
⠀⠀⣐⣺⣿⣾⠇⠈⠻⡇⢸⡿⢿⣿⢱⠀⠉⠛⢿⠃⠀⠀⠀
⠠⢤⣴⣿⣿⠟⠀⢠⠀⠈⡛⢣⠀⠃⢸⣷⡄⠰⣏⠀⠀⠀⠀
⠐⠦⢶⣖⣢⠤⣴⡿⢀⣾⣵⣞⠀⢦⠀⢳⣽⡀⢹⣷⣶⠄⠀
⠀⠠⣿⢋⣴⠟⢟⣱⣿⣿⣿⡏⠀⣼⣆⣿⡿⠧⠾⣿⣯⣤⠄
⠀⠴⠛⣿⠇⣴⠏⣼⣿⣿⣿⣧⣿⣿⣟⣅⣀⣌⠷⠿⢿⡂⠀
⠀⠀⠀⠧⠚⠉⠀⠏⢻⣿⢿⣿⣿⣿⣿⣿⣿⡿⣷⠦⠤⠝⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠀⠙⣎⠹⣿⣿⠙⢧⡘⡷⠂⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢀⣿⠏⠀⠀⢰⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀
         「Lupus Hound」

        """)
    print("---------------------------------------")
    print("""   
    input: 
                 play 
                 credits 
                 exit     
                 
                 """) 
    print("---------------------------------------")
    option = ""
    while option not in ['play', 'credits', 'exit']: 
        option = input("> ").lower()
        if option == 'play':
            introduction()
        elif option == 'credits':
            print("""  

            Created by: 
                  Gian Cyrus F. Salvador
                  Fredmar Declas
                  Doniele Arys Antonio
                  Claudio Van Likigan
                    
                     """)
            input("Enter to continue")
            os.system("cls")
            prompt()

        elif option == 'exit':
            sys.exit()
        else:
            print("Please input valid command('start' or 'quit')")
            
def introduction():
    print("-----------------------------------------------")
    print("             Journey has begun.                ")
    print("-----------------------------------------------")
    press_any_key_to_continue
    os.system('cls')
 
    introduction = """From where the world suffered from the All-Fathering, To where the cities bleak in fear with no restraint from the demon lord. One must understand that the journey you will venture will not leave you in a satisfactory path but rather a harsh place to be in. Venture the misty forests and avoid the hallucinations that you will seek in between try and conquer to achieve victory to your already fallen lands by the hands of the demon lord. This is a place where death is a satisfactory ending for everyone, rather live in time as a survivor, or live in the wretched place as a corpse."""

    print_text_slowly(introduction)
    press_any_key_to_continue()
    os.system('cls')

    character_name = input(print_text_slowly("What is your characters name:"))
    print_text_slowly(f"Now {character_name}!, read carefully in your journey.")
    press_any_key_to_continue()
    os.system('cls')

    instructions = f"""You will enter the misty forests of the All-Fathering, You shall venture the forests and reach him to where he lies dormant. unmoving and Unchanging. Till the both of you meet you will be bewildered crossing treacherous landscapes and encounter enigmatic creatures. Collect the 3 Treasures that enchain the 'LUPUS HOUND' in order to summon it in your area and where you eradicate it with the Royal Treasure given to you that only enlightens when you are fighting the true enemy. """
    print_text_slowly(instructions)
    press_any_key_to_continue()
    os.system('cls')

def print_text_slowly(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    return "> "

def press_any_key_to_continue():
    input("Press Enter to continue...")