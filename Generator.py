from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Generator")

e=Entry(root ,width=30,fg="white",bg="blue",borderwidth=5)
e.pack()


def myClick():
	#Get the entry make int for reverse calculation
	num=int(e.get())
	rev=0
	while(num>0):
		a=num%10
		rev=rev*10+a
		num=num//10
	#list the entry
	a=e.get()
	alist=[]
	for digit in a:
		alist.append (int(digit))
	#list the reverse
	b=str(rev)
	blist=[]
	for digit in b:
		blist.append (int(digit))
	#append entry and reverse into list and mod 10 to have just the unit
	standard=[1,3,4,3,3,4,6,9]
	ab=[]
	for i in range (len(standard)):
		ab.append(int((alist[i]+blist[i])%10))
	de=[]
	for i in range (len(standard)):
		de.append((ab[i]+standard[i])%10)
	de.pop(0)
	de.pop(0)
	code="".join(map(str,de))
	#get the unique code and print it like label but you need to make it str

	myLabel2=Label(root,text="Unique Code : "+str(code))
	myLabel2.pack()


myButton=Button(root,text="Generate!",padx=50,pady=20 ,command=myClick, fg="black",bg="silver")
myButton.pack()






root.mainloop()


