import turtle

bob = turtle.Turtle()
alice = turtle.Turtle()

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

square(bob)
square(alice)

def square(t, length):
        for i in range(4):
            t.fd(length)
            t.lt(90)

square(bob, 100)

def polygon(t, n, length):
        angle = 360 / n
        for i in range(n):
            t.fd(length)
            t.lt(angle)

bob.lt(90)
bob.fd(100)
bob.rt(90)

polygon(bob, 3, 100)

bob.rt(90)
bob.fd(100)
bob.lt(90)
bob.fd(40)
bob.lt(90)
bob.fd(50)
bob.rt(90)
bob.fd(20)
bob.rt(90)
bob.fd(50)

turtle.done()
