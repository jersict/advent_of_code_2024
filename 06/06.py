import copy

# CHECK IF THE MAP LEADS TO A STALL. FOR EVERY STEP CHECK IF 
# THE GUARD HAS ALREADY VISITED THAT LOCATION WITH THE SAME 
# MOVING DIRECTION. IF THEY HAVE THAT MEANS A LOOP, SO RETURN 1. 
# IF THE GUARD LEAVES MAP, RETURN 0.
def map_stalls(map, pos, dir):
  positions_and_dirs = []
  steps = 0
  while pos:
    if [pos[0], pos[1], dir] in positions_and_dirs:
      return 1
    positions_and_dirs.append([pos[0], pos[1], dir])
    pos, dir = make_step(map, pos, dir)
    steps += 1
  return 0



def make_step(map, pos, dir):
  new_pos = []  
# CHECK IF NEXT STEP IS VALID, IF GOES OF MAP RETURN FALSE
# IF IT HITS A "#" MAKE A TURN, ELSE MAKE THE STEP, AND RETURN
# THE NEW POSITION. 
  match DIRS[dir]:
    case 'UP': 
      if pos[0] == 0:
        return False, False
      else:
        next_step = map[pos[0]-1][pos[1]]
        new_pos = [pos[0]-1,pos[1]]
    case 'RIGHT': 
      if pos[1] == len(map)-1:
        return False, False
      else:
        next_step = map[pos[0]][pos[1]+1]
        new_pos = [pos[0],pos[1]+1]
    case 'DOWN': 
      if pos[0] == len(map)-1:
        return False, False
      else:
        next_step = map[pos[0]+1][pos[1]]
        new_pos = [pos[0]+1,pos[1]]
    case 'LEFT': 
      if pos[1] == 0:
        return False, False
      else:
        next_step = map[pos[0]][pos[1]-1]
        new_pos = [pos[0],pos[1]-1]
  if next_step == '#':
    dir += 1
    dir = dir % 4
    return pos, dir 
  else:
    return new_pos, dir

# RUN THIS IF PROGRAM IS RUN FROM THE COMMAND LINE.
if __name__ == "__main__":

  # OPEN AND READ THE INPUT.TXT FILE, THEN CLOSE IT, AS IT IS NO LONGER NEEDED.
  f = open('06\input.txt', 'r')
  lines = f.readlines()
  f.close()

  # DIRECTIONS CONSTANTS
  DIRS = ['UP', 'RIGHT', 'DOWN', 'LEFT']
  VISUALIZE = False

  # DECLARE VARIABLES
  map = []
  pos = []
  dir = 0
  unique_positions = []
  visited = []
  total_stalls = 0

  # PREPROCESS DATA, BUILD MAP, GET PRIMARY POSITION
  for i, line in enumerate(lines):
    l = list(line.strip())
    if '^' in l:
      pos.append(i)
      pos.append(l.index('^'))
    map.append(l)
  
  # COPY pos TO current_pos WHICH WILL BE USED FOR PART 1.
  current_pos = copy.copy(pos)

  # WHILE current_pos HAS A VALUE, IT MEANS IT IS STILL ON THE BOARD.
  # IF THE CURRENT POSITION IS NOT YET IN THE unique_positions, ADD IT.
  # THEN EXECUTE make_step TO GET THE NEXT POSITION AND DIRECTION.
  while current_pos:
    if [current_pos[0], current_pos[1]] not in unique_positions:
      unique_positions.append([current_pos[0], current_pos[1]])
    current_pos, dir = make_step(map, current_pos, dir)
  
  # REMOVE THE FIRST UNIQUE POSITION, AS IT IS THE STARTING POSITION,
  # WHERE A NEW OBSTACLE CAN'T BE PLACED.
  unique_positions.pop(0)

  # FOR EVERY UNIQUE POSITION CHECK IF AN OBSTACLE THERE LEADS TO A STALL.
  # ADD THE RETURN OF THE map_stalls() TO total_stalls
  for i, position in enumerate(unique_positions):
    new_map = copy.deepcopy(map)
    new_map[position[0]][position[1]] = '#'
    total_stalls += map_stalls(new_map, pos, 0)

  # PRINT THE RESULTS
  print('PART 1: The number of unique positions the guard visits is {0}\nPART 2: The number of valid new obstacle positions is {1}'.format(len(unique_positions)+1, total_stalls))