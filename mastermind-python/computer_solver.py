
import game_logic as gl
import display
import text_content as tct
import time
import random
import re
import itertools



# class for code_maker game option
class ComputerSolver:
  # attr_reader :maker_code, :turn_count, :exact_number, :same_number,
  #             :total_number, :find_code_guesses, :four_numbers
  def __init__(self):
    self.maker_code = None
    self.turn_count = 1
    self.find_code_guesses = []
    self.four_numbers = []
    self.code_permutations = None
    self.exact_number = None
    self.same_number = None
    self.total_number = None

  def computer_start(self):
    print(tct.turn_message('code_prompt'))
    self.maker_code = list(self.create_code())
    display.show_code(self.maker_code)
    print(tct.turn_message('code_displayed'))
    self.find_code_numbers()
    if self.four_numbers == self.maker_code:
        self.computer_game_over(self.four_numbers)
    self.find_code_order()
    self.computer_game_over(self.code_permutations[0])

  def create_code(self):
    code_input = input()
    if re.match("^[1-6]{4}$",code_input):
      return code_input
    print(tct.warning_message('code_error'))
    self.create_code()

  def find_code_numbers(self):
    numbers = ['1', '2', '3', '4', '5', '6']
    random.shuffle(numbers)
    self.turn_count = 1
    self.find_code_guesses = []
    self.four_numbers = self.find_four_numbers(numbers)

  def find_four_numbers(self, options, index = 0, guess = []):
    if self.turn_count != 1:
      for _ in range(4-self.total_number):
        guess.pop()
    while True:
      if len(guess) == 4:
        break
      guess.append(options[index])
    self.computer_turn(self.maker_code, guess)
    self.turn_count += 1
    if self.total_number == 4:
      return guess

    return self.find_four_numbers(options, index + 1, guess)

  def computer_turn(self, master, guess):
    print(tct.turn_message('computer', self.turn_count))
    time.sleep(1)
    display.show_code(guess)
    self.exact_number, self.same_number, self.total_number = gl.compare(master, guess)
    display.show_clues(self.exact_number, self.same_number)
    current_guess = guess.copy()
    self.find_code_guesses.append([current_guess, self.exact_number, self.same_number])

  def find_code_order(self):
    self.code_permutations = self.create_permutations(self.four_numbers)
    self.code_permutations = remove_duplicates(self.code_permutations)
    self.compare_previous_guesses()
    self.final_turns()
  
  @staticmethod
  def create_permutations(array):
    return list(itertools.permutations(array))

  def compare_previous_guesses(self):
    for code in self.find_code_guesses:
      self.compare_permutations(code)


  def compare_permutations(self,code):
    self.run_permutations(code[0], code[1], code[2])

  def run_permutations(self,code, exact, same):
    for perm in self.code_permutations:
      exact_number,same_number, _ = gl.compare(perm, code)
      if exact_number != exact or same_number != same:
        self.reduce_perms(perm)


  def reduce_perms(self, code):
    for index, perm in enumerate(self.code_permutations):
      if perm == code:
        self.code_permutations.pop(index)


  def final_turns(self):
    while self.turn_count < 12:
      self.computer_turn(self.maker_code, self.code_permutations[0])
      self.turn_count += 1
      if self.maker_code == self.code_permutations[0]:
        break

      self.run_permutations(self.code_permutations[0], self.exact_number, self.same_number)


  def computer_game_over(self, guess):
    if self.maker_code == guess:
      self.computer_won()
    else:
      print(tct.game_message('computer_lost'))
    gl.repeat_game()


  def computer_won(self):
    if self.turn_count <= 6:
      print(tct.computer_won_message('inconceivable'))
    elif self.turn_count in range(7, 11):
      print(tct.computer_won_message('won'))
    elif  self.turn_count == 12:
      print(tct.computer_won_message('close'))

def remove_duplicates(array) -> list:
  tpls = [tuple(x) for x in array]
  dct = list(dict.fromkeys(tpls))
  duplicate_free = [list(x) for x in dct]
  return duplicate_free