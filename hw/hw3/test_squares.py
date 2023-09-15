from chessboard import *
from color_square import *

def test_row( row, expected ):
    result = check_valid_row( row )
    # print the test results and expected for row
    print( f"Row: {row}, Expected: {expected}, Actual: {result}")

def test_column( column, expected ):
    result = check_valid_column( column )
    # print the test results and expected for column
    print( f"Column: {column}, Expected: {expected}, Actual: {result}")
    

def test_squares():
    # test the column
    test_column('A', True)
    test_column('d', True)
    test_column('Z', False)
    test_column('5', False)
    test_column('-1', False)
    # test the row
    test_row(7, True)
    test_row('5', True)
    test_row(10, False)
    test_row('10', False)
    test_row(-1, False)
    # test the color
    print(f" expected: BLACK, Actual: {black_or_white(3, 'a')}")
    print(f" expected: WHITE, Actual: {black_or_white(5, 'b')}")
    
def main():
    test_squares()

if __name__ == "__main__":
    main()
