import time

print("Hello, you. Let me add two numbers for you.")

time.sleep(0.5)

num1 = input("Enter a number, then press enter: ")
num2 = input("Enter another number, then press enter: ")
print("The sum is", num1 + num2)
print("Did I add that correctly?")

time.sleep(1)

print("Oh no, did I mess up? Let me try again.")

time.sleep(0.5)

num1 = int(input("Enter a number, then press enter: "))
num2 = int(input("Enter another number, then press enter: "))
print("The sum is", num1 + num2)

time.sleep(0.5)

print("Is it correct now?")