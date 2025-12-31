import turtle
import random
import time

# --- Configuration ---
turtle.setup(800, 600)
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Happy New Year!")

# --- Functions for Graphics ---
def firework():
    """Draws a simple starburst 'firework' at a random location."""
    fw = turtle.Turtle()
    fw.hideturtle()
    fw.speed(0)
    fw.penup()
    fw.goto(random.randint(-300, 300), random.randint(-200, 200))
    fw.pendown()
    colors = ["red", "yellow", "blue", "green", "purple", "orange", "white"]
    fw.color(random.choice(colors))
    for _ in range(36):
        fw.forward(random.randint(50, 100))
        fw.backward(random.randint(50, 100))
        fw.right(10)

def show_message():
    """Displays the New Year message in the center of the screen."""
    msg = turtle.Turtle()
    msg.hideturtle()
    msg.color("gold")
    msg.penup()
    msg.goto(0, -250) # Position lower on the screen
    # Use write to display text with specified font
    msg.write("🎉 2026-Where effort meets achievement! 🎉", align="center", font=("Arial", 30, "bold"))
    
# --- Main Logic ---
show_message()
# Create some fireworks for effect
for _ in range(8):
    firework()
    time.sleep(0.1)

# Keep the window open
turtle.done()
