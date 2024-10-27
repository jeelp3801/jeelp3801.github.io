from sympy import symbols, Eq, solve
import turtle

x, y = symbols('x y')
equation = Eq(x**(2/3), y)
solution = solve(equation, (x, y))
x_value = solution[0][0].subs('y', -100)
print(f"When x is {-100}, y is: {x_value}")
"""
while -11<i<11:
    x_value = solution[0][0].subs('y', i)
    print(f"When x is {i}, y is: {x_value}")
    i=i+0.25

------------------------------------
x,y= symbols('x y')
print("Enter the equation here: ")
eq = input("(Single variable x) -- (Space every time there is a sign) \n\n\nf(x)= ").split()
for i in range(0,len(eq)):
    
    if eq[i].isnumeric():
        eq[i]=float(eq[i])
    elif eq[i].isalpha():
        pass
    elif not(eq[i].isspace):
        if 
---------------------------------------
# Input string
input_string = "3*x + (12)**(1/2)"

# Define the variable x
x = 5  # You can set any value for x

# Convert the string to a Python expression and evaluate it
result = eval(input_string)

# Print the result
print(result)
"""
print("Enter the equation here: ")
eq = input("(Single variable x) -- (Space every time there is a sign) \n\n\nf(x)= ")
screen = turtle.Screen()
tur = turtle.Turtle()
tur.forward(300)
tur.forward(-600)
tur.goto(0,0)
tur.right(90)
tur.forward(300)
tur.forward(-600)
tur.goto(0,0)
tur.penup()
for x in range(-10,110):
    y=(eval(eq))
    y=y.real
    print(f"for x= {x}, y is {(y).real}")
    tur.goto(x,(y).real)
    tur.pendown()
    if y>1000:
        break


#tur.forward(100)
screen.exitonclick()