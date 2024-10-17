import turtle

# Set up the turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("green")

# Draw the sun
t.penup()
t.goto(10, 10)  
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(10) 
t.end_fill()

# Draw mountains
t.penup()
t.goto(-200, -100)  
t.pendown()
t.fillcolor("black")
t.begin_fill()

# Mountain 1
t.goto(-100, 100)  
t.goto(0, -100)   
# Mountain 2
t.goto(100, 100)    
t.goto(200, -100)  

t.goto(200, 100)  
t.end_fill()

# Draw the grass
t.penup()
t.goto(-300, -150)  
t.pendown()
t.fillcolor("green")
t.begin_fill()

t.goto(300, -150)   
t.goto(300, -200)
t.goto(-300, -200)
t.goto(-300, -150)

t.end_fill()
turtle.done()