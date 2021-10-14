from game_logic import GameLogic as gl
from display import Display
from text_content import TextContent as tct
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
      self.guess = player_input.split("//")
      turn += 1

      if self.guess[0].downcase == 'q':
        break
      Display.show_code(self.guess)

      if self.computer_code == self.guess:
        break

      self.turn_outcome()

  def turn_messages(turn):
    print(tct.turn_message('guess_prompt', turn))
    if turn == 12
    print(tct.TextContent.warning_message('last_turn'))
  end

  def player_input
    input = gets.chomp
    return input if input.match(/^[1-6]{4}$/)
    return input if input.downcase == 'q'

    puts warning_message('turn_error')
    player_input
  end

  def turn_outcome
    compare(computer_code, guess)
    show_clues(exact_number, same_number)
  end

  def human_game_over(master, guess)
    if master == guess:
      print(game_message('human_won'))
    else:
      print(tct.warning_message('game_over'))
      puts game_message('display_code')
      show_code(master)

    repeat_game