import copy

# CHECK WHETHER THE EQUATION IF A SOLUTION EXISTS WITH USING ADDITION AND MULTIPLICATION
def handle_equation(final_res, current_res, nums):
  if len(nums) == 1:
    if current_res + nums[0] == final_res:
      return True
    elif current_res * nums[0] == final_res:
      return True
    else: return False
  else:
    if current_res > final_res:
      return False
    else:
      new_nums = copy.copy(nums)
      next_num = new_nums.pop(0)
      mul_val = handle_equation(final_res, current_res*next_num, new_nums)
      sum_val = handle_equation(final_res, current_res+next_num, new_nums)
      return mul_val or sum_val

#CHECK WHETHER THE EQUATION IF A SOLUTION EXISTS 
# WITH USING ADDITION MULTIPLICATION AND CONCATENATION.
def handle_concatenation(final_res, current_res, nums):
  if len(nums) == 1:
    if current_res + nums[0] == final_res:
      return True
    elif current_res * nums[0] == final_res:
      return True
    elif int(str(current_res) + str(nums[0])) == final_res:
      return True
    else: return False
  else:
    if current_res > final_res:
      return False
    else:
      new_nums = copy.copy(nums)
      next_num = new_nums.pop(0)
      mul_val = handle_concatenation(final_res, current_res*next_num, new_nums)
      sum_val = handle_concatenation(final_res, current_res+next_num, new_nums)
      concat_val = handle_concatenation(final_res, int(str(current_res) + str(next_num)), new_nums)
      return mul_val or sum_val or concat_val


# RUN THIS IF PROGRAM IS RUN FROM THE COMMAND LINE.
if __name__ == "__main__":
  # OPEN AND READ THE INPUT.TXT FILE, THEN CLOSE IT, AS IT IS NO LONGER NEEDED.
  f = open('07\input.txt', 'r')
  equations = f.readlines()
  f.close()

  # DEFINE VARIABLES
  total_calibration_result = 0
  total_calibration_result_with_concatenation = 0

  # GO THROUGH ALL THE EQUATIONS AND SEPARATE THE RESULT AND NUMBERS.
  for equation in equations:
    equation = equation.strip().split(': ')
    test_value = int(equation[0])
    numbers = [int(x) for x in equation[1].split(' ')]
    first_number = numbers.pop(0)
    # CHECK WHETHER THE EQUATION IF A SOLUTION EXISTS WITH USING ADDITION AND MULTIPLICATION
    if handle_equation(test_value, first_number, numbers):
      total_calibration_result += test_value
      total_calibration_result_with_concatenation += test_value
    # IF NOT, CHECK WHETHER THE EQUATION IF A SOLUTION EXISTS 
    # WITH USING ADDITION MULTIPLICATION AND CONCATENATION.
    elif handle_concatenation(test_value, first_number, numbers):
      total_calibration_result_with_concatenation += test_value
    
  # PRINT THE RESULTS
  print('PART 1: Total calibration result is {0}\nPART 2: The number of valid new obstacle positions is {1}'.format(total_calibration_result, total_calibration_result_with_concatenation))
  