import tkinter as tk

window = tk.Tk()
window.title("猜數字")
window.geometry("300x450")

e = tk.Entry(window)
e.pack()

def send():
    inNum = e.get()
    lb.insert(0, inNum)

b = tk.Button(window, text="送出", width=10, height=2, command=send)
b.pack()

lb = tk.Listbox(window, height=20)
lb.pack(side="bottom")

window.mainloop()