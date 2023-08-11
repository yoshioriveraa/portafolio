#!/usr/bin/python3
import numpy as np
def _main() -> None:
  # TODO: fixme.
  
  N = int(input())

  str1 = input()
  arr1 = np.array([int(i) for i in str1.split(' ')])

  str2 = input()
  arr2 = np.array([int(i) for i in str2.split(' ')])

  for j in (str1 > str2):
    if j == True:
      return 1
    else:
      return 0

if __name__ == '__main__':
  _main()