from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import findimage
import os
import encoding as ec
import decoding as dec

flag=False
statement=''
path=0
store_dir=''
img_p=''
var=''
var1=''

def select_dir():
	global store_dir
	store_dir=filedialog.askdirectory()

def fetchImages(words,num_of_images):
	global store_dir
	num = 20
	if words=='':
		messagebox.showerror("ERROR","Please enter words to be searched")
		return
	if num_of_images == '':
		num_of_images=20
	elif num_of_images.isalpha():
		messagebox.showerror("ERROR","Digits Only Please")
		return
	elif int(num_of_images) < 3 or int(num_of_images) > 200:
		messagebox.showerror("ERROR","The number of images suould be between 3 - 200")
		return
	messagebox.showinfo("MESSAGE","Please wait! Pop up will appear once it is finished")
	num = int(num_of_images)
	if store_dir == '':
		findimage.getImages(words,num_of_images)
	else:
		findimage.getImages(words,num_of_images,store_dir)

def test(cw):
	def goback():
		cw.deiconify()
		newTop.withdraw()
	cw.withdraw()
	newTop=Toplevel(bg="#02001c")
	newTop.geometry("+500+300")
	lab=Label(newTop,text="Enter the keywords separated by space",bg="#02001c",fg="gold")
	getword=Entry(newTop,width=35,relief="sunken")
	lab2=Label(newTop,text="Enter the nunber of images you want",bg="#02001c",fg="gold")
	getnum=Entry(newTop,width=5,relief="sunken")
	btnFolder=Button(newTop,text="Select folder to save images",bg="deepskyblue",fg="#02001c",command=select_dir)
	btn=Button(newTop,text="Search and save",bg="deepskyblue",fg="#02001c",command=lambda: fetchImages(getword.get(),getnum.get()))
	btnback=Button(newTop,text="Back",bg="salmon",fg="#02001c",command=goback)
	lab.grid(pady=2,padx=10)
	getword.grid(pady=2,padx=30)
	lab2.grid(row=3,column=0,pady=5)
	getnum.grid(row=3,column=1,pady=5,padx=1)
	btnFolder.grid(pady=10,padx=30)
	btn.grid(pady=10,padx=30)
	btnback.grid(pady=10,padx=1,sticky=E)
	getword.delete(0,END)
	getword.focus()
	newTop.protocol("WM_DELETE_WINDOW",exit)
	
def click():
	global top3, statement,img_P,path, top1_50
	if path==0:
		statement=e.get()
	if statement=='':
		messagebox.showerror("ERROR","Text cannot be empty")
		return
	if path==1 and var1=='':
		messagebox.showerror("ERROR","Select an file")
		return
	def goback():
		top1_50.deiconify()
		top3.withdraw()
	top1_50.withdraw()
	top3=Toplevel(bg="#02001c")
	top3.geometry("380x245+500+300")
	container = Frame(top3, bg='#02001c')  
	container.grid(row=0, column=0,padx=(30,0),pady=30)    
	l3=Label(container,text="Select the image in which you wish to encode your data",bg="#02001c",fg="gold")
	b3=Button(container,text="Choose from files",bg="deepskyblue",fg="#02001c",borderwidth=4,relief=RAISED,command=cdi,width=15)
	b4=Button(container,text="Advanced",bg="deepskyblue",fg="#02001c",borderwidth=4,relief=RAISED,command=lambda: test(top3),width=15)
	b5=Button(container,text="Encode",bg="yellowgreen",fg="#02001c",borderwidth=4,relief=RAISED,command=enc,width=15)
	b6=Button(top3,text="Back",bg="salmon",fg="#02001c",borderwidth=4,relief=RAISED,command=goback,width=6)
	l3.grid(pady=10, padx=20,row=0,column=0,columnspan=2)
	b3.grid(pady=10, padx=(20,5),row=1,column=0)
	b4.grid(pady=10, padx=(5,20),row=1,column=1)
	b5.grid(pady=(20,0), padx=20,row=2,column=0,columnspan=2)
	b6.grid(pady=5,padx=5,row=1,column=0,sticky=E)
	top3.protocol("WM_DELETE_WINDOW",exit)

