'''
Name: Abdelrahman Wael Mohammed Hanafy      ID:20210490
game number: 0                              game name: SOS game
'''

import os

global score1 , score2 , game_counter , not_empty
score1 = 0
score2 = 0 
game_counter = 0
not_empty = False

#board
def display_board():
    global board
    cols = 4 
    rows = 4

    board = [[' ' for i in range (cols)] for j in range(rows)] #creats a 2D list
    for i in range(4):
        print(board[i])


#input
def user_input():
    global x, y, play_input
    
    while True:
        try:
            y = int(input("Enter the row number: "))
            x = int(input("Enter the cols number: "))
        except:
            print("Please enter a number between 1 and 4\n")
            continue
        
        if 0 < y < 5 and 0 < x < 5:
            break 
        else:
            print("Please enter a number between 1 and 4\n")
    
    while True:
        play_input = input("Enter S or O: ").upper() #if the user enter lowercase 's' or 'o' it make it uppercase
        if play_input == 's'.upper() or play_input == 'o'.upper():
            break
        else:
            print("invalid character \n")


#update
def update(y,x,play_input):
    global not_empty
    x -= 1
    y -= 1
    not_empty = False
    if board [y][x] == ' ':
        board[y][x] = play_input
        
        print("\n") #prints an empty line after each round
        for i in range(4):
            print(board[i])
    else: 
        not_empty = True
    

#check
def check_score(turn):
    global play_again, score1, score2, x, y
    play_again = False
    #checking all possible chances to take a point
    if play_input == 'O': #if the user enters 'O'
        
        #index = user input-1
        try:
            if ((board[y - 1][x - 2] =='S') and (board[y - 1][x] =='S')) and x - 2 >= 0: #horisontal check 
                if turn%2 == 0:
                    score1 += 1 
                    play_again = True
                else:
                    score2 += 1 
                    play_again = True
        except:
           pass


        try:
            if ((board[y - 2][x - 1] =='S') and (board[y][x - 1] =='S')) and y - 2 >= 0: #virtical check
                if turn%2 == 0:
                    score1 += 1 
                    play_again = True
                else:
                    score2 += 1 
                    play_again = True
        except:
            pass
        
        try:
            if ((board[y][x - 2] =='S') and (board[y - 2][x] =='S')) and x - 2 >= 0 and y - 2 >= 0: #right check "/"
                if turn%2 == 0:
                    score1 += 1 
                    play_again = True
                else:
                    score2 += 1 
                    play_again = True
        except:
            pass

        try:
            if ((board[y][x] =='S') and (board[y - 2][x - 2] =='S')) and x - 2 >= 0 and y - 2 >= 0: #left check "\"
                if turn%2 == 0:
                    score1 += 1 
                    play_again = True
                else:
                    score2 += 1 
                    play_again = True
        except:
            pass


    if play_input == 'S': #if the user enters 'S'
        
        #index = user input-1
        #y - 2 or x - 2 will cause a negative index so I had to check that in my conditions  
        try:
            if (board[y - 1][x - 2] =='O' and x-2 >= 0): #horisontal check (left)
                if board[y - 1][x - 3] == 'S' and x - 3 >= 0:
                    if turn%2 == 0:
                        score1 += 1 
                        play_again = True
                    else:
                        score2 += 1 
                        play_again = True
        except:
           pass
    

        try:
            if (board[y - 1][x] =='O'): #horisontal check (right)
                if board[y - 1][x + 1] == 'S':
                    if turn%2 == 0:
                        score1 += 1 
                        play_again = True
                    else:
                        score2 += 1 
                        play_again = True
        except:
           pass

        try:
            if (board[y - 2][x - 1] =='O') and y - 2 >= 0: #virtical check (top)
                if board[y - 3][x - 1] == 'S' and y - 3 >= 0:
                    if turn%2 == 0:
                        score1 += 1 
                        play_again = True
                    else:
                        score2 += 1 
                        play_again = True
        except:
            pass

        try:
            if (board[y][x - 1] =='O'): #virtical check (bottom)
                if board[y + 1][x - 1] == 'S':
                    if turn%2 == 0:
                        score1 += 1 
                        play_again = True
                    else:
                        score2 += 1 
                        play_again = True
        except:
            pass
        
        
        try:
            if  (board[y - 2][x] =='O') and y - 2 >= 0:  #right check "/" (top)
                if board[y - 3][x + 1] == 'S'  and y - 3 >= 0:
                    if turn%2 == 0:
                        score1 += 1 
                        play_again = True
                    else:
                        score2 += 1 
                        play_again = True
        except:
            pass

        try:
            if  (board[y][x - 2] =='O') and x - 2 >= 0: #right check "/" (bottom)
                if board[y + 1][x - 3] == 'S' and x - 3 >= 0:
                    if turn%2 == 0:
                        score1 += 1 
                        play_again = True
                    else:
                        score2 += 1 
                        play_again = True
        except:
            pass

        try:
            if (board[y - 2][x - 2] =='O') and x - 2 >= 0 and y - 2 >= 0: #left check "\" (top)
                if board[y - 3][x - 3] == 'S' and y - 3 >= 0 and x - 3 >= 0:
                    if turn%2 == 0:
                        score1 += 1 
                        play_again = True
                    else:
                        score2 += 1 
                        play_again = True
        except:
            pass

        try:
            if (board[y][x] =='O'): #left check "\" (bottom)
                if board[y + 1][x + 1] == 'S':
                    if turn%2 == 0:
                        score1 += 1 
                        play_again = True
                    else:
                        score2 += 1 
                        play_again = True
        except:
            pass

    
    print("Player1 score: ", score1, "Player2 score: ", score2)


