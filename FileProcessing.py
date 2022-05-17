'''
Benjamin Dominguez
Bellevue University
CIS 245
05/16/22
Your program this week will use the OS library in order to validate that a directory exists before creating a file in that directory.
Your program will prompt the user for the directory they would like to save the file in as well as the name of the file. 
The program should then prompt the user for their name, address, and phone number. 
Your program will write this data to a comma separated line in a file and store the file in the directory specified by the user. 
'''
import os
directory = input("What directory do you want to store your info in?")
d_check = os.path.exists(directory)
if d_check == True:
    print("Directory found")
else:
    print("Directory not found")
name = input("What's your name?")
address = input("What's your address?")
phone = input("What's your phone number?")
try:
    filename = 'Userinfo.txt'
    with open(filename,'a') as file_object:
        file_object.write(f"{name},{address},{phone},")
    with open(filename) as file_object:
        users = file_object.readlines()
    for user in users:
        print(users)
        break
except IOError:
    print("No file found.")