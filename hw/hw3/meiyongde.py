
'''
    check if the row/column is valid or not for the srandard chessboard
'''

def check_valid_row(row):
    # check if row input is string
    if isinstance(row,str):
        if str(row).upper() == 'FIVE':
            row == 5
        
        row = int(row)
        
    # check if row input is int
    if 0 < row <= 8:
        return True
    return False

def check_valid_column(column:str):
    column = column.lower()
    
    if len(column) >= 2:
        return False
    if 97 <= ord(column) <= 104:
        return True
    return False
