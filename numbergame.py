import random

answer = random.randint(1,100)
# print(answer)

userName = input("Welcome to the Game, Enter Your Name:")
print(f"hi, {userName} I am Guessing a number between 1 and 100:")

# chooseLevel = 5 or 10
while True:
  chooseLevel = input("Choose the difficulty Level, Type 'easy' or 'hard':")

  if chooseLevel.lower() == "easy":
    guesses = 10
    break
  if chooseLevel.lower() == "hard":
    guesses = 5
    break

  print("pelease type only given options")

# print(guesses)
triesLeft = guesses

while guesses != 0:
  print(f"You have {guesses} attempts to guess the number")

  userGuess = input(f"Make a guess: ")

  if userGuess.isdigit():
    userGuess = int(userGuess)

    if userGuess == answer:
      print(f"You got it!  The answer was {userGuess}.")
      print(f"You guessed the number in {triesLeft - guesses +1} tries!")
      break

    elif userGuess > answer:
      print("Your guess is too high \n Guess Again")
      guesses -= 1

    else:
      print("Your guess is too low \n Guess Again")
      guesses -= 1

  else:
    print("Please enter only Numbers from 1 to 100")

if guesses == 0:
  print("you Lost the game, all attempts are over")
  print("the actual annwer:", answer)