def read(p):
	global statement
	try:
		file_path = p
		imp = file_path.rfind('.')
		extension = file_path[imp + 1:]
		if extension.lower() != 'txt':
			messagebox.showerror("ERROR","Invalid file type")
			exit()	
		if not os.path.exists(file_path):
			messagebox.showerror("ERROR","File does not exists")
			exit()
		else: 
			with open(file_path,'r') as f:
				statement = f.read()
	except Exception as e:
		messagebox.showerror("ERROR","\nIssue: ",e)
		exit()

def cdf():
	top1_50.filename=filedialog.askopenfilename(initialdir=os.getcwd()+"/sample documents",title="Select a file",filetypes=(("TXT","*.txt"),("All files","*.*")))
	global var1
	var1=top1_50.filename
	read(var1)

def enc():
	global statement,img_p,var1,path
	if img_p=='':
		messagebox.showerror("ERROR","Select an image")
		return	
	ec.encode(statement,img_p)
	r=messagebox.askyesno("Quit","Do you wish to continue?")
	if r==0:
		root.quit()
	else:
		top3.withdraw()
		guid()

def cdi():
	global top3,img_p,statement,img_p
	top3.filename=filedialog.askopenfilename(initialdir=os.getcwd()+"/sample images",title="Select a file",filetypes=(("JPG","*.jpg"),("All files","*.*")))
	img_p=top3.filename
	
def line():
	def goback():
		top1.deiconify()
		top1_50.withdraw()
	global e,path, l, statement, top1, top1_50
	top1.withdraw()
	path=0
	top1_50=Toplevel(bg="#02001c")
	top1_50.geometry("480x150+500+300")
	container = Frame(top1_50, bg='#02001c')  
	container.grid(row=0, column=0,padx=20,pady=(30,0))    
	l=Label(container)
	l=Label(container,text="Enter the encoding text:",bg="#02001c",fg="gold")
	l.grid(row=0,column=0)
	l.config(font=("Arial", 10))
	e=Entry(container,width=45,relief="sunken")
	e.grid(row=0,column=1,columnspan=3,pady=3)
	b=Button(container,text="Select image",bg="deepskyblue",fg="#02001c",command=click,borderwidth=4,relief=RAISED,width=15)
	b.grid(row=1,column=1,padx=10,pady=(20,5))
	b1=Button(top1_50,text="Back",bg="salmon",fg="#02001c",borderwidth=4,relief=RAISED,command=goback,width=6)
	b1.grid(row=1,column=0,pady=(0,10),sticky=E)
	top1_50.protocol("WM_DELETE_WINDOW",exit)

def file_c():
	def goback():
		top1.deiconify()
		top1_50.withdraw()
	top1.withdraw()
	global top1_50,l3,b3,b4,path
	top1_50=Toplevel(bg="#02001c")
	top1_50.geometry("490x160+500+300")
	path=1
	container = Frame(top1_50, bg='#02001c')  
	container.grid(row=0, column=0,padx=30,pady=(30,0))    
	l3=Label(container,text="Select the file conatining data you want to encode",bg="#02001c",fg="gold")
	b3=Button(container,text="Choose the files",bg="deepskyblue",fg="#02001c",borderwidth=4,relief=RAISED,command=cdf,width=15)
	l3.grid(pady=10, padx=10,row=0,column=0)
	b3.grid(pady=10, padx=10,row=0,column=1)
	b=Button(container,text="Select image",bg="deepskyblue",fg="#02001c",borderwidth=4,relief=RAISED,command=click,width=15)
	b1=Button(top1_50,text="Back",bg="salmon",fg="#02001c",borderwidth=4,relief=RAISED,command=goback,width=6)
	b.grid(pady=(10,0), padx=20,row=1,column=0)
	b1.grid(pady=5,padx=10,row=1,column=0,sticky=E)
	top1_50.protocol("WM_DELETE_WINDOW",exit)
	
