import turtle
from PositionService import *

# set background and pen color
turtle.bgpic("shape_window.png")
turtle.bgpic()
turtle.screensize(canvwidth=970, canvheight=635)
_pen = turtle.Turtle()
_pen.color('green')

# drawing circle
def circle(x,y):
    center_x = x
    center_y = y - 80
    _pen.up()
    _pen.goto(center_x,center_y)
    _pen.down()
    _pen.circle(80)
# save the position of circle as previous position
    set_position_x( center_x )
    set_position_y( center_y )
    
# click point in canvas and get the currently position
def get_click(x,y):
    global _pen
    print(f"you just clicked ({x},{y})")
    # get the previous position
    center_x = get_position_x() 
    center_y = get_position_y()
    print(f"your previous position is ({center_x}, {center_y})")
    # compare two position.
    # if click outside, ignore the click. if inside, clear the circle
    if is_visible():
        if center_x - 80 < x < center_x + 80 and center_y < y < center_y + 160:
            print("Clear the previous circle")
            _pen.clear()
            set_visible(False)
    # click on blank canvas, draw the circle
    else:
        circle(x, y)
        set_visible(True)


def main():
    # Draw a circle with a RADIUS of 80 starting at (0, 0)
    circle(0,0)
    screen = turtle.Screen()
    while True:
        screen.onclick(get_click)
        screen.mainloop()

if __name__ == "__main__":
    main()
