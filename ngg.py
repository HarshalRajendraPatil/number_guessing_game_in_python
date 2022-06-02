from os import system


from os import system
import random

system("cls");

play_again = False;
valid_input = False;
random_number = random.randint(1,100);
print(random_number);
lives_for_easy = 10;
lives_for_hard = 5;

print("|| Welcome to the Number Guessing Game ||");
print("I am thinking of a number between 1 and 100.");

def checking(lives, number, user_choice):
    if user_choice == "easy":
        is_alive = False;
        while is_alive != True:
            print(f"You have {lives} attempts remaining to guess the number.");
            if lives > 0:
                user_num = int(input("make a guess:\t"));
                if user_num > number:
                    print("Too high\nGuess again.");
                    lives -= 1;
                    is_alive = False;
                elif user_num < number:
                    print("Too low\nGuess again.");
                    lives -= 1;
                    is_alive = False;
                else:
                    print(f"You got it, the answer was {number}\nIt took you {11 - lives} attempts.");
                    is_alive = True
            else:
                print("You have run out of guesses, you lost.");
                is_alive = True
    else:
        is_alive = False;
        while is_alive != True:
            print(f"You have {lives} attempts remaining to guess the number.");
            if lives > 0:
                user_num = int(input("make a guess:\t"));
                if user_num > number:
                    print("Too high\nGuess again.");
                    lives -= 1;
                    is_alive = False;
                elif user_num < number:
                    print("Too low\nGuess again.");
                    lives -= 1;
                    is_alive = False;
                else:
                    print(f"You got it, the answer was {number}\nIt took you {6 - lives} attempts.");
                    is_alive = True
            else:
                print("You have run out of guesses, you lost.");
                is_alive = True

while play_again != True:

    while (valid_input != True):

        user_choice = input("Choose the difficulty. Type 'easy' or 'hard':\t").lower();

        if user_choice == "easy":
            valid_input = True;
            checking(lives=lives_for_easy, number=random_number, user_choice=user_choice)
        elif user_choice == "hard":
            valid_input = True;
            checking(lives=lives_for_hard, number=random_number, user_choice=user_choice)
        else:
            valid_input = False;
            print("Please enter a valid input.");

    user_choice = input("Do you want to play again (yes/no):\t");
    if user_choice == "yes":
        system("cls");
        random_number = random.randint(1,100);
        print("|| Welcome to the Number Guessing Game ||");
        print("I am thinking of a number between 1 and 100.");
        play_again = False;
        valid_input = False;
    else:
        print("Thx for Playing.");
        play_again = True;