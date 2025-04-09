import time

import random

word = "a"

lives = 5

print("********************************************************************************")

time.sleep(1)

print("\t\t\t\tMAZE OF MYSTERIES")

time.sleep(1)

print("********************************************************************************")

time.sleep(1)

#The main function

def main(lives,word):

    #This will trigger the introduction

    intro()

    while True:

        lives, word, finished = TakeTurn(word,lives)

        if finished:

            break

        if lives < 1:

            break

        if lives == 1:

            temp = "life"

        else:

            temp = "lives"

        print ("You have",lives,temp) #displays the number of lives user has at that point

    if lives < 1:

      print ("Sorry! You ran out of lives! You lose!")

    else:

      print ("You win")

    print("\n")

    print("\t\t\t\tGAME OVER")


#This function is the introduction to the program

def intro():

   file1 = open("intro.txt",'r')

   data1 = file1.readlines()

   for line in data1:

       print(line)

       time.sleep(2)



#This function is the actual 'game' and will determine what happens to the character    

def TakeTurn(word1, lives1):

    time.sleep(1.5)

    print(f"You have reached {word1} junction.\nDo you want to turn left (L), right (R), or go straight ahead (S)?")

    turning = input().lower()

    word1 = "another"  # Grammar switch for next round

    while turning not in ["l", "r", "s"]:
        
        time.sleep(0.7)
        print("Sorry, I didn't understand that.")
        turning = input().lower()

    # Add randomness with slight directional influence
    if turning == "l":
        choice = random.choices(range(1, 11), weights=[2,1,1,1,1,1,1,1,1,1])[0]
    elif turning == "r":
        choice = random.choices(range(1, 11), weights=[1,1,2,2,1,1,1,1,1,1])[0]
    else:
        choice = random.randint(1, 10)

    time.sleep(1)

    # Choices from 1 to 10
    if choice == 1:
        print("You have found the exit!")
        return lives1, word1, True
    elif choice == 2:
        print("You have found a life!")
        time.sleep(1)
        return lives1 + 1, word1, False
    elif choice == 3:
        print("You have found two lives!")
        time.sleep(1)
        return lives1 + 2, word1, False
    elif choice == 4:
        print("You reached a dead end and turn back.")
        time.sleep(2)
        return lives1, word1, False
    elif choice == 5:
        print("You have entered a dark cave.")
        time.sleep(2)
        lives1 = cave(lives1)
        return lives1, word1, False
    elif choice == 6:
        lives1 = treasurechest(lives1)
        return lives1, word1, False
    elif choice == 7:
        print("You fell into a deep ditch and lose a life.")
        time.sleep(2)
        return lives1 - 1, word1, False
    elif choice == 8:
        lives1 = competitor(lives1)
        return lives1, word1, False
    elif choice == 9:
        print("You have encountered a giant who hits you!")
        time.sleep(2)
        print("You lose two lives.")
        return lives1 - 2, word1, False
    else:
        print("A goblin approaches and says the following:")
        time.sleep(2)
        lives1 = goblin(lives1)
        return lives1, word1, False




def treasurechest(lives): #called in option 6

    treasure = 1

    while treasure == 1:

        print ("You have found a treasure chest! Do you want to open it? Y or N?")

        chest = input().lower()

        if chest not in ["y","n","yes","no"]:

            print ("Sorry, I didn't understand that")

        elif chest in ["n", "no"]:

            print ("Okay Bye")

            treasure = 0

        else:

            time.sleep(1)

            print ("Opening...")

            time.sleep(1)

            print ("Opening...")

            time.sleep(1)

            print ("Opening...")

            time.sleep(1)

            chest = random.randint(1,6)

            if chest == 1:

                print ("You have found a life!")

                lives = lives +1

                treasure = 0

            elif chest == 2:

                print ("You have found two lives!")

                lives = lives +2

                treasure = 0

            elif chest == 3:

                print ("A dwarf jumps out and steals one of your lives!")

                lives = lives -1

                treasure = 0

            elif chest == 4:

                print ("An evil fairy steals two of your lives!")

                lives = lives -2

                treasure = 0

            elif chest == 5:

                print ("Sorry, the chest is empty")

                treasure = 0

            else:

                print ("A goblin is in the chest and says the following...")

                time.sleep(2)

                lives = goblin(lives)

                treasure = 0

    return lives



def cave(l):#called in choice 5

    print ("It is dark and you can only make out a small stick on the floor.")

    print("Do you take it? [y/n]: ")

    ch1 = input().lower()

    while ch1 not in ["y","yes","n", "no"]:

        time.sleep (0.7)

        print ("Sorry, I didn't understand that")

        ch1 = input().lower()

    #STICK TAKEN

    if ch1 in ['y','yes']:

       print("You have taken the stick!")

       time.sleep(2)

       stick = 1



    # STICK NOT TAKEN

    else:

     print("You did not take the stick")

     stick = 0



    print("As you proceed further into the cave, you see a small glowing object")

    print("Do you approach the object? [y/n]")

    ch2 = input().lower()

    while ch2 not in ["y","yes","n", "no"]:

        time.sleep (0.7)

        print ("Sorry, I didn't understand that")

        ch2 = input().lower()

