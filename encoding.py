from tkinter import *
from tkinter import messagebox
from PIL import Image
import os

def binary_to_decimal(k):
	temp = []
	for n in k:
		val = int(n)
		fin,inc = 0,0
		while val != 0:
			di = val % 10
			fin = fin + di * 2 ** inc
			val = val//10
			inc += 1
		temp.append(fin)
	return temp


def encode_into_pixels(i, word, pixels):
	inival, ind = i*3, 0
	for k in range(inival, inival + 3):
		for j in range(0, 3):
			if j == 2 and k == inival + 2:
				continue
			pixels[k][j] = pixels[k][j][0:7] + word[ind]
			ind += 1

def encode(statement, image_path):
	statement = "<RNA? "+statement+" ?RNA>"
	flag, new_file_path = False, ''
	imp = image_path.rfind('.')
	extension = image_path[imp + 1:]
	if extension.lower() != 'jpg' and extension.lower() != 'png':
		messagebox.showerror("ERROR","Invalid file type")
		#exit()	
	elif not os.path.exists(image_path):
		messagebox.showerror("ERROR","File does not exists")
		#exit()
	else:
		new_file_path = image_path[0:imp]+'1.'+'png'
	image = Image.open(image_path,'r')
	pix_val = list(image.getdata())
	pix_val = [list(ele) for ele in pix_val]
	width, height = image.size
	values = list(statement)
	characters =list(map(lambda x: format(ord(x),'08b'),values))
	try:
		if (width * height) // 9 < len(characters):
			messagebox.showerror("ERROR","Text size increases Image file size")
			exit()
	except Exception as e:
		messagebox.showerror("ERROR","\nIssue: ",e,"Image encoding not successful!!")
		exit()
	else:
		newlist = []
		for i in range(0, len(pix_val)):
			pix_val[i] = list(map(lambda x: format(x,'08b'),pix_val[i]))
			newlist.append(pix_val[i])
		for i in range(0, len(characters)):
			encode_into_pixels(i, characters[i], newlist)
		newlist = [tuple(binary_to_decimal(e)) for e in newlist]
		new_image = Image.new(image.mode, image.size)
		new_image.putdata(newlist)
		new_image.save(new_file_path)
		response=messagebox.showinfo("Info","Image encoded successfully, New image path: "+new_file_path)
		


