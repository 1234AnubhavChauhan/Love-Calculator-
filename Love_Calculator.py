print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_name = name1+name2
lower_case_name = combined_name.lower()
t = lower_case_name.count("t")
r = lower_case_name.count("r")
u = lower_case_name.count("u")
e = lower_case_name.count("e")

first_digit = t + r + u + e

l = lower_case_name.count("l")
o = lower_case_name.count("o")
v = lower_case_name.count("v")
e = lower_case_name.count("e")

second_digit  = l + o + v + e

final_number = int(str(first_digit) + str(second_digit))

if(final_number<10 or final_number > 90):
  print(f"Your score is {final_number}, you go together like coke and mentos.")
elif(final_number>=40 and final_number<=50):
  print(f"Your score is {final_number}, you are alright together.")
else:
  print(f"Your score is {final_number}.")