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

	def storeImages(imagelist, folder):
		mode = 0o666
		for i in imagelist:
			val = i['largeImageURL'].rfind('.')
			extension = i['largeImageURL'][val+1:]
			if extension.lower() == 'jpg' or extension.lower() == 'png':
				saveImage(i,folder)
			else:
				pass

	def getImages(words,num,folder=os.getcwd()):
		a1 = "https://pixabay.com/api/?key=16344627-110e29474f27c28a4a9923a6a&q="
		a2 = '+'.join(words.split(' '))
		a3 = "&safesearch=true&order=popular&per_page="+str(num)
		res = requests.get(a1+a2+a3)
		data = res.json()
		storeImages(data['hits'],folder)
		showinfo("Success","Images stored in "+str(folder))

except Exception as e:
	showerror("Issue", e)