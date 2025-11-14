import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

img = Image.open("imagen_transparente.png")
photo = ImageTk.PhotoImage(img)

label = tk.Label(root, image=photo, bg="gray")
label.pack()

root.mainloop()
