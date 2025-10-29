from turtle import Screen, Turtle

screen = Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")

segment_1 = Turtle("square")
segment_1.color("white")

segment_2 = Turtle("square")
segment_2.color("white")

segment_3 = Turtle("square")
segment_3.color("white")




screen.exitonclick()