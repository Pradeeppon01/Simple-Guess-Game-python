secret_number=5
i=0
while i<3:
    Guess=input('Guess:')
    if int(Guess) == secret_number:
      print("You won!")
    else:
      i+=1
    
print('You have failed!')