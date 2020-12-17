import turtle,time

def drawpath(pos,len):
    turtle.goto(pos)
    turtle.setheading(22.5)
    turtle.forward(len)
    turtle.goto(pos)
    turtle.setheading(360-22.5)
    turtle.forward(20)

if __name__ == "__main__" :
    print("Current Programm path: "+str(__name__))
    previos_position = turtle.position()
    turtle.color("blue")
    turtle.speed(0)
    firstnbranches=int(input("Wie viele Pfade sollte es von der Wurzel aus geben?"))
    secondnbranches=int(input("Wie viele Pfade sollte es in der zweiten Stufe geben?"))
    thirdnbranches=int(input("Wie viele Pfade sollte es in der drittern Stufe geben?"))
    fourthnbranches=int(input("Wie viele Pfade sollte es in der vierten Stufe geben?"))
    fifthnbranches=int(input("Wie viele Pfade sollte es in der fünften Stufe geben?"))
    turtle.dot(10)
    drawpath(previos_position)
    turtle.done()
