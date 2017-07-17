#!/usr/bin/env python

# |---------------------------------------------|
# |           Welcome to "Server-Spy"           |
# |---------------------------------------------|
# |   This is for finding out where attackers   |
# |   are trying to bruteforce or just simply   |
# |   trying to attack your server. If you're   |
# |   intrested in a version two show support   |
# |---------------------------------------------|
# |             Normal execution                |
# |---------------------------------------------|
# |           python Server-Spy.py              |
# |---------------------------------------------|
# |---------------------------------------------|
# |  Note: This has only been tested on CentOS  |
# |---------------------------------------------|

banner='''
 __                               __             
/ _\ ___ _ ____   _____ _ __     / _\_ __  _   _ 
\ \ / _ \  __\ \ / / _ \  __|____\ \|  _ \| | | |
_\ \  __/ |   \   /  __/ | |_____|\ \ |_) | |_| |
\__/\___|_|    \_/ \___|_|       \__/  __/ \__  |
                                    |_|    |___/ '''

import time, sys, os

print "\x1b[31m|---------------------------------------------|\x1b[0m"
print "\x1b[31m|           Welcome to 'Server-Spy'           |\x1b[0m"
print "\x1b[31m|---------------------------------------------|\x1b[0m"
print "\x1b[31m|   This is for finding out where attackers   |\x1b[0m"
print "\x1b[31m|   are trying to bruteforce or just simply   |\x1b[0m"
print "\x1b[31m|   trying to attack your server. If you're   |\x1b[0m"
print "\x1b[31m|   interested in a version two show support  |\x1b[0m"
print "\x1b[31m|---------------------------------------------|\x1b[0m"
print "\x1b[31m|             D I S C L A I M E R             |\x1b[0m"
print "\x1b[31m|---------------------------------------------|\x1b[0m"
print "\x1b[31m|   Please keep eyes on the screen and read   |\x1b[0m"
print "\x1b[31m|   everything that's displayed for infosec   |\x1b[0m"
print "\x1b[31m|   on your security system!                  |\x1b[0m"
print "\x1b[31m|---------------------------------------------|\x1b[0m"
time.sleep(6)

print banner
os.system('who')
print "|-----------------------------------------------------------------------------|"
print "\x1b[31m If you see more than one login then your server has someone else logged in\x1b[0m"
print "|-----------------------------------------------------------------------------|"
time.sleep(6)



print banner
os.system('users')
print "|-----------------------------------------------------------------------------|"
print "\x1b[31m If you see more than one root ID then someone else is logged in\x1b[0m"
print "|-----------------------------------------------------------------------------|"
time.sleep(6)



print banner
os.system('whoami')
print "|-----------------------------------------------------------------------------|"
print "\x1b[31m This is the ID of your username connected\x1b[0m"
print "|-----------------------------------------------------------------------------|"
time.sleep(6)



print banner
print "|-----------------------------------------------------------------------------|"
print "\x1b[31m ! THIS WILL TAKE A FEW MINUTES TO CAT THE SECURE.LOG ! \x1b[0m"
print "|-----------------------------------------------------------------------------|"
time.sleep(10)
os.system('cat /var/log/secure')
print "|-----------------------------------------------------------------------------|"
print "\x1b[31m Look through and you can find failed login attempts \x1b[0m"
print "|-----------------------------------------------------------------------------|"
time.sleep(6)



print banner
print "|-----------------------------------------------------------------------------|"
print "\x1b[31m ! THIS WILL TAKE A FEW MINUTES TO CAT THE MESSAGES.LOG ! \x1b[0m"
print "|-----------------------------------------------------------------------------|"
time.sleep(10)
os.system('cat /var/log/messages')
print "|-----------------------------------------------------------------------------|"
print "\x1b[31m You can see new modules installed and new sessions of root \x1b[0m"
print "|-----------------------------------------------------------------------------|"
time.sleep(6)



print banner
print "|-----------------------------------------------------------------------------|"
print "\x1b[31m ! THIS WILL TAKE A FEW MINUTES TO CAT THE BASH_HISTORY ! \x1b[0m"
print "|-----------------------------------------------------------------------------|"
time.sleep(10)
os.system('cat .bash_history')
print "|-----------------------------------------------------------------------------|"
print "\x1b[31m Check and see if you see any commands outputted that wasn't you \x1b[0m"
print "|-----------------------------------------------------------------------------|"
time.sleep(6)



print banner
print "|-----------------------------------------------------------------------------|"
print "\x1b[31m Lets find out how many failed login attempts there is \x1b[0m"
print "|-----------------------------------------------------------------------------|"
time.sleep(6)
os.system('grep "authentication failure" /var/log/secure')
print "|-----------------------------------------------------------------------------|"
print "\x1b[31m This will show all failure authentication attempts in SSH  \x1b[0m"
print "|-----------------------------------------------------------------------------|"
time.sleep(6)




print banner
print "|-----------------------------------------------------------------------------|"
print "\x1b[31m Lets find out how many successful login attempts there is \x1b[0m"
print "|-----------------------------------------------------------------------------|"
time.sleep(6)
os.system('cat /var/log/secure | grep sshd.*opened')
print "|-----------------------------------------------------------------------------|"
print "\x1b[31m This will show all successful authentication in SSH  \x1b[0m"
print "|-----------------------------------------------------------------------------|"
time.sleep(6)



print "\x1b[31m  ______ _       _     _              _ \x1b[0m"
print "\x1b[31m |  ____(_)     (_)   | |            | |\x1b[0m"
print "\x1b[31m | |__   _ _ __  _ ___| |__   ___  __| |\x1b[0m"
print "\x1b[31m |  __| | |  _ \| / __|  _ \ / _ \/ _  |\x1b[0m"
print "\x1b[31m | |    | | | | | \__ \ | | |  __/ (_| |\x1b[0m"
print "\x1b[31m |_|    |_|_| |_|_|___/_| |_|\___|\____|\x1b[0m"
time.sleep(6)
print "|-----------------------------------------------------------------------------|"
print "\x1b[31m              Thank you for using Server-Spy  \x1b[0m"
print "|-----------------------------------------------------------------------------|"
print "|        All credits goes to Chris Poole | @codingplanets via Twitter         |"
print "|-----------------------------------------------------------------------------|"
print "|                  Any bugs? Report them to me via Twitter!                   |"
print "|                https://github.com/codingplanets/Server-Spy                  |"
print "|-----------------------------------------------------------------------------|"
print "|-----------------------------------------------------------------------------|"
