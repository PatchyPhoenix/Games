#importing modules
import random # to pick a random option or number
import os  # for clearing the console
import time
from turtle import clear  # for delaying tasks
from colorama import Fore, Style # to format the output

# function for guess
def guess(number):
  chances = 3
  clr = [Fore.BLUE,Fore.RED, Fore.CYAN, Fore.YELLOW,Fore.MAGENTA ,Fore.GREEN]

  while chances>-1:
    try:
      no = int(input(Fore.RESET + "Enter a number from 1 - 10\n"))
    except:
      print(Fore.YELLOW + "Enter a number not a word")
      continue
    if no > 10:
      print(Fore.YELLOW + "The number cannot be larger than 10")
      continue
    if no < 0:
      print(Fore.YELLOW + "The number cannot be less than 0")
      continue
    if no == number:
      for x in clr:
        clearConsole()
        print(x + Style.BRIGHT +  f"Correct! That's the number")
        time.sleep(0.25)
      print(Style.RESET_ALL)
      break
    else:
      if no>number and chances != 0:
        chances = chances - 1
        print(Fore.CYAN + f"The number is smaller than {no}")
      elif no<number and chances != 0:
        chances = chances - 1
        print(Fore.CYAN + f"The number is greater than {no}")
      elif chances <= 0:
        print(Fore.YELLOW + f"Good try. The number was {number}")

# function for rps
def rps(choice, userChoice):
  clr = [Fore.BLUE,Fore.RED, Fore.CYAN, Fore.YELLOW,Fore.GREEN]
  n = 1
  if choice == "rock" and userChoice.lower() == "paper":
      for x in clr:
        clearConsole()
        print(x + Style.BRIGHT + f"You win\nYour move - {userChoice}\nProgram's move - {choice}")
        time.sleep(0.25)
      print(Style.RESET_ALL)
  elif choice == "paper" and userChoice.lower() == "scissors":
      for x in clr:
        clearConsole()
        print(x + Style.BRIGHT + f"You win\nYour move - {userChoice}\nProgram's move - {choice}")
        time.sleep(0.25)
      print(Style.RESET_ALL)
  elif choice == "scissors" and userChoice.lower() == "rock":
      for x in clr:
        clearConsole()
        print(x + Style.BRIGHT + f"You win\nYour move - {userChoice}\nProgram's move - {choice}")
        time.sleep(0.25)
      print(Style.RESET_ALL)
  elif choice == "rock" and userChoice.lower() == "scissors":
    print(Fore.YELLOW + f"You lose\nYour move - {userChoice}\nProgram's move - {choice}")
  elif choice == "paper" and userChoice.lower() == "rock":
    print(Fore.YELLOW + f"You lose\nYour move - {userChoice}\nProgram's move - {choice}")
  elif choice == "scissors" and userChoice.lower() == "paper":
    print(Fore.YELLOW + f"You lose\nYour move - {userChoice}\nProgram's move - {choice}")
  elif choice == userChoice.lower():
    print(Fore.CYAN + f"Tie\nYour move - {userChoice}\nProgram's move - {choice}")

# function to clear the console
def clearConsole():
  command = "clear"
  if os.name in ('nt','dos'):
    command = 'cls'
  os.system(command)
n = 1

# program
while n>0:
  clearConsole() # clear the console
  
  # asking the user which task to perform
  game = input(Fore.RESET + "Hello there! Which game do you want to play?\n-RPS: Rock paper scissors\n-Guess: Guess the number\n-Dice: Roll the dice\n-8ball: Ask the magic 8ball a yes or no question\n")
  
  clearConsole() # clear the console

  # rps
  if game.lower() == "rps":
    allChoices = ["rock","paper","scissors"]
    choice = random.choice(allChoices) # choose a random value from allChoices
    a = 1
    while a>0:
      clearConsole() # clear the console
      userChoice = input("Enter your move, rock, paper or scissors\n") # accept the user's move
      if userChoice.lower() in allChoices:
        break
      else:
        continue
    rps(choice, userChoice) # rps function
  
  # guess
  elif game.lower() == "guess":
    number = random.randint(1,10) # choose a random number from 1 to 10
    guess(number) # guess function

  # dice
  elif game.lower() == "dice":
    clr = [Fore.BLUE,Fore.RED, Fore.CYAN, Fore.GREEN, Fore.YELLOW]
    for x in clr:
      clearConsole()
      print(x + "Rolling the dice...")
      time.sleep(0.25)
    clearConsole()
    dice = random.randint(1,6) # choose a random number from 1 to 6
    print(Fore.CYAN + f"The dice landed on {dice}")

  # 8ball
  elif game.lower() == "8ball":
    question = input("Enter your question\n") # accept the question
    answers = ["Yes", "No", "Maybe","Probably","Probably not","I don't know"]
    answer = random.choice(answers) # choose a random answer
    clearConsole() # clear the console
    clr = [Fore.BLUE,Fore.RED, Fore.CYAN, Fore.GREEN, Fore.YELLOW]
    for x in clr:
      clearConsole()
      print(x + "Thinking")
      time.sleep(0.25)
    clearConsole()
    print(Fore.CYAN + f"Question: {question}\nAnswer: {answer}")

  # exit 
  elif game.lower() == "exit":
    clearConsole()
    print(Fore.RED + Style.DIM + "Exitted")
    time.sleep(1)
    break
  # skip if an invalid option is selected
  else:
    continue
    
  time.sleep(1) # delay the exit task

  # exit
  exit = input(Fore.RED + "Exit?\n")
  if exit.lower() == "yes":
    n = 0
    clearConsole() # clear the console
    print(Fore.RED + Style.DIM + "Exitted") 
    time.sleep(1)