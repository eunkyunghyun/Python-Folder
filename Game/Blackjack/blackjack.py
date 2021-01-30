import random


def restart():
    while True:
        begin = []
        for i in range(2):
            start = cards[random.randint(0, len(cards) - 1)]
            begin.append(start)
        if add(begin) == 21 or begin[0] == begin[1]:
            continue
        else:
            break
    return begin


def give(hand):
    while True:
        value = cards[random.randint(0, len(cards) - 1)]
        if value not in hand:
            break
    return value


def add(hand):
    total = 0
    for i in range(len(hand)):
        total += values[cards.index(hand[i])]
    return total


cards = ['10 of Hearts', '9 of Hearts', '8 of Hearts', '7 of Hearts', '6 of Hearts',
             '5 of Hearts', '4 of Hearts', '3 of Hearts', '2 of Hearts', 'Ace of Hearts',
             'King of Hearts', 'Queen of Hearts', 'Jack of Hearts', '10 of Diamonds',
             '9 of Diamonds', '8 of Diamonds', '7 of Diamonds', '6 of Diamonds', '5 of Diamonds',
             '4 of Diamonds', '3 of Diamonds', '2 of Diamonds', 'Ace of Diamonds', 'King of Diamonds',
             'Queen of Diamonds', 'Jack of Diamonds', '10 of Clubs', '9 of Clubs', '8 of Clubs',
             '7 of Clubs', '6 of Clubs', '5 of Clubs', '4 of Clubs', '3 of Clubs', '2 of Clubs',
             'Ace of Clubs', 'King of Clubs', 'Queen of Clubs', 'Jack of Clubs', '10 of Spades',
             '9 of Spades', '8 of Spades', '7 of Spades', '6 of Spades', '5 of Spades',
             '4 of Spades', '3 of Spades', '2 of Spades', 'Ace of Spades', 'King of Spades',
             'Queen of Spades', 'Jack of Spades']
values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7,
             6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1,
             10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10]

user = restart()
computer = restart()

while True:
    print("Player hand: {} is worth {}".format(user, add(user)))
    choice = str(input("(h)it or (s)tand? "))
    if choice == 'h':
        card = give(user)
        print("You drew {}".format(card))
        user.append(card)
        if add(user) > 21:
            print("Player hand: {} is worth {}".format(user, add(user)))
            print("\nBust!")
            print("Computer wins!")
            user = restart()
            computer = restart()
            print("\n==================== RESTART ====================\n")
            continue
        elif add(user) == 21:
            print("Player hand: {} is worth {}".format(user, add(user)))
            print("\nPlayer got {}! Blackjack!".format(add(user)))
            print("\n==================== RESTART ====================\n")
            continue
    elif choice == 's':
        if add(computer) > add(user):
            print("\nComputer hand: {} is worth {}".format(computer, add(computer)))
            print("\nComputer wins!")
            user = restart()
            computer = restart()
            print("\n==================== RESTART ====================\n")
            continue
        print("\nComputer hand: {} is worth {}".format(computer, add(computer)))
        while add(computer) <= add(user):
            card = give(computer)
            computer.append(card)
            print("Computer drew {}".format(card))
            print("Computer hand: {} is worth {}".format(computer, add(computer)))
            if add(computer) > 21:
                print("\nBust!")
                print("Player wins!")
                break
            elif add(computer) > add(user):
                if add(computer) == 21:
                    print("\nComputer got {}! Blackjack!".format(add(computer)))
                else:
                    print("\nComputer wins!")
                break
        if add(user) > add(computer):
            if add(user) == 21:
                print("\nPlayer got {}! Blackjack!".format(add(user)))
            else:
                print("\nPlayer wins!")
        user = restart()
        computer = restart()
        print("\n==================== RESTART ====================\n")
        continue
