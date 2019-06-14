#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  options = ['rock', 'paper', 'scissors']
  allPossibilities = []

  def roundChoice(round, roundNumber):#creating a function within a function to call later
    for i in options:#iterating through options (rps)
      round.append(i);#pushing each option into the empty array (round)
      if roundNumber == n:# if roundNumber equals n 
        allPossibilities.append(round[:])# 
      else:
        roundChoice(round, roundNumber + 1)
      round.pop()

  roundChoice([], 1)
  return allPossibilities

print(rock_paper_scissors(1))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')