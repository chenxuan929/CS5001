from temperature_conversion import *
def test_convert_fahrenheit_to_celsius( temperature, expected ):
    '''
        Function tests the convert_fahreheit_to_celsius function
    '''
    result = convert_fahrenheit_to_celsius( temperature )
    print(f"Converting {temperature} F to Celsius --")
    print(f">>> result = {result:.1f} expected = {expected}")
    print( )

def test_convert_celsius_to_fahrenheit( temperature, expected ):
    '''
        Function tests the convert_celsius_to_fahrenheit function
    '''
    result = convert_celsius_to_fahrenheit( temperature )
    print(f"Converting {temperature} C to Fahrenheit --")
    print(f">>> result = {result:.1f} expected = {expected}")
    print( )
    
def main():
    
    test_convert_fahrenheit_to_celsius(32, 0.0)
    test_convert_fahrenheit_to_celsius(100, 37.8)
    test_convert_fahrenheit_to_celsius(212, 100.0)
    test_convert_fahrenheit_to_celsius(85.1, 29.5)

    test_convert_celsius_to_fahrenheit(0, 32.0)
    test_convert_celsius_to_fahrenheit(37.8, 100.0)
    test_convert_celsius_to_fahrenheit(100, 212.0)


if __name__ == "__main__":
    main()
