# Python code for catching the ball game
#ege
#omer
#deniz
# importing suitable packages
from tkinter import Tk, Button, Label
from tkinter import Canvas
from random import randint
from tkinter import PhotoImage
from tkinter import messagebox
     
# defining Tk from Tkinter
root = Tk()
root.title("Catch the ball Game")
root.resizable(False, False)

top_frame = Canvas(root, width=600, height=20)
top_frame.pack()

bottom_frame = Canvas(root, width=600, height=30)
bottom_frame.pack()

button0 = Button(top_frame, text='complete game', bg='blue', command=lambda: complete_game())
score_label = Label(top_frame, text="Score: 0")
level_label = Label(bottom_frame, text="Level : 1")

a = 30

button0.place(x=0, y=0)


score_label.place(x=300, y=0)
level_label.place(x=300, y=0)

# for defining the canvas

canvas = Canvas(root, width=600, height=600)

canvas.pack()

# variable for the vertical distance
# travelled by ball
limit = 0

# variable for horizontal distance
# of bar from x-axis
dist = 5

# variable for score
score = 0

# variable for speed
speed = 1

# variable for level
level = 1

m = messagebox.showinfo("Catch the ball game", f"Welcome to the game. Have Fun")




# Class for the Creating and moving ball
class Ball:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas

        self.ball = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="red", tags='dot1')

    def move_ball(self):
        offset = 10
        global speed
        global limit
        global level
        if limit >= 510:
            global dist, score, next
            if (dist - offset <= self.x1 and dist + 40 + offset >= self.x2):
                score += 1
                score_label.config(text="Score: {}".format(score))
                # level changes every point // to make it change every 2 points change 1 to 2
                if score % 1 == 0:
                    # increacing speed and level

                    speed += 0.5
                    level = score + 1
                    level_label.config(text="Level: {}".format(level))
                    check = messagebox.askyesno("Level Up!",
                                                f"Congratulations! You have reached level {level}! \n would you like to continue?")
                    if not check:
                        canvas.delete('dot1')
                        bar.delete_bar(self)
                        score_board()
                        return

                canvas.delete('dot1')
                ball_set()
            else:
                canvas.delete('dot1')
                bar.delete_bar(self)
                score_board()

            return
        limit += speed

        self.canvas.move(self.ball, 0, speed)
        self.canvas.after(10, self.move_ball)


# class for creating and moving bar
class bar:

    # method for creating bar
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas

        # for creating bar using create_rectangle
        self.rod = canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2,
                                           fill="yellow", tags='dot2')

    # method for moving the bar
    def move_bar(self, event):
        global dist
        self.canvas.coords(self.rod, event.x, self.y1, event.x + 40, self.y2)
        dist = event.x

        # # checking the forward or backward button
        # if (num == 1):
        #
        #     # moving the bar in forward direction by
        #     # taking x-axis positive distance and
        #     # taking vertical distance y=0
        #     self.canvas.move(self.rod, 20, 0)
        #
        #     # incrementing the distance of bar from x-axis
        #     dist += 20
        # else:
        #
        #     # moving the bar in backward direction by taking x-axis
        #     # negative distance and taking vertical distance y=0
        #     self.canvas.move(self.rod, -20, 0)
        #
        #     # decrementing the distance of bar from x-axis
        #     dist -= 20


    def delete_bar(self):
        canvas.delete('dot2')


# Function to define the dimensions of the ball
def ball_set():
    global limit
    limit = 0

    # for random x-axis distance from
    # where the ball starts to fall
    value = randint(0, 570)

    # define the dimensions of the ball
    ball1 = Ball(canvas, value, 20, value + 30, 50)

    # call function for moving of the ball
    ball1.move_ball()


# Function for displaying the score
# after getting over of the game
def score_board():
    root2 = Tk()
    root2.title("Catch the ball Game")
    root2.resizable(False, False)
    canvas2 = Canvas(root2, width=300, height=300)
    canvas2.pack()

    w = Label(canvas2, text="\nOOPS...GAME OVER\n\nYOUR SCORE = "
                            + str(score) + "\n  HIGHEST LEVEL REACHED = " + str(level))
    w.pack()

    button3 = Button(canvas2, text="PLAY AGAIN", bg="green",
                     command=lambda: play_again(root2))
    button3.pack()

    button4 = Button(canvas2, text="EXIT", bg="green",
                     command=lambda: exit_handler(root2))
    button4.pack()


# Function for handling the play again request
def play_again(root2):
    global score
    global level
    global limit
    global dist
    global speed

    score = 0
    limit = 0
    dist = 5
    speed = 1
    level = 1

    score_label.config(text="Score: {}".format(score))
    level_label.config(text="Level: {}".format(level))
    root2.destroy()
    main()


# Function for handling exit request
def exit_handler(root2):
    root2.destroy()
    root.destroy()


def complete_game():
    canvas.delete('dot1')
    canvas.delete('dot2')
    Button.destroy(button0)
    Label.destroy(score_label)
    Label.destroy(level_label)
    score_board()




# Main function
def main():


    global score, dist
    score = 0
    dist = 0


    # defining the dimensions of bar
    bar1 = bar(canvas, 5, 560, 45, 575)

    canvas.bind('<Motion>', bar1.move_bar)

    # defining the text,colour of buttons and
    # also define the action after click on
    # the button by calling suitable methods


    # calling the function for defining
    # the dimensions of ball
    ball_set()


    root.mainloop()


# Driver code
if (__name__ == "__main__"):
    main()
