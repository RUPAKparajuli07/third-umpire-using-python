import tkinter 
import cv2 
import PIL.Image, PIL.ImageTk 
from functools import partial
import threading
import time
import imutils 

stream = cv2.VideoCapture("clip.mp4")
flag = True

def play(speed):
    global flag
    print(f"You clicked on play. Speed is {speed}")

    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame).resize((SET_WIDTH, SET_HEIGHT)))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(134, 26, fill="white", font="Times 26 bold", text="Decision Pending")
    flag = not flag

def pending(decision):
    frame = cv2.cvtColor(cv2.imread("pending.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame).resize((SET_WIDTH, SET_HEIGHT)))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    time.sleep(1.5)

    frame = cv2.cvtColor(cv2.imread("sponsors.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame).resize((SET_WIDTH, SET_HEIGHT)))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    time.sleep(2.5)

    if decision == 'out':
        decisionImg = "out.png"
    else:
        decisionImg = "not out.png"
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame).resize((SET_WIDTH, SET_HEIGHT)))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")

def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")

SET_WIDTH = 700
SET_HEIGHT = 800

window = tkinter.Tk()
window.title("Let's find fault of game")


window.state('zoomed')

cv_img = cv2.cvtColor(cv2.imread("welcome.jpg"), cv2.COLOR_BGR2RGB)

canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT, bg='black')
canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)

photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img).resize((SET_WIDTH, SET_HEIGHT)))
image_on_canvas = canvas.create_image(0, 0, anchor=tkinter.NW, image=photo)

button_frame = tkinter.Frame(window, bg='black')
button_frame.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True)

button_frame.pack_propagate(0)

button_font = ('Times New Roman', 30)

btn = tkinter.Button(button_frame, text="<< Previous (fast)", width=20, font=button_font, fg='red', bg='black', command=partial(play, -25))
btn.pack(pady=10)

btn = tkinter.Button(button_frame, text="<< Previous (slow)", width=20, font=button_font, fg='red', bg='black', command=partial(play, -2))
btn.pack(pady=10)

btn = tkinter.Button(button_frame, text="Next (slow) >>", width=20, font=button_font, fg='red', bg='black', command=partial(play, 2))
btn.pack(pady=10)

btn = tkinter.Button(button_frame, text="Next (fast) >>", width=20, font=button_font, fg='red', bg='black', command=partial(play, 25))
btn.pack(pady=10)

btn = tkinter.Button(button_frame, text="Give Out", width=20, font=button_font, fg='red', bg='black', command=out)
btn.pack(pady=10)

btn = tkinter.Button(button_frame, text="Give Not Out", width=20, font=button_font, fg='red', bg='black', command=not_out)
btn.pack(pady=10)

window.mainloop()
