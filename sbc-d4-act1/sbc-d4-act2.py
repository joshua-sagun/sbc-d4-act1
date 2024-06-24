from random import randint
while True:
    hands = ["kulob", "hayang"]

    kulob = hands[0]
    hayang = hands[1]
    print("""
    ---------------CHOICES------------
                    kulob
                    hayang
    """)

    player = input("Enter choices: ")

    c1 = "kulob" if randint(0, 1) == 0 else "hayang" # Randomly choose between "kulob" or "hayang" for c1

    c2 = "hayang" if randint(0, 1) == 1 else "hayang" # Randomly choose between "kulob" or "hayang" for c2
    
    print(f" PLayer Choce: {player}")
    print(f" Computer 1 Choce: {c1}")
    print(f" Computer 2 Choce: {c2}")

    print("\n")
    if player not in ("kulob", "hayang"):
        print("invalid choices")
    elif (player == c1 == c2):
        print("draw")
    elif (player != c1 and player != c2):
        print("player 1 wins")
    elif (c1 != player and c1 != c2):
        print("computer 1 wins")
    elif (c2 != player and c2 != c1):
        print("computer 2 wins")
    
    else:
        print("Wala Daug, PLay again")
