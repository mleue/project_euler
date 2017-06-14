from collections import Counter

card_value_to_numeric = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
  }
card_numeric_to_value = {n: v for v, n in card_value_to_numeric.items()}

class PokerCard:
  def __init__(self, card_string):
    self.value = card_string[0]
    self.suit = card_string[1]

def hand_to_cards(card_string_list):
  """return a list of poker cards from a string description of a hand"""
  return sort_hand((PokerCard(card_string) for card_string in card_string_list))

def sort_hand(hand):
  """return sorted hand"""
  return sorted(hand, key=lambda card: card_value_to_numeric[card.value])

def is_royal_flush(hand):
  """return True if the hand is a royal flush"""
  values = ['T', 'J', 'Q', 'K', 'A']
  if not len(set((card.suit for card in hand))) == 1:
    return False
  for value, card in zip(values, hand):
    if not value == card.value:
      return False
  return True

def is_straight_flush(hand):
  """return True if the hand is a straight flush"""
  lowest_value_numeric = card_value_to_numeric[hand[0].value]
  try:
    values = [card_numeric_to_value[n] for n in range(lowest_value_numeric, lowest_value_numeric+5)]
  except KeyError:
    return False
  if not len(set((card.suit for card in hand))) == 1:
    return False
  for value, card in zip(values, hand):
    if not value == card.value:
      return False
  return True

def is_n_of_a_kind(hand, n):
  """return True if the hand is n of a kind"""
  value_counter = Counter((card.value for card in hand))
  if any((count == n for count in value_counter.values())):
    return card_value_to_numeric[[value for value, count in value_counter.items() if count == n][0]]
  else:
    return False

def is_n_of_a_suit(hand, n):
  """return True if the hand is n of a kind"""
  suit_counter = Counter((card.suit for card in hand))
  return any((count == n for count in suit_counter.values()))

def is_four_of_a_kind(hand):
  """return True if the hand is four of a kind"""
  return is_n_of_a_kind(hand, 4)

def is_full_house(hand):
  """return True if the hand is three of a kind and a pair"""
  return is_n_of_a_kind(hand, 3) and is_n_of_a_kind(hand, 2)

def is_flush(hand):
  """return True if the hand is a flush"""
  return is_n_of_a_suit(hand, 5)

def is_straight(hand):
  """return True if the hand is a straight"""
  lowest_value_numeric = card_value_to_numeric[hand[0].value]
  try:
    values = [card_numeric_to_value[n] for n in range(lowest_value_numeric, lowest_value_numeric+5)]
  except KeyError:
    return False
  for value, card in zip(values, hand):
    if not value == card.value:
      return False
  return True

def is_three_of_a_kind(hand):
  """return True if the hand is three of a kind"""
  return is_n_of_a_kind(hand, 3)

def is_two_pairs(hand):
  """return True if the hand is two pairs"""
  value_counter = Counter((card.value for card in hand))
  return sorted(value_counter.values()) == [1, 2, 2]

def is_pair(hand):
  """return True if the hand is a pair"""
  return is_n_of_a_kind(hand, 2)

def get_high_card(hand):
  """pop and return highest card from a hand"""
  high_card = max(hand, key=lambda card: card_value_to_numeric[card.value])
  return hand.pop(hand.index(high_card))

def get_hand_rating(hand):
  """return the rating of a hand"""
  rating = None
  rating = is_royal_flush(hand)
  if rating:
    return 9
  rating = is_straight_flush(hand)
  if rating:
    return 8
  rating = is_four_of_a_kind(hand)
  if rating:
    return 7 + rating/100
  rating = is_full_house(hand)
  if rating:
    return 6
  rating = is_flush(hand)
  if rating:
    return 5
  rating = is_straight(hand)
  if rating:
    return 4
  rating = is_three_of_a_kind(hand)
  if rating:
    return 3 + rating/100
  rating = is_two_pairs(hand)
  if rating:
    return 2
  rating = is_pair(hand)
  if rating:
    return 1 + rating/100
  else:
    return 0

if __name__ == '__main__':
  player1_win_count = 0
  with open('p054_poker.txt') as f:
    for line in f:
      card_string_list = line.split()
      hand1 = hand_to_cards(card_string_list[:5])
      hand2 = hand_to_cards(card_string_list[5:])
      hand1_rating = get_hand_rating(hand1)
      hand2_rating = get_hand_rating(hand2)
      if hand1_rating > hand2_rating:
        player1_win_count += 1
      elif hand1_rating == hand2_rating:
        while hand1_rating == hand2_rating:
          hand1_high_card = get_high_card(hand1)
          hand2_high_card = get_high_card(hand2)
          hand1_rating = card_value_to_numeric[hand1_high_card.value]
          hand2_rating = card_value_to_numeric[hand2_high_card.value]
        if hand1_rating > hand2_rating:
          player1_win_count += 1

  print(player1_win_count)
