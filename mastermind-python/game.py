from itertools import repeat
import text_instructions as tit
import text_content as tct
from game_logic import repeat_game
import computer_solver as cs
import human_solver as hs
import re

# main class that starts the game
def play():
    print(tit.instructions())
    game_mode = mode_selection()
    if game_mode == '1':
      code_maker()
    if game_mode == '2':
      code_breaker()


def mode_selection():
  text_input = input("Enter the mode selection ")
  it_is = re.match("^[1-2]{1}$",str(text_input))
  if it_is:
    return text_input
  print(tct.warning_message('answer_error'))
  return mode_selection()

def code_maker():
  maker = cs.ComputerSolver()
  maker.computer_start()

def code_breaker():
  breaker = hs.HumanSolver()
  breaker.player_turns()
