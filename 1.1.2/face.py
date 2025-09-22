# import the turtle module
import turtle as trtl

# create the turtle object
painter = trtl.Turtle()

# User picks the color of the drawing
#color = input("What is your favorite color?")
color = "purple"


painter.circle(50)

# Penup stops the turtle from drawing
painter.penup()
painter.forward(100)
#Pendown start the turtle drawing

painter.pendown()
painter.circle(50)



# get the screen object and make it persist
wn = trtl.Screen()
wn.mainloop()