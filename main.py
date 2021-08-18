from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)  # don't refresh the screen until typing update

sam = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(sam.up, "Up")
screen.onkey(sam.down, "Down")
screen.onkey(sam.left, "Left")
screen.onkey(sam.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    sam.move()

    # Detect collision with food
    if sam.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        sam.extend()

    # Detect collision with wall
    if sam.head.xcor() > 280 or sam.head.xcor() < -280 or sam.head.ycor() > 280 or sam.head.ycor() < -280:
        scoreboard.reset()
        sam.reset()

    # Detect collision of tail
    for segment in sam.segments[1:]:
        if sam.head.distance(segment) < 10:
            scoreboard.reset()
            sam.reset()


screen.exitonclick()
