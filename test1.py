import random
import os
os.system('cls' or 'clear')

class color : 
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHITE = '\033[0m'
javab = random.randint(1 , 15)
hads = input(color.RED + "Please enter your number :")
hads = int(hads)

while hads != javab :
    if hads > javab :
        print (color.GREEN,"The number is smaller" , '\U0001F914')
    else :
        print (color.WHITE + "The number is bigger" , '\U0001F914')
    hads = input(color.RED + "Please enter your number:")
    hads = int(hads)

print (color.WHITE +"You guessed righttt...!!!!!" , '\U0001F92A' ) 
