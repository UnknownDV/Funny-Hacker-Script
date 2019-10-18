import time, platform, subprocess

database = input("What database would you like to access? : ")

n = 0

while n <= 100:
    if n == 100:
        print("You've broken into {}".format(database))
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
                    print("Downloaded files to User/21rcrank/user/Documents/hidden_files/stolenFiles")
                    break
                else:
                    print("Downloading sensitive files... {}".format(m))
                    m += 10
                    time.sleep(0.5)
        elif userinput == "end":
            if platform.system()=="Windows":
                subprocess.Popen("cls", shell=True).communicate() #I like to use this instead of subprocess.call since for multi-word commands you can just type it out, granted this is just cls and subprocess.call should work fine
            else: #Linux and Mac
                print("\033c", end="")
            break
        else:
            print("Invalid input")
        #break
    else:
        print("hacking {}... {}".format(database, n))
        n += 10
        time.sleep(1)
