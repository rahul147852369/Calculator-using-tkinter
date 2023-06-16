from tkinter import*

root=Tk()

root.geometry("600x300")
root.maxsize(600,300)
root.minsize(300,150)
root.title("Calculator")


def click(event):
    global scvalue
    text = event.widget.cget("text")
    #print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                value="Error"


        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

f1=Frame(root,bg="grey",relief=SUNKEN,borderwidth=5)
scvalue=StringVar()
scvalue.set("")
screen=Entry(f1,textvar=scvalue,font="comicsans 15 bold")
screen.pack(ipadx=7,pady=15,padx=10)
f1.pack()

f=Frame(root,bg="aliceblue")
b=Button(f,text="7",font="lucida 15 bold")
b.pack(side=LEFT,ipadx=5,padx=7)
b.bind("<Button-1>",click)
b=Button(f,text="8",font="lucida 15 bold")
b.pack(side=LEFT,ipadx=5,padx=7)
b.bind("<Button-1>",click)
b=Button(f,text="9",font="lucida 15 bold")
b.pack(side=LEFT,ipadx=5,padx=7)
b.bind("<Button-1>",click)
b=Button(f,text="C",font="lucida 15 bold")
b.pack(side=LEFT,ipadx=5,padx=7)
b.bind("<Button-1>",click)
f.pack(padx=10)

f=Frame(root,bg="aliceblue")
b=Button(f,text="4",font="lucida 15 bold")
b.pack(side=LEFT,ipadx=5,padx=7,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="5",font="lucida 15 bold")
b.pack(side=LEFT,ipadx=5,padx=7,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="6",font="lucida 15 bold")
b.pack(side=LEFT,ipadx=5,padx=7,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="/",font="lucida 15 bold")
b.pack(side=LEFT,ipadx=5,padx=7,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="aliceblue")
b=Button(f,text="1",font="lucida 15 bold")
b.pack(side=LEFT,ipadx=5,padx=7,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="2",font="lucida 15 bold")
b.pack(side=LEFT,ipadx=5,padx=7,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="3",font="lucida 15 bold")
b.pack(side=LEFT,ipadx=5,padx=7,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="+",font="lucida 15 bold")
b.pack(side=LEFT,ipadx=5,padx=7,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="aliceblue")
b=Button(f,text="0",font="lucida 15 bold")
b.pack(side=LEFT,ipadx=5,padx=7,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="-",font="lucida 15 bold")
b.pack(side=LEFT,ipadx=5,padx=7,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="*",font="lucida 15 bold")
b.pack(side=LEFT,ipadx=5,padx=7,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="=",font="lucida 15 bold")
b.pack(side=LEFT,ipadx=5,padx=7,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="aliceblue")
b=Button(f,text=".",font="lucida 15 bold")
b.pack(side=LEFT,ipadx=5,padx=7,pady=3)
b.bind("<Button-1>",click)
f.pack()



root.mainloop()
