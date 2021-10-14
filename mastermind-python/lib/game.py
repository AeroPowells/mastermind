import text_instructions as tit
import text_content as tct
import display
import computer_solver as cs
import human_solver as hs

# main class that starts the game
def play():
  print(tit.instructions())
  game_mode = mode_selection()
  if game_mode == '1':
    code_maker()
  if game_mode == '2':
    code_breaker()

def mode_selection():
  input = input()
  if input.match("/^[1-2]$/"):
    return input
  print(tct.warning_message('answer_error'))
  mode_selection()

def code_maker():
  maker = cs.ComputerSolver()
  maker.computer_start()

def code_breaker():
  breaker = hs.HumanSolver()
  breaker.player_turns()
