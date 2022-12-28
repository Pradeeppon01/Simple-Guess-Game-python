secret_number=5
guess_count=0
guess_limit=3
print("Guess a number between 1-15")
while guess_count<guess_limit:
    Guess=input('Guess:')
    guess_count += 1
    if int(Guess) == secret_number:
      print("You won!")
      break
else:
  print('You have failed!')
