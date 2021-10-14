
import game_logic as gl
import display
import text_content as tct
import time
import random




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
    self.maker_code = self.create_code().split("//")
    display.show_code(self.maker_code)
    print(tct.turn_message('code_displayed'))
    self.find_code_numbers()
    self.find_code_order()
    self.computer_game_over(self.code_permutations[0])
  

  def create_code(self):
    code_input = input()
    if code_input.match("/^[1-6]{4}$/"):
      return code_input
    print(tct.warning_message('code_error'))
    self.create_code()

  def find_code_numbers(self):
    numbers = ['1', '2', '3', '4', '5', '6']
    options = random.shuffle(numbers)
    self.turn_count = 1
    self.find_code_guesses = []
    self.four_numbers = self.find_four_numbers(options)

  def find_four_numbers(self, options, index = 0, guess = []):
    if self.turn_count != 1:
      guess.pop(4 - self.total_number)
    if guess.len() != 4:
      guess << options[index] 
    self.computer_turn(self.maker_code, guess)
    self.turn_count += 1
    if self.total_number == 4:
      return guess
    else:
      self.find_four_numbers(options, index + 1, guess)
  

  def computer_turn(self, master, guess):
    print(tct.turn_message('computer', self.turn_count))
    time.sleep(1)
    display.show_code(guess)
    self.exact_number, self.same_number, self.total_number = gl.compare(master, guess)
    display.show_clues(self.exact_number, self.same_number)
    current_guess = guess.clone
    self.find_code_guesses.append([current_guess, self.exact_number, self.same_number])
  

  def find_code_order(self):
    self.code_permutations = self.create_permutations(self.four_numbers)
    self.code_permutations = set(self.code_permutations)
    self.compare_previous_guesses()
    self.final_turns()
  

  def create_permutations(array):
    array.permutation.to_a
  

  def compare_previous_guesses(self):
    for code in self.find_code_guesses:
      self.compare_permutations(code)


  def compare_permutations(self,code):
    self.run_permutations(code[0], code[1], code[2])


  def run_permutations(self,code, exact, same):
    for perm in self.code_permutations:
      gl.compare(perm, code)
      if not self.exact_number == exact and self.same_number == same:
        self.reduce_perms(perm)


  def reduce_perms(self, code):
    self.code_permutations = list(filter(lambda x: (x==code), self.code_permutations))


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

