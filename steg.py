from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import encoding as ec
import decoding as dec

def encoding():
	global e
	global l,statement
	global top1
	top2.withdraw()
	top1=Toplevel(bg="#02001c")
	top1.geometry("+500+300")
	l=Label(top1)
	l=Label(top1,text="Enter the encoding text:",bg="#02001c",fg="whitesmoke")
	l.grid(row=0,column=0)
	e=Entry(top1,width=45,relief="sunken")
	e.grid(row=0,column=1,columnspan=3)
	b=Button(top1,text="View the images",bg="whitesmoke",fg="#02001c",command=click).grid(row=1,column=0)


def click():
	top1.withdraw()
	global top
	top=Toplevel(bg="#02001c")
	top.geometry("+400+100")
	global pr
	global num
	l2=Label(top)
	bf=Button(top)
	b=Button(top)
	bb=Button(top)	
	bselect=Button(top) 
	
	p1="D:/COLLEGE SEM 4/PYTHON LAB/Final Mip/sample images/dog.jpg"
	p2="D:/COLLEGE SEM 4/PYTHON LAB/Final Mip/sample images/flower.jpg"
	p3="D:/COLLEGE SEM 4/PYTHON LAB/Final Mip/sample images/london.jpg"
	p4="D:/COLLEGE SEM 4/PYTHON LAB/Final Mip/sample images/lotus.jpg"
	p5="D:/COLLEGE SEM 4/PYTHON LAB/Final Mip/sample images/newyork.jpg"
	p6="D:/COLLEGE SEM 4/PYTHON LAB/Final Mip/sample images/rain.jpg"
	p7="D:/COLLEGE SEM 4/PYTHON LAB/Final Mip/sample images/xmas.jpg"

	img1= ImageTk.PhotoImage(Image.open(p1))
	img2= ImageTk.PhotoImage(Image.open(p2))
	img3= ImageTk.PhotoImage(Image.open(p3))
	img4= ImageTk.PhotoImage(Image.open(p4))
	img5= ImageTk.PhotoImage(Image.open(p5))
	img6= ImageTk.PhotoImage(Image.open(p6))
	img7= ImageTk.PhotoImage(Image.open(p7))
 
	global ilist,p_list
	ilist=[img1,img2,img3,img4,img5,img6,img7]
	p_list=[p1,p2,p3,p4,p5,p6,p7]
	 
	global img_label	
	img_label=Label(top,image=img1)
	l2=Label(top,text="Select the image you want to encode:",bg="#02001c",fg="whitesmoke").grid(row=0,column=0,columnspan=3)
	
	def forward(num):
		global img_label
		img_label.grid_forget()
		img_label=Label(top,image=ilist[num-1])
		bf=Button(top,text=">>",bg="whitesmoke",fg="#02001c",command=lambda:forward(num+1),width=10)
		bb=Button(top,text="<<",bg="whitesmoke",fg="#02001c",command=lambda:back(num-1),width=10)
		if num==len(ilist):
			bf=Button(top,text=">>",bg="whitesmoke",fg="#02001c",state=DISABLED,width=10)
		img_label.grid(row=1,column=0,columnspan=3)           
		bb.grid(row=2,column=0)
		bf.grid(row=2,column=2)
		
	def back(num):
		global img_label,e
		img_label.grid_forget()
		img_label=Label(top,image=ilist[num-1])
		bf=Button(top,text=">>",bg="whitesmoke",fg="#02001c",command=lambda:forward(num+1),width=10)
		bb=Button(top,text="<<",bg="whitesmoke",fg="#02001c",command=lambda:back(num-1),width=10)
		if num==1:
			bb=Button(top,text="<<",bg="whitesmoke",fg="#02001c",state=DISABLED,width=10)
		img_label.grid(row=1,column=0,columnspan=3)           
		bb.grid(row=2,column=0)
		bf.grid(row=2,column=2)
		
	def click_image():
		if c.get()==options[0]:
			ec.encode(e.get(),p_list[0])
		if c.get()==options[1]:
			ec.encode(e.get(),p_list[1])
		if c.get()==options[2]:
			ec.encode(e.get(),p_list[2])	
		if c.get()==options[3]:
			ec.encode(e.get(),p_list[3])
		if c.get()==options[4]:
			ec.encode(e.get(),p_list[4])
		if c.get()==options[5]:
			ec.encode(e.get(),p_list[5])
		if c.get()==options[6]:
			ec.encode(e.get(),p_list[6])
		r=messagebox.askyesno("Quit","Do you wish to continue?")
		if r==0:
			#top3.withdraw()
			root.quit()
		else:
			top.withdraw()
			guid()
	
	bb=Button(top,text="<<",command=back,bg="whitesmoke",fg="#02001c",width=10,state=DISABLED)
	bselect=Button(top,text="Encode",bg="whitesmoke",fg="#02001c",command=click_image,width=10)
	bf=Button(top,text=">>",bg="whitesmoke",fg="#02001c",command=lambda:forward(2),width=10)
	label=Label(top,text="Select the image from the drop down menu",bg="#02001c",fg="whitesmoke").grid(row=3,column=1)
	options=["Dog","Flower","London","Lotus","New York","Rain","Xmas"]
	c=ttk.Combobox(top)
	c=ttk.Combobox(top,value=options)
	c.grid(row=4,column=1)
	global B,E
	#B=Button(top,text="Quit",bg="whitesmoke",fg="#02001c",command=top1.quit,width=10).grid(row=5,column=2,padx=5,pady=10)
	
	img_label.grid(row=1,column=0,columnspan=3)
	bb.grid(row=2,column=0,pady=10,sticky=E)
	bselect.grid(row=5,column=1,padx=5,pady=10)
	bf.grid(row=2,column=2,padx=10,sticky=W)
	
		
	
