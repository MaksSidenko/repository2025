import random
options = ("rock", "paper", "scissors")
running = True

while running:
  user_choice = None
  computer_choice = random.choice(options)
  while user_choice not in options:
    user_choice =  input("Print: rock, paper, scissors: ").lower()
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")
    while True:
        play_again = input("Want to play again: type yes or no: ").lower()
        if play_again in ("yes", "no", "y", "n"):
            break
        print("Please type 'yes' or 'no'.")
    running = play_again in ("yes", "y")
print("Thanks for playing")


















# import random

# options = ("rock", "paper", "scissors")

# running = True


# while running:
#     user_choice = None
#     computer_choice = random.choice(options)
#     while user_choice not in options:
#         user_choice = input("Choose rock, paper, or scissors: ").lower()

#     print(f"Computer chose: {computer_choice} user chose: {user_choice}")

#     if user_choice == computer_choice:
#         print("It's a tie!")
#     elif (user_choice == "rock" and computer_choice == "scissors") or \
#         (user_choice == "paper" and computer_choice == "rock") or \
#         (user_choice == "scissors" and computer_choice == "paper"):
#         print("You win!")
#     else:
#         print("Computer wins!")
#     play_again = input("Play again? (yes/no): ").lower()

#     if play_again == "no":
#         running = False

# print("Thanks for playing!")        



# ("")
# input(" ")
# print()
# *
# 8
#_


