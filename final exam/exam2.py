'''
    Chenxuan Xu
    Exam 2
'''
def add_value(lst, val):
    for i in range(len(lst)):
        lst[i] += val

def multiply_value(lst, val):
    for i in range(len(lst)):
        lst[i] = lst[i] * val

def higher_order(lst, val, function):
    function(lst, val)

def flip_lists(lst):
    for i in range(len(lst)):
        lst[i][0], lst[i][1] = lst[i][1], lst[i][0]

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        if width <= 0 or height <= 0:
            raise ValueError
    def area(self):
        return self.width * self.height
    def contains(self, a_point):
        if self.x <= a_point.x<= self.x + self.width and self.y <= a_point.y <= self.y + self.height:
            return True
        return False
    def __eq__(self, other):
        if self.area() == other.area():
            return True
        return False

def ducks(dict, prefixes, suffix):
    if len(prefixes) == 0:
        return False
    if len(prefixes) >= 1:
        key = prefixes[0]
        dict[key] = suffix
        answer = prefixes[1:]
        return ducks(dict, answer, suffix)
    
def is_missing(lst):
    n = len(lst)
    end = max(lst)
    if end <=n:
        end = end + 1
    number_list = sorted(set(range(1, end + 1)).difference(lst))
    s = [str(integer) for integer in number_list]#O(n)
    number = int(''.join(s))
    return number

def is_ambigram(n:int):
    if n < 0:
        raise ValueError
    n = list(str(n))
    answer = 0
    lst = ['1', '2', '5', '8', '0']
    for each in n:
        if each in lst:
            answer += 1
    if answer == len(n) and n == n[::-1]:
        return True
    else:
        return False
