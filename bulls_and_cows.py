import random
import tkinter as tk
from tkinter import messagebox

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(nums)
target = ""
for i in range(4):
    target += str(nums[i])

window = tk.Tk()
window.title("猜數字")
window.geometry("300x450")

e = tk.Entry(window)
e.pack()

def getResult(inNum):
    global target
    numA = 0
    numB = 0
    for i in range(4):
        if inNum[i] == target[i]:
            numA += 1

    for i in range(4):
        for j in range(4):
            if inNum[j] == target[i] and i != j:
                numB += 1

    if numA == 4:
        return "恭喜答對!"
    else:
        return str(numA) + "A" + str(numB) + "B"


def send():
    inNum = e.get()
    if len(inNum) != 4:
        messagebox.showerror(title="輸入錯誤", message="請輸入四位數字")
        return

    result = getResult(inNum)

    e.delete(0, "end")
    lb.insert(0, inNum + "   " + result)

b = tk.Button(window, text="送出", width=10, height=2, command=send)
b.pack()

lb = tk.Listbox(window, height=20)
lb.pack(side="bottom")

window.mainloop()


