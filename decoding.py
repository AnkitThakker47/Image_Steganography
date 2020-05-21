from PIL import Image
import os

strn=''
def BinaryToDecimal(binary): 
    decimal = 0 
    for digit in binary: 
        decimal = decimal*2 + int(digit) 
    return decimal

def get_ascii(i,newlist):
    inival=i*3
    asc=''
    for k in range(inival,inival+3):
        for j in range(0,3):
            if j==2 and k==inival+2:
                continue
            asc=asc+newlist[k][j][-1]  
    return asc

def decode(img_path):
	image = Image.open(img_path,'r')
	pix_val = list(image.getdata())
	pix_val = [list(ele) for ele in pix_val]
	newlist = []
	for i in range(0, len(pix_val)):
		pix_val[i] = list(map(lambda x: format(x,'08b'),pix_val[i]))
		newlist.append(pix_val[i])
	strn=''
	i=0
	st_end=' ?RNA>'
	while True:
		if strn[-6:]==st_end:
			break
		if len(strn)==6:
			if strn!='<RNA? ':
				return False
		ascstr=get_ascii(i,newlist)
		ascstr=BinaryToDecimal(ascstr)
		ch=chr(ascstr)
		strn=strn+ch
		i+=1
	strn=strn[6:]
	strn=strn[0:-6]
	l=[]
	l.insert(0,'True')
	l.insert(1,strn)
	return l