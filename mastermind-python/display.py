from emoji import emojize

def code_colors(number):
  return {
    '1': "🔴",
    '2': "🔵",
    '3': "🟢",
    '4': "🟡",
    '5': "🟣",
    '6': "🟠",
  }[number]

def clue_colors(clue):
  return {
    '*': "⬜",
    '?': "🟫"
  }[clue]

def show_code(array):
  for num in len(array):
    print(code_colors(num))

def show_clues(exact, same):
  print('  Clues: ')
  for _ in exact:
    print(clue_colors('*'))
  for _ in same:
    print(clue_colors('?'))
  print('')
