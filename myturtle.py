import turtle
angle=80
def square_func(size,angle):
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)
    #turtle.setheading(127)
    #turtle.up()
    #turtle.goto(50,40)
    #turtle.down()
    turtle.home()
    #turtle.circle(25)
def turtle_state():
    v2=turtle.isdown()
    v3=turtle.heading()
    vx=turtle.xcor()
    vy=turtle.ycor()
    print("turtle is down?", v2)
    print("current angle: ", v3)
    print("xcor: ", vx, "ycor: ", vy)

def main():
    size=int(input("enter a size: "))
    square_func(size,angle)
    size=int(input("enter a size: "))
    square_func(size,angle)
    size=int(input("enter a size: "))
    square_func(size,angle)
    turtle_state()
    input("press key to continue.. ")
main()    