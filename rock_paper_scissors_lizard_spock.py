import random

print("=" * 38)
print(" Rock, Paper, Scissors, Lizard, Spock")
print("=" * 38)

print()
print("1) ✊ (Rock)")
print("2) ✋ (Paper)")
print("3) ✌️ (Scissors)")
print("4) 🦎 (Lizard)")
print("5) 🖖 (Spock)")

rock = "✊ (Rock)"
paper = "✋ (Paper)"
scissors = "✌️ (Scissors)"
lizard = "🦎 (Lizard)"
spock = "🖖 (Spock)"

print()
player = int(input("Pick a number: "))

if player == 1:
    result_p = rock
elif player == 2:
    result_p = paper
elif player == 3:
    result_p = scissors
elif player == 4:
    result_p = lizard
elif player == 5:
    result_p = spock
else:
    print("Option does not exist!")

computer = random.randint(1, 5)

if computer == 1:
    result_c = rock
elif computer == 2:
    result_c = paper
elif computer == 3:
    result_c = scissors
elif player == 4:
    result_c = lizard
elif player == 5:
    result_c = spock
else:
    print("Option does not exist!")

print()
print(f"You chose: {result_p}")
print(f"CPU chose: {result_c}")

print()
if player == computer:
    print("Tied!")
elif result_c == scissors and result_p == paper:
    print("The CPU won!")
elif result_c == paper and result_p == scissors:
    print("The player won!")
elif result_c == paper and result_p == rock:
    print("The CPU won!")
elif result_c == rock and result_p == paper:
    print("The player won!")
elif result_c == rock and result_p == lizard:
    print("The CPU won!")
elif result_c == lizard and result_p == rock:
    print("The player won!")
elif result_c == lizard and result_p == spock:
    print("The CPU won!")
elif result_c == spock and result_p == lizard:
    print("The player won!")
elif result_c == spock and result_p == scissors:
    print("The CPU won!")
elif result_c == scissors and result_p == spock:
    print("The player won!")
elif result_c == scissors and result_p == lizard:
    print("The CPU won!")
elif result_c == lizard and result_p == scissors:
    print("The player won!")
elif result_c == lizard and result_p == paper:
    print("The CPU won!")
elif result_c == paper and result_p == lizard:
    print("The player won!")
elif result_c == paper and result_p == spock:
    print("The CPU won!")
elif result_c == spock and result_p == paper:
    print("The player won!")
elif result_c == spock and result_p == rock:
    print("The CPU won!")
elif result_c == rock and result_p == spock:
    print("The player won!")
elif result_c == rock and result_p == scissors:
    print("The CPU won!")
elif result_c == scissors and result_p == rock:
    print("The player won!")