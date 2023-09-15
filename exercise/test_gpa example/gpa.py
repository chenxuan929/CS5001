from calculate_gpa import calculate_gpa
def test_update_gpa(current_gpa, num_classes, new_grade, expected):
    '''
        Function tests the calculate_gpa function <etc>
    '''
    print(f"Testing inputs {current_gpa}, {num_classes}, {new_grade}")
    print(f"Expected result = {expected}")
    actual = calculate_gpa(current_gpa, num_classes, new_grade)
    print(f"Actual result = {actual}\n*****\n")
def main():
    # Test 1: 0.0, 0 classes, get a 3.5. GPA should be 3.5
    test_update_gpa(0.0, 0, 3.5, 3.5)
    
    # Test 2: 4.0, 1 classes, get a 1.0. GPA should be 2.5
    test_update_gpa(4.0, 1, 1.0, 2.5)
if __name__ == "__main__":
    main()
    
