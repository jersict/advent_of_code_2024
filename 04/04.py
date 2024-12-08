# VERY UGLY SEARCH FOR 'XMAS'ES IN EVERY DIRECTION FROM THE FOUND 'X'
def find_xmases(word_search, x, y):
  found = 0
  if x > 2 and y > 2:
    if word_search[x][y]+word_search[x-1][y-1]+word_search[x-2][y-2]+word_search[x-3][y-3] == "XMAS":
      found += 1
  if x < len(word_search)-3 and y > 2:
    if word_search[x][y]+word_search[x+1][y-1]+word_search[x+2][y-2]+word_search[x+3][y-3] == "XMAS":
      found += 1
  if x > 2 and y < len(word_search[x])-3:
    if word_search[x][y]+word_search[x-1][y+1]+word_search[x-2][y+2]+word_search[x-3][y+3] == "XMAS":
      found += 1
  if x < len(word_search)-3 and y < len(word_search[x])-3:
    if word_search[x][y]+word_search[x+1][y+1]+word_search[x+2][y+2]+word_search[x+3][y+3] == "XMAS":
      found += 1
  if x > 2:
    if word_search[x][y]+word_search[x-1][y]+word_search[x-2][y]+word_search[x-3][y] == "XMAS":
      found += 1
  if x < len(word_search)-3:
    if word_search[x][y]+word_search[x+1][y]+word_search[x+2][y]+word_search[x+3][y] == "XMAS":
      found += 1
  if y < len(word_search[x])-3:
    if word_search[x][y]+word_search[x][y+1]+word_search[x][y+2]+word_search[x][y+3] == "XMAS":
      found += 1
  if y > 2:
    if word_search[x][y]+word_search[x][y-1]+word_search[x][y-2]+word_search[x][y-3] == "XMAS":
      found += 1
  return found

# ALMOST AS UGLY SEARCH FOR 'X-MAS' AROUND THE FOUND 'A'.
def find_x_mases(word_search, x, y):
  if not 0 < x < len(word_search)-1 or not 0 < y < len(word_search[x])-1:
    return 0
  if word_search[x-1][y-1]+word_search[x][y]+word_search[x+1][y+1] in ['MAS','SAM'] and word_search[x-1][y+1]+word_search[x][y]+word_search[x+1][y-1] in ['MAS','SAM']:
    print(x, y)
    return 1
  return 0


# RUN THIS IF PROGRAM IS RUN FROM THE COMMAND LINE.
if __name__ == "__main__":

  # OPEN AND READ THE INPUT.TXT FILE, THEN CLOSE IT, AS IT IS NO LONGER NEEDED.
  f = open('input.txt', 'r')
  lines = f.readlines()
  f.close()

  # DEFINE VARIABLES
  word_search = []
  xmases = 0
  x_mases = 0

  # PARSE WORD SEARCH GRID
  for line in lines:
    word_search.append(list(line.strip()))

  # GO THROUGH THE ENTIRE WORD SEARCH GRID
  for x in range(len(word_search)):
    for y in range(len(word_search[x])):
      # IF 'X' IS FOUND, ADD THE NUMBER OF 
      # 'XMAS'ES IT IS PART OF.
      if word_search[x][y] == 'X':
        xmases += find_xmases(word_search, x, y)
      # IF 'A' IS FOUND, ADD THE NUMBER OF 
      # 'X-MAS'ES IT IS PART OF. IT CAN BE 1 AT MAX.
      elif word_search[x][y] == 'A':
        x_mases += find_x_mases(word_search, x, y)

  # PRINT THE RESULTS
  print('PART 1: There are {0} XMAS-es in the word search\nPART 2: There are {1} X-MAS-es in the word search'.format(xmases, x_mases))
