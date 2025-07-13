import time
from colorama import Fore
import os
import pyperclip

def Greet():
    print(r"__   ______  _____    ______                                 _             ")
    print(r"\ \ / / __ \|  __ \  |  ____|                           | | (_)            ")
    print(r" \ V / |  | | |__) | | |__   _ __   ___ _ __ _   _ _ __ | |_ _  ___  _ __  ")
    print(r"  > <| |  | |  _  /  |  __| | '_ \ / __| '__| | | | '_ \| __| |/ _ \| '_ \ ")
    print(r" / . \ |__| | | \ \  | |____| | | | (__| |  | |_| | |_) | |_| | (_) | | | |")
    print(r"/_/ \_\____/|_|  \_\ |______|_| |_|\___|_|   \__, | .__/ \__|_|\___/|_| |_|")
    print(r"                                              __/ | |                      ")
    print(r"                                             |___/|_|                      ")
    print(r"")
    print(r"--------------------------------------------------------------------------------------------")
    print(Fore.RED)
    print(r" 	 _              _____      _                          __   ___      _______ ")
    print(r" 	| |            / ____|    (_)                         \ \ / | \    / /_   _|")
    print(r" 	| |__  _   _  | |     _ __ _ _ __ ___  ___  ___  _ __  \ V / \ \  / /  | |  ")
    print(r" 	| '_ \| | | | | |    | '__| | '_ ` _ \/ __|/ _ \| '_ \  > <   \ \/ /   | |  ")
    print(r" 	| |_) | |_| | | |____| |  | | | | | | \__ \ (_) | | | |/ . \   \  /   _| |_ ")
    print(r" 	|_.__/ \__, |  \_____|_|  |_|_| |_| |_|___/\___/|_| |_/_/ \_\   \/   |_____|")
    print(r" 	        __/ |                                                               ")
    print(r" 	       |___/                                     			                ")
    print(Fore.WHITE)
    print("Select Categories: \nA.Set Data \nB.Encrypt \nC.Decrypt \nD.Pair Keys \nE.Info \nF.Reset \nG.Check Data \nH.Exit")

class Cryption:
    def __init__(self, plainText="", key="", chiperText=""):
        self.plainText = plainText
        self.key = key
        self.chiperText = chiperText
        self.warning = "Text and plainText must have a same Length"

    def Encryption(self):
        if len(self.key) != len(self.plainText):
            return self.warning
        resultEncrypt = ""
        for i in range(len(self.key)):
            x = chr(ord(self.plainText[i]) ^ ord(self.key[i]))
            resultEncrypt += x
        return resultEncrypt

    def Decryption(self):
        if len(self.key) != len(self.chiperText):
            return self.warning
        resultDecrypt = ""
        for i in range(len(self.key)):
            x = chr(ord(self.chiperText[i]) ^ ord(self.key[i]))
            resultDecrypt += x
        return resultDecrypt

    def repairKeys(self):
        pairKeysResult = ""
        if len(self.key) != len(self.plainText):
            if len(self.key) > 0:
                for i in range(len(self.plainText)):
                    pairKeysResult += self.key[i % len(self.key)]
            else:
                print("The length of Keys and PlainText is the same")
        self.key = pairKeysResult

class selection:
    def OptionA(settings):
        Node1 = str(input("Please insert a PlainText: "))
        Node2 = str(input("Please insert a keys: "))
        Node3 = str(input("Please insert a ChiperText(Optional if you have not encrypt one): "))
        settings = Cryption(Node1, Node2, Node3)
        print(Fore.GREEN + "Successfully saved data!")
        print(Fore.WHITE, end="")
        dialog = input("Would you like to see the result?: ").lower()
        if dialog == "y":
            print("Text: " + settings.plainText)
            print("Key: " + settings.key)
        return settings

    def OptionB(settings):
        if settings is not None:
            result = settings.Encryption()
            dialog = input("Would you like to save the result?[Y/N]: ")
            print(result)
            if dialog.upper() == "Y":
                settings.chiperText = result
                print(Fore.GREEN + "Successfully saved data!")
                print(Fore.WHITE, end="")

            copy = input("Copy to clipboard? [Y/N]: ")
            if copy.upper() == "Y":
                pyperclip.copy(result)
                print(Fore.GREEN + "Copied to clipboard!")
            else:
                print(Fore.RED + "No Cipher Text copied!")
            print(Fore.WHITE, end="")

    def OptionC(settings):
        if settings is not None and settings.chiperText != "":
            result = settings.Decryption()
            print(result)

            copy = input("Copy to clipboard? [Y/N]: ")
            if copy.upper() == "Y":
                pyperclip.copy(result)
                print(Fore.GREEN + "Copied to clipboard!")
            print(Fore.WHITE, end="")
        else:
            print(Fore.RED + "No Cipher Text found!")
            print(Fore.WHITE, end="")

    def OptionD(settings):
        if settings.key != "":
            settings.repairKeys()
            dialog = input("Would you like to save the result?[Y/N]: ")
            if dialog.upper() == "Y":
                print(Fore.GREEN + "Successfully saved data!")
                print(Fore.WHITE, end="")
            elif settings.key == "":
                print(Fore.RED + "No keys found!")
                print(Fore.WHITE, end="")

    def OptionE(settings):
        print("I made this program just to test,\nhow far I have learned programming")

    def OptionF(settings):
        if settings.plainText != "" and settings.key != "":
            settings = Cryption()
            print(Fore.GREEN + "Successfully reset your data!")
        else:
            print(Fore.RED + "Your data is empty, please Set your data")
        print(Fore.WHITE, end="")
        return settings

    def OptionG(settings):
        print(Fore.YELLOW + "==[Current Data]==" + Fore.WHITE)
        print("PlainText   :", settings.plainText if settings.plainText else "(empty)")
        print("Key         :", settings.key if settings.key else "(empty)")
        print("CipherText  :", settings.chiperText if settings.chiperText else "(empty)")

    def OptionH(settings):
        t = 3
        while t > 0:
            print("Exit in " + str(t), end="\r")
            t -= 1
            time.sleep(1)
        os._exit(0)

keywords = {
    "A": selection.OptionA,
    "B": selection.OptionB,
    "C": selection.OptionC,
    "D": selection.OptionD,
    "E": selection.OptionE,
    "F": selection.OptionF,
    "G": selection.OptionG,
    "H": selection.OptionH
}

def main():
    debounce = "Y"
    settings = Cryption()

    if debounce == "Y":
        Greet()

    while debounce == "Y":
        Options = str(input("Select Category: ")).upper()
        if Options in keywords:
            result = keywords[Options](settings)
            if result is not None:
                settings = result
        else:
            print(Fore.RED + "Invalid option, please try again.")
            print(Fore.WHITE, end="")

if __name__ == "__main__":
    main()
