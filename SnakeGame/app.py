from turtle import Screen, Turtle
from time import sleep

screen = Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")

starting_position = [(0, 0 ), (-20, 0), (-40, 0)]
segments = []

for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    for seg in segments:
        seg.forward(20)

break

# start a proper game loop (we broke out of the previous placeholder loop above)
screen.tracer(0)

head = segments[0]

while True:
# move each segment to the position of the segment in front of it
for idx in range(len(segments) - 1, 0, -1):
    new_x = segments[idx - 1].xcor()
    new_y = segments[idx - 1].ycor()
    segments[idx].goto(new_x, new_y)
head.forward(20)

screen.update()
sleep(0.1)

screen.exitonclick()