def encoding():
	def goback():
		top2.deiconify()
		top1.withdraw()
	global e, l,statement,top1
	top2.withdraw()
	top1=Toplevel(bg="#02001c")
	top1.geometry("280x150+500+300")
	container = Frame(top1, bg='#02001c')  
	container.grid(row=0, column=0,padx=30,pady=15)    
	b1=Button(container,text="Encode single line message",borderwidth=4,relief=RAISED,bg="yellowgreen",fg="black",command=line, width=25)
	b2=Button(container,text="Encode message from file",borderwidth=4,relief=RAISED,bg="yellowgreen",fg="black",command=file_c,width=25)
	b3=Button(top1,text="Back",bg="salmon",fg="black",borderwidth=4,relief=RAISED,command=goback,width=6)
	b1.grid(pady=5, padx=20)
	b2.grid(pady=5, padx=20)
	b3.grid(pady=5,padx=15,sticky=E)
	top1.protocol("WM_DELETE_WINDOW",exit)
	
def deci():
	global var
	if var=='':
		messagebox.showerror("ERROR","Select an Imange")
	else:
		d(var)
		

def d(v):
	try:
		image_path = v
		imp = image_path.rfind('.')
		extension = image_path[imp + 1:]
		if extension.lower() != 'png':
			messagebox.showerror("ERROR","Invalid file type")
		if not os.path.exists(image_path):
			messagebox.showerror("ERROR","File does not exists")
		else: 
			l1=dec.decode(image_path)
			if l1[0]=='True':
				new_file_path = image_path[0:imp]+'_dec.txt'
				f=open(new_file_path,'w')
				f.write(l1[1])
				f.close()
				response=messagebox.showinfo("Info","Image decoded successfully, New text file path: "+new_file_path+".txt")
				if response =="ok":
					r=messagebox.askyesno("Quit","Do you wish to continue?")
					if r==0:
						top3.withdraw()
						root.quit()
					else:
						top3.withdraw()
						guid()
			if l1[0]==False:
				messagebox.showerror("ERROR","Image has no encoded data")
	except Exception as e:
		messagebox.showerror("ERROR","\nIssue: "+str(e))
		
def cdfd():
	top3.filename=filedialog.askopenfilename(initialdir="/sample images",title="Select a file",filetypes=(("PNG","*.png"),("All files","*.*")))
	global var
	var=top3.filename

def decoding():
	def goback():
		top2.deiconify()
		top3.withdraw()
	top2.withdraw()
	global top3,var
	top3=Toplevel(bg="#02001c")
	top3.geometry("440x170+500+300")
	container = Frame(top3, bg='#02001c')  
	container.grid(row=0, column=0,padx=30,pady=(30,0))    
	l3=Label(container,text="Select the image you want to decode",bg="#02001c",fg="gold")
	b3=Button(container,text="Choose the files",bg="deepskyblue",fg="#02001c",borderwidth=4,relief=RAISED,command=cdfd,width=12)
	b4=Button(container,text="Decode",bg="yellowgreen",fg="#02001c",borderwidth=4,relief=RAISED,command=deci,width=12)
	b5=Button(top3,text="Back",bg="salmon",fg="#02001c",borderwidth=4,relief=RAISED,command=goback,width=6)
	l3.grid(pady=10, padx=20,row=0,column=0)
	b3.grid(pady=10, padx=20,row=0,column=1)
	b4.grid(pady=10, padx=20,row=1,columnspan=2,column=0)
	b5.grid(pady=5, padx=5,row=1,column=0,sticky=E)
	top3.protocol("WM_DELETE_WINDOW",exit)

