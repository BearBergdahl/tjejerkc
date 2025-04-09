import turtle

# Game configuration settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PADDLE_WIDTH = 1
PADDLE_HEIGHT = 5
PADDLE_SPEED = 30
BALL_SPEED_X = 0.15
BALL_SPEED_Y = 0.15
WINNING_SCORE = 5
BALL_SPEEDUP = 1.05  # Ball gets faster after each hit

# Colors
BG_COLOR = "green"
PADDLE_A_COLOR = "red"
PADDLE_B_COLOR = "blue"
BALL_COLOR = "black"
TEXT_COLOR = "black"

# Fonts
GAME_OVER_FONT = ("Courier", 32, "bold")
GAME_OVER_COLOR = "red"

# Initialize global variables
paused = False
ball_x = BALL_SPEED_X
ball_y = BALL_SPEED_Y
score_a = 0
score_b = 0

# Window setup
wind = turtle.Screen()
wind.title("Pong")
wind.bgcolor(BG_COLOR)
wind.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
wind.tracer(0)

# Paddle A
bar_A = turtle.Turtle()
bar_A.shape("square")
bar_A.color(PADDLE_A_COLOR)
bar_A.penup()
bar_A.shapesize(stretch_wid=5, stretch_len=1)
bar_A.goto(-350, 0)

# Paddle B
bar_B = turtle.Turtle()
bar_B.shape("square")
bar_B.color(PADDLE_B_COLOR)
bar_B.penup()
bar_B.shapesize(stretch_wid=5, stretch_len=1)
bar_B.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color(BALL_COLOR)
ball.penup()
ball.goto(0, 0)

# Scoreboard
sboard = turtle.Turtle()
sboard.shape("square")
sboard.color(TEXT_COLOR)
sboard.penup()
sboard.hideturtle()
sboard.goto(0, 260)
sboard.write("Player A: 0 Player B: 0 \n first to get 5 wins", align="center", font=("Courier", 24, "normal"))

# Functions to move paddles
def bar_a_up():
    if bar_A.ycor() < 230:
        bar_A.sety(bar_A.ycor() + PADDLE_SPEED)

def bar_a_down():
    if bar_A.ycor() > -230:
        bar_A.sety(bar_A.ycor() - PADDLE_SPEED)



# Function to toggle pause
def toggle_pause():
    global paused
    paused = not paused

# Keyboard bindings
wind.listen()
wind.onkeypress(bar_a_up, "a")
wind.onkeypress(bar_a_down, "z")

wind.onkeypress(toggle_pause, "space")
wind.onkeypress(wind.bye, "Escape")  

# Function to run the game loop
def game_loop():
    global ball_x, ball_y, score_a, score_b
    while True:
        wind.update()
        if paused:
            continue

        # Ball movement
        ball.setx(ball.xcor() + ball_x)
        ball.sety(ball.ycor() + ball_y)

        # Border collision
        if ball.ycor() > 290:
            ball.sety(290)
            ball_y *= -1
        elif ball.ycor() < -290:
            ball.sety(-290)
            ball_y *= -1

        # Scoring
        if ball.xcor() > 390:
            score_a += 1
            sboard.clear()
            sboard.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball_x *= -1
        elif ball.xcor() < -390:
            score_b += 1
            sboard.clear()
            sboard.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball_x *= -1

        # Paddle collision
        if ball.xcor() < -340 and bar_A.ycor() - 50 < ball.ycor() < bar_A.ycor() + 50:
            ball_x *= -1
        elif ball.xcor() > 340 and bar_B.ycor() - 50 < ball.ycor() < bar_B.ycor() + 50:
            ball_x *= -1

        # Check for winning condition
        if score_a == WINNING_SCORE or score_b == WINNING_SCORE:
            break

    # Display "Game over!" message
    game_over_board = turtle.Turtle()
    game_over_board.hideturtle()
    game_over_board.color(GAME_OVER_COLOR)
    game_over_board.penup()
    game_over_board.goto(0, -60)
    game_over_board.write("Game over!", align="center", font=GAME_OVER_FONT)

    # Add instructions for the user
    game_over_board.goto(0, -100)
    game_over_board.write("Press 'Escape' to exit", align="center", font=("Courier", 16, "normal"))

# Start the game loop
game_loop()
