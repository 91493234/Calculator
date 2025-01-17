import tkinter as tk
from PIL import Image, ImageTk
import ctypes


root = tk.Tk()

# making window
root.geometry('400x516')
root.minsize(330, 516)
root.maxsize(400, 516)
root.title('Calculator')
root.configure(bg='#272727')
root.iconbitmap('calculator.ico')

ctypes.Win11.shcore.SetProcessDpiAwareness(1)

def numbers(button_text):
    user_input.insert(tk.END, button_text + "")
def delete_entry():
    try:
        # Get the current cursor position
        current_position = user_input.index(tk.INSERT)
        
        # Calculate the position of the character before the cursor
        line, column = current_position.split('.')
        column = int(column) - 1
        
        # Ensure we're not deleting a character outside the text range
        if column >= 0:
            previous_position = f"{line}.{column}"
            user_input.delete(previous_position, current_position)
    except Exception as e:
        pass 

def delete():
    user_input.delete(1.0, tk.END) 

def answer():
    try:
        # Get the content of the Text widget
        expression = user_input.get(1.0, tk.END).strip()
        # Evaluate the expression and display the result
        result = eval(expression)
        user_input.delete(1.0, tk.END)  # Clear the text widget
        user_input.insert(tk.END, str(result))  # Insert the result into the text widget
    except Exception as e:
        # If there is an error, display an error message
        user_input.delete(1.0, tk.END)
        user_input.insert(tk.END, "Error")


#storing color
background_color = "#272727"

# storing images

image1 = tk.PhotoImage(file='b1.png')
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

user_input = tk.Text(bg=background_color,fg='white', font='Inder 28 bold', width=18, height=3)
user_input.place(x=8, y=22)

tk.Button(image=image1,bg=background_color, borderwidth=0, highlightthickness=0, command=lambda:numbers("."), activebackground=background_color).place(x=90, y=175)
tk.Button(image=image2,bg=background_color, borderwidth=0, highlightthickness=0, command=delete, activebackground=background_color).place(x=163, y=175)
tk.Button(image=image3,bg=background_color, borderwidth=0, highlightthickness=0, command=delete_entry, activebackground=background_color).place(x=241, y=175)
tk.Button(image=image4,bg=background_color, borderwidth=0, highlightthickness=0, command=lambda:numbers("*"), activebackground=background_color).place(x=319, y=175)
tk.Button(image=image5,bg=background_color, borderwidth=0, highlightthickness=0, command=lambda:numbers("7"), activebackground=background_color).place(x=90, y=244)
tk.Button(image=image6,bg=background_color, borderwidth=0, highlightthickness=0, command=lambda:numbers("8"), activebackground=background_color).place(x=163, y=244)
tk.Button(image=image7,bg=background_color, borderwidth=0, highlightthickness=0, command=lambda:numbers("9"), activebackground=background_color).place(x=241, y=244)
tk.Button(image=image8,bg=background_color, borderwidth=0, highlightthickness=0, command=lambda:numbers("/"), activebackground=background_color).place(x=319, y=244)
tk.Button(image=image9,bg=background_color, borderwidth=0, highlightthickness=0, command=lambda:numbers("4"), activebackground=background_color).place(x=90, y=313)
tk.Button(image=image10,bg=background_color, borderwidth=0, highlightthickness=0, command=lambda:numbers("5"), activebackground=background_color).place(x=163, y=313)
tk.Button(image=image11,bg=background_color, borderwidth=0, highlightthickness=0, command=lambda:numbers("6"), activebackground=background_color).place(x=241, y=313)
tk.Button(image=image12,bg=background_color, borderwidth=0, highlightthickness=0, command=lambda:numbers("-"), activebackground=background_color).place(x=319, y=313)
tk.Button(image=image13,bg=background_color, borderwidth=0, highlightthickness=0, command=lambda:numbers("1"), activebackground=background_color).place(x=90, y=379)
tk.Button(image=image14,bg=background_color, borderwidth=0, highlightthickness=0, command=lambda:numbers("2"), activebackground=background_color).place(x=163, y=379)
tk.Button(image=image15,bg=background_color, borderwidth=0, highlightthickness=0, command=lambda:numbers("3"), activebackground=background_color).place(x=241, y=379)
tk.Button(image=image16,bg=background_color, borderwidth=0, highlightthickness=0, command=lambda:numbers("+"), activebackground=background_color).place(x=319, y=379)
tk.Button(image=image17,bg=background_color, borderwidth=0, highlightthickness=0, command=lambda:numbers("0"), activebackground=background_color).place(x=94, y=451)
tk.Button(image=image18,bg=background_color, borderwidth=0, highlightthickness=0, command=answer, activebackground=background_color).place(x=319, y=444)

root.mainloop()
