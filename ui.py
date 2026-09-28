import tkinter as tk
import random

colors = ["#0a0a0a", "#353839", "#2B2D42", "#0c0d1b"]
rt = tk.Tk()
rt.title("The Void")
rt.geometry("500x400")

scrWidth = rt.winfo_screenwidth()
scrHeight = rt.winfo_screenheight()

box = tk.Frame(rt, bg="black")
box.pack(fill="both", expand=True)


def flicker(num=8):
    if num <= 0:
        rt.geometry(f"350x400+{scrWidth-370}+{scrHeight-500}")
        box.config(bg="black")

        rt.deiconify()
        return
    rt.withdraw()
    rt.after(70, lambda: show(num))


def show(num):
    scale = random.uniform(0.5, 1.0)
    width = int(500 * scale)
    height = int(400 * scale)
    x = random.randint(0, scrWidth - width)
    y = random.randint(0, scrHeight - height)

    rt.geometry(f"{width}x{height}+{x}+{y}")
    box.config(bg=random.choice(colors))

    rt.deiconify()
    rt.after(70, lambda: flicker(num - 1))



rt.after(20, flicker)
print(scrWidth, scrHeight)

rt.mainloop()