import turtle
__import__("turtle").__traceable__ = False

def draw_squre(t, size):
    for i in range(4):
        t.forward(size)
        t.left(90)

def draw_multicolor_squre(t, size):
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(size)
        t.left(90)
wn = turtle.Screen()
#wn.bgcolor("green")
wn.title("Hello, U")
alex = turtle.Turtle()
alex.shape('turtle')
alex.color("blue")
alex.pensize(3)

size = 20
for n_of_square in range(10):
    draw_multicolor_squre(alex, size)
    alex.right(12)
    size += 4


# draw_squre(alex, 50)

# alex.forward(50)
# alex.left(90)
# alex.forward(30)

wn.mainloop()
