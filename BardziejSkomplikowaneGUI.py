import tkinter as tk
from tkinter import ttk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GUI")
        self.geometry("1200x800")

        # Create main frames
        self.frame_header = HeaderFrame(self)
        self.frame_header.pack(fill="x")

        self.frame_content = ContentFrame(self)
        self.frame_content.pack(fill="both", expand=True)

        self.frame_footer = FooterFrame(self)
        self.frame_footer.pack(fill="x")

class HeaderFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="#f0f0f0")

        # Create header widgets
        self.label_title = tk.Label(self, text="GUI", font=("Arial", 24))
        self.label_title.pack(pady=10)

class ContentFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="#ffffff")

        # Create content widgets
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        for i in range(10):
            tab_frame = TabFrame(self.notebook, i)
            self.notebook.add(tab_frame, text=f"Tab {i+1}")

class FooterFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="#f0f0f0")

        # Create footer widgets
        self.label_copyright = tk.Label(self, text="Copyright 2023 GUI")
        self.label_copyright.pack(pady=10)

class TabFrame(tk.Frame):
    def __init__(self, master, tab_number):
        super().__init__(master)
        self.config(bg="#ffffff")

        # Create tab widgets
        self.label_tab = tk.Label(self, text=f"Tab {tab_number+1} Content")
        self.label_tab.pack(pady=10)

        # Create buttons
        for i in range(10):
            button = tk.Button(self, text=f"Button {i+1}", command=lambda i=i: self.button_click(i))
            button.pack(side="left", padx=5)

        # Create table
        self.table = ttk.Treeview(self, columns=("Column1", "Column2", "Column3"))
        self.table.pack(fill="both", expand=True)

        self.table.heading("#0", text="Row")
        self.table.heading("Column1", text="Column 1")
        self.table.heading("Column2", text="Column 2")
        self.table.heading("Column3", text="Column 3")

        for i in range(10):
            self.table.insert("", "end", values=(f"Row {i+1}", f"Cell {i+1}", f"Cell {i+2}", f"Cell {i+3}"))

    def button_click(self, button_number):
        print(f"Button {button_number+1} clicked!")

if __name__ == "__main__":
    app = Application()
    app.mainloop()