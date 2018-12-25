import cv2
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from keras.models import load_model
from my_preprocessing import parse_line
from PIL import ImageTk, ImageDraw
import PIL
import PIL.Image
from tkinter import *
import os

width = 300
height = 300
center = height//2
white = (255, 255, 255)
green = (0,128,0)
cnn_model = load_model('./Models/Quick_Draw_CNN.h5')

def save():
	global image1
	filename = "image.png"
	image1.save(filename)
	img1 = cv2.imread(filename)
	img1 = np.array(img1)
	img1 = np.invert(img1)
	# print(img1.shape)
	img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
	img1 = cv2.resize(img1,(28,28))
	cv2.imshow("image",img1)
	img1 = img1.reshape((1,28,28,1))
	img1 = img1/255.0
	result = cnn_model.predict(img1)
	ans = np.argmax( result[0] )
	print(ans)

def paint(event):
    # python_green = "#476042"
	x1, y1 = (event.x - 1), (event.y - 1)
	x2, y2 = (event.x + 1), (event.y + 1)
	cv.create_oval(x1, y1, x2, y2, fill="black",width=10)
	draw.line([x1, y1, x2, y2],fill="black",width=10)

def clear():
	global cv,image1,draw
	cv.delete("all")
	image1 = PIL.Image.new("RGB", (width, height), white)
	draw = ImageDraw.Draw(image1)
	
	

root = Tk()

# Tkinter create a canvas to draw on
cv = Canvas(root, width=width, height=height, bg='white')
cv.pack()

# PIL create an empty image and draw object to draw on
# memory only, not visible
image1 = PIL.Image.new("RGB", (width, height), white)
draw = ImageDraw.Draw(image1)

# do the Tkinter canvas drawings (visible)
# cv.create_line([0, center, width, center], fill='green')

cv.pack(expand=YES, fill=BOTH)
cv.bind("<B1-Motion>", paint)

# do the PIL image/draw (in memory) drawings
# draw.line([0, center, width, center], green)

# PIL image can be saved as .png .jpg .gif or .bmp file (among others)
# filename = "my_drawing.png"
# image1.save(filename)
button=Button(text="save",command=save)
button.pack()
button1=Button(text="clear",command=clear)
button1.pack()
root.mainloop()
