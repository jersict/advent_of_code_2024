def get_summits(map, pos):
  current_height = 0
  peaks = []
  make_step(map, pos, current_height, peaks)
  return len(list(set(peaks)))

def get_rating(map, pos):
  current_height = 0
  return make_step(map, pos, current_height, [])
  


def make_step(map, pos, height, peaks):
  rating = 0
  if map[pos[0]][pos[1]] == '9':
    peaks.append(pos)
    return 1
  else:
    if check_step(map, pos, height, 'up'):
      rating += make_step(map, (pos[0] - 1, pos[1]), height+1, peaks)
    if check_step(map, pos, height, 'down'):
      rating += make_step(map, (pos[0] + 1, pos[1]), height+1, peaks)
    if check_step(map, pos, height, 'right'):
      rating += make_step(map, (pos[0], pos[1]+1), height+1, peaks)
    if check_step(map, pos, height, 'left'):
      rating += make_step(map, (pos[0], pos[1]-1), height+1, peaks)
    return rating


def check_step(map, pos, height, dir):
  match dir:
    case 'up':
      if pos[0] > 0 and int(map[pos[0]-1][pos[1]]) == height+1:
        return True
    case 'down':
      if pos[0] < len(map) - 1 and int(map[pos[0]+1][pos[1]]) == height+1:
        return True
    case 'left':
      if pos[1] > 0 and int(map[pos[0]][pos[1]-1]) == height+1:
        return True
    case 'right':
      if pos[1] < len(map[pos[0]]) - 1 and int(map[pos[0]][pos[1]+1]) == height+1:
        return True
    case _:
      raise ValueError(f'Invalid direction {dir}')





  

if __name__ == "__main__":
  # OPEN AND READ THE INPUT.TXT FILE, THEN CLOSE IT, 
  # AS IT IS NO LONGER NEEDED.
  f = open('inputs\\10\\input.txt', 'r')
  lines = f.readlines()
  f.close()

  # DEFINE VARIABLES
  map = []
  starts = []
  sum_of_scores = 0
  sum_of_ratings = 0

  # PARSE MAP
  for i, line in enumerate(lines):
    line = line.strip()
    map.append(list(line))
    for j, c in enumerate(line):
      if c == '0':
        starts.append((i, j))

  for start in starts:
    sum_of_scores += get_summits(map, start)
    sum_of_ratings += get_rating(map, start)
  print('sum of scores', sum_of_scores)
  print('sum of ratings', sum_of_ratings)
