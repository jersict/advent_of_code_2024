
# CHECK WHETHER THE PROVIDED UPDATE IS ORDERED CORRECTLY.
def check_update(update):
  was_correct = True
  is_incorrect = True
  while is_incorrect:
    # ASSUME IT IS CORRECT. IF THIS IS NOT CHANGED
    # ON LINE 24, LOOP OF FIXING IT IS BROKEN.
    is_incorrect = False
    # FOR EVERY PAGE OF THE UPDATE...
    for i, page in enumerate(update):
      # CHECK IF IT IS ORDERED INCORRECTLY, AND BREAK IF IT IS.
      # THAT MUST BE DONE BECAUSE WE ONLY MAKE ONE CHANGE AT 
      # THE TIME, AND THAT HAS ALREADY HAPPENED, THUS WE HAVE 
      # TO ASSUME IT IS ORDERED CORRECTLY UNTIL PROVEN 
      # OTHERWISE BY LINE 21.
      if is_incorrect: break
      for y in range(i+1, len(update), 1):
        # FOR EVERY PAIR OF PAGES IN THE UPDATE CHECK 
        # IF THEIR ORDER IS INCORRECT. 
        if update[y] in rules.keys() and page in rules[update[y]]:
          # IF IT IS INCORRECT MARK THAT IN was_correct 
          # AND CHANGE THEIR ORDER.
          was_correct = False
          update[i] = update[y] 
          update[y] = page
          # SET is_incorrect TO True, WHICH WILL MAKE 
          # IT BREAK THE PREVIOUS LOOP, THEN BREAK THIS LOOP 
          # AND RETURN TO THE START OF THE WHILE LOOP, WHERE 
          # WE AGAIN ASSUME THE ORDER IS CORRECT AND CHECK AGAIN.
          is_incorrect = True
          break
  # RETURN THE INFORMATION IF INITIAL ORDER WAS CORRECT, 
  # ALONG WITH THE MIDDLE NUMBER.
  return was_correct, int(update[int((len(update)-1)/2)])

# OPEN AND READ THE INPUT.TXT FILE, THEN CLOSE IT, AS IT IS NO LONGER NEEDED.
f = open('inputs\\05\\input.txt', 'r')
lines = f.readlines()
f.close()

# DEFINE VARIABLES
past_rules = False
rules = {}
updates = []
sum_of_correct_middles = 0
sum_of_sorted_middles = 0

# PARSE INPUTS, RULES TO rules AND UPDATES TO updates.
for line in lines:
  if line == '\n':
    past_rules = True
    continue
  if not past_rules:
    line = line.strip().split('|')
    if line[0] not in rules.keys():
      rules[line[0]] = [line[1]]
    else:
       rules[line[0]].append(line[1])
  else:
    updates.append(line.strip().split(','))

# GO THROUGH ALL THE UPDATES AND CHECK IF THEY 
# CAN BE CORRECTLY-ORDERED. IF THEY WERE IN THE 
# CORRECT ORDER FROM THE START ADD THE MIDDLE 
# NUMBER TO THE sum_of_correct_middles. IF IT 
# NEEDED TO BE SORTED ADD THE MIDDLE TO 
# sum_of_sorted_middles.
for update in updates:
  was_correct, middle = check_update(update)
  if was_correct: 
    sum_of_correct_middles += middle
  else: 
    sum_of_sorted_middles += middle

  # PRINT THE RESULTS
  print('PART 1: The sum of middle numbers of correctly-ordered updates is {0}\nPART 2: The sum of middle numbers of correctly-ordered updates AFTER SORTING is {1}'.format(sum_of_correct_middles, sum_of_sorted_middles))
