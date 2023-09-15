class SimpleFraction:
    # creating SimpleFraction instance, setting default values of 1 and 1
    def __init__(self, numerator=1, denominator=1):
        # raising error when denominator is zero
        if denominator == 0:
            raise ValueError
        # assigning values to the data members of the class
        else:
            self.numerator = numerator
            self.denominator = denominator
    
    def get_numerator(self):
        return self.numerator
    
    def get_denominator(self):
        return self.denominator
    
    def make_reciprocal(self):
        # setting current instance’s numerator as its denominator
        # current instance’s denominator as its numerator
        new_numerator = self.denominator
        new_denominator = self.numerator
        # returning new SimpleFraction
        return SimpleFraction(new_numerator, new_denominator)
    
    def validate(self):
        # Checking to ensure that the numerator and denominator are integers
        if not (isinstance(self.get_numerator(), int)
                or not isinstance(self.get_denominator(), int)):
            raise ValueError
        
    def multiply(self, other):
        # Multipling the current instance with a whole number
        if isinstance(other, int):
            new_numerator = self.numerator * other
            new_denominator = self.denominator
        else:
            # Multipling the current instance with another SimpleFraction
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
        return SimpleFraction(new_numerator, new_denominator)

    def divide(self, other):
        # Dividing the current instance with an whole number 
        if isinstance(other, int):
            new_numerator = self.numerator
            new_denominator = self.denominator * other
        # Dividing the current instance with another SimpleFraction 
        else:
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
        return SimpleFraction(new_numerator, new_denominator)  
    
    def __str__(self):
        # Returning a string representation of SimpleFraction instances
        return f'{self.get_numerator()}/{self.get_denominator()}'
    
    def __eq__(self, other):
        # dividing each other to check if is equal one
        answer = self.divide(other)
        # Returnning True if they are equal, False otherwise
        return answer.get_numerator() == answer.get_denominator()
            
