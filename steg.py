from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import encoding as ec
import decoding as dec

flag=False
statement=''
path=0

def test(cw):
	def goback():
		cw.deiconify()
		newTop.withdraw()
	cw.withdraw()
	newTop=Toplevel(bg="#02001c")
	newTop.geometry("400x210+500+300")
	lab=Label(newTop,text="Enter the keywords separated by space",bg="#02001c",fg="gold")
	getword=Entry(newTop,width=45,relief="sunken")
	btnFolder=Button(newTop,text="Select folder to save images",bg="deepskyblue",fg="#02001c")
	btn=Button(newTop,text="Search and save",bg="deepskyblue",fg="#02001c")
	btnback=Button(newTop,text="Back",bg="deepskyblue",fg="#02001c",command=goback)
	lab.pack(pady=2)
	getword.pack(pady=2)
	btnFolder.pack(pady=10)
	btn.pack(pady=10)
	btnback.pack(pady=10)
	getword.focus()
	
def click():
	global top3, statement,img_P,path, top1_50
	if path==0:
		statement=e.get()
	if statement=='':
		messagebox.showerror("ERROR","Text cannot be empty")
		return
	def goback():
		top1_50.deiconify()
		top3.withdraw()
	top1_50.withdraw()
	top3=Toplevel(bg="#02001c")
	top3.geometry("400x230+500+300")
	container = Frame(top3, bg='#02001c')  
	container.grid(row=0, column=0,padx=30,pady=30)    
	l3=Label(container,text="Select the image in which you wish to encode your data",bg="#02001c",fg="gold")
	b3=Button(container,text="Choose the files",bg="deepskyblue",fg="#02001c",borderwidth=4,relief=RAISED,command=cdi,width=15)
	b4=Button(container,text="Back",bg="deepskyblue",fg="#02001c",borderwidth=4,relief=RAISED,command=goback,width=15)
	b5=Button(container,text="Advanced",bg="deepskyblue",fg="#02001c",borderwidth=4,relief=RAISED,command=lambda: test(top3),width=15)
	l3.grid(pady=10, padx=20)
	b3.grid(pady=10, padx=20)
	b5.grid(pady=10, padx=20)
	b4.grid(pady=10,padx=20)

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
	global var
	var=top1_50.filename
	read(var)

def cdi():
	global top3,img_p,statement
	top3.filename=filedialog.askopenfilename(initialdir=os.getcwd()+"/sample images",title="Select a file",filetypes=(("JPG","*.jpg"),("All files","*.*")))
	img_p=top3.filename
	ec.encode(statement,img_p)
	r=messagebox.askyesno("Quit","Do you wish to continue?")
	if r==0:
		root.quit()
	else:
		top3.withdraw()
		guid()

def line():
	def goback():
		top1.deiconify()
		top1_50.withdraw()
	global e,path, l, statement, top1, top1_50
	top1.withdraw()
	path=0
	top1_50=Toplevel(bg="#02001c")
	top1_50.geometry("500x150+500+300")
	container = Frame(top1_50, bg='#02001c')  
	container.grid(row=0, column=0,padx=30,pady=30)    
	l=Label(container)
	l=Label(container,text="Enter the encoding text:",bg="#02001c",fg="gold")
	l.grid(row=0,column=0)
	l.config(font=("Arial", 10))
	e=Entry(container,width=45,relief="sunken")
	e.grid(row=0,column=1,columnspan=3,pady=3)
	b=Button(top1_50,text="Select image",bg="deepskyblue",fg="#02001c",command=click).grid(row=1,column=0)
	b1=Button(top1_50,text="Back",bg="deepskyblue",fg="#02001c",command=goback).grid(row=3,column=0,pady=10)

