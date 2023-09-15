# check which color in the row and colum
def black_or_white(row, column):
    column = ord(column)
    row = int(row)
    if (row + column) % 2 == 0:
        return "BLACK"
    else:
        return "WHITE"
