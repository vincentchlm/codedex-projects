import random

print('================================')
print('Rock Paper Scissors Lizard Spock')
print('================================')
print('1) ✊')
print('2) ✋')
print('3) ✌️')
print('4) 🦎')
print('5) 🖖')
player = int(input('Pick a number: '))
computer = random.randint(1, 5)
#if input player 1
if player == 1:
    if computer == 1:
        print("You chose: ✊")
        print("CPU chose: ✊")
        print("It's a tie!")
    elif computer == 2:
        print("You chose: ✊")
        print("CPU chose: ✋")
        print("You lose.")
    elif computer == 3:
        print("You chose: ✊")
        print("CPU chose: ✌️")
        print("The player won!")
    elif computer == 4:
        print("You chose: ✊")
        print("CPU chose: 🦎")
        print("The player won!")
    elif computer == 5:
        print("You chose: ✊")
        print("CPU chose: 🖖")
        print("You lose.")
#if input player 2
elif player == 2:
    if computer == 1:
        print("You chose: ✋")
        print("CPU chose: ✊")
        print("The player won!")
    elif computer == 2:
        print("You chose: ✋")
        print("CPU chose: ✋")
        print("It's a tie!")
    elif computer == 3:
        print("You chose: ✋")
        print("CPU chose: ✌️")
        print("You lose.")
    elif computer == 4:
        print("You chose: ✋")
        print("CPU chose: 🦎")
        print("You lose.")
    elif computer == 5:
        print("You chose: ✋")
        print("CPU chose: 🖖")
        print("The player won!")
#if input player 3
elif player == 3:
    if computer == 1:
        print("You chose: ✌️")
        print("CPU chose: ✊")
        print("You lose.")
    elif computer == 2:
        print("You chose: ✌️")
        print("CPU chose: ✋")
        print("The player won!")
    elif computer == 3:
        print("You chose: ✌️")
        print("CPU chose: ✌️")
        print("It's a tie!")
    elif computer == 4:
        print("You chose: ✌️")
        print("CPU chose: 🦎")
        print("The player won!")
    elif computer == 5:
        print("You chose: ✌️")
        print("CPU chose: 🖖")
        print("You lose.")
#if input player 4
elif player == 4:
    if computer == 1:
        print("You chose: 🦎")
        print("CPU chose: ✊")
        print("You lose.")
    elif computer == 2:
        print("You chose: 🦎")
        print("CPU chose: ✋")
        print("The player won!")
    elif computer == 3:
        print("You chose: 🦎")
        print("CPU chose: ✌️")
        print("You lose.")
    elif computer == 4:
        print("You chose: 🦎")
        print("CPU chose: 🦎")
        print("It's a tie!")
    elif computer == 5:
        print("You chose: 🦎")
        print("CPU chose: 🖖")
        print("The player won!")
#if input player 5
elif player == 5:
    if computer == 1:
        print("You chose: 🖖")
        print("CPU chose: ✊")
        print("The player won!")
    elif computer == 2:
        print("You chose: 🖖")
        print("CPU chose: ✋")
        print("The player won!")
    elif computer == 3:
        print("You chose: 🖖")
        print("CPU chose: ✌️")
        print("The player won!")
    elif computer == 4:
        print("You chose: 🖖")
        print("CPU chose: 🦎")
        print("You lose.")
    elif computer == 5:
        print("You chose: 🖖")
        print("CPU chose: 🖖")
        print("It's a tie!")
else:
    print('Wrong input!')