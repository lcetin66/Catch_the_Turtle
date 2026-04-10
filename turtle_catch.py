import turtle, random, time

drawing_screen = turtle.Screen()
drawing_screen.bgcolor("light blue")
drawing_screen.title("Catch the Turtle")

t = turtle.Turtle()
t.hideturtle()
t.penup()

t2 = turtle.Turtle()  # score 
t2.hideturtle()
t2.penup()

ttime = turtle.Turtle()  # time
ttime.hideturtle()
ttime.penup()

x_c = 0
y_c = 0
score = 0
running = True
ready = False
seconds = 30

def update_positions():
    screen_h = drawing_screen.window_height() / 2
    screen_w = drawing_screen.window_width() / 2

    # Score: top left
    t2.goto(-screen_w + 40, screen_h - 40)
    # Time: top right
    ttime.goto(screen_w - 160, screen_h - 40)


def random_coordinate():  # random position
    global x_c, y_c, ready
    screen_h = drawing_screen.window_height() / 2 * 0.9
    screen_w = drawing_screen.window_width() / 2 * 0.9
    x_c = random.randint(-int(screen_w), int(screen_w))
    y_c = random.randint(-int(screen_h), int(screen_h))
    ready = True
    return x_c, y_c


def player_score():  # update score
    t2.clear()
    update_positions()
    t2.write(f"Skor: {score}", font=("Arial", 20, "bold"), align="left")


def time_countdown():  # coundown function
    global seconds, running
    update_positions()
    if seconds > 0:
        seconds -= 1
        ttime.clear()
        ttime.write(f"Time: {seconds}", font=("Arial", 20, "bold"), align="left")
        drawing_screen.ontimer(time_countdown, 1000)
    else:
        running = False


def click_turtle(x, y):  # click control
    global running, ready, score
    if not running or not ready:
        return
    if abs(x_c - x) < 20 and abs(y_c - y) < 20:
        old_color = t.pencolor()
        t.color("red")
        t.write("Vurdun!", align="center", font=("Arial", 16, "bold"))
        t.color(old_color)
        score += 1
        player_score()
    else:
        t.write("Iskaladın!", align="center", font=("Arial", 16, "bold"))


drawing_screen.onclick(click_turtle)
update_positions()
player_score()
time_countdown()

t.shape("turtle")
t.color("green")

turtle_show_again = 0.55  #visibility interval (seconds)
while seconds > 0:
    if not running:
        break
    t.clear()
    t.hideturtle()
    rnd_x, rnd_y = random_coordinate()
    t.goto(rnd_x, rnd_y)
    t.showturtle()
    time.sleep(turtle_show_again)

turtle.done()
