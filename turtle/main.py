import colorgram
import turtle as t
import random

tim = t.Turtle()
rgb_colors = []

colors = colorgram.extract('turtle.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

tim.penup()
t.colormode(255)
tim.speed("fastest")
for i in range(0, 500, 50):
    for j in range(0, 500, 50):
        tim.setpos(j-250, i-250)
        tim.dot(20, random.choice(rgb_colors))


screen = t.Screen()
screen.exitonclick()