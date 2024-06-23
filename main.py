#Jesse Warren, 3-22-23
#Uno! 
import random
import time
#These lists are used for varoius things, as they contain all the necessary values for cards excluding wilds. 
color_list = ["red", "yellow", "green", "blue"]
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "skip", "draw 2"] 

class Deck:
  def __init__(self, card_list):
    self.card_list = card_list
  def fill_deck(self):
    for x in range(2):
      for color in color_list:
        for num in num_list:
          self.card_list.append((color, num))
      #Don't mind the double spaces before wild card names in printings. 
      for y in range(2):
        self.card_list.append(("", "draw 4"))
        self.card_list.append(("", "wild"))
      self.card_list.append(("", "trade hands"))
  def first_card(self):
    one_card = ("", "")
    #This loop makes sure that a number card is chosen. 
    while type(one_card[1]) != int:
      one_card = random.choice(self.card_list)
    global up_card
    up_card = one_card
    self.card_list.remove(one_card)

class Hand:
  def __init__(self, cards):
    self.cards = cards
  def draw_card(self):
    #Picks a card from the deck, adds it to the hand, and removes it from the deck.   
    one_card = random.choice(deck.card_list)
    self.cards.append(one_card)
    deck.card_list.remove(one_card)
  def play_card(self, upcard, card_choice):
    discard_pile.dese_cards.append(upcard)
    global up_card
    up_card = self.cards[card_choice]
    self.cards.pop(card_choice)
  def check_hand(self):
    print("Your hand has", end = " ")
    for x in range(len(self.cards)):
      card = self.cards[x]
      #This whole mess is for the sake of grammar, so that there is an "and" between the second-to-last and last cards, and a period at the end. 
      if x == (len(self.cards) - 1):
        print("a " + str(card[0]) + " " + str(card[1]) + ".")
      else:
        print("a " + str(card[0]) + " " + str(card[1]) + ",", end = " ")
      if x == (len(self.cards) - 2): 
        print("and", end = " ")
    print()
    time.sleep(wait_time * 3)

class Discard: 
  def __init__(self, dese_cards):
    self.dese_cards = dese_cards
  #This function has yet to be used. 
  def empty(self, dese_cards):
    for x in range(len(self.dese_cards)):
      one_card = random.choice(self.dese_cards)
      deck.card_list.append(one_card)
      self.dese_cards.remove(one_card)
    print(len(self.dese_cards))

def best_of_same_nums(playcard_nums, numbers, playable_cards):
  #The place in your hand and then the full cards of the two best cards to play with the same number. 
  best_playcards = [playcard_nums[numbers[-1]], playcard_nums[numbers[-2]]]
  best_playcards_full = [comp.cards[best_playcards[0]], comp.cards[best_playcards[1]]]
  best_colors = []
  for card in best_playcards_full:
    best_colors.append(card[0])
  hand_colors = []
  for card in comp.cards:
    hand_colors.append(card[0])
  color_count = {}
  #So color_count is {name of a color: how many cards of that color are in the hand}. 
  for color in color_list:
    color_count[color] = hand_colors.count(color)
  #Get the the number of occurances of the colors of the best playable cards, and play the card that has the most prevalent color. 
  best_color_count = [color_count.get(best_colors[0]), color_count.get(best_colors[1])]
  if best_color_count[0] > best_color_count[0]:
    num_choice = -1
  else:
    num_choice = -2
  card_choice = playcard_nums.get(numbers(num_choice))
  return card_choice

def full_player_draw_card():
  print("You cannot play any cards. ")
  print()
  time.sleep(wait_time)
  skip = False
  player.draw_card()
  card_choice = -1
  choice_card = player.cards[-1]
  #Standard checking if you can play the card you drew. 
  if choice_card[0] == up_card[0] or choice_card[1] == up_card[1] or choice_card[0] == "":
    print("You can play the " + str(choice_card[0]) + " " + str(choice_card[1]) + " that you drew. ")
    print()
    time.sleep(wait_time)
    player.play_card(up_card, card_choice)
    if type(up_card[1]) == str:
      skip = special_card(player, comp, up_card[1])
  else:
    print("You draw a " + str(choice_card[0]) + " " + str(choice_card[1]) + ". ")
    print()
    time.sleep(wait_time)
  return skip

