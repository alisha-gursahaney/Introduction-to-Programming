# Name: Alisha Gursahaney
# Net Id: amg9zd

def card_to_value(card):
    '''

    :param card: str variable card representing a single card in blackjack
    :return: numeric blackjack score of the card
    '''
    if card == "A":
        return 1
    elif card == "T" or card == "J" or card == "Q" or card == "K":
        return 10
    else:
        return int(card)


def hard_score(hand):
    '''

    :param hand: blackjack hand as a str
    :return: the “hard” score of the hand, where all aces are treated as one
    '''
    hand = list(hand)
    new_hand = [card_to_value(card) for card in hand]
    return sum(new_hand)


def soft_score(hand):
    '''

    :param hand: blackjack hand as a str
    :return: the “soft” score of the hand, where the first ace is treated as eleven
    '''
    if hand.count("A") != 0:
        hand = list(hand)
        where_A = hand.index("A")
        hand[where_A] = "11"
        new_hand = [card_to_value(card) for card in hand]
        return sum(new_hand)
    else:
        return hard_score(hand)

