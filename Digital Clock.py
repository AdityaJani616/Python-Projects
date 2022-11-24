from tkinter import*
import time
root=Tk()
root.title("Digital Clock")
root.geometry("420x150")
root.resizable(0,0)

text_font=("boulder",68,'bold')
background="yellow"
foreground="blue"
border_width=25

label = Label(root, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)

def digital_clock():
    curr_time=time.strftime("%H:%M:%S")
    label.config(text=curr_time)
    label.after(200,digital_clock)
digital_clock()
root.mainloop()