# |20.DAN|

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
  screen.update()
  time.sleep(0.1)
  snake.move()

  if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    scoreboard.increase_score()

  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    scoreboard.reset()

  for segment in snake.segments[1:]:
    if segment == snake.head:
      pass
    elif snake.head.distance(segment) < 10:
      scoreboard.reset()
      snake.reset()

screen.exitonclick()

# |21.DAN|

# CLASS INHERITANCE (NASLEDJIVANJE)

# NPR
# class Fish(Animal): Zagrada sluzi da pokaze klasu od koje klasa Fish nasledjuje stvari
#   def __init__(self): Klasicno pravljenje inicijatora tj. konstruktora
#     super().__init__(): super() sluzi da oznaci super klasu tj klasu Animal i .__init__() oznacava da se inicijalizuje(nasledjuje) sve iz klase Animal u klasi Fish

# class Animal:
#     def __init__(self):
#         self.num_eyes = 2

#     def breathe(self):
#         print("Inhale, exhale.")

# class Fish(Animal):
#     def __init__(self):
#         super().__init__()

#     def breathe(self):
#         super().breathe()
#         print("doing this underwater.")

#     def swim(self):
#         print("moving in water.")

# nemo = Fish()
# nemo.breathe()

# SLICING

# piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
# piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")
# print(piano_tuple[1:]) printuje sve od prvog do poslednjeg elementa