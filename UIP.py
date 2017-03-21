import googleMaps as gm
import processModule as pm
import encurtador as e
import webbrowser as w
import os
import time

#This is the user interface program, and it's made by Henrique Almeida Marcomini
#The idea of this module is to provide a hook to whatever module its attached on

auxAddressArray = []

def menu():
    #include a console cleaner here later
    print("PLEASE THE MENU BELOW =)")
    print("1 - To insert a new address")
    print("2 - To remove a address")
    print("3 - To see all addres")
    print("4 - To calculate the route")
    print("0 - To leave")
    return int(raw_input()) #use input() for python 3

def addAddress():
    print("Enter the desired address : ")
    address = raw_input()
    res = gm.validate(address)
    if res != "DeuRuim":
        auxAddressArray.append(res)
        print("Good, I found it and added -",res)
    else:
        print("Sorry, could not locate the address")
    time.sleep(1)

def seeAddress():
    for i in range(len(auxAddressArray)):
        print (i,"-",auxAddressArray[i])

def delAddress():
    seeAddress()
    print("Which one you would like to delete (input just the number)")
    index = int(raw_input())
    if index<len(auxAddressArray) :
        print ("Deleting index", index)
        del auxAddressArray[index]


def calculate():
    print("Doing my math")
    magic = gm.kComplete(auxAddressArray)
    Rlist = pm.nearestPoint(magic)
    for i in range(len(Rlist)):
        Rlist[i] = magic["code"][Rlist[i]]
    url = "https://www.google.com.br/maps/dir/"
    for i in Rlist:
        url +=i.replace(" ","+")+"/"
    print "view "+e.code(url)["id"]
    w.open(url,new=2)
    raw_input()


#First of all we must greet the user
print("Hello folk, thank you for preference")
choice = 5
while choice != 0:
    choice =  menu()
    if choice == 1:
        addAddress()
    elif choice == 2:
        delAddress()
    elif choice == 3:
        seeAddress()
        time.sleep(5)
    elif choice == 4:
        calculate()
    elif choice != 0:
        print("This choice does no exist")
    os.system('cls' if os.name=='nt' else 'clear')