def full_comp_draw_card():
  comp.draw_card()
  print("The computer draws a card. ")
  print()
  time.sleep(wait_time)
  skip = False
  card_choice = -1
  choice_card = comp.cards[card_choice]
  #Same as for player. 
  if choice_card[0] == up_card[0] or choice_card[1] == up_card[1] or choice_card[0] == "":
    comp.play_card(up_card, card_choice)
    print("The computer played the card that it drew, a " + str(choice_card[0]) + " " + str(choice_card[1]) + ". ")
    print()
    time.sleep(wait_time)
    if type(up_card[1]) == str:
      skip = special_card(comp, player, up_card[1])
  return skip
    
def player_play(playable_cards):
  card_choice = input("Which card will you play? Enter the number that corresponds to its place in the order your cards were listed in. ")
  print()
  while True:
    try:
      if (int(card_choice) - 1) in playable_cards:
        #The minus 1 is for the indeces starting at 0. 
        card_choice = int(card_choice) - 1
        player.play_card(up_card, card_choice)
        skip = False
        if type(up_card[1]) == str:
          skip = special_card(player, comp, up_card[1])
        break
      else:
        card_choice = invalid_input(card_choice)
    except:
      card_choice = invalid_input(card_choice)
  return skip

def comp_play(playable_cards):
  playcard_nums = {}
  #Getting {the card's color: its placement in the hand}. 
  for x in playable_cards:
    card = comp.cards[x]
    playcard_nums[card[1]] = (x)
  numbers = list(playcard_nums.keys())
  special = False
  #Check for special cards, and if there are any, remove non-special cards from playing candidates. 
  for key in numbers:
    if type(key) == str:
      special = True
  if special == True:
    remove_list = []
    for key in numbers:
      if type(key) == int:
        remove_list.append(key)
    for key in remove_list:
      numbers.remove(key)
    #It just works out that sorting reversed works to have the right priority order. 
    numbers.sort(reverse = True)
  else:
    numbers.sort()
  if len(numbers) > 1:
    #It makes strategic sense to, if one has multiple playable cards with the same value, play the card that would lead to letting you play more cards on future turns. 
    if numbers[-1] == numbers[-2]:
      card_choice = best_of_same_nums(playcard_nums, numbers, playable_cards)
      comp.play_card()
    else:
      card_choice = playcard_nums[numbers[-1]]
      comp.play_card(up_card, card_choice)
  else:
    card_choice = playcard_nums[numbers[-1]]
    comp.play_card(up_card, card_choice)
  skip = False
  print("The computer plays a " + str(up_card[0]) + " " + str(up_card[1]) + ". ")
  print()
  time.sleep(wait_time)
  if type(up_card[1]) == str:
    skip = special_card(comp, player, up_card[1])
  return skip

def draw_re(type, target):
  playable_cards = []
  global times
  #This weird thing is to check if the variable times exists, and if not, define it. 
  try:
    if times > 1:
      pass
  except:
    times = 1
  for x in range(len(target.cards)):
    card = target.cards[x]
    if card[1] == type:
      playable_cards.append(x)
  if len(playable_cards) > 0:
    print("The draw can be deflected! ")
    print()
    time.sleep(wait_time)
    #times is used to track how many times a draw has been deflected. 
    times += 1
    if target == player:
      player.check_hand()
      player_play(playable_cards)
    else:
      comp_play(playable_cards)
  else:
    for x in range(int(type[-1]) * times):
      target.draw_card()
      #Tell the player what they drew. Could be improved by making it all one sentence like check_hand(). 
      if target == player:
        new_card = player.cards[-1]
        print("You draw a " + str(new_card[0]) + " " + str(new_card[1]) + ". ")
        time.sleep(wait_time)
    if target == player:
      print()

