import random

print('How many times do you want to roll? ') #Asking number of rolls
numberRolls = input() #USER IMPUT

print('How sides are on your dice? ') #Asking sides of dice
numberSides = input() #USER IMPUT

for rolls in range (int(numberRolls)):  #times dice rolled USING FOR
    randomDice = random.randrange(int(numberSides))+1  #defining the dice with sides
    print(randomDice)

    if randomDice == int(numberSides): #checking for crit USING IF
        print('critical hit!')

    elif randomDice==1: #checking for crit failure USING ELIF
        print('critical failure!')
        
print('program is done running. hope you liked your rolls')

# SOURCES:
# https://www.w3schools.com/python/ref_func_input.asp
# https://www.geeksforgeeks.org/how-to-take-integer-input-in-python/
# https://github.com/dotcoda/diceRoll
