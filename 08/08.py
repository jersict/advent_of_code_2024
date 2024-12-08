# TUPLE ADDITION FUNCTION
def add(a, b):
  return (a[0]+b[0], a[1]+b[1])

# TUPLE SUBTRACTION FUNCTION
def subtract(a, b):
  return (a[0]-b[0], a[1]-b[1])

# TUPLE SCALE FUNCTION
def scale(a, n):
  return (a[0]*n, a[1]*n)

# TUPLE INVERSION FUNCTION
def invert(a):
  return (-a[0], -a[1])

# FOR THE POSITION ON THE MAP, FOR EACH ANTENNA, 
# CHECK IF THERE IS ANOTHER ANTENNA IN THE SAME 
# DIRECTION, BUT WITH DOUBLE DISTANCE. IF YES 
# RETURN 1, ELSE RETURN CHECK OTHER ANTENNAS. 
# IF ANTENNAS RUN OUT RETURN 0.
def check_if_antinode(pos, antennas):
  for group in antennas:
    for antenna in group:
      distance = subtract(antenna, pos)
      if distance == (0,0):
        continue
      if add(pos, scale(distance, 2)) in group:
        #print(pos)
        return 1     
  return 0

# FOR EACH GROUP OF ANTENNAS (ONES WITH THE 
# SAME SYMBOL), GO THROUGH EACH PAIR OF ANTENNAS 
# AND APPEND THEIR ANTINODES. AT THE END REMOVE 
# THE DUPLICATES BY CONVERTING TO DICT AND BACK.
def list_resonant_antinodes(antennas):
  antinodes = []
  for group in antennas:
    for i in range(len(group)):
      for j in range(i+1, len(group), 1):
        first_antenna = group[i]
        second_antenna = group[j]
        antinodes.append(first_antenna)
        antinodes.append(second_antenna)
        direction = subtract(first_antenna, second_antenna)
        n = 1
        while(True):
          next_node = add(first_antenna, scale(direction, n))
          if 0 > next_node[0] or len(map)-1 < next_node[0] or 0 > next_node[1] or len(map)-1 < next_node[1]:
            n = 1
            break
          antinodes.append(next_node)
          n+=1
        direction = invert(direction)
        while(True):
          next_node = add(second_antenna, scale(direction, n))
          if 0 > next_node[0] or len(map)-1 < next_node[0] or 0 > next_node[1] or len(map)-1 < next_node[1]:
            n = 1
            break
          antinodes.append(next_node)
          n+=1
  return list(dict.fromkeys(antinodes))


# RUN THIS IF PROGRAM IS RUN FROM THE COMMAND LINE.
if __name__ == "__main__":
  # OPEN AND READ THE INPUT.TXT FILE, THEN CLOSE IT, 
  # AS IT IS NO LONGER NEEDED.
  f = open('08\input.txt', 'r')
  lines = f.readlines()
  f.close()

  # DEFINE VARIABLES
  map = []
  antennas = {}
  antinodes = 0

  # SCAN MAP, SAVE ANTENNA LOCATIONS TO antennas DICTIONARY.
  for i, line in enumerate(lines):
    map_line = list(line.strip())
    for j in range(len(map_line)):
      if map_line[j] != '.':
        antenna = map_line[j]
        if antenna not in antennas.keys():
          antennas[antenna] = []
        antennas[antenna].append((i, j))
    map.append(map_line)
  
  # CONVERT antennas TO LIST, TO EASE THE NAVIGATION.
  antennas = list(antennas.values())
  
  # GO OVER THE ENTIRE MAP AND CHECK FOR EVERY 
  # POSITION IF IT CONTAINS AND ANTINODE. ADD THE 
  # RESULT TO antinodes.
  for m in range(len(map)):
    for n in range(len(map[m])):
      antinodes += check_if_antinode((m, n), antennas)
  
  # GET A LIST OF ALL RESONANT ANTINODES. SAVE THE LENGTH.
  resonant_antinodes = len(list_resonant_antinodes(antennas))
  
  # PRINT THE RESULTS
  print('PART 1: There are a total of {0} antinodes\nPART 2: There are a total of {1} resonant antinodes'.format(antinodes, resonant_antinodes))
  