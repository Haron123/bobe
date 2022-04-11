import os
import re
import time
import random
import getpass
import datetime
from colorama import Fore, Back, Style


# Nothing
def nothing():
    nothing = 1

def bobe():
    with open('owords.txt', 'r') as owords:
        owordslist = owords.readlines()

    with open('bwords.txt', 'r') as bwords:
        bwordslist = bwords.readlines()


    startmsg = bwordslist[random.randrange(0,535)] + ' ' + owordslist[random.randrange(0,226)] + ' ' + bwordslist[random.randrange(0,535)]         
    startmsg = startmsg + " Encryption" 
    startmsg = startmsg.replace('\r', '').replace('\n', '')
    return startmsg
    



# Start code and Selection
def start():
    
    os.system('clear')
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT   + bobe() + " Started...")
    print("[1] Encrypting                               ")
    print("[2] Decrypting                               ")
    print("[3] Misc                                     ")
    print(Style.RESET_ALL)
    Selection = input(Fore.LIGHTYELLOW_EX + Style.BRIGHT)
    if Selection == "1":
        encrypt()
    elif Selection == "2":
        decrypt()   
    elif Selection == "3":
        misc()    
    


# Encrypt with parameters
def encrypt():
    # Gets current date and time in a Path friendly way
    date_time = (str(datetime.datetime.now()))
    cleandatetime = re.sub('[\W\_]', "-", date_time)
    # Gets current path
    path = os.getcwd()

    # User questions
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "Working Directory: " + path)
    print("Enter File Directory: ")
    file = input(Fore.LIGHTYELLOW_EX + Style.BRIGHT)
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "Enter Password: ")
    password = input(Fore.LIGHTYELLOW_EX + Style.BRIGHT)
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "Should the Backup have a Specific Name? [Leave empty if Name should just be the Default, If name already exists it gets deleted]: ")
    name = input(Fore.LIGHTYELLOW_EX + Style.BRIGHT)
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "Destination Folder/Directory [Leave empty if Destination should just be the Default, Default is Working Directory]: ")
    destination = input(Fore.LIGHTYELLOW_EX + Style.BRIGHT)



    #Clear out ' and spaces at the start and end if existing
    while file.endswith(" ") or file.endswith("'"):
        file = file[:-1]    

    while file.startswith(" ") or file.startswith("'"):
        file = file[1:]    
        
    

    # Compressing File
    backupfile = path + '/Backup' + cleandatetime + '.zip'
    print(backupfile)

    os.system("zip -r '" + backupfile + "' '" + file + "'")
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Succesfully Compressed")
  

    #Renaming Encrypted File if wanted
    if not name:
        nothing()       
    else:
        os.rename(os.path.basename(os.path.normpath(backupfile)), "'" + name + ".zip'")
        backupfile = path + "'/" + name + ".zip'"

    
    
    
    #Encrypting File and Changing Directory
    os.system('echo ' + str (password) + ' | gpg -c --batch --yes --passphrase-fd 0 "' + backupfile + '"')
    print("Sucessfully Encrypted")
    os.system('rm -rf "' + backupfile + '"')
    print("Succesfully deleted Temporary Files")
    print("Backup file created at: " + backupfile + '.gpg')
    # Changing Destination Directory
    if not destination:
       # os.system('mv '+ backupfile +'.gpg /tmp/' + os.path.basename(os.path.normpath(backupfile + '.gpg')))
       nothing()
    else:
        os.system('mv '+ backupfile +'.gpg /' + destination + '/' + os.path.basename(os.path.normpath(backupfile + '.gpg'))) 

    print("Closing Script and Cleaning Console")
    print(Style.RESET_ALL)
    time.sleep(1)


def decrypt():
     # Gets current date and time in a Path friendly way
    date_time = (str(datetime.datetime.now()))
    cleandatetime = re.sub('[\W\_]', "-", date_time)
    # Gets current path
    path = os.getcwd()

    # User questions
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "Working Directory: " + path)
    print("Enter File Directory: ")
    file = input(Fore.LIGHTYELLOW_EX + Style.BRIGHT)
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "Enter Password: ")
    password = input(Fore.LIGHTYELLOW_EX + Style.BRIGHT)
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "Destination Folder/Directory [Leave empty if Destination should just be the Default, Default is Working Directory]: ")
    destination = input(Fore.LIGHTYELLOW_EX + Style.BRIGHT)
  
    


        #Clear out ' at the start and end if existing
    while file.endswith(" ") or file.endswith("'"):
        file = file[:-1]    

    while file.startswith(" ") or file.startswith("'"):
        file = file[1:]  

    newfile = os.path.splitext(file)[0]  

    os.system("echo " + str (password) + " | gpg -d --batch --yes --passphrase-fd 0 '" + file + "' > " + os.path.splitext(file)[0])

    if not destination:
        nothing() 
    else:
        os.system("mv '" + newfile + "' " + destination) 

    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Successfully decrypted")
    print("Successfully moved to Destination")
    print("Closing Script and Cleaning Console")  
    print(Style.RESET_ALL)
    time.sleep(1) 



def misc():
    # Stuff for when im out of ideas and add random bullshit
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "[1] Whats Bobe?                              ")
    print("[2] What does Bobe mean?                     ")
    print("[3] Whats Bobe for?                          ")
    print(Style.RESET_ALL)
    Selection = input(Fore.LIGHTYELLOW_EX + Style.BRIGHT)
    if Selection == "1":
        print("Bobe is a Simple tool to encrypt and decrypt files with gpg")
        
    elif Selection == "2":
        print("Bobe can mean anything, Best or Better Encryption, Bad or Badder Encryption, Back on Bed Encryption")   
        
    elif Selection == "3":
        print("Bobe is Easily Accesible by everyone and helps Securing your Files against anyone")   
    start() 
        


start()












 