import time

print("Welcome to the Cobb County Readiness Quiz\nYou can test your knowledge to see whether or not you are ready for college")
time.sleep(2)

print("The quiz will consit of 10 multiple choice questions.\nThe quiz will keep track of your score while taking it and at the end you will recieve your final grade")
time.sleep(2)

print("Select a/b/c/d or enter the answer, to answer each question.")
time.sleep(2)

print("Good luck, and let's begin!!!")
score = 0

q_attempted = 0

print("")

def correct_answer():
  global score
  score += 1
  print("You selected the correct answer!")
  
# Question 1
print("Q1. (BLANK)is the applied science of energy and matter?")
answer = input("a. Psychology \nb. Engineering \nc. Management \d. Medicine").lower()
q_attempted += 1
if answer == "b" or answer == "engineering":
  correct_answer()
else:
   print("Sorry, that was not the correct answer.")
