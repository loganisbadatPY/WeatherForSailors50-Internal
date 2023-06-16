from tkinter import *
from tkinter import ttk

import tkinter
from functools import partial

from PIL import Image, ImageTk, ImageFont

def validateLogin(username):
	print("username entered :", username.get())
	return

#window
tkWindow = Tk()
tkWindow.minsize(700, 700)
tkWindow.maxsize(700,700)
tkWindow.title('Weather For Sailors')
tkWindow.resizable(width = False, height = False)

#Background Image, using pillow, much easier to use. use place instead of grid, has much more flexibility
ocean_image = Image.open(r"/Users/logan/Documents/Weather For Sailing/assets/photoImageLogInPage.png")
ocean_image = ocean_image.resize((700, 700))
ocean_image_tk = ImageTk.PhotoImage(ocean_image)

ocean_image_label = Label(tkWindow, image=ocean_image_tk)
ocean_image_label.place(x=-2, y=0)

#Logo image, agian using pillow
boat_logo = Image.open(r"/Users/logan/Documents/Weather For Sailing/assets/Sailing App logo.png")
boat_logo = boat_logo.resize((256, 256))
boat_logo_tk = ImageTk.PhotoImage(boat_logo)

boat_logo_label = Label(tkWindow, image= boat_logo_tk)
boat_logo_label.place(x=235, y=3)
#username label and text entry box
usernameLabel = Label(tkWindow, text="Username:").place(x=10, y=200)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).place(x=10, y=200)

validateLogin = partial(validateLogin, username)
#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).place(x=10, y=200)

#Putting the ocean_image_label below everything listed, lower means putting it behind it
ocean_image_label.lower(loginButton)
ocean_image_label.lower(usernameLabel)
ocean_image_label.lower(usernameEntry)

tkWindow.mainloop()