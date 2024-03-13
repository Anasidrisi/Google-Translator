from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text="type",src="English",dest="Hindi"):
    test1=text
    src1=src
    dest1=dest 
    trans = Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s=comb_sor.get()
    d=comb_dest.get()
    masg = sor_txt.get(1.0,END)
    Textget = change(text = masg, src=s , dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,Textget)

root = Tk()
root.title("Translator")
root.geometry("500x800")
root.config(bg = 'brown')

Lab_txt = Label(root,text="Translator", font=("Time New Roman",40,"bold"),bg='white')
Lab_txt.place(x=100,y=40,height=50,width=300)
frame = Frame(root).pack(side=BOTTOM)

Lab_txt = Label(root,text="Source Text", font=("Time New Roman",20,"bold"),fg='Black')
Lab_txt.place(x=100,y=100,height=20,width=300)

sor_txt = Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
sor_txt.place(x=10,y=130,height=150,width=480)


list_Text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame,value = list_Text)
comb_sor.place(x=10,y=300,height=40,width=150)
comb_sor.set("English")
button_change = Button(frame,text="Translate",relief=RAISED,command=data)
button_change.place(x=170,y=300,height=40,width=150)

comb_dest = ttk.Combobox(frame,value = list_Text)
comb_dest.place(x=330,y=300,height=40,width=150)
comb_dest.set("English")

Lab_txt = Label(root,text="Dest Text", font=("Time New Roman",20,"bold"),fg='Black')
Lab_txt.place(x=100,y=360,height=20,width=300)

dest_txt = Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
dest_txt.place(x=10,y=400,height=150,width=480)







root.mainloop()
