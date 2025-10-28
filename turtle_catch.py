import turtle
import random
import time

drawing_screen = turtle.Screen()
drawing_screen.bgcolor("light blue")
drawing_screen.title("Catch the Turtle")

score = 0  # Baslangic skoru

t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.penup()

t2 = turtle.Turtle()   # skor yazısı için ayrı turtle
t2.hideturtle()
t2.penup()
t2.goto(-380, 380)
t2.write("Skor: "+ str(score), font=("Arial", 20, "bold"), align="left")

running = True
x_c = 0
y_c = 0
ready = False  # koordinatlar hazır mı

def random_coordinate():
    global x_c, y_c, ready
    x_c = random.randint(-400, 400)
    y_c = random.randint(-200, 300)
    ready = True
    return x_c, y_c

def click_turtle(x, y):
    global running, ready, score
    if not ready:
        return
    try:
        if abs(x_c - x) < 20 and abs(y_c - y) < 20:
            old_color = t.pencolor()
            t.color("red")
            t.write("Vurdun!", align="center", font=("Arial", 16, "bold"))
            t.color(old_color)
            score += 1
            t2.clear()
            t2.write(f"Skor: {score}", font=("Arial", 20, "bold"))
        else:
            t.write("Iskaladın!", align="center", font=("Arial", 16, "bold"))
    except TypeError:
        pass

drawing_screen.onclick(click_turtle)

for i in range(20):
    if not running:
        break
    t.clear()
    t.hideturtle()
    rnd_x, rnd_y = random_coordinate()
    t.goto(rnd_x, rnd_y)
    t.showturtle()
    time.sleep(3)

turtle.done()
