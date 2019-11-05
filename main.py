import time
import random
from os import system, name
from SystemConfiguration import SCDynamicStoreCopyConsoleUser
import sys

username = (SCDynamicStoreCopyConsoleUser(None, None, None) or [None])[0]
username = [username,""][username in [u"loginwindow", None, u""]]

ip1 = random.randint(0, 255)
ip2 = random.randint(0, 255)
ip3 = random.randint(0, 255)
ip4 = random.randint(0, 255)
ip = f"{ip1}.{ip2}.{ip3}.{ip4}"

version = "0.1.1"
print(f"Hello, {username}")
print(f"SERIAL ACCESS BUS v{version}") # This makes it look more legit
print("WARNING!\nUNAUTHORIZED ACCESS IS STRICTLY PROHIBITED!\
      \nACCESS WITHOUT PERMISSION MAY RESULT IN CRIMINAL PERSECUTION.\
      \nPROCEED WITH CAUTION.")

target = input("Target to attack: ")
print(f"ESTABLISHING CONNECTION TO {ip} ({target})")
print() # Blank line

def clear_screen():
    if name == "nt": # This is Windows
        _ = system('cls') # Much simpler. The underscore is to prevent it printing a random 0 to the screen
    else: #Literally everything else
        _ = system('clear')

n = 0
while n <= 100:
        print(f"Breaching fire wall... {n}%", end="\r")
        n += 5
        time.sleep(1)
print()
print("Firewall breached")
print(f"Successfully accessed {target}")

while True:

    userinput = input("What would you like to do? : ")
    if userinput == "transfer money":
        progress = 0
        while progress <= 100:
            if progress == 100:
                print(f"Transferred 56743873 to {username}'s bank.")
                break
            else:
                print("transferring... {}".format(progress))
                progress += 20
                time.sleep(1)
    elif userinput == "download sensitive files":
        m = 0
        while m <= 100:
            if m == 100:
                print(f"Downloaded files to User/{username}/Documents/hidden_files/stolenFiles")
                break
            else:
                print("Downloading sensitive files... {}".format(m))
                m += 10
                time.sleep(0.5)
    elif userinput == "end":
        clear_screen()
        break
    else:
        print("Invalid input")
