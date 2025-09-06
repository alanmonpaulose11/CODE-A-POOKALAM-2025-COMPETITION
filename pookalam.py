import turtle

# --- Main Configuration ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
BACKGROUND_COLOR = "#1A472A"  # A dark green, like a banana leaf
TITLE = "Traditional Onam Pookalam"

# --- Drawing Functions ---

def setup_screen():
    """Sets up the turtle screen for drawing."""
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.bgcolor(BACKGROUND_COLOR)
    screen.title(TITLE)
    screen.tracer(0)  # Turn off animation for instant drawing
    return screen

def draw_filled_circle(t, radius, color):
    """A helper function to draw a filled circle from the center."""
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_pookalam_layers(t):
    """Draws the concentric circles of the Pookalam with real flower colors."""
    t.width(2)
    # Each tuple contains (radius, color, flower_name)
    flower_layers = [
        (350, "#006400", "A border of green leaves"),
        (330, "#FFD700", "Gold for Marigold (Jamanthi)"),
        (290, "#FFFFFF", "White for Jasmine (Mulla) or Thumbapoo"),
        (250, "#FF8C00", "Dark Orange for Chembarathi"),
        (210, "#DC143C", "Crimson for Globe Amaranth (Vadamalli)"),
        (170, "#FFFFE0", "Light Yellow for another layer of Jamanthi"),
        (130, "#9932CC", "Purple for Butterfly Pea (Shankupushpam)"),
        (90, "#B22222",  "Firebrick Red for the center"),
    ]

    for radius, color, comment in flower_layers:
        print(f"Drawing layer: {comment}") # Prints the flower being drawn
        draw_filled_circle(t, radius, color)

def draw_central_design(t):
    """Draws a simple star-like design in the center."""
    t.penup()
    t.goto(0, 0)
    t.width(5)
    t.color("white")
    
    num_points = 8
    for _ in range(num_points):
        t.pendown()
        t.forward(120)
        t.penup()
        t.backward(120)
        t.left(360 / num_points)

def write_greeting(t):
    """Writes 'Happy Onam' at the bottom."""
    t.penup()
    t.goto(0, -380)
    t.color("white")
    t.write("Happy Onam!", align="center", font=("Georgia", 30, "bold"))

# --- Main Execution ---

def main():
    """The main function to orchestrate the drawing."""
    screen = setup_screen()
    pookalam_turtle = turtle.Turtle()
    pookalam_turtle.speed(0)
    pookalam_turtle.hideturtle()

    # Draw all the components
    draw_pookalam_layers(pookalam_turtle)
    draw_central_design(pookalam_turtle)
    write_greeting(pookalam_turtle)
    
    # Show the final drawing
    screen.update() 
    
    # Keep the window open until clicked
    screen.exitonclick()

if __name__ == "__main__":
    main()
