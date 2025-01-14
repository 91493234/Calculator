import tkinter as tk
import math

root = tk.Tk()

# making window
root.geometry('400x516')
root.minsize(330, 516)
root.maxsize(400, 516)
root.title('Calculator')
root.configure(bg='#272727')

#storing color
background_color = "#272727"

# storing images
image1 = tk.PhotoImage(file = 'b1.png')
image2= tk.PhotoImage(file='b2.png')
image3= tk.PhotoImage(file='b3.png')
image4= tk.PhotoImage(file='b4.png')
image5= tk.PhotoImage(file='b5.png')
image6= tk.PhotoImage(file='b6.png')
image7= tk.PhotoImage(file='b7.png')
image8= tk.PhotoImage(file='b8.png')
image9= tk.PhotoImage(file='b9.png')
image10= tk.PhotoImage(file='b10.png')
image11= tk.PhotoImage(file='b11.png')
image12= tk.PhotoImage(file='b12.png')
image13= tk.PhotoImage(file='b13.png')
image14= tk.PhotoImage(file='b14.png')
image15= tk.PhotoImage(file='b15.png')
image16= tk.PhotoImage(file='b16.png')
image17= tk.PhotoImage(file='b17.png')
image18= tk.PhotoImage(file='b18.png')


# frame = tk.Frame(root, pady=30)
# frame.pack(anchor='nw', side='top', pady=17)

user_input = tk.Label(pady=30,bg=background_color, fg='white',text='12345678901234567890', font='Inder 25')
user_input.place(y=22)

tk.Button(image=image1,bg=background_color, borderwidth=0, highlightthickness=0, command=print('.')).place(x=90, y=175)
tk.Button(image=image2,bg=background_color, borderwidth=0, highlightthickness=0).place(x=163, y=175)
tk.Button(image=image3,bg=background_color, borderwidth=0, highlightthickness=0).place(x=241, y=175)
tk.Button(image=image4,bg=background_color, borderwidth=0, highlightthickness=0).place(x=319, y=175)
tk.Button(image=image5,bg=background_color, borderwidth=0, highlightthickness=0).place(x=90, y=244)
tk.Button(image=image6,bg=background_color, borderwidth=0, highlightthickness=0).place(x=163, y=244)
tk.Button(image=image7,bg=background_color, borderwidth=0, highlightthickness=0).place(x=241, y=244)
tk.Button(image=image8,bg=background_color, borderwidth=0, highlightthickness=0).place(x=319, y=244)
tk.Button(image=image9,bg=background_color, borderwidth=0, highlightthickness=0).place(x=90, y=313)
tk.Button(image=image10,bg=background_color, borderwidth=0, highlightthickness=0).place(x=163, y=313)
tk.Button(image=image11,bg=background_color, borderwidth=0, highlightthickness=0).place(x=241, y=313)
tk.Button(image=image12,bg=background_color, borderwidth=0, highlightthickness=0).place(x=319, y=313)
tk.Button(image=image13,bg=background_color, borderwidth=0, highlightthickness=0).place(x=90, y=379)
tk.Button(image=image14,bg=background_color, borderwidth=0, highlightthickness=0).place(x=163, y=379)
tk.Button(image=image15,bg=background_color, borderwidth=0, highlightthickness=0).place(x=241, y=379)
tk.Button(image=image16,bg=background_color, borderwidth=0, highlightthickness=0,).place(x=319, y=379)
tk.Button(image=image17,bg=background_color, borderwidth=0, highlightthickness=0).place(x=94, y=451)
tk.Button(image=image18,bg=background_color, borderwidth=0, highlightthickness=0).place(x=319, y=444)




root.mainloop()