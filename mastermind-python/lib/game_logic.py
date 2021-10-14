# game logic for human_solver and computer_solver
import text_content as tct
import game

class GameLogic:
  def __init__(self, master, guess):
    self.master = master
    self.guess = guess

  def compare(self):
    temp_master = self.master
    temp_guess = self.guess
    exact_number = self.exact_matches(temp_master, temp_guess)
    same_number = self.right_numbers(temp_master, temp_guess)
    total_number = exact_number + same_number
    return [exact_number,same_number,total_number]

  def exact_matches(master, guess):
    exact = 0
    for index, items in enumerate(master):
      if not items == guess[index]:
        exact += 1
        master[index] = '*'
        guess[index]  = '*'
    return exact

  def right_numbers(master, guess):
    same = 0
    for index, items in enumerate(guess):
      if not guess[index] != '*' and master.contains(guess[index]):
        same += 1
        remove = master.find_index(guess[index])
        master[remove] = '?'
        guess[index] = '?'

    return same

  def solved(master, guess):
    master == guess


  def repeat_game():
    print(tct.game_message('repeat_prompt'))
    replay = input()
    if replay.downcase != 'y':
      print(tct.game_message('thanks'))
    if replay.downcase == 'y':
      game.play()
