from random import randint, shuffle
from collections import deque
from fields import fields


def dice_roll(eyes=4):
  """Return result of a random dice roll with the number of eyes specified."""
  return randint(1, eyes)


def go_to_jail():
  """Return jail position."""
  return field_name_to_pos['JAIL']


def advance_pos(pos, advance):
  """Return the advanced position wrapped around the end."""
  return (pos + advance) % len(fields)


def apply_community_card(pos):
  """Return position after applying the community card."""
  card = community_cards.popleft()
  community_cards.append(card)

  if card == 'NO_EFFECT':
    return pos
  else:
    return field_name_to_pos[card]


def apply_chance_card(pos):
  """Return position after applying the chance card."""
  card = chance_cards.popleft()
  chance_cards.append(card)

  if card == 'NO_EFFECT':
    return pos
  elif card == '-3':
    return move(advance_pos(pos, -3), advanced=True)
  elif card == 'R':
    while not fields[pos][0] == 'R':
      pos = advance_pos(pos, 1)
    return pos
  elif card == 'U':
    while not fields[pos][0] == 'U':
      pos = advance_pos(pos, 1)
    return pos
  else:
    return field_name_to_pos[card]


def move(pos, advanced=None):
  """Roll the dice and make move, return resulting position."""
  if advanced is None:
    roll1, roll2 = dice_roll(), dice_roll()

    if roll1 == roll2:
      consecutive_doubles.append((roll1, roll2))
      if len(consecutive_doubles) == 3:
        consecutive_doubles.clear()
        return go_to_jail()
    else:
      consecutive_doubles.clear()

    pos = advance_pos(pos, roll1+roll2)

  if 'CC' in fields[pos]:
    return apply_community_card(pos)
  elif 'CH' in fields[pos]:
    return apply_chance_card(pos)
  elif 'G2J' in fields[pos]:
    return go_to_jail()
  else:
    return pos


if __name__ == '__main__':
  print(fields)
  field_name_to_pos = {name: i for i, name in enumerate(fields)}
  community = ['GO', 'JAIL'] + 14*['NO_EFFECT']
  shuffle(community)
  chance = ['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1', 'R', 'R', 'U', '-3'] + 6*['NO_EFFECT']
  shuffle(chance)
  community_cards = deque(community)
  chance_cards = deque(chance)

  pos_counter = dict()
  number_of_moves = 1000000
  pos = 0
  consecutive_doubles = []
  for _ in range(number_of_moves):
    pos = move(pos)
    if pos in pos_counter:
      pos_counter[pos] = pos_counter[pos] + 1
    else:
      pos_counter[pos] = 1

  print(len(list(pos_counter.items())))
  # print(sorted([(fields[pos], count/number_of_moves) for pos, count in pos_counter.items()], key=lambda x: x[1], reverse=True))
  print(sorted([(pos, count/number_of_moves) for pos, count in pos_counter.items()], key=lambda x: x[1], reverse=True))
