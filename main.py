import time
import random
from os import system, name


ips = ["128.11.234.4", "174.233.46.73", "134.76.845.9"]
ipChoice = random.choice(ips)


version = "0.1.1"
print(f"SERIAL ACCESS BUS v{version}") # This makes it look more legit
print("WARNING!\nUNAUTHORIZED ACCESS IS STRICTLY PROHIBITED!\nACCESS WITHOUT PERMISSION MAY RESULT IN CRIMINAL PERSECUTION.\nPROCEED WITH CAUTION.")

target = input("Target to attack: ")
print(f"ESTABLISHING CONNECTION TO {ipChoice} ({target})")
print() # Blank line

def clear_screen():
    if name == "nt": # This is windows
        _ = system('cls') # Much simpler. The underscore is to prevent it printing a random 0 to the screen
    else: #Linux and Mac
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
                print("Transferred 56743873 to offshores bank.")
                break
            else:
                print("transferring... {}".format(progress))
                progress += 20
                time.sleep(1)
    elif userinput == "download sensitive files":
        m = 0
        while m <= 100:
            if m == 100:
                print("Downloaded files to User/user/Documents/hidden_files/stolenFiles")
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
