from tkinter import *
import png
import time
from PIL import Image,ImageTk
import  pyqrcode
from pyqrcode import *
from barcode import EAN13
from barcode.writer import ImageWriter

app=Tk()
app.title('QR And Barcode Generator')
app.geometry('500x700')


label1=Label(app,text='Enter Title',fg='#0084FF',font='Roboto 8 bold')
entry1=Entry()

label2=Label(app,text='Information',fg='#0084FF',font='Roboto 8 bold')
entry2=Entry()

label3=Label(app,image=None)
label4=Label(app,image=None)

label5=Label(app,fg='#0084FF')
label6=Label(app,fg='#0084FF')

def qr():
	qrfile=entry1.get()
	if qrfile=='':
		pass
	else:
		info=entry2.get()
		gqr=pyqrcode.create(info)
		gqr.png(f'{qrfile}.png')
		img1=Image.open(f'{qrfile}.png')
		img1=img1.resize((200,400))
		img1=ImageTk.PhotoImage(img1)
		label3.config(image=img1)
		label3.update()
		label5.config(text='QR Saved')
		label5.update()
		label5.config(text=' ')
		label5.update()
		time.sleep(1)
	
	
def bar():
	qrfile=entry1.get()
	info=entry2.get()
	gbar=EAN13(info,writer=ImageWriter())
	gbar.save(qrfile)
	img2=Image.open(f'{qrfile}.png')
	img2=img2.resize((400,200))
	img2=ImageTk.PhotoImage(img2)
	label4.config(image=img2)
	label4.update()
	label6.config(text='Barcode Saved')
	label6.update()
	label6.config(text=' ')
	label6.update()
	time.sleep(1)
	
btn1=Button(text='QR code',bg='#00FFF6',activebackground='#00FFF6',fg='#A700FF',activeforeground='#A700FF',command=qr)

btn2=Button(text='Barcode',bg='#00FFF6',activebackground='#00FFF6',fg='#A700FF',activeforeground='#A700FF',command=bar)


label1.grid(row=1,column=1,pady=5,padx=2)
entry1.grid(row=1,column=2,pady=5,padx=2)
label2.grid(row=2,column=1,pady=5,padx=2)
entry2.grid(row=2,column=2,pady=5,padx=2)

btn1.grid(row=3,column=1,pady=50,padx=25)
btn2.grid(row=3,column=2,pady=50,padx=25)

label3.grid(row=4,column=1,pady=5,padx=5)
label4.grid(row=4,column=2,pady=5,padx=5)

label5.grid(row=5,column=1,pady=5,padx=5)
label6.grid(row=5,column=2,pady=5,padx=5)


app.mainloop() 