import typing


class Options:
    def __init__(self, name):
        self.name = name

    def run(self):
        username = (SCDynamicStoreCopyConsoleUser(None, None, None) or [None])[0]
        username = [username, ""][username in ["loginwindow", None, ""]]
        money = str(random.randint(10000000, 99999999))
        while True:

            print("Pick an option")

            for i in range(len(options)):
                print(str(i + 1) + ":", options[i])
            userinput = int(input("What would you like to do? : "))

            if userinput in range(1, 5):
                userinput = options[userinput - 1]
            else:
                print("Invalid input!")
            if userinput == "Transfer Money":
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
                        print(
                            f"Downloaded files to User/{username}/Documents/hidden_files/stolenFiles"
                        )
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

    def __str__(self):
        return self.name
