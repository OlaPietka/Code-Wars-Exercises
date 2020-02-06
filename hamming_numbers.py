import itertools

hamming_num = []
init = True

def hamming(n):
  global init
  
  if init:
      global hamming_num
      
      possible_int = list(itertools.product(range(0, 33), repeat=3))
      hamming_num = [2**i[0] * 3**i[1] * 5**i[2] for i in possible_int]
      hamming_num.sort()
      init = False
      
  return hamming_num[n - 1]