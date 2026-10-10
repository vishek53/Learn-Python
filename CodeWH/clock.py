
import turtle
import time
import math

# ------------------------------
# 1. Set up the screen
# ------------------------------
screen = turtle.Screen()
screen.title("Analog Clock")
screen.bgcolor("black")
screen.setup(width=700, height=700)
screen.tracer(0)

# ------------------------------
# 2. Create drawing turtle
# ------------------------------
clock = turtle.Turtle()
clock.hideturtle()
clock.speed(0)
clock.pensize(2)

# ------------------------------
# 3. Draw the clock face
# ------------------------------
def draw_clock_face():
    clock.clear()
    clock.penup()
    clock.goto(0, -250)
    clock.setheading(0)
    clock.pendown()
    clock.color("white")
    clock.circle(250)

    # Draw 60 tick marks
    for i in range(60):
        clock.penup()
        clock.goto(0, 0)
        clock.setheading(90 - i * 6)
        clock.forward(230)

        if i % 5 == 0:
            clock.pensize(4)
            clock.forward(20)
        else:
            clock.pensize(1)
            clock.forward(8)

        clock.pendown()
        clock.forward(0)

    clock.penup()

    # Draw numbers 1 to 12
    for number in range(1, 13):
        angle = math.radians(90 - number * 30)
        x = 195 * math.cos(angle)
        y = 195 * math.sin(angle)

        clock.goto(x, y - 10)
        clock.color("white")
        clock.write(
            str(number),
            align="center",
            font=("Arial", 16, "normal")
        )

# ------------------------------
# 4. Create clock hands
# ------------------------------
def draw_hand(angle, length, color, width):
    hand = turtle.Turtle()
    hand.hideturtle()
    hand.speed(0)
    hand.color(color)
    hand.pensize(width)
    hand.penup()
    hand.goto(0, 0)
    hand.setheading(angle)
    hand.pendown()
    hand.forward(length)
    hand.hideturtle()
    return hand

# ------------------------------
# 5. Update the clock
# ------------------------------
def update_clock():
    # Get the current local time
    current_time = time.localtime()

    seconds = current_time.tm_sec
    minutes = current_time.tm_min
    hours = current_time.tm_hour % 12

    # Calculate hand angles
    second_angle = 90 - seconds * 6
    minute_angle = 90 - (minutes * 6 + seconds * 0.1)
    hour_angle = 90 - (hours * 30 + minutes * 0.5)

    # Remove the previous hands
    screen.tracer(0)
    for hand in hands:
        hand.clear()
        hand.hideturtle()

    # Draw new hands
    hands[0] = draw_hand(second_angle, 215, "red", 2)
    hands[1] = draw_hand(minute_angle, 175, "lime", 4)
    hands[2] = draw_hand(hour_angle, 125, "blue", 6)

    # Draw the center point
    clock.penup()
    clock.goto(0, -5)
    clock.dot(12, "white")
    clock.goto(0, 0)
    clock.dot(6, "blue")

    screen.update()

    # Run again after one second
    screen.ontimer(update_clock, 1000)

# ------------------------------
# 6. Start the clock
# ------------------------------
draw_clock_face()

hands = [
    turtle.Turtle(),
    turtle.Turtle(),
    turtle.Turtle()
]

for hand in hands:
    hand.hideturtle()

update_clock()

turtle.done()