#check if any player win and print the result
def if_win():
    if score1 > score2:
        print("Player1 Win!")

    elif score2 > score1:
        print("Player2 Win!")

    else:
        print("draw!")


#instructions of the game
def instructions():
    print('''
    Hello and welcome to SOS game!
    written by: Abdelrahman Wael Mohammed 
    date: 25-2-2022

    This is the instructions of the game:
    First: you enter the row number as follows:
    1  [' ', ' ', ' ', ' ']
    2  [' ', ' ', ' ', ' ']
    3  [' ', ' ', ' ', ' ']
    4  [' ', ' ', ' ', ' ']
    
    Second: you enter the column number as follows:
      1    2    3    4
    [' ', ' ', ' ', ' ']
    [' ', ' ', ' ', ' ']
    [' ', ' ', ' ', ' ']
    [' ', ' ', ' ', ' ']

    and this is the full grid map with the right input
    ['(1,1)', '(1,2)', '(1,3)', '(1,4)']
    ['(2,1)', '(2,2)', '(2,3)', '(2,4)']
    ['(3,1)', '(3,2)', '(3,3)', '(3,4)']
    ['(4,1)', '(4,2)', '(4,3)', '(4,4)']
    
    Third: you enter the chosen letter (S or O)

    Then have fun :)

    Press enter to start

    ''')


#clear thr console
def clear():
    os.system('cls')



#main game starts here
while True: 
    clear()
    instructions()
    start_game = input() #letting the game start after the user presses enter
    clear()
    display_board()
    i = 0
    game_counter = 0
    score1 = 0
    score2 = 0
    
    while game_counter < 16: #every game has 16 rounds
        if i%2 == 0:
            print("Player1 Turn")
        else:
            print("Player2 Turn")

        user_input()
        update(y,x,play_input)
        if not_empty:  #not empty variable will return true if the square is not empty
            print("Please choose an empty square \n") #this if statment checks if the square is empty
            continue
        check_score(i)

        i += 1
        if play_again : #if player got a point he continue playing so this i variable will do that 
            i += 1

        game_counter += 1 #every game has a max 16 rounds so game counter will calculate that

        if game_counter >= 16:
            if_win()
    
    while True:            
        replay = input("Play again? (y for yes - n for no) ")
        if replay == 'y' or replay == 'n':
            break
        else:
                print("Invalid Input!")

    if replay == 'n':
            break 
    else:
        continue




