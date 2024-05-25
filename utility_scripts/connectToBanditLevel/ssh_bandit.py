######################################################
#
#  *** THIS IS SCRIPT COVERED BY GPLV3 LICENSE ***
# 
# Author link: https://github.com/bandit-ita
# 
# Jay Kalt Author:    https://github.com/JayKalt
# antogit-sys Author: https://github.com/antogit-sys
#
# - - - - - - - - -
# Note: 
#
#   ~ the goal of this script is to simplify 
#   access to each bandit level, it is not 
#   intended for advanced use ~   
#
# Created in: 25/05/2024
# 
#####################################################

import os
import sys

def CLEAR(): os.system("clear")

#
#avendo passato sys.argv a argv possiamo 
#usare semplicemente argv
#
def main(argc, argv):

    # - se è presente username allora ..
    if argc == 2: #se ne ha 1(esludendo il nome del file)
        CLEAR()
        usr = argv[1] #prendo username passato da terminale

        banner("BANDIT CONNECT", usr)

        #ssh banditX@bandit.labs.overthewire.org -p 2220
        #tldr ssh
        os.system("ssh "+usr+"@bandit.labs.overthewire.org -p 2220")
    
    else: #altrimenti
        help()

################################################### 

# - banner di benvenuto per lo script
def banner(title, usr):
    #14 trattini sotto perche la stringa è di dimensione 14
    print(title)
    print("-"*len(title)) #lunghezza stringa (strlen)
    print(f"username -> {usr}") #tramite f (format) dico a python che {usr} e una varaibile
    print("domain   -> bandit.labas.overthewire.org\n")
    print("response bandit: ")

# - mostra all' utente come si usa lo script
def help():
    print("USAGE: ")
    print("\tpython3 ssh_bandit.py <username>\n")


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
