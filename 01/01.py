# OPEN AND READ THE INPUT.TXT FILE
f = open('inputs\\01\\input.txt', 'r')
lines = f.readlines()
f.close()

# DEFINE VARIABLES
first_list = []
second_list = []
second_list_appearances = {}
diff = 0
similarity_score = 0

# PREPROCESS INPUTS
for line in lines:
  #SPLIT THE INPUT BY THREE SPACES AND APPEND THEM AS INTEGERS TO THEIR RESPECTIVE LISTS.
  vals = line.strip().split("   ")
  first_list.append(int(vals[0]))
  second_list.append(int(vals[1]))
  # FOR THE SECOND VALUE ALSO CHECK IF IT ALREADY EXISTS IN THE DICTIONARY. IF NOT ADD IT TO THE DICTIONARY ELSE INCREMENT THE COUNT BY ONE.
  if int(vals[1]) not in second_list_appearances.keys():
    second_list_appearances[int(vals[1])] = 1
  else :
    second_list_appearances[int(vals[1])] += 1

# SORT BOTH LISTS (NEEDED FOR PART 1, DOES NOT AFFECT PART 2)
first_list.sort()
second_list.sort()

# CALCULATE THE DIFFERENCE AND SIMILARITY SCORE
for i, first in enumerate(first_list):
  diff += abs(first - second_list[i])
  if first in second_list_appearances.keys():
    similarity_score += first*second_list_appearances[first]

# PRINT THE RESULTS
print('PART 1: The difference is {0}\nPART 2: The similarity score is {1}'.format(diff, similarity_score))
