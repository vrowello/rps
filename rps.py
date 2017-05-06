import random

computer_choice = random.randrange(0, 3)
user_choice = raw_input('rock, paper, or scissors? ')
#print(computer_choice)
#print(user_choice)

if user_choice == 'rock' and computer_choice == 0:
    print("CPU Chose Rock, It's a Tie!")
elif user_choice == 'paper' and computer_choice == 0:
    print("CPU Chose Rock, You Win!")
elif user_choice == "scissors" and computer_choice == 0:
    print("CPU Chose Rock, You Lose!")
elif user_choice == 'rock' and computer_choice == 1:
    print("CPU Chose Paper, You Lose!")
elif user_choice == 'paper' and computer_choice == 1:
    print("CPU Chose Paper, It's a Tie")
elif user_choice == 'scissors' and computer_choice == 1:
    print("CPU Chose Paper, You Win!")
elif user_choice == 'rock' and computer_choice == 2:
    print("CPU Chose Scissors, You Win!")
elif user_choice == 'paper' and computer_choice == 2:
    print("CPU Chose Scissors, You Lose!")
elif user_choice == 'scissors' and computer_choice == 2:
    print("CPU Chose Scissors, It's a Tie!")
else:
    print("Try again in all lowercase")
