from emoji import emojize

def code_colors(number):
  color_dict = {
    '1': "🔴",
    '2': "🔵",
    '3': "🟢",
    '4': "🟡",
    '5': "🟣",
    '6': "🟠",
  }
  return color_dict[number]

def clue_colors(clue):
  return {
    '*': "⬜",
    '?': "🟫"
  }[clue]

def show_code(array):
  for num in array:
    print(code_colors(num))

def show_clues(exact, same):
  print('  Clues: ')
  for _ in range(exact):
    print(clue_colors('*'))
  for _ in range(same):
    print(clue_colors('?'))
  print('')
