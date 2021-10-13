
import game_logic as gl
import display
import text_content as tct
import time




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
    self.maker_code = ComputerSolver.create_code().split("//")
    display.show_code(self.maker_code)
    print(tct.turn_message('code_displayed'))
    ComputerSolver.find_code_numbers()
    ComputerSolver.find_code_order()
    ComputerSolver.computer_game_over(self.code_permutations[0])
  

  def create_code():
    code_input = input()
    if code_input.match("/^[1-6]{4}$/"):
      return code_input
    print(tct.warning_message('code_error'))
    ComputerSolver.create_code()

  def find_code_numbers(self):
    numbers = %w[1 2 3 4 5 6]
    options = numbers.shuffle
    self.turn_count = 1
    self.find_code_guesses = []
    self.four_numbers = ComputerSolver.find_four_numbers(options)

  def find_four_numbers(self, options, index = 0, guess = []):
    if self.turn_count != 1:
      guess.pop(4 - self.total_number)
    if guess.len() != 4:
      guess << options[index] 
    ComputerSolver.computer_turn(self.maker_code, guess)
    self.turn_count += 1
    if self.total_number == 4:
      return guess
    else:
      ComputerSolver.find_four_numbers(options, index + 1, guess)
  

  def computer_turn(self, master, guess):
    print(tct.turn_message('computer', turn_count))
    time.sleep(1)
    display.show_code(guess)
    gl.compare(master, guess)
    display.show_clues(exact_number, same_number)
    current_guess = guess.clone
    self.find_code_guesses.append([current_guess, exact_number, same_number])
  

  def find_code_order(self):
    self.code_permutations = ComputerSolver.create_permutations(self.four_numbers)
    self.code_permutations = set(self.code_permutations)
    ComputerSolver.compare_previous_guesses()
    ComputerSolver.final_turns()
  

  def create_permutations(array):
    array.permutation.to_a
  

  def compare_previous_guesses(self):
    for code in self.find_code_guesses:
      ComputerSolver.compare_permutations(code)


  def compare_permutations(code):
    ComputerSolver.run_permutations(code[0], code[1], code[2])


  def run_permutations(self,code, exact, same):
    for perm in self.code_permutations:
      gl.compare(perm, code)
      if self.exact_number:
        ComputerSolver.reduce_perms(perm) exact_number == exact && same_number == same


  def reduce_perms(self, code):
    self.code_permutations.reject! do |perm|
      perm == code


  def final_turns(self):
    while self.turn_count < 12
      ComputerSolver.computer_turn(self.maker_code, self.code_permutations[0])
      self.turn_count += 1
      break if solved?(maker_code, @code_permutations[0])

      run_permutations(@code_permutations[0], exact_number, same_number)


  def computer_game_over(self, guess):
    if self.maker_code == guess:
      computer_won()
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
