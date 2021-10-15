
def formatting(description, string):
  out_message = {
    'underline': '\033[4m'+'\033[4m'.join(str(string)),
    'red': '\033[91m'+string
  }[description]
  return out_message


def game_message(message):
  out_message = {
    'human_won': "  You broke the code! Congratulations, you win! \n\n",
    'display_code': "Here is the 'master code' that you were trying to break:",
    'computer_lost': "\nYou out-smarted the computer & won the game!",
    'repeat_prompt': "\n\nDo you want to play again? Press 'y' for yes (or any other key for no).",
    'thanks': 'Thank you for playing Mastermind!'
  }[message]
  return out_message

def computer_won_message(message):
  out_message = {
    'inconceivable': "\nInconceivable! Either your code only had 1-2 different numbers or the computer's randomized numbers just happened to be in a perfect order.",
    'won': "\nGame over. The computer broke your code.",
    'close': "\nThat was close, but the computer finally broke your code."
  }[message]
  return out_message


def turn_message(message, number = None):
  out_message = {
    'guess_prompt': F"Turn {number}: Type in four numbers (1-6) to guess code, or 'q' to quit game.",
    'computer': F"\nComputer Turn {number}:",
    'breaker_start': "The computer has set the 'master code' and now it's time for you to break the code.\n\n",
    'code_prompt': "Please enter a 4-digit 'master code' for the computer to break.",
    'code_displayed': "is your 'master code'.\n"
  }[message]
  return out_message


def warning_message(message):
  out_message = {
    'answer_error': formatting('red', "Enter '1' to be the code MAKER or '2' to be the code BREAKER."),
    'turn_error': formatting('red', 'Your guess should only be 4 digits between 1-6.'),
    'last_turn': formatting('red', 'Choose carefully. This is your last chance to win!'),
    'code_error': formatting('red', "Your 'master code' must be 4 digits long, using numbers between 1-6."),
    'game_over': formatting('red', 'Game over. That was a hard code to break!')
  }[message]
  return out_message
