import tkinter as tk



def update_length(event):
    length = len(input.get())
    lengthLabel.config(text=f"length: {length}")
    

window = tk.Tk()

window.geometry("300x300")
window.title("EXTRA CALLENGE GUI")

label = tk.Label(window, text="You can input your text here", font="Arial")
label.pack(padx=20, pady=20)

input = tk.Entry(window, width= 40, font="Arial")
input.pack(padx=10, pady=10)

lengthLabel = tk.Label(window, text = "Length: 0")
lengthLabel.pack()

input.bind("<KeyRelease>", update_length)
window.mainloop()