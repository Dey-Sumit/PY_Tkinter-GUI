import random
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from string import ascii_uppercase
window=Tk()
window.title("Hey HangMan")
window.iconbitmap('hang_icon.ico')

															
														#pack and grid both used in a canvas inside of a frame
f=Frame(window,borderwidth=2,bg="black",relief=SUNKEN)		
f.grid(row=0,column=0)
can=Canvas(f,width=630,height=335)
can.pack(expand=YES,fill=BOTH)
img=PhotoImage(file="background1.png")
can.create_image(0,0,image=img,anchor=NW)



window.resizable(0,0) #fixed size

w_height=335					#to make window in centre
w_width=630
s_height=window.winfo_screenheight()
s_width=window.winfo_screenwidth()
x=int((s_width/2)-(w_width/2))
y=int((s_height/2)-(w_height/2))
window.geometry("{}x{}+{}+{}".format(w_width,w_height,x,y))





word_list= ["BANANA","ORANGE","GUAVA","APPLE","PEN","PAPER","ROCK","MUSIC","RUBBER","PENCIL","MANGO","LICHI"]


photos= [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"), PhotoImage(file="images/hang2.png"), PhotoImage(file="images/hang3.png"), PhotoImage(file="images/hang4.png"), PhotoImage(file="images/hang5.png"), PhotoImage(file="images/hang6.png"), PhotoImage(file="images/hang7.png"), PhotoImage(file="images/hang8.png"), PhotoImage(file="images/hang9.png"), PhotoImage(file="images/hang10.png"), PhotoImage(file="images/hang11.png")]
					#fetching the image files of hangman : )

def newGame():					#function of every new game
	global word_wid_spaces
	global no_of_guess
	no_of_guess=0
	imgLabel.config(image=photos[0])
	the_word=random.choice(word_list)
	word_wid_spaces=" ".join(the_word)
	lblWord.set(" ".join("_"*len(the_word)))


def guess(letter):				#guessing function
	global no_of_guess
	if no_of_guess<11:
		txt=list(word_wid_spaces)
		guessed=list(lblWord.get())
		if word_wid_spaces.count(letter)>0:
			for c in range(len(txt)):
				if txt[c]== letter:
					guessed[c]=letter
				lblWord.set("".join(guessed))
				if lblWord.get()==word_wid_spaces:
					messagebox.showinfo("HangMan","Yayy! You guessed the word")
					newGame()
		else:
			no_of_guess +=1
			imgLabel.config(image=photos[no_of_guess])
			if no_of_guess==11:
					messagebox.showwarning("HangMan","Oops! You can't save him.")



imgLabel=Label(can,bg="#36c5f1",borderwidth=2,relief="raised")
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
imgLabel.config(image=photos[0])
lblWord=StringVar()
Label(can, textvariable=lblWord,font=("Consolas 24 bold"),bg="#453466",fg="white",borderwidth=1,relief="groove").grid(row=0, column=4,columnspan=8, padx=10)

n=0
for c in ascii_uppercase:				#setting the buttons fron A 2 Z
	Button(can, text=c, command=lambda c=c: guess(c), font=("Helvetica 15 bold"),bg='white',width=5,activebackground='black',activeforeground='white').grid(row=1+n//9, column=n%9)
	n+=1

Button(can,text="New\nGame", command=lambda:newGame(),font=("Helvetica 9 bold"),activebackground='green',activeforeground='white',bg="red").grid(row=3,column=8,sticky="NSWE")

newGame()
window.mainloop()
