import turtle,random

def drawpath(len,level):

    oldpos = turtle.position()
    if level > 0:
        turtle.setheading(22.5)
        turtle.pendown()
        turtle.forward(len)
        turtle.dot(5)
        turtle.penup()
        drawpath(len*0.6,level = level - 1)
        turtle.goto(oldpos)
        turtle.setheading(-22.5)
        turtle.pendown()
        turtle.forward(len)
        turtle.dot(5)
        turtle.penup()
        drawpath(len*0.6,level = level - 1)
    else:

        return;

if __name__ == "__main__" :
    print("Current Programm path: "+str(__name__))
    previos_position = turtle.position()
    turtle.color("blue")
    turtle.speed(0)
    layeramaount = int(input("Wie Viele Ebenen wird es geben?"))

    turtle.dot(10)

    drawpath(200,layeramaount)
