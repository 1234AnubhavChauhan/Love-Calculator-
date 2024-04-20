#Welcome to the Love Calculator ......
print("The Love Calculator is calculating your score...")

#Taking the names 
name1 = input() # What is your name?
name2 = input() # What is your loved ones name?

#Combining both names in order to have a combined name so that we can work upon it 
combined_name = name1+name2

#Converting the combined name to lowercase in order to avoid confusion between uppercase and lowercase 
lower_case_name = combined_name.lower()

#Getting the number of t's, r's , u's and e's in the name 
t = lower_case_name.count("t")
r = lower_case_name.count("r")
u = lower_case_name.count("u")
e = lower_case_name.count("e")

#Generating the first digit of the number 
first_digit = t + r + u + e

#Again repaeting the same for "love"
l = lower_case_name.count("l")
o = lower_case_name.count("o")
v = lower_case_name.count("v")
e = lower_case_name.count("e")

#Generating the second digit of the number 
second_digit  = l + o + v + e

#Final number is concatinating the first and second digit by first converting them into string and then converting the whole number into integer .
final_number = int(str(first_digit) + str(second_digit))


#Applying the if else conditions 
if(final_number<10 or final_number > 90):
  print(f"Your score is {final_number}, you go together like coke and mentos.")
elif(final_number>=40 and final_number<=50):
  print(f"Your score is {final_number}, you are alright together.")
else:
  print(f"Your score is {final_number}.")

#Thank you !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
