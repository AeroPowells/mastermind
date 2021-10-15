import game_logic as gl
import display
import text_content as tct
import random
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
    self.human_game_over(self.computer_code, self.guess)

  def turn_order(self):
    turn = 1
    while turn <= 12:
      tct.turn_messages(turn)
      self.guess = self.player_input.split("//")
      turn += 1

      if self.guess[0].lower == 'q':
        break
      display.show_code(self.guess)

      if self.computer_code == self.guess:
        break

      self.turn_outcome()

  def turn_outcome(self):
    gl.compare(self.computer_code, self.guess)
    display.show_clues(self.exact_number, self.same_number)

def turn_messages(turn):
  print(tct.turn_message('guess_prompt', turn))
  if turn == 12:
    print(tct.warning_message('last_turn'))


  def player_input():
    input = input()
    if input.lower() == 'q':
      return input
    if input.isnumeric():
      if all(int(c) <= 6 and int(c) >= 0 for c in str(input)) and len(input) == 4:
        return input

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