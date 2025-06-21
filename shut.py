from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 15")
def log_out():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1")

st = Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="aqua")

r_button= Button(st, text="Restart", font=("Arial", 20,"bold"),relief=RAISED, cursor="hand2", command=restart, bg="green")
r_button.place(x=150, y=60, width=200, height=50)

rt_button= Button(st, text="Restart Time", font=("Arial",20,"bold"),relief=RAISED, cursor="hand2", command=restart_time, bg="yellow")
rt_button.place(x=150, y=170, width=200, height=50)

lg_button= Button(st, text="Log-Out", font=("Arial", 20,"bold"),relief=RAISED, cursor="hand2", command=log_out, bg="orange")
lg_button.place(x=150, y=280, width=200, height=50)

st_button= Button(st, text="ShutDown", font=("Arial", 20,"bold"),relief=RAISED, cursor="hand2", command=shutdown, bg="red")
st_button.place(x=150, y=390, width=200, height=50)

st.mainloop()
