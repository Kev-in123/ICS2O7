import random

def game(player1, player2, player3):
  all_rolls = [random.randint(1, 6) + random.randint(1, 6) for i in range(3)]
  while all_rolls[0] == all_rolls[1] or all_rolls[0] == all_rolls[2] or all_rolls[1] == all_rolls[2]:
    all_rolls = [random.randint(1, 6) + random.randint(1, 6) for i in range(3)]
  
  players = [player1, player2, player3]
  highestroll = max(all_rolls)
  return f"The highest roll is {highestroll} and was rolled by {players[all_rolls.index(highestroll)]}\n{players[0]} rolled: {all_rolls[0]}\n{players[1]} rolled: {all_rolls[1]}\n{players[2]} rolled: {all_rolls[2]}"

name1 = str(input("Enter player ones name: "))
name2 = str(input("Enter player twos name: "))
name3 = str(input("Enter player threes name: "))

print(game(name1, name2, name3))
