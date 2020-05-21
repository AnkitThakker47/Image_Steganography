import os
import requests
import socket
import random
from tkinter import *
from tkinter.messagebox import *


try:
	socket.create_connection(("www.google.com",80))
	#showinfo("Connected","u r connected")


	def saveImage(image,dir):
		with open(dir+ '/' + str(image['id'])+".jpg", "wb") as f:
			r1 = requests.get(image["largeImageURL"])
			f.write(r1.content)		

	def storeImages(imagelist):
		mode = 0o666
		dir = "D:/" + str(getwords.get())
		while os.path.exists(dir):
#please use your own default directory name like data:/ or e:/
			dir = "D:/" + str(getwords.get()) + str(random.randrange(0,1000))
		else:
			os.mkdir(dir)
		#print(imagelist)
		for i in imagelist:
			val = i['largeImageURL'].rfind('.')
			extension = i['largeImageURL'][val+1:]
			if extension.lower() == 'jpg' or extension.lower() == 'png':
				saveImage(i,dir)
			else:
				pass
		return dir
			
	def getImages():
		a1 = "https://pixabay.com/api/?key=16344627-110e29474f27c28a4a9923a6a&q="
		words = getwords.get()
		a2 = '+'.join(words.split(' '))
		#print(a2)
		a3 = "&safesearch=true&order=popular"
		res = requests.get(a1+a2+a3)
		#print(res)
		data = res.json()
		#print(data)
		val = storeImages(data['hits'])
		showinfo("Success",val + " directory created")
		getwords.delete(0, END)

except Exception as e:
	showerror("issue", e)


if __name__ == '__main__':
	root = Tk()
	root.title("Scraping images from pixabay")
	root.geometry("600x450+400+200")
	root.configure(background='#FF9196')
	root.resizable(False, False)



	lblwords = Label(root, text = "Enter the words for images to be searched", font = ('Arial', 18, 'bold'), bg = '#FF9196')
	lblinfo = Label(root, text = "(please enter keywords separated by space)", font = ('Arial', 18, 'bold'), bg = '#FF9196')
	getwords = Entry(root, width = 35,bd = 5, font = ('Arial', 18, 'bold'))
	btn = Button(root, text = "Search", font = ('Arial', 18, 'bold'), command = getImages)



	lblwords.pack(pady = 20)
	lblinfo.pack()
	getwords.pack(pady = 20)
	btn.pack(pady = 20)
	getwords.focus()



	root.mainloop()