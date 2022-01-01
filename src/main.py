from tkinter import *
from imagescrapper import search_and_download
from PIL import ImageTk, Image
import os

class Student:
	def __init__(self):
		self.win = Tk()
		self.canvas = Canvas(self.win, width=800, height=600, bg='#344feb')
		self.canvas.pack(expand=YES, fill=BOTH)
		width = self.win.winfo_screenwidth()
		height = self.win.winfo_screenheight()
		x = int(width/2 - 800/2)
		y = int(height/2 - 700/2)
		self.win.geometry("800x600+" + str(x) + "+" + str(y))
		self.win.resizable(width = False, height = False)
		self.win.title("Students")

	def add_frame(self):
		self.frame = Frame(self.win, height=580, width=760, bg = "#e8faff")
		self.frame.place(x = 20, y = 10)
		#search frame
		self.label1 = Label(self.frame, text = "Image Searcher", font = ("times new roman", 30, "bold"), fg = '#344feb', bg = '#e8faff').place(x = 30, y = 30)
		self.label2 = Label(self.frame, text = "search:", font = ("times new roman", 15, "bold"), fg = 'black', bg = '#e8faff').place(x = 30, y = 340)
		self.img = Image.open('images/Googleimg.png').resize((400, 140), Image.ANTIALIAS)
		self.ph = ImageTk.PhotoImage(self.img)
		self.label3 = Label(self.frame, image = self.ph)
		self.label3.place(x = 180, y = 130)
		self.label3.config(bg = "#e8faff")
		self.label4 = Label(self.frame, text = "How many images?", font = ("times new roman", 15, "bold"), fg = 'black', bg = '#e8faff').place(x = 30, y = 370)
		self.entry1 = Entry(self.frame, font = ("times new roman", 15, "bold"), fg = 'black', bg = 'white', relief = 'flat')
		self.entry1.place(x = 510, y = 340)
		self.entry2 = Entry(self.frame, font = ("times new roman", 15, "bold"), fg = 'black', bg = 'white', relief = 'flat')
		self.entry2.place(x = 510, y = 370)
		self.button1 = Button(self.frame, text = "Download", font = ("times new roman", 20, "bold"), fg = "white", relief = "flat", bg = "#344feb", command = self.scrap).place(x = 30, y = 480)
		self.win.mainloop()

	def scrap(self):
		x = self.entry2.get()
		x = int(x)
		y = self.entry1.get()
		DRIVER_PATH = 'Path to your chrome driver'
		search_and_download(search_term = y, driver_path = DRIVER_PATH, number_images = x)

x = Student()
x.add_frame()
