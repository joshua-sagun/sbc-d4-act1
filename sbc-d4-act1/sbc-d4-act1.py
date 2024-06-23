from random import randint

while True:   
    random_num = []
    while len(random_num) < 3:
        num = randint(1, 5) 
        random_num.append(num)
        

    bet = input("Enter your bet 3  digit numbers separated by spaces(ex: 1 3 4): ")
    bet = list(map(int, bet.split()))
    result = random_num

    print(f"Bet: {' '.join(map(str, bet))}")
    print(f"Result: {' '.join(map(str, result))}")

    sorted_bet = sorted(bet)
    sorted_result = sorted(result)

    #print(sorted_bet)
    #print(sorted_result)

    if (bet == result):
        print("Daug Kaw!")
    elif (sorted_bet == sorted_result):
        print("Daug ka sa Ramble")
    else:
        print("Pilde kaw")