def check_valid_row(row):
    # check if row input is string
    if isinstance(row, str):
        row = int(row)
        
    # check if row input is int
    if 0 < row <= 8:
        return True
    return False

def check_valid_column(column: str):
    column = column.lower()
    # avoids negative number and etc
    if len(column) >= 2:
        return False
    # returns the number representing the unicode code of a specified character
    if 97 <= ord(column) <= 104:
        return True
    return False
