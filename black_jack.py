# globals

kind = {"heart", "diamond", "spade", "club"}
number = {"ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"}

deck = {(k, n) for k in kind for n in number}


# functions
def hand_value(hand):
    s = 0
    for card in hand:
        n = card[1]
        if n == "jack" or n == "queen" or n == "king":
            s += 10
        elif n == "ace":  # exw ena 8ema sxetika me to an o paixtis exei hdh tuxh figoura kai A kai meta ksana A
            if s > 10:  # alla logika lunetai automata gt an ekane 21 8a stamatage epitopou to paixnidi.
                s += 1  # px fila: {('diamond', 'jack'), ('spade', 'ace'), ('club', 'ace')}
            else:
                s += 11
        else:
            s += n
    return s


def player(hand):
    hand.add(deck.pop())
    hand.add(deck.pop())
    while True:
        print(hand, "Sum=", hand_value(hand))
        choice = input("h-hit or s-Stand: ")
        if choice == "h":
            hand.add(deck.pop())
            if hand_value(hand) >= 21:
                return hand_value(hand)
        elif choice == "s":
            return hand_value(hand)


def computer(value_player, hand):
    hand.add(deck.pop())
    hand.add(deck.pop())

    while True:
        value = hand_value(hand)

        if value >= 21:
            return value
        elif value >= value_player:
            return value
        else:
            hand.add(deck.pop())


# main

def main():
    rounds = 1
    score = [0, 0]

    while True:
        print("=" * 15)
        print("Round " + str(rounds))
        print("=" * 15)

        player_hand = set()
        player_value = player(player_hand)

        print(f"{player_hand} Sum: {player_value}")
        if player_value == 21:
            print("You WON!!")
            result = "Player"
        elif player_value > 21:
            print("You LOST!!")
            result = "Computer"
        else:
            print("Computer's Turn!!")
            computer_hand = set()
            computer_value = computer(player_value, computer_hand)
            print(f"{computer_hand} Sum: {computer_value}")
            if computer_value > 21:
                print("You WON!!")
                result = "Player"
            else:
                print("You LOST!!")
                result = "Computer"

        if result == "Player":
            score[0] += 1
        else:
            score[1] += 1

        print(f"Score: Player:{score[0]} - Computer:{score[1]}")
        choice = input("Do you want to play again? (y-YES or n-NO):")
        if choice == "n":
            break

        rounds += 1


main()
