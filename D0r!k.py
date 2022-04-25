#!/usr/bin/env/python3
# This Python file uses the following encoding: utf-8

# ===== #
#   
# ▀█████████▄     ▄████████         
#   ███    ███   ███    ███         Author: 0x W3b Mor0ccan!
#   ███    ███   ███    █▀          GitHub: https://github.com/OxWeb4
#  ▄███▄▄▄██▀   ▄███▄▄▄             Facebook: Facebook: https://www.facebook.com/OxWeb1
# ▀▀███▀▀▀██▄  ▀▀███▀▀▀            
#   ███    ██▄   ███    █▄         
#   ███    ███   ███    ███         
# ▄█████████▀    ██████████         
#                                   
#          Dor!K_Py....!
# ===== #

# ===== #
# Created April | Copyright (c) 2020 0x W3b Mor0ccan!.
# ===== #

########################################################################

# A notice to all nerds and n00bs...
# If you will copy the developer's work it will not make you a hacker..!
# Respect all developers, we doing this because it's fun...

########################################################################


from __future__ import print_function
try:
    from googlesearch import search

except ImportError:
    print("")

import sys
import time


# Dorks Eye v1.0


if sys.version[0] in "2":
    print ("\n[x] .la sate HAdi Maktkhamche bi Python dir Python3 For Run Sat Wa chokrane \n")
    print ("\n\n\tDorks Eye \033[1;91mBsa7a Ou ra7a ......! \033[0m😃\n\n")
    exit()


class colors:
    CRED2 = "\33[91m"
    CBLUE2 = "\33[94m"
    ENDC = "\033[0m"


banner = ("""

'||''|.                   '||'  |'  _ '||''|.           
 ||   ||    ...   ... ..   || .'       ||   || .... ... 
 ||    || .|  '|.  ||' ''  ||'|.       ||...|'  '|.  |  
 ||    || ||   ||  ||      ||  ||      ||        '|.|   
.||...|'   '|..|' .||.    .||.  ||.   .||.        '|    
                                               .. |     
                                                ''  """)


for col in banner:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0025)

x = ("""
          Author: 0x W3b Mor0ccan!
          GitHub: https://github.com/OxWeb4
          Facebook: Facebook: https://www.facebook.com/OxWeb1\n """)
for col in x:
    print(colors.CBLUE2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

y = "\n\t\tHi there, Shall we play a game..? 😃\n"
for col in y:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

z = "\n"
for col in z:
    print(colors.ENDC + col, end="")
    sys.stdout.flush()
    time.sleep(0.4)


try:
    data = input("\n[+] Fine Biti T7ot Lfile Li radi Tkharj ? (Y/N) ").strip()
    l0g = ("")

except KeyboardInterrupt:
        print ("\n")
        print ("\033[1;91m[!] Sf RAhe Khrajti Khay .!\033[0")
        time.sleep(0.5)
        print ("\n\n\t\033[1;91m[!] Bsa7a Ou ra7a ......!\033[0m😃\n\n")
        time.sleep(0.5)
        sys.exit(1)


def logger(data):
    file = open((l0g) + ".txt", "a")
    file.write(str(data))
    file.write("\n")
    file.close()


if data.startswith("y" or "Y"):
    l0g = input("[~] Give The File a Name: ")
    print ("\n" + "  " + "»" * 78 + "\n")
    logger(data)
else:
    print ("[!] Tsana Wa7d 1 min...")
    print ("\n" + "  " + "»" * 78 + "\n")


def dorks():
    try:
        dork = input("\n[+] 7ot D0rk Li bari T9alb 3lih  ")
        amount = input("[+] Dkhal L3adad Dyale Les Site Li bitihom Ybano : ")
        print ("\n ")

        requ = 0
        counter = 0

        for results in search(dork, tld="com", lang="en", num=int(amount), start=0, stop=None, pause=2):
            counter = counter + 1
            print ("[+] ", counter, results)
            time.sleep(0.1)
            requ += 1
            if requ >= int(amount):
                break

            data = (counter, results)

            logger(data)
            time.sleep(0.1)

    except KeyboardInterrupt:
            print ("\n")
            print ("\033[1;91m[!] Sf RAhe Khrajti Khay .!\033[0")
            time.sleep(0.5)
            print ("\n\n\t\033[1;91m[!] Bsa7a Ou ra7a ......!\033[0m😃\n\n")
            time.sleep(0.5)
            sys.exit(1)

    print ("[•] Done... Exiting...")
    print ("\n\t\t\t\t\033[34md0r!k_Py\033[0m")
    print ("\t\t\033[1;91m[!] Bsa7a Ou ra7a ......!\033[0m😃\n\n")
    sys.exit()


# =====# Main #===== #
if __name__ == "__main__":
    dorks()
