print("\033[34m",
      "--------------> One-Million-To-One challenge <--------------",
      "\033[0m")
print("\033[34m", "                ----------------------------", "\033[0m")

print(
    "\n you have to guess which number i had picked🤔🤔 from 0 to 1,000,000🤔🤔\n")
attempts = 0
while True:

  print(
      "\033[33m",
      "\n-------> you can put a negative number to exit <----------",
      "\033[0m",
  )
  attempts += 1

  guess_input = input("\nwhat is your guess --->  ")
  if not guess_input.lstrip('-').isdigit():
    print(
        "\033[31m",
        "Please input an integer only.\n you cannot put an float or string or any other object ",
        "\033[0m")
    continue

  guess_number = int(guess_input)

  if guess_number == 650000:
    print("\ncorrect !!!")
    if attempts == 1:
      print("\033[32m", "it took you ONLY", attempts,
            "guess to get it correct👍🥳", "\033[0m")
      print("\033[32m", "You are great in terms of guessing", "\033[0m")
      break
    elif attempts > 1 and attempts <= 3:
      print("\033[32m", "it took you", attempts, "guesses to get it correct👍🥳",
            "\033[0m")
      print("\033[32m", "You are great in terms of guessing", "\033[0m")
      break
    elif attempts > 3 and attempts <= 7:
      print("\033[36m", "it took you", attempts, "guesses to get it correct👍",
            "\033[0m")
      print("\033[36m", "You are ok in terms of guessing😏😏", "\033[0m")
      break
    elif attempts >= 8:
      print("\033[30m", "it took you", attempts, "guesses to get it correct👎",
            "\033[0m")
      print("\033[30m", "You are bad in terms of guessing😒😒", "\033[0m")
      break

  elif guess_number > 650000 and guess_number < 800000:
    print("\nhigh, but very close🤔")

  elif guess_number > 800000 and guess_number < 1000000:
    print("\n🤔Too high")

  elif guess_number >= 0 and guess_number <= 200000:
    print("\nToo low🤔")

  elif guess_number > 200000 and guess_number <= 400000:
    print("\nlow 😕😕")

  elif guess_number > 400000 and guess_number < 650000:
    print("\nlow, but very close 😕😕")

  elif guess_number > 1000000:
    print("\nout of range")
  else:
    print("\nYou cannot input a text")

  if attempts == 4:
    print(
        "\033[35m",
        "\n__________let me give you a HINT MY GUESS IS IN 6 digits___________\n",
        "\033[0m",
    )

print("\033[34m",
      "\n\n<-------------------thanks for playing------------------->",
      "\033[0m")
