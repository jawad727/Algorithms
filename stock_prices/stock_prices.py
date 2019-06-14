#!/usr/bin/python

ary = [100, 90, 80, 50, 20, 10]

import argparse

def find_max_profit(prices):
  highest_return = -1000000
  lowest_sofar = 1000000

  for i in range(0, len(prices)):
    if prices[i] - lowest_sofar > highest_return:
      highest_return = prices[i] - lowest_sofar
    if prices[i] < lowest_sofar:
      lowest_sofar = prices[i]
  return(highest_return)




# We need to iterate through the array
# For each iteration we need to subtract smallest number so far from current number and store the value if its the biggest
# We then return the biggest return 

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))