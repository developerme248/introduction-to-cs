import math

# Function to Calculate Math Expressions
def calc_math_expression(num1, num2, operator):
  if operator =="+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == ":" and num2 != 0:
    return num1 / num2
  else:
    return None
  
# Function to get a String Expression and split and pass it to calc_math_expression
def calc_math_expression_from_str(str_input):
  input_data = str_input.split()
  try:
    return calc_math_expression(float(input_data[0]), float(input_data[2]), input_data[1])
  except:
    print("Enter valid expression")

# Function to find the Largest and Smallest numbers
def find_largest_and_smallest_numbers(num1=0.0, num2=0.0, num3=0.0):
  if num1 > num2 and num1> num3:
    if num2 > num3:
      return (num1, num3)
    else:
      return (num1, num2)
  elif num2 > num1 and num2 > num3:
    if num1 > num3:
      return (num2, num3)
    else:
      return (num2, num1)
  else:
    if num1 > num2:
      return (num3, num2)
    else:
      return (num3, num1)

# Funcion to find the roots of a Quadratic Equation
def quadratic_equation_solver(a, b, c):
  x1 = x2 = None
  if a != 0:
    discriminant = b**2 - (4 * a * c)
    if discriminant == 0:
      x1 = -b / (2 * a)
    elif discriminant > 0:
      x1 = (-b + math.sqrt(discriminant)) / (2 * a)
      x2 = (-b - math.sqrt(discriminant)) / (2 * a)
  return (x1, x2)

# Function to capture user input for a, b, and c and then compute the roots of the Quadratic Equation
def quadratic_equation_solver_from_user_input():
  abc = input("Enter coefficients of the Quadratic Equation: ")
  abc =[a, b, c] = abc.split()
  if all(digit.isnumeric() for digit in abc):
    print(quadratic_equation_solver(float(a), float(b), float(c)))
  else:
    print("Enter valid numeric values for the coefficients")

# Function to check if at least 2 temperatures (out of 3) are greater than the minimum temperature
def temp_checker(min_temp, temp_1, temp_2, temp_3):
  greater_than_min_temp = 0
  for temp in [temp_1, temp_2, temp_3]:
    if temp > min_temp:
      greater_than_min_temp += 1
  
  if greater_than_min_temp>= 2:
    return True
  else:
    return False
