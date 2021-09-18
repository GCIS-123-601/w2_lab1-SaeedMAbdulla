import turtle
def test_state():
    turtle.forward(40)
    turtle.down()
    turtle.right(55)
    turtle.setheading(90)
    turtle.goto(33,90)
    turtle.left(10)
    turtle.home()
def main():
    test_state()
    input("press key to continue..")
main()