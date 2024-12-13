# RUN THIS IF PROGRAM IS RUN FROM THE COMMAND LINE.
if __name__ == "__main__":
  # OPEN AND READ THE INPUT.TXT FILE, THEN CLOSE IT, 
  # AS IT IS NO LONGER NEEDED.
  f = open('09\input.txt', 'r')
  file = f.read()
  disk_map = list(file.strip())
  f.close()

  # disk_map = list('2333133121414131402')
  
  # DEFINE VARIABLES FOR PART 1
  checksum = 0
  filled_loop = int(disk_map.pop(0))
  empty_loop = 0
  front_id = 0
  position = 0 
  map_position = 0
  back_id = int(len(disk_map)/2)
  back_val = int(disk_map.pop(-1))

  while True:
    for i in range(filled_loop):
      checksum += position * front_id
      position += 1
    empty_loop = int(disk_map.pop(0))
    if len(disk_map) < 1:
      break
    for i in range(empty_loop):
      if back_val == 0:
        disk_map.pop(-1)
        back_val = int(disk_map.pop(-1))
        back_id -= 1
      checksum += position * back_id      
      back_val -= 1
      position += 1
    if len(disk_map) < 1:
      break    
    filled_loop = int(disk_map.pop(0))
    front_id += 1
  for i in range(back_val):
    checksum += position * back_id
    position += 1
  
  disk_map = [int(x) for x in file.strip()]
  # disk_map = [int(x) for x in '1254321']

  # DEFINE VARIABLES FOR PART 2
  checksum_part_2 = 0
  last_pos_start = sum(disk_map)
  empty_spaces = []
  position_from_start = 0
  back_id = int(len(disk_map)/2) 
  moved = False

  # POPULATE THE DICTIONARY OF EMPTY SPACES
  for i in range(len(disk_map)):
    size = disk_map[i]
    #SKIP IF IT IS A TAKEN SPACE
    if i % 2 == 0:
      position_from_start += size
      continue
    empty_spaces.append((position_from_start, size))
    position_from_start += size

  empty_spaces.sort()
  for j in range(len(disk_map)-1, -1, -2):
    moved = False
    size = disk_map[j]
    last_pos_start -= size
    max_size_available = max([x[1] for x in empty_spaces])
    if size <= max_size_available: 
      for x, space in enumerate(empty_spaces):
        if space[1] >= size and space[0] < last_pos_start:
          moved = True
          position = space[0]
          for i in range(size):
            checksum_part_2 += (position+i)*back_id
          removed = empty_spaces.pop(x)
          if size < space[1]:
            remainder = space[1] - size
            empty_spaces.append((position+size, remainder))
            empty_spaces.sort()
          back_id -= 1
          last_gap = disk_map[j-1]
          last_pos_start = last_pos_start - last_gap  
          break
      if not moved:
        for i in range(size):
          checksum_part_2 += (last_pos_start+i)*back_id
        back_id -= 1
        last_gap = disk_map[j-1]
        last_pos_start = last_pos_start - last_gap  
    else:

      for i in range(size):
        checksum_part_2 += (last_pos_start+i)*back_id
      back_id -= 1
      last_gap = disk_map[j-1]
      last_pos_start = last_pos_start - last_gap  

  print(checksum, checksum_part_2)
