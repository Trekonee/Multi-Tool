import os
import webbrowser
from colorama import init, Fore, Style
import requests
import time
from nitro import nitro
from phonedork import phonedork, display_phone_dorks
from maildork import maildork, display_dorks
from googledork import google_dorks
from link import generate_links, display_links
from clear import clear_screen
from changename import trek, nitrogx, phone, mail, Pseudo


def main():
    init(autoreset=True) 

    while True:
        clear_screen()
        print(f"{Fore.YELLOW}Options:{Style.RESET_ALL}")
        print("[1] -Pseudo")
        print("[2] -Phone")
        print("[3] -Mail")
        print("[4] -DataBase")
        print("[5] -Nitro GX Codes")
        print("[6] -Exit")

        choice = input(f"{Fore.RED}[#TREKONEE#] Select an option : {Style.RESET_ALL}")

        if choice == '1':
            Pseudo()
            username = input("[#TREKONEE#] Enter username : ")
            links = generate_links(username)
            display_links(links)

            save_option = input("[#TREKONEE#] Do you want to save the information in a file (Y/N) : ").lower()
            
            if save_option == 'o':

                filename = input("[#TREKONEE#] Enter the name of the file to save the information (default: 'Pseudo_Osint.txt'): ") or 'Pseudo_Osint.txt'

                with open(filename+".txt", 'a+') as file:
                    file.write(f'\n\nNew search! \nUsername:: {username}\nLinks : {links}')
                    print(f"The information has been saved in '{filename}'.")
            elif save_option == 'n':
                print("The information has not been saved.")
            else:
                print("Invalid option. The information has not been saved.")
            
            input("Press Enter to return to the menu...")

        elif choice == '2':
            phone()
            username = input("Enter the phone number : ")
            phone()
            phone_dorks = phonedork(username)
            display_phone_dorks(phone_dorks)
            input("[#TREKONEE#] Press Enter to return to the menu...")
  
            
        elif choice == '3':
            mail()
            email = input("Enter email address : ")
            mail()
            # Vérification de l'adresse e-mail
            dorks = maildork(email)
            display_dorks(dorks)
            input("[#TREKONEE#] Press Enter to return to the menu...")
            mail()
            dorks = maildork(username)
            display_dorks(dorks)

        elif choice == '4':
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

        elif choice == '5':
            nitrogx()
            nitro()

        elif choice == '6':
            print("Even if you leave this program, I'll always be in your nightmares...")
            time.sleep(2)
            clear_screen()
            break
        else:
            print(f"{Fore.RED}Learn to read and I will destroy your life :{Style.RESET_ALL}")

if __name__ == "__main__":
    main()