import tkinter as tk

# Function to update the entry widget with the pressed button's text
def button_click(value):
    current_text = entry.get()
    new_text = current_text + value
    entry.delete(0, tk.END)
    entry.insert(tk.END, new_text)

# Function to evaluate the expression and display the result
def evaluate_expression():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry widget
def clear_entry():
    entry.delete(0, tk.END)

# Creating the main window
root = tk.Tk()
root.title("Simple Calculator")

# Creating the entry widget to display expressions and results
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Creating buttons for digits and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0, 4)
]

# Adding buttons to the window
for button in buttons:
    text = button[0]
    row = button[1]
    col = button[2]
    colspan = button[3] if len(button) > 3 else 1
    if text == '=':
        btn = tk.Button(root, text=text, width=5, height=2, command=evaluate_expression)
    elif text == 'C':
        btn = tk.Button(root, text=text, width=5, height=2, command=clear_entry)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col, columnspan=colspan)

# Running the main loop
root.mainloop()
