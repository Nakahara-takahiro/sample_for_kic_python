from turtle import *

class Joystick(Turtle):
  def __init__(self, pos=(100,100), radius=50):
    self.input = Vec2D(0,0)
    self.center = Vec2D(*pos)
    self.radius = radius
    super().__init__(shape='circle')
    tracer(0)
    self.penup()
    self.setpos(self.center-(0,self.radius))
    self.pendown()
    self.pen(pensize=3, fillcolor='gray')
    self.circle(self.radius)
    self.penup()
    self.fillcolor('red')
    self.setpos(self.center)
    tracer(1)
    self.target = None
    self.ondrag(self.Drag)
    self.onrelease(self.Release)

  def Release(self, x, y):
    self.setpos(self.center)
    self.input = Vec2D(0.,0.)

  def Drag(self, x, y):
    vec = Vec2D(x,y) - self.center
    if abs(vec)>self.radius:
      vec *= self.radius/abs(vec)
      x, y = self.center + vec
    self.input = (Vec2D(x,y) - self.center)*self.radius**-1
    self.setpos(x,y)

class Cart(Turtle):
  def __init__(self):
    super().__init__(shape='turtle')
    self.speed(0)
    self.velocity = 0.0
    self.handle = 0.0

  def Tick(self, dt):
    distance = self.velocity*dt
    self.forward(50.0*distance)
    self.setheading(self.heading() + 200.0*self.handle*distance)

stick = Joystick()
cart = Cart()

def tick():
  dt = 0.1
  cart.handle = -stick.input[0]
  cart.velocity = stick.input[1]
  cart.Tick(dt)
  ontimer(tick, int(dt*1000))

ontimer(tick)
mainloop()