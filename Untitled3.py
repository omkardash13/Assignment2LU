#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#initialization of variables
a = 0
b = 0
c = 0
#print final result
def printAnswer(input_number, a, b, c):
  print("User input: ", input_number, " A:", a, " B:", b, " C:",c)
#load balancer for A
def balance_A(remainder):
  if remainder > 20:
    return 20
  else:
    return remainder

#load balancer for B
def balance_B(remainder):
  if remainder > 10:
    return 10
  elif remainder < 1:
    return 0
  else:
    return remainder
user_input = int(input("Enter number between 1 to 60:"))
#validate input
if user_input > 0 and user_input < 61:
  remaining_input = user_input
  a = balance_A(remaining_input)
  remaining_input = remaining_input - a
  b = balance_B(remaining_input)
  remaining_input = remaining_input - b
  c = remaining_input
  printAnswer(user_input, a, b, c)
  
else:
  print("Invalid input number")


# In[ ]:




