########################################################
#                                                      #
#                S N A K E    G A M E                  #
#                                                      #
########################################################

from tkinter import *
import random
import constants

class Snake:
    def __init__(self):
        self.body_size = constants.settings['BODY_PARTS']
        self.coordinates = []
        self.squares = []
        for i in range(0, constants.settings['BODY_PARTS']):
            self.coordinates.append([0, 0])
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + constants.gWindow['SPACE_SIZE'], y + constants.gWindow['SPACE_SIZE'], fill=constants.settings['SNAKE_COLOUR'], tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, int(constants.gWindow['GAME_WIDTH'] / constants.gWindow['SPACE_SIZE'])-1) * constants.gWindow['SPACE_SIZE']
        y = random.randint(0, int(constants.gWindow['GAME_HEIGHT'] / constants.gWindow['SPACE_SIZE']) - 1) * constants.gWindow['SPACE_SIZE']
        self.coordinates = [x, y]
        canvas.create_rectangle(x, y, x + constants.gWindow['SPACE_SIZE'], y + constants.gWindow['SPACE_SIZE'], fill=constants.settings['FOOD_COLOUR'], tag="food")

# Exit game
def closeWindow():
    root.destroy()

# Restart game
def restart():
    global snake, food, score, direction
    canvas.delete(ALL)
    snake = Snake()
    food = Food()
    score = 0
    constants.settings['START_SPEED'] = 200
    direction = constants.settings['START_DIRECTION']
    label.config(text="Score:{}".format(score))
    nextTurn(snake, food)

def nextTurn(snake, food):
    x, y = snake.coordinates[0]
    if direction == "up":
        y -= constants.gWindow['SPACE_SIZE']
    elif direction == "down":
        y += constants.gWindow['SPACE_SIZE']
    elif direction == "left":
        x -= constants.gWindow['SPACE_SIZE']
    elif direction == "right":
        x += constants.gWindow['SPACE_SIZE']
    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + constants.gWindow['SPACE_SIZE'], y + constants.gWindow['SPACE_SIZE'], fill=constants.settings['SNAKE_COLOUR'])
    snake.squares.insert(0, square)
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        # increase speed with each food
        if(constants.settings['START_SPEED'] >= 5):
            constants.settings['START_SPEED'] -= 5
        label.config(text="Score: {}".format(score))
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    if collisions(snake):
        gameOver()
    else:
        root.after(constants.settings['START_SPEED'], nextTurn, snake, food)

def changeDirection(new_direction):
    global direction
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction


def collisions(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= constants.gWindow['GAME_WIDTH']:
        return True
    elif y < 0 or y >= constants.gWindow['GAME_HEIGHT']:
        return True
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False

def gameOver():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, (canvas.winfo_height()/2)-200, font=('consolas',80), text="GAME OVER", fill="red", tag="gameover")
    button1 = Button(root, text = "Quit" , anchor = W, command=closeWindow)
    button1.configure(width = 10, height=2, bg='red', relief = FLAT)
    button2 = Button(root, text = "Restart" , anchor = W, command=restart)
    button2.configure(width = 10, height=2, bg='green', relief = FLAT)
    canvas.create_window(canvas.winfo_width()/2+50, canvas.winfo_height()/2, anchor=NW, window=button1)
    canvas.create_window(canvas.winfo_width()/2-200, canvas.winfo_height()/2, anchor=NW, window=button2)

### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### 

root = Tk()
root.title(constants.gWindow['TITLE'])
root.resizable(False, False)

score = 0
direction = constants.settings['START_DIRECTION']

label = Label(root, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(root, bg=constants.settings['BACKGROUND_COLOUR'], height=constants.gWindow['GAME_HEIGHT'], width=constants.gWindow['GAME_WIDTH'])
canvas.pack()

root.update()

window_width = root.winfo_width()
window_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

root.bind('<Left>', lambda event: changeDirection('left'))
root.bind('<Right>', lambda event: changeDirection('right'))
root.bind('<Up>', lambda event: changeDirection('up'))
root.bind('<Down>', lambda event: changeDirection('down'))

snake = Snake()
food = Food()

nextTurn(snake, food)

root.mainloop()