import random
import subprocess

max_val_input = input("Enter Max Number: ")
try:
    max_val = int(max_val_input)
except ValueError:
    print("Invalid input. Please enter a valid integer.")

rounds_input = input("Enter Number of Rounds to Play: ")
try:
    rounds = int(rounds_input)
except ValueError:
    print("Invalid input. Please enter a valid integer.")

print(f"We will play {rounds} rounds with a max value of {max_val}. Good luck!")

num_correct = 0

for round in range(0, rounds):
    print(f"========[ Round {round + 1}]========")
    a = random.randint(1, max_val)
    b = random.randint(1, max_val)
    op_code = random.randint(0, 3)
    match op_code:
        case 0:
            op = "+"
            correct_answer = a + b
        case 1:
            op = "-"
            if b > a:
               c = a
               a = b
               b = c
            correct_answer = a - b
        case 2:
            op = "x"
            correct_answer = a * b
        case 3:
            op = "/"
            a = a * b
            correct_answer = a / b

    answer = input(f"{a} {op} {b} = ")
    if int(answer) == correct_answer:
        print("Correct!")
        num_correct += 1
    else:
        print("Incorrect")

print("\n")
if num_correct == rounds:
    subprocess.run(["/opt/homebrew/bin/figlet -w 180 -k -f broadway -c \"You Won\" | /opt/homebrew/bin/lolcat"], shell=True)
else:
    print(f"You got {num_correct} correct out of {rounds}!")

