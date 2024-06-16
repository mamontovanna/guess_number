from random import randint
import argparse

def input_args():
    parser=argparse.ArgumentParser(
        description="To get name and number from the terminal"
    )
    parser.add_argument("-n", "--name", 
                        required="True", dest="name",
                        help="The name of a player"
                        )


    args=parser.parse_args()
    return args

def guess_number(name="Player"):
    exit=''
    fr=to=0
    game_count=0
    win=0
    fail=0
    print(f"Hello, {name}! Try to guess which number I'm thinking of... \n But firstly enter the number from:\n\n")
    fr=int(input())
    print("... and enter the number to:\n")
    to=int(input())
    while (fr>=to):
        print("Please, enter correct numbers!\n The first number must be less than the second number!\n\n")
        fr=int(input("First number: \n"))
        to=int(input("... and enter the second number:\n"))
    while exit!='q':
        game_count+=1
        print(f"\n\n{name}, Try to guess which number I'm thinking from {fr} to {to}...\n")
        player_number=int(input())
        while(player_number not in range(fr, to+1)):
            player_number=int(input(f"Please, enter the number from {fr} to {to}"))

        python_number=randint(fr,to)
        print(f"\n{name}, you choose {player_number}.")
        print(f"I was thinking about the number {python_number}.")

        if player_number==python_number:
            win+=1
            print(f"\nCongratulations! You win!")
            print(f"\nGame count: {game_count}")
            print(f"\n{name}'s wins: {win}")
            

        else:
            fail+=1
            print(f"Sorry, {name}. Better luck next time")
            print(f"\nGame count: {game_count}")
            print(f"\n{name}'s wins: {win}")
        print(f"\nYour winning percentage: {(win/(win+fail))*100}%")
        print(f"\nPlay again, {name}?")   
        print("\nY for Yes \nQ for Quit")
        exit=input().lower()

arg=input_args()
guess_number(arg.name)



            


    


    


      
