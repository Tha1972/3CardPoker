import random

deck = ['2s', '2h', '2c', '2d',
        '3s', '3h', '3c', '3d',
        '4s', '4h', '4c', '4d',
        '5s', '5h', '5c', '5d',
        '6s', '6h', '6c', '6d',
        '7s', '7h', '7c', '7d',
        '8s', '8h', '8c', '8d',
        '9s', '9h', '9c', '9d',
        '10s', '10h', '10c', '10d',
        'Js', 'Jh', 'Jc', 'Jd',
        'Qs', 'Qh', 'Qc', 'Qd',
        'Ks', 'Kh', 'Kc', 'Kd',
        'As', 'Ah', 'Ac', 'Ad']

def restart_deck():
    global deck
    deck = ['2s', '2h', '2c','2d',
        '3s', '3h', '3c','3d',
        '4s', '4h', '4c','4d',
        '5s', '5h', '5c','5d',
        '6s', '6h', '6c','6d',
        '7s', '7h', '7c','7d',
        '8s', '8h', '8c','8d',
        '9s', '9h', '9c','9d',
        '10s', '10h', '10c','10d',
        'Js', 'Jh', 'Jc','Jd',
        'Qs', 'Qh', 'Qc','Qd',
        'Ks', 'Kh', 'Kc','Kd',
        'As', 'Ah', 'Ac','Ad',
        ]

#######################################################################################################################

def dealer():

    restart_deck()

    dealer_cards = []

    for i in range(3):

        new_card = deck[random.randint(0, 51-i)]
        dealer_cards.append(new_card)
        deck.remove(new_card)

    return dealer_cards

def player():

    restart_deck()

    player_cards = []

    for i in range(3):
        new_card = deck[random.randint(0, 51 - i)]
        player_cards.append(new_card)
        deck.remove(new_card)

    return player_cards

#######################################################################################################################

def flush_checker(hand):

    same_suit_num = []

    clubs = 0
    diamonds = 0
    hearths = 0
    spades = 0


    for i in hand:

        if len(i) == 2:
            if i[1] == 'c':
                clubs += 1
            elif i[1] == 'd':
                diamonds += 1
            elif i[1] == 's':
                spades += 1
            elif i[1] == 'h':
                hearths += 1
        else:
            if i[2] == 'c':
                clubs += 1
            elif i[2] == 'd':
                diamonds += 1
            elif i[2] == 's':
                spades += 1
            elif i[2] == 'h':
                hearths += 1

    same_suit_num.extend((clubs, hearths, spades, diamonds))

    if max(same_suit_num) == 3:
        return True
    else:
        return False

def tok_checker(hand):

    same_number_num = []

    for i in hand:
        if len(i) == 3:
            same_number_num.append('10')
        else:
            same_number_num.append(i[0])

    for i in range(2,11):
        if same_number_num.count(str(i)) == 3:
            return True

    if same_number_num.count('J') == 3:
        return True

    elif same_number_num.count('Q') == 3:
        return True

    elif same_number_num.count('K') == 3:
        return True

    elif same_number_num.count('A') == 3:
        return True

    else:
        return False

def straight_checker(hand):

    straight_num = []

    for i in hand:

        if i[0] == 'J':
            straight_num.append(11)
        elif i[0] == 'Q':
            straight_num.append(12)
        elif i[0] == 'K':
            straight_num.append(13)
        elif i[0] == 'A':
            straight_num.append(14)
        elif len(i) == 3:
            straight_num.append(10)
        else:
            straight_num.append(int(i[0]))

    straight_num.sort()

    if straight_num[1] - 1 == straight_num[0] and straight_num[1] == straight_num[2] - 1:
        return True
    else:
        return False

def straight_flush_checker(hand):
    if straight_checker(hand) and flush_checker(hand):
        return True
    else:
        return False

def royal_flush_checker(hand):
    if straight_flush_checker(hand):
        for i in hand:
            if 'A' in i:
                return True
    else:
        False

