import game_logic as gl
import display
import text_content as tct
import random
import re
# class for code_breaker game option
class HumanSolver():
  def __init__(self):
    self.computer_code = [str(random.randint(1,6)),str(random.randint(1,6)),str(random.randint(1,6)),str(random.randint(1,6))]
    self.guess = None
    self.exact_number = None
    self.same_number = None

  def player_turns(self):
    print(tct.turn_message('breaker_start'))
    self.turn_order()
    human_game_over(self.computer_code, self.guess)

  def turn_order(self):
    turn = 1
    while turn <= 12:
      turn_messages(turn)
      self.guess = list(player_input())
      turn += 1

      if self.guess[0].lower() == 'q':
        break
      display.show_code(self.guess)

      if self.computer_code == self.guess:
        break

      self.turn_outcome()

  def turn_outcome(self):
    self.exact_number, self.same_number, self.total_number = gl.compare(self.computer_code, self.guess)
    display.show_clues(self.exact_number, self.same_number)

def turn_messages(turn):
  print(tct.turn_message('guess_prompt', turn))
  if turn == 12:
    print(tct.warning_message('last_turn'))


def player_input():
  play_input = input()
  if play_input.lower() == 'q':
    return play_input
  if re.match("^[1-6]{4}$", str(play_input)):
    return play_input

    print(tct.warning_message('turn_error'))
    player_input()


def human_game_over(master, guess):
  if master == guess:
    print(tct.game_message('human_won'))
  else:
    print(tct.warning_message('game_over'))
    print(tct.game_message('display_code'))
    display.show_code(master)

  gl.repeat_game()