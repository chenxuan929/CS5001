import turtle

def draw_square(myTurtle, sideLength):
    myTurtle.forward(sideLength) #side 1
    myTurtle.right(90)
    myTurtle.forward(sideLength) #side 2
    myTurtle.right(90)
    myTurtle.forward(sideLength) #side 3
    myTurtle.right(90)
    myTurtle.forward(sideLength) #side 4
    myTurtle.right(90)

def main():
    t = turtle.Turtle()
    draw_square(t,100)

if __name__ == "__main__":
    main()



def menu(question):
    answer = input(question)
    return answer

def main():
    question = ('How do you like to keep active?\n'
                ' A: Running\n B: Birdwatching\n'
                ' C: Swimming\n D: Does laying on a couch count?\n Your answer:')
    answer = menu(question)
    print('You selected: ', answer)

main()



    
