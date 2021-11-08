import os

print("There are two parts to this.\nClick on program1.py on the left to see the code for the 1st part.\nClick on program2.py on the left to see the code for the 2nd part.")
program = input("Enter 1 for program1 or 2 for program2: ")

while program not in ["1", "2"]:
  os.system('clear')
  print("That's not a valid input")
  program = input("Enter 1 for program1 or 2 for program2: ")

os.system('clear')

if program == '1':
  import program1
elif program == '2':
  import program2