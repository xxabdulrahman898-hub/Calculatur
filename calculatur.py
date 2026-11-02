import tkinter as tk
from tkinter import messagebox

def on_click(button_text):
    current = entry.get()
    if button_text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            messagebox.showerror("Error", "Invalid Expression")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

root = tk.Tk()
root.title("Dark Calculator")
root.configure(bg='#1e1e1e')

for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

entry = tk.Entry(root, font=('Arial', 36, 'bold'), bg='#1e1e1e', fg='white', borderwidth=0, justify='right')
entry.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=10, pady=30)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

operators = ['/', '*', '-', '+', '=']
row_val = 1
col_val = 0

for button in buttons:
    color = '#ff9500' if button in operators else '#333333'
    
    action = lambda x=button: on_click(x)
    
    btn = tk.Button(root, text=button, font=('Arial', 22, 'bold'), bg=color, fg='white', 
                    borderwidth=0, command=action)
    btn.grid(row=row_val, column=col_val, sticky='nsew', padx=2, pady=2)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()