# APPROACH SPIDER

    if ch2 in ['y','yes']:

        print ("You approach the object...")

        time.sleep(2)

        print ("As you draw closer, you begin to make out the object as an eye!")

        time.sleep(1)

        print ("The eye belongs to a giant spider!")

        print("Do you try to fight it? [Y/N]")

        ch3 = input().lower()

        while ch3 not in ["y","yes","n", "no"]:

         time.sleep (0.7)

         print ("Sorry, I didn't understand that")

         ch3 = input().lower()

        if ch3 in ['y','yes']:



            # WITH STICK

            if stick == 1:

                print ("You only have a stick to fight with!")

                print ("You quickly jab the spider in its eye and gain an advantage")

                time.sleep(2)

                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                print ("                  Fighting...                   ")

                print ("   YOU MUST HIT ABOVE A 5 TO KILL THE SPIDER    ")

                print ("IF THE SPIDER HITS HIGHER THAN YOU, YOU WILL DIE")

                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                time.sleep(2)

                user = int(random.randint(3, 10)) #user generates the number the user hits with

                spider = int(random.randint(1, 5)) #spider generates the number the spider hits with

                print ("you hit a", user)

                print ("the spider hits a", spider)

                time.sleep(2)



                if spider > user:

                    print ("The spider overpowers you. You have lost all your lives.")

                    l = 0

                    return l



                elif user < 5:

                    print ("You didn't do enough damage to kill the spider, but you manage to escape. You lose three lives.")

                    l = l - 3

                    return l



                else:

                    print ("You killed the spider!")

                    return l



            # WITHOUT STICK

            else:

                print ("You don't have anything to fight with!")

                time.sleep(2)

                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                print ("                  Fighting...                   ")

                print ("   YOU MUST HIT ABOVE A 5 TO KILL THE SPIDER    ")

                print ("IF THE SPIDER HITS HIGHER THAN YOU, YOU WILL DIE")

                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                time.sleep(2)

                user = int(random.randint(1, 8))

                spider = int(random.randint(1, 5))

                print ("you hit a", user)

                print ("the spider hits a", spider)

                time.sleep(2)



                if spider > user:

                    print ("The spider overpowers you. You have lost all your lives.")

                    l = 0

                    return l



                elif user < 5:

                    print ("You didn't do enough damage to kill the spider, but you manage to escape. You lose three lives.")

                    l = l - 3

                    return l



                else:

                    print ("You killed the spider!")

                    return l



        #DON'T FIGHT SPIDER

        print ("You choose not to fight the spider.")

        time.sleep(1)

        print ("As you turn away, it ambushes you and impales you with its fangs!!! You lose all lives.")

        l = 0

        return l



    # DON'T APPROACH SPIDER

    else:

        print ("You turn away from the glowing object, and attempt to leave the cave...")

        time.sleep(1)

        print ("But something won't let you....")

        time.sleep(2)

        print ("Your path is suddenly blocked by a huge spider and it ambushes you and impales you with its fangs!!! You lose all lives")

        l = 0

        return l

    

#COMPETITOR

def competitor(lives):

    print("You have come across another player")

    time.sleep(2)

    print("Get ready for battle")

    time.sleep(2)

    print("-----------------------------------")

    time.sleep(2)

    print("THE BATTLE BEGINS")

    time.sleep(2)

    print("-----------------------------------")

    time.sleep(2)

    a = random.randint(1,10)

    if a > lives:

        print("Competitor has",a - lives, "more lives than you")

        print("You lose!!!")

        lives = 0

    elif a == lives:

        print("Both of you have", a, "lives")

        print("It's a tie! You neither lose nor gain lives")

    else:

        print("You have ",lives - a, "more lives than the competitor")

        print("You win!! You get two extra lives")

        lives+=2

    return lives



def goblin(l):

        time1 = [1,2.5,1,1,1]

        text = ["'Do you want to play my magical roulette?\n There are three different outcomes:'",

                "1.You lose a life", "2.You gain a life","3.Nothing happens"]

        print_on_a_timer(time1,text)

        goblin = 0

        while goblin == 0:

            print ("Do you want to play? Y or N?")

            choice2 = input().lower()

            time.sleep(1)

            if choice2 not in ["y","n","yes","no"]:

                print ("Sorry I didnt understand that")

            elif choice2 in ["n","no"]:

                print ("Okay bye")

                return l

            else:

                print ("Let's play!")

                time.sleep(1)

                print ("Spinning...")

                time.sleep(1)

                print ("Spinning...")

                time.sleep(1)

                print ("Spinning...")

                time.sleep(1)

                roulette = random.randint(1,3)

                if roulette == 1:

                    print ("Nothing happens")

                    return l

                    goblin = 1

                elif roulette == 2:

                    print ("I’m going to have to take one of your lives")

                    l = l -1

                    return l

                    goblin = 1

                else:

                    print ("Here! Have a life!")

                    l = l +1

                    return l

                    goblin = 1

        



def print_on_a_timer(times, lines):

    for times, lines in zip(times, lines):

        time.sleep(times)

        print(lines)



main(lives,word)

