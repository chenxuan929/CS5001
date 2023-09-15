from SimpleFraction import SimpleFraction
import unittest

class Testing(unittest.TestCase):
    # setting some example to check the functions
    c = SimpleFraction(1,3)
    d = SimpleFraction(2,2)
    e = SimpleFraction()
    
    def test_init(self):
        # testing __init__ function
        a = SimpleFraction(1,1)
        b = SimpleFraction()
        self.assertEqual(a.get_numerator(), b.get_denominator())
        self.assertEqual(a.make_reciprocal(), b.make_reciprocal())
        
    def test_numerator(self):
        # testing get_numerator function
        self.assertEqual(str(self.c.get_numerator()), '1')

    def test_denominator(self):
        # testing get_denominator function
        self.assertEqual(str(self.c.get_denominator()), '3')
        
    def test_multiply(self):
        # testing multiply function
        self.assertEqual(str(self.c.multiply(3)), '3/3')
        
    def test_divide(self):
        # testing divide function
        self.assertEqual(str(self.c.divide(3)), '1/9')
                
    def test_eq(self):
        # testing __eq__ function
        e = SimpleFraction()
        d = SimpleFraction(2,2)
        self.assertEqual(self.c.__eq__(e), False)
        self.assertEqual(self.e.__eq__(d), True)
        
    def test_recip(self):
        # testing make_reciprocal function
        self.assertEqual(str(self.c.make_reciprocal()), '3/1')
        
    def test_str(self):
        # testing __str__ function
        self.assertEqual(str(self.c.__str__()), '1/3')
        
def main():
    unittest.main(verbosity=2)
    
if __name__ == "__main__":
    main()