def file_c():
	def goback():
		top1.deiconify()
		top1_50.withdraw()
	top1.withdraw()
	global top1_50,l3,b3,b4,path
	top1_50=Toplevel(bg="#02001c")
	top1_50.geometry("380x230+500+300")
	path=1
	container = Frame(top1_50, bg='#02001c')  
	container.grid(row=0, column=0,padx=30,pady=30)    
	l3=Label(container,text="Select the file conatining data you want to encode",bg="#02001c",fg="gold")
	b3=Button(container,text="Choose the files",bg="deepskyblue",fg="#02001c",borderwidth=4,relief=RAISED,command=cdf,width=15)
	l3.grid(pady=10, padx=20)
	b3.grid(pady=(0,10), padx=20)
	b=Button(container,text="Select image",bg="deepskyblue",fg="#02001c",command=click,width=15)
	b1=Button(container,text="Back",bg="deepskyblue",fg="#02001c",command=goback,width=15)
	b.grid(pady=(10,10), padx=20)
	b1.grid(pady=(15,10), padx=20)
	
def encoding():
	def goback():
		top2.deiconify()
		top1.withdraw()
	global e, l,statement,top1
	top2.withdraw()
	top1=Toplevel(bg="#02001c")
	top1.geometry("280x140+500+300")
	container = Frame(top1, bg='#02001c')  
	container.grid(row=0, column=0,padx=30,pady=15)    
	b1=Button(container,text="Encode single line message",bg="yellowgreen",fg="black",command=line, width=25)
	b2=Button(container,text="Encode message from file",bg="yellowgreen",fg="black",command=file_c,width=25)
	b3=Button(container,text="Back",bg="yellowgreen",fg="black",command=goback,width=25)
	b1.grid(pady=5, padx=20)
	b2.grid(pady=5, padx=20)
	b3.grid(pady=5,padx=20)

def d(v):
	try:
		l1=[]
		image_path = v
		imp = image_path.rfind('.')
		extension = image_path[imp + 1:]
		if image_path == '':
			messagebox.showerror("ERROR","Please Select an file")
		elif extension.lower() != 'png':
			messagebox.showerror("ERROR","Invalid file type")
			#exit()
		elif not os.path.exists(image_path):
			messagebox.showerror("ERROR","File does not exists")
			#exit()
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
			else:
				messagebox.showerror("ERROR","Image has no encoded data")
				#exit()
	except Exception as e:
		messagebox.showerror("ERROR","\nIssue: "+str(e))
		exit()
		
def cdfd():
	top3.filename=filedialog.askopenfilename(initialdir="/sample images",title="Select a file",filetypes=(("PNG","*.png"),("All files","*.*")))
	global var
	var=top3.filename
	d(var)

def decoding():
	def goback():
		top2.deiconify()
		top3.withdraw()
	top2.withdraw()
	global top3
	top3=Toplevel(bg="#02001c")
	top3.geometry("300x200+500+300")
	container = Frame(top3, bg='#02001c')  
	container.grid(row=0, column=0,padx=30,pady=30)    
	l3=Label(container,text="Select the image you want to decode",bg="#02001c",fg="gold")
	b3=Button(container,text="Choose the files",bg="deepskyblue",fg="#02001c",borderwidth=4,relief=RAISED,command=cdfd,width=12)
	b4=Button(container,text="Back",bg="deepskyblue",fg="#02001c",borderwidth=4,relief=RAISED,command=goback,width=12)
	l3.grid(pady=10, padx=20)
	b3.grid(pady=10, padx=20)
	b4.grid(pady=10, padx=20)

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
	L5=Label(top2,text="6.The decoded information is obtained in a text file present in the same folder.",bg="#02001c",fg="whitesmoke",font=(("Arial",13))).grid(row=6,column=0,columnspan=2)
	
	B1=Button(top2,text="Encoding",bg="gold",fg="#02001c",command=encoding).grid(row=7,column=0,pady=10, sticky=E)
	B2=Button(top2,text="Decoding",bg="gold",fg="#02001c",command=decoding).grid(row=7,column=1,padx=5,pady=10,sticky=W)
	B3=Button(top2,text="Back",bg="gold",fg="#02001c",command=goback).grid(row=7,column=2,padx=5,pady=10,sticky=N)

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
	B=Button(root,text="Guidelines for the project",bg="greenyellow",fg="#02001c",command=guid)
	
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
