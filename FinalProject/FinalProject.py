#Michael Lopez
#SE126 
#Final Project Build - Game of Thrones Cast Database

#PROGRAM PROMPT
#=----------------------------------------=


#INTIALIZATION
#=----------------------------------------=
import csv
import sys
from os import system, name 
from time import sleep 
records = 0

#VARIABLE DICTIONARY
#=----------------------------------------=
#answer    =     condition for loop
#records   =     records count
#file      =     csvfile friendly name


#LIST PREP
#=----------------------------------------=
actorName = []
actorBirthday = []
showName = []


#FUNCTIONS
#=----------------------------------------=
def clear(): #CLEAR SCREEN FUNCTION
        
        if name == 'nt':
            _= system('cls')
        else:
            _=system('clear')

def menu(): #MENU FUNCTION       
    print("\t\t\tMAIN MENU")
    print("\t\t\n=-----------------------------------------------------------------------------------------------------------=")
    print("\t\t\t1. Search by Character Name")
    print("\t\t\t2. Search by Actor or Actress")
    print("\t\t\t3. Exit")
    response = int(input("Please enter your choice [1 - 3]: "))
    while response != 1 and response != 2 and response != 3:

        print("*ERROR*ERROR*")
        response = int(input("Please enter your choice [1 - 3]: "))

    return response

def swap(listname, index): #BUBBLE SORTING FUNCTION
    t = listname[index]
    listname[index] = listname[index + 1]
    listname[index + 1] = t

def askAgainFunction(): #ALLOWING THE USER TO BE ABLE TO SEARCH AS MANY TIMES AS THEY WANT
    
    ans = input("\n\n\t\t\tEnter Y to search another actor or character: ") 
    ans = ans.upper() 
    
    while ans != "Y" and ans != "N":
        
        print("\t\t\t\t**ERROR**")
        ans = input("\t\t\tEnter Y to search another actor or character: ")
        ans = ans.upper()

    return ans

#CONNECT TO FILE
#=----------------------------------------=
with open("C:/Users/Michael/OneDrive - New England Institute of Technology/Desktop/NEIT SE126 - Python II/FinalProject/finalProject.txt") as csvfile: #*--Insert txt file path there...-=
    
    file = csv.reader(csvfile)
    for rec in file:
        records += 1
        #print(rec) #<-- TEST
        #STORING DATA INTO LISTS
        actorName.append(rec[0])
        actorBirthday.append(rec[1])
        showName.append(rec[2])

#DISCONNECT FROM FILE
#=----------------------------------------=
print("\t\t\t***ORIGINAL FILE DATA***\n") 
print("{0:15} \t {1:10} \t {2:15}".format("ACTOR/ ACTRESS NAME", "BIRTH DATE","CHARACTER NAME")) 
print("=-----------------------------------------------------------------------------------------------------------=")
for i in range(0, records):
#ORIGINAL FILE DATA
    print("{0:15} \t {1:10} \t {2:15}".format(actorName[i],actorBirthday[i],showName[i]))

print("\n\nWelcome to my Final Project!") #SLEEP AND CLEAR SCREEN FUNCTIONS
sleep(3)
print("\t You will now be entering the program shortly..")
sleep(2)
print("\t\t Have Fun! ")
sleep(1)
clear()


for i in range(0, records - 1):
    
    for k in range(0, records - 1):
            
        if actorName[k] > actorName[k + 1]: # > Is for increasing order,  < is for decreasing

                #SWAP!
            temp = actorName[k]
            actorName[k] = actorName[k+1]
            actorName[k+1] = temp

            temp = actorBirthday[k]
            actorBirthday[k] = actorBirthday[k+1]
            actorBirthday[k+1] = temp
                
            temp = showName[k]
            showName[k] = showName[k+1]
            showName[k+1] = temp


print("\t\t\t***SORTED FILE DATA***\n") 
print("{0:15} \t {1:10} \t {2:15}".format("ACTOR/ ACTRESS NAME", "BIRTH DATE","CHARACTER NAME")) 
print("=-----------------------------------------------------------------------------------------------------------=")
for i in range(0, records):
#DISPLAYING SORTED DATA W/ BUBBLE SORT
    print("{0:15} \t {1:10} \t {2:15}".format(actorName[i],actorBirthday[i],showName[i]))

print("\n\nThis is the ORDERED list!") #SLEEP AND CLEAR SCREEN FUNCTIONS
sleep(3)
print("\t You will now be entering the program shortly...")
sleep(2)
print("\t\t Have Fun! ")
sleep(1)
clear()


answer = "y"

while answer == "y":
    
    userChoice = menu()

    if userChoice == 1:
#USER CHOICE 1 || SEARCH BY CHARACTERS NAME
        search = input("Please enter the Character's name you're searching for: ")
        found = -1
        for i in range(0,records):

            if search  == showName[i]: #FOUND
                found = i
        if found >= 0:
            print("Your Search for", search, "was found! Here's there info: ")
            print("{0:15} \t {1:10} \t {2:15}".format(actorName[i],actorBirthday[i],showName[i]))
                #askAgainFunction()
        else:
            print("Your search for", search, "was NOT FOUND!")
        askAgainFunction()
    

    elif userChoice == 2:
#USER CHOICE 2 || SEARCH BY ACTORS/ACTRESS NAME
        search = input("Please enter the Actor/Actress name you're searching for: ")
        found = -1
        for i in range(0,records):

            if search  == actorName: #FOUND
                found = i
        if found >= 0:
            print("Your Search for", search, "was found! Here's there info: ")
            print("{0:15} \t {1:10} \t {2:15}".format(actorName[i],actorBirthday[i],showName[i]))
                #askAgainFunction()
        else:
            print("Your search for", search, "was NOT FOUND!")
                #askAgainFunction()
    
    elif userChoice == 3:
#EXITING THE PROGRAM
        print("\n\tEXITING THE PROGRAM...")
        print("\t\t THANKS for using  my program! ")
        sleep(3)
        clear()


    else:
#ASK AGAIN || INCORRECT INPUT
        print("Incorrect input, please select [1 - 3]")
        askAgainFunction()

clear()
print("\n\t\t\tThanks for using my Program!")
print("\t\t\tHave a great break!")
