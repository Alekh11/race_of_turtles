from turtle import Turtle,Screen 
import random
import turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=500 , height=400)
bet = screen.textinput(title = "Make your bet", prompt="Which turtle will win the race? Choose a color: ")
colors = ["red","yellow","green","white","orange", "blue", "pink"]
y_axis = [-70, -40, -10, 20, 50, 80]
all_turtles = []

race_on = False

for turtle_index in range(0,6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_axis[turtle_index])
    all_turtles.append(new_turtle)
if bet: 
    race_on = True
    
while race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230 :
            race_on = False 
            winning_color = turtle.pencolor()
            if winning_color == turtle.pencolor() == bet:
                print(f"The {winning_color} turtle wins the race. You WON!")
            else :
                print (f"The {winning_color} turtle won. You LOSE! ")
            
            
            random_distance = random.randint(0,10)
            turtle.forward(random_distance)




screen.exitonclick()