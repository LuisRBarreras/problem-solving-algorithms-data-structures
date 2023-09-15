# anagram detection problem for strings. 
# One string is an anagram of another if the second is simply a rearrangement of the first. 
#  For the sake of simplicity, we will assume that the two strings in question are of equal length and 
# that they are made up of symbols from the set of 26 lowercase alphabetic characters. 
# Our goal is to write a boolean function that will take two strings and return whether they are anagrams.
from collections import defaultdict

def is_anagram(word1, word2):
  result = True
  characters_set = {}

  for char in word1:
    if char not in  characters_set:
      characters_set[char] = 0

    characters_set[char] += 1

  for char in word2:
    if char not in  characters_set:
      result = False
    characters_set[char] -= 1
    

  print(characters_set, characters_set.values())

  for value in characters_set.values():
    if value != 0:
      result = False

  
  return result
  
  
if __name__ == '__main__':
    # my_fraction = Fraction(3, 5)
    # f2 = Fraction(1,2)
    # print(my_fraction + f2)
    case1 = is_anagram('alla', 'alla')
    assert case1 == True

    case2 = is_anagram('ailla', 'alla')
    assert case2 == False
  
