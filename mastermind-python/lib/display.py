# frozen_string_literal: true

# module with display information for game
class Display:
  def code_colors(number):
    return {
      '1': "\e[101m  1  \e[0m ",
      '2': "\e[43m  2  \e[0m ",
      '3': "\e[44m  3  \e[0m ",
      '4': "\e[45m  4  \e[0m ",
      '5': "\e[46m  5  \e[0m ",
      '6': "\e[41m  6  \e[0m ",
    }[number]

  def clue_colors(clue):
    return {
      '*': "\e[91m\u25CF\e[0m ",
      '?': "\e[37m\u25CB\e[0m "
    }[clue]

  def show_code(array):
    for num in len(array):
      print(Display.code_colors(num))

  def show_clues(exact, same):
    print('  Clues: ')
    for _ in exact:
      print(Display.clue_colors('*'))
    for _ in same:
      print(Display.clue_colors('?'))
    print('')