import turtle
import random

my_screen = turtle.Screen()
my_screen.bgcolor("light green")
my_screen.title("Catch The Turtle")
FONT = ('Arial',20,'bold')
grid_size = 10
y_coordinate = [20,10,0,-10]
x_coordinate = [-20,-10,0,10,20]
turtles = []
score = 0
my_score = turtle.Turtle()
countdown_turtle = turtle.Turtle()
game_over = False

def setup_score_turtle():
    my_score.hideturtle()
    my_score.penup()
    full_screen = my_screen.window_height()/2
    y = full_screen * 0.85
    my_score.goto(0,y)
    my_score.color("dark blue")
    my_score.write(arg="score : 0",move=False,align="center",font=FONT)

def turtle_shape(x,y):
    def turtle_click(x,y):
        global score
        score +=1
        my_score.clear()
        my_score.write(arg=f"score : {score}",move=False,align="center",font=FONT)
    
    turtleShape = turtle.Turtle()
    turtleShape.onclick(turtle_click)
    turtleShape.shape("turtle")
    turtleShape.penup()
    turtleShape.color("green")
    turtleShape.shapesize(2,2,2)
    turtleShape.goto(x * grid_size,y * grid_size)
    turtles.append(turtleShape)

def turtlePlaces():
    for x in x_coordinate:
        for y in y_coordinate:
            turtle_shape(x,y)

def invisible_turtle():
    for turtleShape in turtles:
        turtleShape.hideturtle()

def show_turtle_random():
    if not game_over:
        invisible_turtle()
        random.choice(turtles).showturtle()
        my_screen.ontimer(show_turtle_random,500)

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    full_screen = my_screen.window_height()/2
    y = full_screen * 0.85
    countdown_turtle.goto(0,y-30)
    countdown_turtle.color("dark red")
    countdown_turtle.clear()
    if time >= 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"time : {time}",move=False,align="center",font=FONT)
        my_screen.ontimer(lambda: countdown(time-1),1000)
    else:
        game_over = True
        countdown_turtle.clear()
        invisible_turtle()
        countdown_turtle.write(arg="Game Over",move=False,align="center",font=FONT)


def start_game():
    turtle.tracer(0)
    turtlePlaces()
    setup_score_turtle()
    invisible_turtle()
    turtle.tracer(1)
    show_turtle_random()
    countdown(5)

def finish_game():
    turtle.mainloop()

start_game()
finish_game()