def choose_color(who, type):
  global up_card
  if who == player:
    color_choice = input("What color will you make it? Type your answer using only lowercase characters. ")
    print()
    while True:
      if color_choice in color_list:
        up_card = (color_choice, "any")
        break
      else:
        color_choice = invalid_input(color_choice)
  else:
    hand_colors = []
    #Gets how many of each color are in the computer's hand, and then the computer chooses the color that it has the most of. 
    for card in comp.cards:
      #So "" isn't appended if the computer has another wild card. 
      if card[0] in color_list:
        hand_colors.append(card[0])
    color_dict = {}
    for color in color_list:
      color_dict[hand_colors.count(color)] = color
    color_nums = list(color_dict.keys())
    #Since the computer is going to give its hand to the player, it should make the color one that it has the least of. 
    if type == "trade hands":
      color_nums.sort(reverse = True)
    else:
      color_nums.sort()
    up_card = (color_dict[color_nums[-1]], "any")
    print("The computer makes it " + str(up_card[0]) + ". ")
    print()
    time.sleep(wait_time)
  
#This function is a dispatcher for the different things that special cards can do. 
def special_card(who, target, type):
  if type == "draw 4" or type == "wild" or type == "trade hands":
    choose_color(who, type)
  if type == "draw 2" or type == "draw 4":
    draw_re(type, target)
  if type == "trade hands":
    save_cards = list(who.cards)
    who.cards = list(target.cards)
    target.cards = list(save_cards)
  #All the other special cards skip. 
  if type != "trade hands" and type != "wild": 
    skip = True
  else:
    skip = False
  try:
    #If a draw has been deflected an even number of times, it's like it doesn't skip the other person, at least in terms of this code. 
    if type((times + 1) / 2) == float:
      skip = False
  except:
    pass
  return skip

def invalid_input(var):
  var = input("That is not a valid input. Please try again. ")
  print()
  return var

def turn(who):
  if up_card[1] == "any":
    print("Any " + str(up_card[0]) + " card can be played. ")
  else:
    print("The card that is face up is a " + str(up_card[0]) + " " + str(up_card[1]) + ". ")
  print()
  time.sleep(wait_time)
  if who == player:
    who.check_hand()
  playable_cards = []
  for x in range(len(who.cards)):
    card = who.cards[x]
    if card[0] == up_card[0] or card[1] == up_card[1]:
      playable_cards.append(x)
  if len(playable_cards) == 0:
    #Letting you play wild cards if you can't play anything else. 
    for x in range(len(who.cards)):
      card = who.cards[x]
      if card[0] == "":
        playable_cards.append(x)
  skip = False  
  if len(playable_cards) > 0: 
    if who == player:
      skip = player_play(playable_cards)
    else:
      skip = comp_play(playable_cards)
  else:
    if who == player:
      skip = full_player_draw_card()
    else:
      skip = full_comp_draw_card()
  if len(who.cards) == 1:
    print("Uno! ")
    print()
    time.sleep(wait_time)
  if who == comp and len(who.cards) > 1:
    print("The computer has " + str(len(who.cards)) + " cards in its hand. ")
    print()
    time.sleep(wait_time)
  if len(deck.card_list) == 0:
    discard_pile.empty()
  #"Skips" the other player's turn. 
  if skip == True:
    turn(who)
      
wait_time = input("How long, in seconds, do you want the program to delay between printing? This number will be tripled for right after your hand is printed. ")
print()
while True:
  try:
    wait_time = float(wait_time)
    break
  except:
    wait_time = invalid_input(wait_time)
#Setting up all the objects. 
player = Hand([])
comp = Hand([])
deck = Deck([])
discard_pile = Discard([])
deck.fill_deck()
for x in range(7):
  player.draw_card()
  comp.draw_card()
deck.first_card()
going = True 
while going == True: 
  turn(player)
  if len(player.cards) == 0:
    going = False
    break
  turn(comp)
  if len(comp.cards) == 0:
    going = False
    break
if len(player.cards) == 0:
  loser = comp
  print("The player wins", end = " ")
else:
  loser = player
  print("The computer wins", end = " ")
loser_points = 0
for card in loser.cards:
  if type(card[1]) == str:
    card = [card[0], card[1]]
    #Special cards are worth twenty points. 
    card[1] = 20
  loser_points += card[1]
if loser_points == 1:
  print("by " + str(loser_points) + " point! ")
else:
  print("by " + str(loser_points) + " points! ")