import re

# USE REGULAR EXPRESSIONS TO FIND ALL OCCURRENCES OF mul(n,m), 
# WHERE n AND m REPRESENT DIGITS. THE REGEX RETURNS ONLY THE n,m PART, 
# SO WE ONLY NEED TO SPLIT THE STRING AND CONVERT IT TO NUMBERS.
# GO THROUGH ALL THE OCCURRENCES AND SUM THE MULTIPLICATIONS AND RETURN THE RESULT. 
def calculateMuls(line):
  exp = '(?<=mul\()(\d+,\d+)(?=\))'

  all = re.findall(exp, line)
  sum = 0
  for x in all:
    x = x.split(',')
    sum += int(x[0]) * int(x[1])
  return sum


# RUN THIS IF PROGRAM IS RUN FROM THE COMMAND LINE.
if __name__ == "__main__":

# OPEN AND READ THE INPUT.TXT FILE, THEN CLOSE IT, AS IT IS NO LONGER NEEDED.
  f = open('inputs\\03\\input.txt', 'r')
  line = f.read()
  f.close()

# DEFINE VARIABLES
  do = True
  dos = []
  s = ''
  sum_part_2 = 0

# GO THROUGH THE ENTIRE COMMAND, CHARACTER BY CHARACTER.
# STOP 6 CHARACTERS BEFORE THE END, TO AVOID GOING OUT OF BOUNDS
# WE CAN DO THAT BECAUSE NO COMMAND IS SHORTER THAN 6 CHARACTERS.
  for c in range(len(line)-7):
    # CHECK IF THE CURRENT COMMAND IS don't(). IF IT IS, CHANGE do TO False, 
    # APPEND THE s VARIABLE, THAT CONTAINS THE COMMAND BETWEEN THE LAST do() AND THIS don't() 
    # TO dos ARRAY AND RESET THE s VARIABLE TO EMPTY.
    if line[c:c+7] == 'don\'t()':
      dos.append(s)
      s=''
      do = False
    # ELSE IF THE COMMAND IS do(), JUST CHANGE do TO True.
    elif line[c:c+4] == 'do()':
      do = True
    # IF do IS True ADD THE CHARACTER TO s. 
    if do:
      s+=line[c]
  # AT THE END APPEND THE s AND THE END OF THE line TO dos. 
  dos.append(s+line[-7:])

  # FOR PART 1, JUST CALCULATE THE MULS IN THE ENTIRE LINE
  sum_part_1 = calculateMuls(line)

  # FOR PART 2, DO THROUGH THE ENTIRE dos ARRAY AND CALCULATE
  # MULS FOR EVERY STRING BETWEEN do() AND don't(), AND SUM THEM UP.
  for l in dos:
    sum_part_2 += calculateMuls(l)

  # PRINT THE RESULTS
  print('PART 1: The sum of all muls is {0}\nPART 2: The sum of muls between do()s and don\'t()s is {1}'.format(sum_part_1, sum_part_2))
