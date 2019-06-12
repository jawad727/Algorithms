#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):

  minimum_number = 1000000

  for key in recipe:
    if key in ingredients:

      eachBatch = ingredients[key] / recipe[key]
      if eachBatch < minimum_number:
        minimum_number = int(eachBatch)

    else:
      minimum_number = 0

  return minimum_number

# The function takes in a recipe dictionary and a ingredients dictionary
# It needs iterate through the keys in the first dictionary and match them with the keys of the second
# 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))