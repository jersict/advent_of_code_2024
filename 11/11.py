import copy

if __name__ == "__main__":
  # OPEN AND READ THE INPUT.TXT FILE, THEN CLOSE IT, 
  # AS IT IS NO LONGER NEEDED.
  f = open('inputs\\11\\input.txt', 'r')
  line = f.read().strip().split(' ')
  f.close()
  stones = {x:line.count(x) for x in line}

  for i in range(75):
    new_state = {}
    shift = 0
    for key in stones.keys():
      if key == '0':
        if '1' in new_state.keys():
          new_state['1'] += stones['0']
        else:
          new_state['1'] = stones['0']
      elif len(key)%2 == 0:
        first = str(int(key[:len(key)//2]))
        second = str(int(key[-len(key)//2:]))
        if first in new_state.keys():
          new_state[first] += stones[key]
        else:
          new_state[first] = stones[key]
        if second in new_state.keys():
          new_state[second] += stones[key]
        else:
          new_state[second] = stones[key]
      else:
        new_key = str(int(key)*2024)
        if new_key in new_state.keys():
          new_state[new_key] += stones[key]
        else:
          new_state[new_key] = stones[key]
    
    stones  = new_state
    if i == 24:
      print(sum(stones.values()))
  print(sum(stones.values()))
  

