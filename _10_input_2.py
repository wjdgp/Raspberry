try:
  while True:
    userInput = input(">>>") # for string
    print("You entered", userInput)
    if userInput == 'quit()':
      print('bye...')
      break

except keyboardInterrupt:
  pass