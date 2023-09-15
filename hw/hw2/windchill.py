from temperature_conversion import *
def calculate_windchill(temperature, speed):
    '''
    Function: calculate_windchill
        Calculates windchill based on international formula (Metric)
    Parameters:
        temperature in Fahrenheit
        speed in miles per hour
    Returns: windchill index (floating point value) based on applied formula
    Require: temp/speed in metric units
    Ensure: metric -> imperial unit conversions prior to calculation
    '''

    # 1 Miles per hour = 1.61 kilometers-per-hour
    T = convert_fahrenheit_to_celsius( temperature )
    V = speed * 1.61
    
    Windchill_Index = float( 13.12 + 0.6215 * T - 11.37
                             * (V ** 0.16) + 0.3965 * T * ( V ** 0.16))
    
    answer = convert_celsius_to_fahrenheit( Windchill_Index )
    
    return answer
