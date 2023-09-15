class SimpleFraction:
    def __init__(self, numerator = 1, denominator= 1):
        if denominator == 0 or numerator == 0:
            raise ValueError
        else:
            self.numerator = numerator
            self.denominator = denominator

    def get_numerator(self):
        return self.numerator
    
    def get_denominator(self):
        return self.denominator
    
    def make_reciprocal(self):
        new_numerator = self.denominator
        new_denominator = self.numerator
        return SimpleFraction(new_numerator, new_denominator)
    
    def validate(self):
        if not (isinstance(self.get_numerator(),int) and isinstance(self.get_denominator(),int)):
            raise ValueError
        
    def multiply(self, other):
        if isinstance(other, int):
            if other == 0:
                raise ValueError
            else:
                new_numerator = self.numerator * other
                new_denominator = self.denominator
        else:
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
        return SimpleFraction(new_numerator, new_denominator)

    def divide(self, other):
        if isinstance(other, int):
            if other == 0:
                raise ValueError
            else:
                new_numerator = self.numerator
                new_denominator = self.denominator * other
        else:
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
        return SimpleFraction(new_numerator, new_denominator)
            
    
    def __str__(self):
        return f'{self.get_numerator()}/{self.get_denominator()}'
    
    def __eq__(self, other):
        answer = self.divide(other)
        return answer.get_numerator() == answer.get_denominator()
            
