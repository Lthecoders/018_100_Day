# value_11 = "40000"
# # value_11 = float(eval(value_11))
# value_11 = int(value_11)
# print(int(value_11))
# print(type(value_11))
# """
# Full form of eval(): The eval() function is short for "evaluate" in Python.
# Its purpose is to take a string that contains a Python expression or statement
# and interpret it as code to be executed."""

# print("One-Million-To-One")
# print("------------------")

# print("\npick any number from 0 to 1,000,000🤔🤔")
# attempts = 0
# while True:

#   print("\nyou can put an negative number to exit")
#   attempts += 1

#   guess_number = int(input("\n\nwhat is your guess "))
#   if not str(guess_number).isdigit():
#     print("\nexited successfully....")
#     exit()
#     # continue
#   if int(guess_number) == 650000:
#     print("\ncorrect")
#     if attempts >=1 and attempts<= 3:
#       print("it took you", attempts, "guesses to get it correct👍🥳")
#       print("You are great in terms of guessing")
#       break
#     elif attempts > 3 and attempts <= 7:
#       print("it took you", attempts, "guesses to get it correct👍")
#       print("You are ok in terms of guessing😏😏")
#       break
#     elif attempts >= 8:
#       print("it took you", attempts, "guesses to get it correct👎")
#       print("You are bad in terms of guessing😒😒")
#       break

#   elif (guess_number) > 650000 and (guess_number) < 800000:
#     print("\nhigh,but very close")

#   elif (guess_number) > 800000 and (guess_number) < 1000000:
#     print("\nToo high")

#   elif (guess_number) >= 0 and (guess_number) <= 200000:
#     print("\nToo low")

#   elif (guess_number) > 200000 and (guess_number) <= 400000:
#     print("\nlow")

#   elif (guess_number) > 400000 and (guess_number) < 650000:
#     print("\nlow,but very close")

#   elif (guess_number) > 1000000:
#     print("\nout of range")
#   else:
#     print("\n you can cannot intput an text")

print("Welcome to Guess the Number.")
print()
print(
    "Guess a number between 1 and 1,000,000 and I will tell you if you are too low, too high, or get it correct."
)
print()
print("Let's play!")

correct_number = 2300
attempt = 1

while True:
  user_guess = int(input("Pick a number between 1 and 1,000,000: "))
  if user_guess < 0:
    print("Now we'll never know what the answer is …")
    exit()
  if user_guess < correct_number:
    print("That number is too low. Try again!")
    attempt += 1
  elif user_guess > correct_number:
    print("That number is too high. Try again!")
    attempt += 1
    continue
  elif user_guess == correct_number:
    print("You are a winner! 🥳🥳")
    break
  else:
    print("That is not a number I recognize.")
print("It took you", attempt, "attempt(s) to get the correct answer.")
