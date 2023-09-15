
class Fraction:
    """Class Fraction"""
    def __init__(self, top, bottom):
        """Constructor definition"""
        self.num = top
        self.den = bottom
        
    def __str__(self):
      return f"{self.num}/{self.den}"

    def __add__(self, other_fraction):
      new_num = self.num * other_fraction.den + \
                 self.den * other_fraction.num
      new_den = self.den * other_fraction.den

      return Fraction(new_num, new_den)