import turtle

def draw_flower():
  window = turtle.Screen()
  window.bgcolor("red")
  brad = turtle.Turtle()
  brad.shape("turtle")
  brad.color("yellow")
  brad.speed(10)
  for i in range(0,20):
    brad.forward(60)
    brad.left(45)
    brad.forward(30)
    brad.left(90)
    brad.forward(30)
    brad.left(45)
    brad.forward(60)
    brad.left(30)
    brad.right(10)

  brad.forward(10)
  brad.right(90)
  brad.forward(200)
  brad.right(90)
  brad.forward(10)
  brad.right(90)
  brad.forward(200)

  window.exitonclick()

draw_flower()

def draw_object(m,n=None):
  no_of_polygon = m
  no_of_sides = n

  window = turtle.Screen()
  window.bgcolor("red")
  brad = turtle.Turtle()
  brad.shape("turtle")
  brad.color("yellow")
  brad.speed(10)

  for i in range():
