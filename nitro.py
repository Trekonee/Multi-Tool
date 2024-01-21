import requests as Requests
import time as Time
import subprocess as Sub
import os as OS
from colorama import init, Fore, Style
from changename import nitrogx

def nitro():

    Filed = OS.path.join(OS.path.dirname(__file__), "Codes.txt")

    Numero = int(input(f"{Fore.BLUE}Enter the number of Opera GX Nitro codes: {Style.RESET_ALL}"))
    PartnerID = str(input(f"{Fore.BLUE}Enter your Partner ID: {Style.RESET_ALL}"))
    nitrogx()
    
    name_file = input(f"{Fore.BLUE}Enter a name for the file to save the codes : {Style.RESET_ALL}")
    with open(f"{name_file}.txt", "w") as File:
        for _ in range(Numero):
            URI = "https://api.discord.gx.games/v1/direct-fulfillment"
            Data = {"partnerUserId": PartnerID}

            Resp = Requests.post(URI, json = Data)
            try:
                JSON = Resp.json()

            except Requests.exceptions.JSONDecodeError:
                print("ERROR: The server didn't return a valid JSON response. Please try again later.")
                continue

            Token = JSON.get('token', '').replace("'", "")
            File.write(f"https://discord.com/billing/partner-promotions/1180231712274387115/{Token}\n\n")

            Time.sleep(0.05)

            print(f"https://discord.com/billing/partner-promotions/1180231712274387115/{Token}")

    Time.sleep(1.5)
    Sub.Popen(["notepad.exe", f"{name_file}.txt"])

if __name__ == "__main__":
    nitro()