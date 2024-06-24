from random import randint

while True:   
    random_num = []
    while len(random_num) < 3:
        num = randint(1, 5) 
        random_num.append(num)
        

    bet = input("Enter your bet 3  digit numbers separated by spaces(ex: 1 3 4): ") # Prompt the user to enter their bet as three-digit numbers separated by spaces.
    bet = list(map(int, bet.split())) # Converts a string 'bet' into a list of integers.
# Splits the string 'bet' by whitespace and maps each resulting substring to an integer.
    result = random_num # Assigns the value of 'random_num' to 'result'.

    print(f"Bet: {' '.join(map(str, bet))}") # Constructs a string representation of the list 'bet' with elements converted to strings,
# separated by spaces, and prints it.
    print(f"Result: {' '.join(map(str, result))}") # Constructs a string representation of the iterable 'result' with elements converted to strings,
# separated by spaces, and prints it.

    sorted_bet = sorted(bet)
    sorted_result = sorted(result)

    #print(sorted_bet)
    #print(sorted_result)

    if (bet == result): # Check if the bet matches the result.
        print("Daug Kaw!")
    elif (sorted_bet == sorted_result): # Check if the sorted version of bet matches the sorted version of result.
        print("Daug ka sa Ramble")
    else:
        print("Pilde kaw")
