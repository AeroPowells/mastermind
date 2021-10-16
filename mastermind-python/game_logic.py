# game logic for human_solver and computer_solver
import text_content as tct
import game



def compare(compare_master,compare_guess):
  temp_master = compare_master.copy()
  temp_guess = compare_guess.copy()
  exact_number = exact_matches(temp_master, temp_guess)
  same_number = right_numbers(temp_master, temp_guess)
  total_number = exact_number + same_number
  return [exact_number,same_number,total_number]

def exact_matches(exact_master, exact_guess):
  exact = 0
  for index, items in enumerate(exact_master):
    if items == exact_guess[index]:
      exact += 1
      exact_master[index] = '*'
      exact_guess[index]  = '*'
  return exact

def right_numbers(master, guess):
  same = 0
  for index, items in enumerate(guess):
    if guess[index] != '*' and guess[index] in master:
      same += 1
      remove = master.index(guess[index])
      master[remove] = '?'
      guess[index] = '?'

  return same


def repeat_game():
  print(tct.game_message('repeat_prompt'))
  replay = input()
  if replay.lower() != 'y':
    print(tct.game_message('thanks'))
  if replay.lower() == 'y':
    game.play()