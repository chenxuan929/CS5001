from turtle import *
import turtle as tur

def getPosition(x,y):
    print(f" you just clicked ({x}, {y})")
    

def main():
    screen = tur.Screen()
    screen.onclick(getPosition)
    screen.mainloop()
    
main()
