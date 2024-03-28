import turtle

# יצירת חלון ומחולת ציור
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("ציור מגניב")

# יצירת פנטגון מצופה במספר צבעים
turtle.speed(100000000)  # קביעת מהירות הציור
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for _ in range(36):
    for color in colors:
        turtle.color(color)
        turtle.begin_fill()
        for _ in range(5):
            turtle.forward(100)
            turtle.right(144)
        turtle.end_fill()
        turtle.right(10)

# סיום
turtle.hideturtle()
screen.mainloop()