def guid():
	def goback():
		root.deiconify()
		top2.withdraw()
	root.withdraw()
	global top2
	top2=Toplevel(bg="#02001c")
	top2.geometry("+300+200")
	B1=Button(top2)
	B2=Button(top2)
	
	L1=Label(top2,text="GUIDELINES FOR THE PROJECT",bg="#02001c",fg="deepskyblue",font=(("Arial",20,"bold italic"))).grid(row=0,column=0,columnspan=2)
	L2=Label(top2,text="1.Select encoding button for encoding the data or decoding button for decoding.",bg="#02001c",fg="whitesmoke",font=(("Arial",13))).grid(row=1,column=0,columnspan=2)
	L3=Label(top2,text="2.If you select encoding, select the button according to your choice.",bg="#02001c",fg="whitesmoke",font=(("Arial",13))).grid(row=2,column=0,columnspan=2)
	L4=Label(top2,text="3.You can enter the text directly or select a text document containing data.",bg="#02001c",fg="whitesmoke",font=(("Arial",13))).grid(row=3,column=0,columnspan=2)
	L5=Label(top2,text="4.Select image from the images folder to encode data into the image.",bg="#02001c",fg="whitesmoke",font=(("Arial",13))).grid(row=4,column=0,columnspan=2)
	L6=Label(top2,text="5.If you select decoding,select the image to be decoded from the image folder",bg="#02001c",fg="whitesmoke",font=(("Arial",13))).grid(row=5,column=0,columnspan=2)
	L7=Label(top2,text="6.The decoded information is obtained in a text file present in the same folder.",bg="#02001c",fg="whitesmoke",font=(("Arial",13))).grid(row=6,column=0,columnspan=2)
	L8=Label(top2,text="7.Use the advanced button to search images based on keywords",bg="#02001c",fg="whitesmoke",font=(("Arial",13))).grid(row=7,column=0,columnspan=2)
	L9=Label(top2,text="8.Please wait for pop up after choosing image file since big image file might take time to process.",bg="#02001c",fg="whitesmoke",font=(("Arial",13))).grid(row=8,column=0,columnspan=2)

	B1=Button(top2,text="Encoding",bg="gold",fg="#02001c",borderwidth=4,relief=RAISED,command=encoding).grid(row=9,column=0,pady=10, sticky=E)
	B2=Button(top2,text="Decoding",bg="gold",fg="#02001c",borderwidth=4,relief=RAISED,command=decoding).grid(row=9,column=1,padx=5,pady=10,sticky=W)
	B3=Button(top2,text="Back",bg="salmon",fg="#02001c",borderwidth=4,relief=RAISED,command=goback).grid(row=9,column=2,padx=5,pady=10,sticky=N)
	top2.protocol("WM_DELETE_WINDOW",exit)

def home():
	global img 
	img=ImageTk.PhotoImage(Image.open("sample images/saved1.png"))
	img_label=Label(root,image=img,width=500,height=324)
	img_label.grid(row=0,column=0)
	
	s1=Label(root,text="OSTPL PROJECT",bg="#02001c",fg="gold",font=(("Arial",16,"bold italic")))
	s2=Label(root,text="IMAGE STEGANOGRAPHY",bg="#02001c",fg="deepskyblue",font=(("Arial",16,"bold  italic")))
	s3=Label(root,text="GROUP MEMBERS",bg="#02001c",fg="salmon",font=(("Arial",14,"underline")))
	s4=Label(root,text="Ms. RIYA TASGAONKAR-1811122",bg="#02001c",fg="whitesmoke",font=(("Arial",14)))
	s5=Label(root,text="Mr. ANKIT THAKKER-1811123",bg="#02001c",fg="whitesmoke",font=(("Arial",14)))
	s6=Label(root,text="Mr .NIKHIL NAMBOODIRI-1811126",bg="#02001c",fg="whitesmoke",font=(("Arial",14)))
	B=Button(root,text="Guidelines for the project",bg="greenyellow",fg="#02001c",borderwidth=4,relief=RAISED,command=guid)
	
	s1.grid(row=1,column=0,pady=10)
	s2.grid(row=2,column=0,pady=10)
	s3.grid(row=3,column=0)
	s4.grid(row=4,column=0)
	s5.grid(row=5,column=0)
	s6.grid(row=6,column=0)
	B.grid(row=7,column=0,pady=10)

root=Tk()
root.title("OSTPL PROJECT")
root.config(bg="#02001c")
root.geometry('505x600+400+30')
home()

root.mainloop()
