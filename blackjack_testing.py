# Name: Alisha Gursahaney
# Net Id: amg9zd

import blackjack

print(blackjack.card_to_value("2"))
print(blackjack.card_to_value("Q"))
print(blackjack.card_to_value("A"))

hand1 = "AJ"
hand2 = "27T"
hand3 = "KAA"

print("Hand 1 hard:", blackjack.hard_score(hand1), "- soft:", blackjack.soft_score(hand1))
print("Hand 2 hard:", blackjack.hard_score(hand2), "- soft:", blackjack.soft_score(hand2))
print("Hand 3 hard:", blackjack.hard_score(hand3), "- soft:", blackjack.soft_score(hand3))