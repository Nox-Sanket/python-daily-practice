import random

# Using a more descriptive name than 'list'
options = [0, 1, 2] 

# Convert input to int immediately
val = int(input("Enter 0 (Rock), 1 (Paper), or 2 (Scissors): "))
ans = random.choice(options)

print(f"Computer chose: {ans}")

if val == ans:
    print("Draw")
elif val == 0: # User chose Rock
    if ans == 1:
        print("You lose")
    else:
        print("You won")
elif val == 1: # User chose Paper
    if ans == 2:
        print("You lose")
    else:
        print("You won")
elif val == 2: # User chose Scissors
    if ans == 0:
        print("You lose")
    else:
        print("You won")
