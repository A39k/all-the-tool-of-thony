import tkinter as tk
from tkinter import ttk, messagebox, filedialog, colorchooser

def submit_text():
    text_content = text.get("1.0", "end").strip()
    messagebox.showinfo("Text Submitted",f"Entered Text:\n{text_content}")
                                                

mainWindow = tk.Tk()

mainWindow.title("All the Tools by Jenny")
mainWindow.geometry("800x700")

# Create Notebook Tab
notebook = ttk.Notebook(mainWindow)
notebook.pack(fill="both", expand=True)

# Add Tabs
tab_basic = ttk.Frame(notebook, padding = 10)
tab_selection = ttk.Frame(notebook, padding = 10)
tab_advanced = ttk.Frame(notebook, padding = 10)

notebook.add(tab_basic, text = "Basic Widgets")
notebook.add(tab_selection, text = "Selection Widgets")
notebook.add(tab_advanced, text = "Advanced Widgets")

# Contents of the tab basic
ttk.Label(tab_basic, text = "Label: Hello, Jenny!").grid(row=0, column=0, padx=10, pady=10)
ttk.Entry(tab_basic).grid(row=0, column=1, padx=10, pady=10)

ttk.Label(tab_basic, text = "Username:").grid(row=1, column=0, padx=10, pady=10)
ttk.Entry(tab_basic).grid(row=1, column=1, padx=10, pady=10)

ttk.Label(tab_basic, text = "Password").grid(row=2, column=0, padx=10, pady=10)
ttk.Entry(tab_basic).grid(row=2, column=1, padx=10, pady=10)

text = tk.Text(tab_basic, height=5, width=30)
text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
ttk.Button(tab_basic, text = "Submit", command = submit_text).grid(row=4, column=0, columnspan=2, pady=10)

canvas = tk.Canvas(tab_basic, width=200 , height=100, bg="lightblue")
canvas.create_oval(50, 20, 150, 80, fill = "red")
canvas.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Content of the selection tab
ttk.Label(tab_selection, text = "Checkbutton:").grid(row=0, column=0, padx=10, pady=10)
check_var = tk.BooleanVar()
ttk.Checkbutton(tab_selection, text = "Tick me", variable = check_var).grid(row=0, column=1, padx=10, pady=10)




mainWindow.mainloop()