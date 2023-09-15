import turtle

turtle.bgpic("shape_window.png")
turtle.screensize(canvwidth=970, canvheight=635)

def create_square(x,y):
    # move turtle to square's start point
    turtle.color('red')
    turtle.up()
    turtle.goto(x-40,y-40)
    turtle.down()
    # drawing square
    for i in range(4):
        turtle.forward(80)
        turtle.left(90)

def create_circle(x,y):
    # move turtle to circle's start point
    turtle.color('blue')
    turtle.up()
    turtle.goto(x-0,y-40)
    turtle.down()
    # drawing circle
    turtle.circle(40)

def driver():
    create_square(0,0)
    create_circle(0,0)
    
    # let user input the new position
    square_x_pos = int(input(" Insert x position for square: "))
    square_y_pos = int(input(" Insert y position for square: "))
    circle_x_pos = int(input(" Insert x position for circle: "))
    circle_y_pos = int(input(" Insert y position for circle: "))
    turtle.clear()

    turtle.fillcolor("red")
    turtle.begin_fill()
    create_square(square_x_pos,square_y_pos)
    turtle.end_fill()
    
    turtle.fillcolor("blue")
    turtle.begin_fill()
    create_circle(circle_x_pos,circle_y_pos)
    turtle.end_fill()

def main():
    driver()

if __name__ == "__main__":
    main()
