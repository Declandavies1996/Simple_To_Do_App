import tkinter as tk

root = tk.Tk()
root.title("To Do App With GUI - Using tkinter")

listbox = tk.Listbox(root)
listbox.pack()

entry = tk.Entry(root)
entry.pack()

add_button = tk.Button(root, text="Add To List")
add_button.pack()

def add_item():
    text = entry.get() #Retrieves The Words From The Textbox
    listbox.insert(tk.END, text) #Add Words To The List

add_button.config(command=add_item)  # When button is clicked, call add_item function

root.mainloop()