def pair_checker(hand):

    same_number_num = []

    for i in hand:
        if len(i) == 3:
            same_number_num.append('10')
        else:
            same_number_num.append(i[0])

    for i in range(2,11):
        if same_number_num.count(str(i)) == 2:
            return True

    if same_number_num.count('J') == 2:
        return True

    elif same_number_num.count('Q') == 2:
        return True

    elif same_number_num.count('K') == 2:
        return True

    elif same_number_num.count('A') == 2:
        return True

    else:
        return False

#######################################################################################################################

def value_dealer(d):

    if royal_flush_checker(d):
        return 7
    elif straight_flush_checker(d):
        return 6
    elif tok_checker(d):
        return 5
    elif straight_checker(d):
        return 4
    elif flush_checker(d):
        return 3
    elif pair_checker(d):
        return 2
    else:
        return 1

def value_player(p):

    if royal_flush_checker(p):
        return 7
    elif straight_flush_checker(p):
        return 6
    elif tok_checker(p):
        return 5
    elif straight_checker(p):
        return 4
    elif flush_checker(p):
        return 3
    elif pair_checker(p):
        return 2
    else:
        return 1

def winner(players, dealers):
    global dealer_deck
    global player_deck
    global player_wins
    global dealer_wins
    global tie_games
    global DNE

    confirm_count = 0

    point = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    final_dealer = []
    final_player = []

    #Checks if the dealer can play

    for i in dealers:
        if 'Q' in i or 'K' in i or 'A' in i:
            confirm_count += 1

    if confirm_count >= 1 or tok_checker(dealers) or pair_checker(dealers) or straight_checker(dealers) or flush_checker(dealers):

        #Checks who wins

        if value_dealer(dealers) > value_player(players):
            dealer_wins += 1
            return 0

        elif value_dealer(dealers) < value_player(players):
            player_wins += 1
            return 1

        # Check who wins if they both have same rank

        else:
            for i in dealers:
                if len(i) == 3:
                    final_dealer.append(8)
                else:
                    final_dealer.append(point.index(str(i[0])))

            for i in players:

                if len(i) == 3:
                    final_player.append(8)
                else:
                    final_player.append(point.index(str(i[0])))

            if int(max(final_dealer)) > int(max(final_player)):
                dealer_wins += 1
                return 0

            elif int(max(final_dealer)) < int(max(final_player)):
                player_wins += 1
                return 1

            else:
                final_dealer.sort()
                final_player.sort()

                if final_dealer[1] > final_player[1]:
                    dealer_wins += 1
                    return 0

                elif final_dealer[1] < final_player[1]:
                    player_wins += 1
                    return 1

                else:
                    if final_dealer[0] > final_player[0]:
                        dealer_wins += 1
                        return 0

                    elif final_dealer[0] < final_player[0]:
                        player_wins += 1
                        return 1

                    else:
                        tie_games += 1
                        return 2
    else:
        DNE += 1
        return 3

#######################################################################################################################

money = 1000
ante = 0

player_wins = 0
dealer_wins = 0
tie_games = 0
DNE = 0

count = 0

def play_game():

    global dealer_deck
    global money
    global ante

    player_deck = player()
    dealer_deck = dealer()

    #Making first bet
    print('')
    print("New Game")
    print('')
    print("Money:", money)

    ante = int(input("Ante: "))

    while ante > money/2:
        ante = int(input("Un valid number. Enter valid Ante: "))


    money -= ante

    print("Your deck", player_deck)

    cont = int(input('Fold(0) or Play(1): '))

    if int(cont) == 1:
        money -= ante
        return winner(player_deck, dealer_deck)
    else:
        return 10

def main():

    global money

    while money > 0:

        result = play_game()

        if result ==  1:
            money += (ante*4)
            print("You win! (+", ante*2, ") Money:", money)
            print('Dealers deck:', dealer_deck)

        elif result == 0:
            print("You lost! (-", ante*2, ") Money:", money)
            print('Dealers deck:', dealer_deck)

        elif result == 3:
            print("Dealer doesn't qualify!")
            print('Dealers deck:', dealer_deck)
            money += (ante*2)
            print("Money:", money)

        elif result == 10:
            print("You folded. -", ante)

        else:
            money += (ante * 2)
            print("Impossible tie game")
            print(dealer_deck)
            print(result)
main()



#######################################################################################################################
