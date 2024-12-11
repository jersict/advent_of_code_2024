
def checkReport(levels, problem_dampener=False):

  # CHECK IF THE FIRST TWO VALUES HAPPEN TO BE THE SAME.
  # IF SO, RETURN 0, AS IT IS AUTOMATICALLY UNSAFE REPORT.
  if levels[0] == levels[1] and not problem_dampener:
    return 0

  # CHECK IF REPORT IS ASCENDING
  if levels[0] < levels[1]:
    # GO THROUGH ALL PAIRS OF LEVELS
    for i, level in enumerate(levels):
      # IF THIS IS THE LAST LEVEL, RETURN 1, THE REPORT IS SAFE
      if i == len(levels)-1:
        return 1
      # CHECK IF THE NEXT LEVEL IS BIGGER BY AT LEAST 1 AND AT MOST 3 THAN THIS ONE
      if 0 < (levels[i+1] - levels[i]) < 4:
        continue
      # IF NOT, CHECK IF PROBLEM DAMPENER IS AVAILABLE.
      else: 
        # IF YES, CHANGE IT TO FALSE
        if problem_dampener:
          problem_dampener = False
          # GO THROUGH ALL LEVELS AND REMOVE ONE BY ONE TO SEE IF THE REPORT IS SAFE
          for j in range(len(levels)):
            # IF THE ANY REPORT IS SAFE, RETURN 1
            if checkReport(levels[:j]+levels[j+1:]):
              # print(levels, levels[:j]+levels[j+1:])
              return 1
          # IF NONE OF REPORTS WAS SAFE, RETURN 0
          print(levels)
          return 0

        # ELSE RETURN 0, AS IT IS UNSAFE.
        else:
          return 0

  # ELSE IT IS DESCENDING
  else:
    # GO THROUGH ALL PAIRS OF LEVELS
    for i, level in enumerate(levels):
      # IF THIS IS THE LAST LEVEL, RETURN 1, THE REPORT IS SAFE
      if i == len(levels)-1:
        return 1
      # CHECK IF THE THIS LEVEL IS BIGGER BY AT LEAST 1 AND AT MOST 3 THAN NEXT ONE
      if 0 < (levels[i] - levels[i+1]) < 4:
        i += 1
        continue
      # IF NOT, CHECK IF PROBLEM DAMPENER IS AVAILABLE.
      else: 
        # IF YES, CHANGE IT TO FALSE AND CONTINUE
        # IF YES, CHANGE IT TO FALSE
        if problem_dampener:
          problem_dampener = False
          # GO THROUGH ALL LEVELS AND REMOVE ONE BY ONE TO SEE IF THE REPORT IS SAFE
          for j in range(len(levels)):
            # IF THE ANY REPORT IS SAFE, RETURN 1
            if checkReport(levels[:j]+levels[j+1:]):
              # print(levels, levels[:j]+levels[j+1:])
              return 1
          # IF NONE OF REPORTS WAS SAFE, RETURN 0
          print(levels)
          return 0
        # RETURN 0 AS IT IS UNSAFE.
        else:
          return 0
  # IF NONE OF THE ABOVE WORKED, EXIT WITH CODE 1
  exit(1)

# RUN THIS IF PROGRAM IS RUN FROM THE COMMAND LINE.
if __name__ == "__main__":

  # OPEN AND READ THE INPUT.TXT FILE, THEN CLOSE IT, AS IT IS NO LONGER NEEDED.
  f = open('inputs\\02\\input.txt', 'r')
  lines = f.readlines()
  f.close()

  # DEFINE VARIABLES
  safe_reports = 0
  safe_reports_with_one_unsafe = 0

  # GO THROUGH EACH LINE
  for line in lines:
    
    # SPLIT THE REPORT INTO LEVELS
    levels = [int(x) for x in line.strip().split(' ')]
    # CHECK IF THE REPORT IS SAFE AND ADD THE RESULT
    safe_reports += checkReport(levels)
    safe_reports_with_one_unsafe += checkReport(levels, True)


  print('PART 1: There are {0} safe reports if we allow no bad levels.\nPART 2: There are {1} safe reports if we allow one bad level\n'.format(safe_reports, safe_reports_with_one_unsafe))