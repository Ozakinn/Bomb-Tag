# Emoji ref used: https://unicode.org/emoji/charts/emoji-list.html

import time #For countdown purposes
import os #Clears the previous battlefield
from pynput import keyboard #Handles and read the player 1 key press. Must press 'a'. Ito po ref: https://pynput.readthedocs.io/en/latest/keyboard.html
import asyncio #Create a bot that runs async. plays on its own. ref: https://www.velotio.com/engineering-blog/async-features-in-python

#This are global values which will be widely used inside the gam of every fucntions.
#This are players health.
p1HPini = 20   #Initialize and declare player 1 HP or your HP. DO NOT MODIFY PO hindi pa sya dynamic.
p2HPini = 20   #Initialize and declare player 2 HP or BOT HP. DO NOT MODIFY PO hindi pa sya dynamic.
bot_difficulty = 0 #Initialize and declare p2/BOT Difficulty.
bot_emoji = 0 #Set bot emoji based on difficulty.


#this function is where the battle happens, constantly updating based on other functions
def battlefield(p1HP, p2HP):
    p1 = "-"    #p1 = "--------------------"  Player 1 LifeLine 20HP
    p2 = "-"    #p2 = "--------------------"  Player 2 LifeLine 20HP

    os.system("cls") #CLEAR SCREEN FOR WINDOWS

    #Get bot emoji
    global bot_emoji
    
    #Initialize and declare start of looping for their lifeline/HP.
    x = 1
    y = 1

    #This is for debug purposes only. Shows players HP during the bomb tag.
    #print("P1 HP: ",p1HP,"| P2/BOT HP: ",p2HP)

    #Loop the lifeline/hp of player 1. Updates progress or the dashes.
    while x <= p1HP:
        p1 = p1 + "-"
        x+=1

    #Loop the lifeline/hp of player 2/BOT. Updates progress or the dashes.
    while y <= p2HP:
        p2 = p2 + "-"
        y+=1

    #This clears the last dashes to ensure the bomb is beside the player who lost.
    if p1HP == 0:
        p2 = p2 + "-"
        p1 = ""

    if p2HP == 0:
        p1 = p1 + "-"
        p2 = ""
        
    #This a variable that handles current progress of the battlefield.
    bomb = p1+"\U0001F4A3"+p2

    #Prints the frame of the battlefield aling with the battle in progress.
    print(" __________________________________________________")
    print("|                                                  |")
    print("|                                                  |")
    print("|                                                  |")
    print("|\U0001F464",bomb,bot_emoji+"|")
    print("|                                                  |")
    print("|                                                  |")
    print("|__________________________________________________|")

    #This prints the result of the battle.
    if p1HPini == 0:
        print("")
        print("                  You Lost! \U0001F622")
        print("")
        return False #quit the game without handling errors. let the error dont display. we just end it.
        
        
    elif p2HPini == 0:
        print("")
        print("                  You Won! \U0001F389")
        print("")
        quit() #quit the game
        
#function to run the the bot async
def starting_Bot():
    #This calls an async main function for bot.
    asyncio.run(main_bot())
    


#this function allows the game to start
def game_start():
    #the global allows us to get the latest values of p1HPini and p2HPini
    global p1HPini, p2HPini

    os.system("cls") #CLEAR SCREEN FOR WINDOWS
    battlefield(p1HPini, p2HPini) # PREVIEW OF BATTLEFIELD
    
    #Remind user that the game will start and keeping pressing 'a'
    print("")
    print("    Keeping pressing 'a' till you win!")
    print("    Game Starts in 3 secs")
    time.sleep(1)
    print("    Game Starts in 2 secs")
    time.sleep(1)
    print("    Game Starts in 1 sec")
    time.sleep(1)

    
    
    # Collect and listens to key events then runs the game as well.
    with keyboard.Listener(on_release=on_release) as listener:
        starting_Bot() #call the function to run the bot async

    #listern to the key press until no one dies.
    while p1HPini != 0 and p2HPini != 0:
        listener.start() #start listeing to key press.


    

    


#this async function create task for bot.
async def main_bot():

    #create task for bot
    task = asyncio.create_task (async_bot())
    await task
        

#this is the async fucntion for bot.
async def async_bot():

    #We call the two global values again to get the latest values.
    global p1HPini, p2HPini, bot_difficulty

    #This loops the bot to continue to fight to avoid the bomb untill ones die.
    while p1HPini != 0 and p2HPini != 0:

        #stop the loop of async botf when p1 dies/lose.
        if p1HPini == 0:
            break
        #stop the loop of async botf when p2/bot dies/lose.
        if p2HPini == 0:
            break

        #os.system("cls") #CLEAR SCREEN FOR WINDOWS
        
        #How strong the bot will be.
        #Lower means stronger bot.
        #Higher means weaker bot.
        await asyncio.sleep(bot_difficulty)

        #this condition is for safety check.
        #meaning to bot only run when no one dies yet.
        if p1HPini >= 1 and p2HPini >= 1:

            #DEBUG Purposes, check if the loops runs.
            #print("bot runs")

            #Since this function is for bot, we want to reduce P1 HP then increase P2 HP/Dashes.
            p1HPini = p1HPini - 1
            p2HPini = p2HPini + 1

            #Update the battlefield.
            #display the progress of the bomb tag.
            battlefield(p1HPini, p2HPini)
        
    
#this function only run when a key is pressed
def on_release(key):

    #We call the two global values again to get the latest values or the HP.
    global p1HPini, p2HPini

    #Accept 'a' key only for player 1.
    if key.char == ('a'):

        #this condition will avoid game resul being deleted from spamming 'a'
        if p1HPini != 0 and p2HPini != 0:
            os.system("cls") #CLEAR SCREEN FOR WINDOWS
            #DEBUG Purposes, check if the loops runs.
            #print("pressed a")
            
            #Since this function is for player 1, we want to reduce P2/BOT HP then increase P1 HP/Dashes.
            p1HPini = p1HPini + 1
            p2HPini = p2HPini - 1

            #Update the battlefield.
            #display the progress of the bomb tag.
            battlefield(p1HPini, p2HPini)

        

