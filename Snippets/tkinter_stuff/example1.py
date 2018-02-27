import tkinter
import tkinter.messagebox
top = tkinter.Tk()


def helloCallBack():
    x = tkinter.messagebox.showinfo("Hello Python", "Hello World")
    print(x)


def callback_maker(i, m):
    def inner():
        print(tkinter.messagebox.showinfo(i, m))

    return inner


messages = list('abcd')
for index, m in enumerate(messages):

    b = tkinter.Button(top, text=m, command=callback_maker(index, m))

    b.pack()
top.mainloop()
