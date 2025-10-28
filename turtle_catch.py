import turtle, random, time

drawing_screen = turtle.Screen()
drawing_screen.bgcolor("light blue")
drawing_screen.title("Catch the Turtle")

t = turtle.Turtle()
t.hideturtle()
t.penup()

t2 = turtle.Turtle() # skor yazısı için ayrı turtle
t2.hideturtle()
t2.penup()

ttime = turtle.Turtle()
ttime.hideturtle()
ttime.penup()

x_c = 0
y_c = 0

def random_coordinate():
    global x_c, y_c, ready
    x_c = random.randint(-400, 400)
    y_c = random.randint(-200, 300)
    ready = True
    return x_c, y_c

score = 0  # Baslangic skoru
running = True
ready = False  # Koordinatlar
seconds = int(30)
remain = seconds

t.shape("turtle")
t.color("green")

t2.goto(-380, 380)
t2.write("Skor: "+ str(score), font=("Arial", 20, "bold"), align="left")

ttime.goto(-250, 380)
ttime.write("Time: " + str(remain), font=("Arial", 20, "bold"), align="left")

def time_countdown():
    global seconds, running

    if seconds > 0:
        seconds -= 1
        ttime.clear()
        ttime.write("Time: " + str(seconds), font=("Arial", 20, "bold"), align="left")
        drawing_screen.ontimer(time_countdown, 1000)
    else:
        running = False

def click_turtle(x, y):
    global running, ready, score

    if not running:
        return
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
time_countdown()

while seconds > 0:
    if not running:
        break
    t.clear()
    t.hideturtle()
    rnd_x, rnd_y = random_coordinate()
    t.goto(rnd_x, rnd_y)
    t.showturtle()
    time.sleep(0.55)

turtle.done()
