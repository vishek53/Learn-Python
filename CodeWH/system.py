
import turtle
import math
import random

# ----------------------------------
# 1. Set up the screen
# ----------------------------------
screen = turtle.Screen()
screen.title("Solar System with Moon")
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.tracer(0)

# ----------------------------------
# 2. Draw background stars
# ----------------------------------
stars = turtle.Turtle()
stars.hideturtle()
stars.speed(0)
stars.penup()
stars.color("white")

for i in range(100):
    x = random.randint(-380, 380)
    y = random.randint(-380, 380)

    stars.goto(x, y)
    stars.dot(random.randint(1, 3))

# ----------------------------------
# 3. Draw the Sun
# ----------------------------------
sun = turtle.Turtle()
sun.shape("circle")
sun.color("orange", "yellow")
sun.shapesize(2.5)
sun.penup()
sun.goto(0, 0)
sun.speed(0)

# ----------------------------------
# 4. Draw planetary orbits
# ----------------------------------
orbit_drawer = turtle.Turtle()
orbit_drawer.hideturtle()
orbit_drawer.speed(0)
orbit_drawer.color("gray")
orbit_drawer.pensize(1)
orbit_drawer.penup()

# name, color, orbit radius, speed, size
planet_data = [
    ("Mercury", "gray", 55, 4.0, 0.25),
    ("Venus", "orange", 85, 3.0, 0.40),
    ("Earth", "deepskyblue", 120, 2.4, 0.45),
    ("Mars", "red", 155, 1.9, 0.35),
    ("Jupiter", "orange", 205, 1.2, 1.00),
    ("Saturn", "khaki", 250, 0.9, 0.85),
    ("Uranus", "cyan", 290, 0.65, 0.65),
    ("Neptune", "blue", 325, 0.5, 0.65)
]

# Draw the eight circular orbits
for name, color, radius, speed, size in planet_data:
    orbit_drawer.penup()
    orbit_drawer.goto(0, -radius)
    orbit_drawer.setheading(0)
    orbit_drawer.pendown()
    orbit_drawer.circle(radius)

orbit_drawer.penup()

# ----------------------------------
# 5. Create the planets
# ----------------------------------
planets = []

for name, color, radius, speed, size in planet_data:

    # Create the planet
    planet = turtle.Turtle()
    planet.shape("circle")
    planet.color(color)
    planet.shapesize(size)
    planet.penup()
    planet.speed(0)

    # Create its text label
    label = turtle.Turtle()
    label.hideturtle()
    label.penup()
    label.color("white")

    # Store the planet's information
    item = {
        "name": name,
        "radius": radius,
        "speed": speed,
        "angle": random.randint(0, 359),
        "planet": planet,
        "label": label
    }

    planets.append(item)

# ----------------------------------
# 6. Create the Moon
# ----------------------------------
moon = turtle.Turtle()
moon.shape("circle")
moon.color("lightgray")
moon.shapesize(0.20)
moon.penup()
moon.speed(0)

moon_label = turtle.Turtle()
moon_label.hideturtle()
moon_label.penup()
moon_label.color("white")

# Moon's orbital settings
moon_radius = 18
moon_speed = 8
moon_angle = 0

# Draw the Moon's orbit around Earth
moon_orbit = turtle.Turtle()
moon_orbit.hideturtle()
moon_orbit.speed(0)
moon_orbit.color("dimgray")
moon_orbit.pensize(1)
moon_orbit.penup()

# ----------------------------------
# 7. Animate the solar system
# ----------------------------------
def animate():
    global moon_angle

    earth_x = 0
    earth_y = 0

    # Move all planets around the Sun
    for item in planets:

        radius = item["radius"]
        angle = item["angle"]
        speed = item["speed"]

        # Convert degrees into radians
        radians = math.radians(angle)

        # Calculate coordinates relative to the Sun
        x = radius * math.cos(radians)
        y = radius * math.sin(radians)

        # Move the planet
        item["planet"].goto(x, y)

        # Update the planet label
        item["label"].clear()
        item["label"].goto(x, y + 12)
        item["label"].write(
            item["name"],
            align="center",
            font=("Arial", 8, "normal")
        )

        # Remember Earth's position
        if item["name"] == "Earth":
            earth_x = x
            earth_y = y

        # Advance the planet's angle
        item["angle"] = (angle + speed) % 360

    # ----------------------------------
    # 8. Move the Moon around Earth
    # ----------------------------------

    # Calculate the Moon's position relative to Earth
    moon_radians = math.radians(moon_angle)

    moon_x = earth_x + moon_radius * math.cos(moon_radians)
    moon_y = earth_y + moon_radius * math.sin(moon_radians)

    # Move the Moon to its new position
    moon.goto(moon_x, moon_y)

    # Update the Moon's label
    moon_label.clear()
    moon_label.goto(moon_x, moon_y + 8)
    moon_label.write(
        "Moon",
        align="center",
        font=("Arial", 7, "normal")
    )

    # Draw the Moon's orbit around Earth's current position
    moon_orbit.clear()
    moon_orbit.penup()
    moon_orbit.goto(earth_x, earth_y - moon_radius)
    moon_orbit.setheading(0)
    moon_orbit.pendown()
    moon_orbit.circle(moon_radius)
    moon_orbit.penup()

    # Advance the Moon's angle
    moon_angle = (moon_angle + moon_speed) % 360

    # Update everything together
    screen.update()

    # Repeat after 30 milliseconds
    screen.ontimer(animate, 30)


# ----------------------------------
# 9. Start the animation
# ----------------------------------
animate()

turtle.done()