#this function allows the game to have different difficulty/enemy
def choose_difficulty():

    #delcare and initialize input checker for difficulty
    diffCheck = 0

    #call this global variables to dnamically change the difficulty and emoji
    global bot_difficulty, bot_emoji

    #while loop for input error checking untill the user enter correct selection
    while diffCheck == 0:
        
        os.system("cls") #CLEAR SCREEN FOR WINDOWS

        #display options
        print("")
        print(" ______________________________")
        print("|                              |")
        print("|         \U0001F4A3BOMB TAG\U0001F4A3         |")
        print("|   \U0001F464by: Krystler Cataniag\U0001F916  |")
        print("|______________________________|")
        print("")
        print("          (1) \U0001F476Easy")
        print("          (2) \U0001F468Average")
        print("          (3) \U0001F9B8Hard")
        print("          (4) \U0001F9DBExpert")
        print("          (5) \U0001F479Master")
        print("")

        #ask for user input
        diff_Select = input("Select Difficulty:")

        #catch/handle error when user input is incorrect
        try:
            #check if input can be converted to int
            #if not jump to EXCEPT
            diffSelectCheck = int(diff_Select)

                
            #condition for EASY = 1
            if diffSelectCheck == 1:

                #remind what the user selected
                print("")
                print("            You've Selected")
                print("                 \U0001F476Easy")
                print("")
                time.sleep(2) #wait for 2 secs

                #the loop should now stop here
                diffCheck = 1

                #Change the global variable
                bot_difficulty = .5 # .5 = 500ms or half a second. How the bot frequently update the bomb tag
                bot_emoji = "\U0001F476" #emoji baby 👶

                game_start() #start the game b gonig to this game_start function

                
            #condition for AVERAGE = 2
            if diffSelectCheck == 2:

                #remind what the user selected
                print("")
                print("            You've Selected")
                print("               \U0001F468Average")
                print("")
                time.sleep(2) #wait for 2 secs

                #the loop should now stop here
                diffCheck = 1

                bot_difficulty = .3 # .3 = 300ms. How the bot frequently update the bomb tag
                bot_emoji = "\U0001F468" #emoji adult 👨

                game_start() #start the game b gonig to this game_start function

                
            #condition for HARD = 3
            if diffSelectCheck == 3:

                #remind what the user selected
                print("")
                print("            You've Selected")
                print("                 \U0001F9B8Hard")
                print("")
                time.sleep(2) #wait for 2 secs

                #the loop should now stop here
                diffCheck = 1

                bot_difficulty = .2 # .2 = 200ms. How the bot frequently update the bomb tag
                bot_emoji = "\U0001F9B8" #emoji superwoman 🦸

                game_start() #start the game b gonig to this game_start function

                
            #condition for EXPERT = 4
            if diffSelectCheck == 4:

                #remind what the user selected
                print("")
                print("            You've Selected")
                print("                \U0001F9DBExpert")
                print("")
                time.sleep(2) #wait for 2 secs

                #the loop should now stop here
                diffCheck = 1

                bot_difficulty = .1 # .1 = 100ms. How the bot frequently update the bomb tag
                bot_emoji = "\U0001F9DB" #emoji magician/vampire? 🧛

                game_start() #start the game b gonig to this game_start function

                
            #condition for MASTER = 5
            if diffSelectCheck == 5:

                #remind what the user selected
                print("")
                print("            You've Selected")
                print("                \U0001F479Master")
                print("")
                time.sleep(2) #wait for 2 secs

                #the loop should now stop here
                diffCheck = 1 

                bot_difficulty = .05 # .05 = 50ms. How the bot frequently update the bomb tag
                bot_emoji = "\U0001F479" #emoji ogre 👹

                game_start() #start the game b gonig to this game_start function

            
        
        except:
            #continue to ask difficulty until the user enter correct value.
            diffCheck = 0
            print("")
            print("Plese enter numbers only based on difficulty.")
            time.sleep(2)
            

#function for menu selection
def menu():
    #delcare and initialize input checker for menu
    menuCheck = 0

    #while loop for input error checking until the user enter correct selection
    while menuCheck == 0:
        
        os.system("cls") #CLEAR SCREEN FOR WINDOWS

        #display the selection
        print("")
        print(" ______________________________")
        print("|                              |")
        print("|         \U0001F4A3BOMB TAG\U0001F4A3         |")
        print("|   \U0001F464by: Krystler Cataniag\U0001F916  |")
        print("|______________________________|")
        print("")
        print("          (1) Start Game")
        print("          (2) Quit Game")
        print("")

        #ask for user input
        menuSelect = input("Select Menu:")


        #catch/handle error when user input is incorrect
        try:
            #check if input can be converted to int
            #if not jump to EXCEPT
            menuSelectCheck = int(menuSelect)

            
            #Menu select for START GAME
            if menuSelectCheck == 1:

                #stop the loop of selecting menu
                menuCheck = 1
                
                print("Starting Game...") #just to remind the game is starting
                
                time.sleep(1) #sleep for 1 sec

                #now goto difficulty selection
                choose_difficulty()
                break

            #Menu select for QUIT GAME
            if menuSelectCheck == 2:
                break

            
            
        except:
            #continue to ask for menu selection until a correct value is entered based on display menu.
            menuCheck = 0
            print("")
            print("Plese enter numbers only based on menu.")
            time.sleep(2)


#start the whole project
menu()
