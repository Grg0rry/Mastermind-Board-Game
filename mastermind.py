import random

main_guess = []
attempts = 0
main_loop = True

# Function to solve for C and P
def values(correct_answer, guess):
    i = 0
    pos_correct = 0
    col_correct = 0

    # Solve for correct colour and in correct position (P value)
    for x in guess: 
        if (x == correct_answer[i]):
            pos_correct += 1
            correct_answer[i] = '-'
            guess[i] = '-'
        i += 1
        
    # Remove the '-' from both colours and guess and also the repeated values from guess
    for i in range(4):
        if ('-' in guess):
            guess.remove('-')
        if ('-' in correct_answer):
            correct_answer.remove('-')    
    guess = list(dict.fromkeys(guess))

    # Solve for correct colour but in wrong position (C value)
    for x in guess:
        if (x in correct_answer):
            col_correct += 1
            
    correct_answer.clear()
    guess.clear()
    return col_correct, pos_correct

# Help menu
def introduction():
    while True:
        print("---------------------------------------------------------------")
        print("HELP MENU".center(62, ' '))
        print("---------------------------------------------------------------")
        print("Freqenctly Asked Questions")
        print(" (1): How to Play?\n", "(2): What is the C and P?\n", "(3): How do I win?\n", "(4): Back to the Game\n")
        x = input("Enter Your Choice (1/2/3/4): ")
        if x == '1':
            print("Question 1: How to Play?")
            print("Part 1: ", end = '')
            how_play_pt1()
            print("Part 2: ", end = '')
            how_play_pt2()
            print("Part 3: ", end = '')
            how_play_pt3()
            continue
        elif x == '2':
            print("Question 2: ", end ='')
            how_play_pt2()
            continue
        elif x == '3':
            print("Question 3: ", end ='')
            how_play_pt3()
            continue
        elif x == '4':
            break
        else:
            print("Enter only (1/2/3/4)")
            continue

def how_play_pt1():
    print("How to make an attempt? ")
    print("\tGuess the password in as few tries as possible")
    print("\tPassword is made out of combination of four colours")
    print()
    print("\tImportant Note:")
    print("\tThese same colour can repeat more than once in the password")
    print("\tThere are a total of six possible colours which could be selected")
    print("\tThe possible colours can be found in the Menu tab")
    print("\tYou will be given unlimitted attempts to guess until the password is guessed correctly")
    print()

def how_play_pt2():
    print("What is the C and P?")
    print("\tAfter making your attempt, you will see")
    print("\tC P | ")
    print("\tthe values under C: number of correct colours but at the wrong position")
    print("\tthe values under P: number of correct colours at the right position")
    print()
    print("\tImportant Note:")
    print("\tIn this scenario (BLUE   BLUE   RED   BLUE)")
    print("\tCase 1: BLUE correct position is the 3rd colour")
    print("\tC P |")
    print("\t1 0 | BLUE   BLUE   RED   BLUE ")
    print()
    print("\tCase 2: All three BLUE at the correct position")
    print("\tC P |")
    print("\t0 3 | BLUE   BLUE   RED   BLUE ")
    print()

def how_play_pt3():
    print("How to win?")
    print("\tOnly way to tell if the pattern entered is right or wrong is to use the C and P")
    print("\tSo key to victory is to use the C and P well")
    print("\tAll the best and Have fun Guessing")

def score_num(num):
    return num[1]

def scoreboard(attempts):
    score = [['Kim', 10], ['Thomas', 6], ['Greg', 4]]
    name = '' 
    while len(name) == 0:
        name = input("Please enter your name: ")
    achievement = [name, attempts]
    score.append(achievement)
    score.sort(key = score_num)
    print("-----------------------------------------")
    print("SCOREBOARD".center(40, ' '))
    print("-----------------------------------------")
    print("NAME". center(20), "SCORE".center(20))
    for x in range(len(score)):
        print()
        for y in range(2):
            print(str(score[x][y]).center(20), end = ' ')
        print()

while main_loop == True:
    pos_correct = 0
    # Randomize colours and select four
    colour_lst = {'R':'RED', 'G':'GREEN', 'Y':'YELLOW', 'B':'BLUE', 'O':'ORANGE', 'P':'PINK'}
    colour_lst2 = ["RED", "GREEN", "YELLOW", "BLUE", "ORANGE", "PINK"]
    shortcut = ["R", "G", "Y", "B", "O", "P"]
    main_colours = random.choices(colour_lst2, k=4)

    # Initialize GAME
    print("\t -----------------------------------------")
    print("MASTERMIND".center(62, ' '))
    print("\t -----------------------------------------")

    # Repeat till user gets all 4 colours
    while pos_correct < 4:
        print("---------------------------------------------------------------")
        print("Menu".center(62, ' '))
        print("---------------------------------------------------------------")
        print("Enter code")
        print("R - RED, G - GREEN, Y - YELLOW, B - BLUE, O - ORANGE, P - PINK")
        print("Example: RED GREEN YELLOW BLUE ---> R G Y B")
        print("Enter ""HELP"" For instructions on the game!!")
        print("---------------------------------------------------------------")
        raw_guess = list((input("Enter your choice = ").upper()).split())
    
        # Answer validation (Check if input have met the requirement)
        repeat = 0
        if ("HELP" in raw_guess):
            introduction()
            continue
        elif len(raw_guess) == 4:
            for x in raw_guess:
                if x not in shortcut:
                    repeat = 1
        else:
            repeat = 1
        
        if repeat == 1:
            print("Wrong Format/Choice!! Please Try again!!")
            continue

        # Converts user input to full letter and store in guess
        user_guess = []
        colour_into_list = colour_lst.items()
        for x in raw_guess:
            for i in colour_into_list:
                if i[0] == x:
                    user_guess.append(i[1])
        main_guess.append(user_guess)

        temp_col = []
        temp_guess = []
        for x in range (4):    
            temp_col.append(main_colours[x])
            temp_guess.append(user_guess[x])
    
        # Check if any number is correct
        print("---------------------------------------------------------------")
        print("C P |")
        x = values(temp_col, temp_guess)
        pos_correct = x[1]

        print(x[0], x[1], "|", end = ' ')
        for i in range (0,4):
            print('%13s' % main_guess[attempts][i], end = ' ')
        print()
        print("---------------------------------------------------------------")
        attempts += 1

    #Display complete results
    print("---------------------------------------------------------------")
    print("PASSWORD DECODED".center(62, ' '))
    print("CONGRATULATION!! YOU HAVE BECOME THE MASTERMIND".center(62, ' '))
    print("---------------------------------------------------------------")
    scoreboard(attempts)
    print()
    print("-----------------------------------------")
    print("YOUR ANSWERS".center(40, ' '))
    print("-----------------------------------------")
    for z in range (attempts):
        for i in range (0, 4):
            print('%9s' % main_guess[z][i], end = ' ')
        print()
        print("-----------------------------------------")    
    print("number of attempts: ", attempts)
    print()
    invalid = 1
    while invalid == 1:
        repeat = input("Would you like to play again? (y/n): ").lower()
        if repeat == 'y':
            break
        elif repeat == 'n':
            invalid = 2
    if invalid == 2:
        break   

print("Thank You for playing !! Hope to see you again")
