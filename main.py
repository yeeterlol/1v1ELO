import requests
import colorama 
import json
import time
import random
from time import sleep
from colorama import init, Fore 
from os import system, name
quotes = ["Boost your elo with 1v1Elo!", "If you need help, go to the 1v1Elo github and submit a issue at https://github.com/yeeterlol/1v1Elo/issues", "Gain unlimited elo today!", "Nice little easter egg :)", "Boost your 1v1.lol Elo!", "If you bought this, you got scammed. Sorry to say it!", "10/10 coding moment", "You might get rate limited so try again later! :)", "fortnite balls", "You are logged in as User, UID 1", "For unlimited elo no rate limited, type 2!!!!"]

init(autoreset=True)
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
    
try:
    config = json.load(open('config.json'))
except:
    print(f'{Fore.RED}Adding config.json!')
    with open("config.json", "a") as file:
      file.write("""
{
 "token": "INSERT-TOKEN" 
}
                """)
    exit()

check = config["token"]

if check == "INSERT-TOKEN":
    print(f'{Fore.RED}Please put your token in config.json!')
    exit()
else:
    pass

def main():
  print(Fore.RED + """
 ██╗██╗   ██╗ ██╗███████╗██╗      ██████╗ 
███║██║   ██║███║██╔════╝██║     ██╔═══██╗
╚██║██║   ██║╚██║█████╗  ██║     ██║   ██║
 ██║╚██╗ ██╔╝ ██║██╔══╝  ██║     ██║   ██║
 ██║ ╚████╔╝  ██║███████╗███████╗╚██████╔╝
 ╚═╝  ╚═══╝   ╚═╝╚══════╝╚══════╝ ╚═════╝
""")
  print(Fore.RED + random.choice(quotes))
  print(Fore.BLUE + "1) Boost")
  print(Fore.BLUE + "2) Exit")
  choice = input("> ")
  if choice == "1":
    clear()
    elo()
  elif choice == "2":
    leave()
  else: 
    print(Fore.BLUE + "You didn't insert something or it wasn't correct")
    time.sleep(1)
    clear() 
    main()

def elo():
  print(Fore.RED + "Thank you using 1v1ELO! I hope you enjoy our program :)")
  while True: 
    headers = {
      "accept": "*/*",
      "accept-language": "en-US,en;q=0.9",
      "auth-token": check,
      "cache-control": "no-cache",
      "content-type": "application/x-www-form-urlencoded",
      "firebase-config-ids": "{\"BattlePassID\":\"BPS2\",\"GameEventsID\":\"default\",\"DailyRewardsID\":\"default\",\"GameModesID\":\"default\",\"StoreSettingsID\":\"default\",\"ProductsID\":\"default\",\"GeneralConfigID\":\"default\",\"ChallengesID\":\"default\"}",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "sec-gpc": "1"
    }
    r = requests.get("https://us-central1-justbuild-cdb86.cloudfunctions.net/player/updateProgressAndStats?gameMode=1v1_Competitive&matchResult=win&killsCount=1&deathsCount=0&isCompetitive=true&rankType=0&battlePassId=BPS2", headers=headers)
    j = r.json()
    r = j["CustomRating"]
    print(Fore.RED + f"Your elo: {r}")
    time.sleep(5)
    
  
def leave():
  print(Fore.RED + "Goodbye!")
  exit()

main()