def d(v):
	try:
		l1=[]
		image_path = v
		imp = image_path.rfind('.')
		extension = image_path[imp + 1:]
		if extension.lower() != 'png':
			raise Exception("Invalid file type")
		if not os.path.exists(image_path):
			raise Exception("File does not exists")
		else: 
			l1=dec.decode(image_path)
			if l1[0]=='True':
				new_file_path = image_path[0:imp]+'_dec'
				f=open(new_file_path,'w')
				f.write(l1[1])
				f.close()
				response=messagebox.showinfo("Info","Image decoded successfully, New text file path: "+new_file_path+".txt")
				#if response=="ok":
				if response =="ok":
					r=messagebox.askyesno("Quit","Do you wish to continue?")
					if r==0:
						top3.withdraw()
						root.quit()
					else:
						top3.withdraw()
						guid()
			else:
				print('Image has no encoded data')
	except Exception as e:
		print("\nIssue: ", e)


def cd():
	top3.filename=filedialog.askopenfilename(initialdir="/sample images",title="Select a file",filetypes=(("PNG","*.png"),("All files","*.*")))
	global var
	var=top3.filename
	d(var)
	
def decoding():
	top2.withdraw()
	global top3
	top3=Toplevel(bg="#02001c")
	top3.geometry("+500+300")
	global l3,b3,b4
	l3=Label(top3,text="Select the image you want to decode",bg="#02001c",fg="whitesmoke").grid(row=0,column=0,columnspan=3)
	b3=Button(top3,text="Choose the files",bg="whitesmoke",fg="#02001c",borderwidth=4,relief=RAISED,command=cd,width=12).grid(row=1,column=1)
	#b4=Button(top3,text="Quit",bg="whitesmoke",fg="#02001c",command=top3.quit,width=10).grid(row=1,column=1)

def guid():
	root.withdraw()
	global top2
	top2=Toplevel(bg="#02001c")
	top2.geometry("+300+200")
	B1=Button(top2)
	B2=Button(top2)
	L1=Label(top2,text="GUIDELINES OF THE PROJECT",bg="#02001c",fg="whitesmoke",font=(("Arial",20,"bold underline"))).grid(row=0,column=0,columnspan=2)
	L2=Label(top2,text="1.Select encoding button for encoding the image or decoding button for decoding.",bg="#02001c",fg="whitesmoke",font=(("Arial",13))).grid(row=1,column=0,columnspan=2)
	L3=Label(top2,text="2.If you select encoding,enter the text you want to encode in the image.",bg="#02001c",fg="whitesmoke",font=(("Arial",13))).grid(row=2,column=0,columnspan=2)
	L4=Label(top2,text="3.From the image gallery,select the image to be encoded from drop down.",bg="#02001c",fg="whitesmoke",font=(("Arial",13))).grid(row=3,column=0,columnspan=2)
	L5=Label(top2,text="4.Click the Encode button,which will then return a new encoded image.",bg="#02001c",fg="whitesmoke",font=(("Arial",13))).grid(row=4,column=0,columnspan=2)
	L6=Label(top2,text="5.If you select decoding,select the image to be decoded from the image folder",bg="#02001c",fg="whitesmoke",font=(("Arial",13))).grid(row=5,column=0,columnspan=2)
	L5=Label(top2,text="4.On clicking the decode button,a new text file is generated containing the message.",bg="#02001c",fg="whitesmoke",font=(("Arial",13))).grid(row=6,column=0,columnspan=2)
	B1=Button(top2,text="Encoding",bg="whitesmoke",fg="#02001c",command=encoding).grid(row=7,column=0,pady=10,sticky=E)
	B2=Button(top2,text="Decoding",bg="whitesmoke",fg="#02001c",command=decoding).grid(row=7,column=1,padx=5,pady=10,sticky=W)


def home():
	global img 
	img=ImageTk.PhotoImage(Image.open("D:/COLLEGE SEM 4/PYTHON LAB/Final Mip/sample images/st.jpeg"))
	img_label=Label(root,image=img,width=550,height=400)
	img_label.grid(row=0,column=0)
	
	s1=Label(root,text="OSTPL PROJECT",bg="#02001c",fg="whitesmoke",font=(("Arial",14,"bold underline")))
	s2=Label(root,text="TOPIC: IMAGE STEGANOGRAPHY",bg="#02001c",fg="whitesmoke",font=(("Arial",14,"bold underline")))
	s3=Label(root,text="GROUP MEMBERS",bg="#02001c",fg="whitesmoke",font=(("Arial",14,"underline")))
	s4=Label(root,text="Ms. RIYA TASGAONKAR-1811122",bg="#02001c",fg="whitesmoke",font=(("Arial",14)))
	s5=Label(root,text="Mr. ANKIT THAKKER-1811123",bg="#02001c",fg="whitesmoke",font=(("Arial",14)))
	s6=Label(root,text="Mr .NIKHIL NAMBOODIRI-1811126",bg="#02001c",fg="whitesmoke",font=(("Arial",14)))
	B=Button(root,text="Guidelines for the project",bg="whitesmoke",fg="#02001c",command=guid)
	
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
root.geometry('555x650+400+30')

home()

root.mainloop()


