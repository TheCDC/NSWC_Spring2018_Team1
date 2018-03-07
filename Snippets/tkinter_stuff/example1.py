import tkinter
import tkinter.messagebox
top = tkinter.Tk()


def helloCallBack():

    tkinter.messagebox.showinfo("Hello Python", "Hello World")


B = tkinter.Button(top, text="Hello", command=helloCallBack)

B.pack()

    x = tkinter.messagebox.showinfo("Hello Python", "Hello World")
    print(x)


def callback_maker(i, m):
    """A closure for dynamically callbacks for the buttons."""

    def inner():
        print(tkinter.messagebox.showinfo(i, m))

    return inner


messages = list('abcd')
# loop over some strings and make buttons
for index, m in enumerate(messages):

    b = tkinter.Button(top, text=index, command=callback_maker(index, m))

    b.pack()

top.mainloop()
