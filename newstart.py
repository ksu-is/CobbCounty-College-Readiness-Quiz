import time

print("Welcome to the Cobb County Readiness Quiz.\nYou can test your knowledge to see whether or not you are ready for College!")
time.sleep(2)

print("The Quiz will consit of 10 Multiple Choice Questions.\nThe Quiz will keep track of your score and at the end you will recieve your Final Grade.")
time.sleep(2)

print("Select a/b/c/d or Enter the Answer, to Answer Each Question.")
time.sleep(2)

print("Good Luck, and Let's Begin!!!")
score = 0

q_attempted = 0

print("")

def correct_answer():
  global score
  score += 1
  print("You selected the correct answer!")
  
# Question 1
print("Q1. (BLANK)is the applied science of energy and matter?")
answer = input("a. Psychology \nb. Engineering \nc. Management \nd. Medicine \n").lower()
q_attempted += 1
if answer == "b" or answer == "engineering":
  correct_answer()
else:
   print("Sorry, that was not the correct answer.")

print("")

# Question 2
print("Q2. The science of human behavior is:")
answer = input("a. Anthropology \nb. Sociology \nc. Engineering \nd. Psychology \n").lower()
q_attempted += 1
if answer == "d" or answer == "psychology":
  correct_answer()
else:
   print("Sorry, that was not the correct answer.")

print("")

# Question 3
print("Q3. Culture and the study of learned behavior comprise the domain of:")
answer = input("a. Management \nb. Anthropology \nc. Sociology \nd. Psychology \n").lower()
q_attempted += 1
if answer == "b" or answer == "anthropology":
  correct_answer()
else:
   print("Sorry, that was not the correct answer.")

print("")

# Question 4
print("Q4. People respond with a(n) in the midsit of environmental change.")
answer = input("a. Open Behavior \nb. Proactive Behavior \nc. Sympathetic Behavior \nd. Reactive Behavior \n").lower()
q_attempted += 1
if answer == "d" or answer == "reactive behavior":
  correct_answer()
else:
   print("Sorry, that was not the correct answer.")

print("")

# Question 5
print("Q5. The specific setting within which organizational behavior is enacted would be called the:")
answer = input("a. Organizational Structure \nb. External Environment \nc. Organizational Context \nd. Situation \n").lower()
q_attempted += 1
if answer == "c" or answer == "organizational context":
  correct_answer()
else:
   print("Sorry, that was not the correct answer.")

print("")

# Question 6
print("Q6. Which of the following is not internal component of a work organization?")
answer = input("a. Structure \nb. Task \nc. Technology \nd. Consumers \n").lower()
q_attempted += 1
if answer == "d" or answer == "consumers":
  correct_answer()
else:
   print("Sorry, that was not the correct answer.")

print("")

# Question 7
print("Q7. The task of an organization is reflected in its:")
answer = input("a. Human Resources \nb. Mission or Purpose \nc. Input Materials \nd. Structure \n").lower()
q_attempted += 1
if answer == "b" or answer == "mission or purpose":
  correct_answer()
else:
   print("Sorry, that was not the correct answer.")

print("")

# Question 8
print("Q8. In an open system the transformation or conversion of inputs to outputs is accomplished with")
answer = input("a. Technology \nb. Task \nc. Regulatory agencies \nd. Clients \n").lower()
q_attempted += 1
if answer == "a" or answer == "technology":
  correct_answer()
else:
   print("Sorry, that was not the correct answer.")

print("")

# Question 9
print("Q9. A federal regulatory agency can be considered part of an organization's:")
answer = input("a. Formal Structure \nb. Labor Market \nc. External Task Environment \nd. Transformation Technology \n").lower()
q_attempted += 1
if answer == "c" or answer == "external task environment":
  correct_answer()
else:
   print("Sorry, that was not the correct answer.")

print("")

# Question 10
print("Q10. An organization's suppliers, customers, and federal regulators are called the:")
answer = input("a. Task Environment \nb. Market \nc. Political Enviroment \nd. General Environment \n").lower()
q_attempted += 1
if answer == "a" or answer == "task environment":
  correct_answer()
else:
   print("Sorry, that was not the correct answer.")

print("The Cobb County College Readiness Quiz is over. Your score is " + str(score) + "/" + str(q_attempted) + ".")

# Final Message
if score <= 1:
  print("Based off your score of " + str(score) + "/" + str(q_attempted) + " your not ready for College.")
elif score == 2:
  print("Based off your score of " + str(score) + "/" + str(q_attempted) + " your not ready for College.")
elif score == 3:
  print("Based off your score of " + str(score) + "/" + str(q_attempted) + " your not ready for College.")
elif score == 4:
  print("Based off your score of " + str(score) + "/" + str(q_attempted) + " your not ready for College.")
elif score == 5:
  print("Based off your score of " + str(score) + "/" + str(q_attempted) + " your not ready for College.")
elif score == 6:
 print("Based off your score of " + str(score) + "/" + str(q_attempted) + " your ready for College but you need more practice.")
elif score == 7:
 print("Based off your score of " + str(score) + "/" + str(q_attempted) + " your ready for College but you need more practice.")
elif score >= 8:
  print("Based off your score of " + str(score) + "/" + str(q_attempted) + " your ready for College but you need more practice.")
elif score >= 9:
  print("Based off your score of " + str(score) + "/" + str(q_attempted) + " your ready for College but you need more practice.")
else:
  print("Based off your score of " + str(score) + "/" + str(q_attempted) + " your ready for College!!!Congratulations!")
