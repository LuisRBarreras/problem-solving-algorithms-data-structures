# from fractions import Fraction
from src.anagram import is_anagram

def find_min_number(collection):
  min_number = None
  for number in collection:
    if min_number == None or min_number > number:
       min_number = number
    
  return min_number

if __name__ == '__main__':
    # my_fraction = Fraction(3, 5)
    # f2 = Fraction(1,2)
    # print(my_fraction + f2)
    result = is_anagram('alla', 'alla')
    print(result)
    



      
  


    # Write two Python functions to find the minimum number in a list. 
    # The first function should compare each number to every other number on the list. 
    # The second function should be linear 