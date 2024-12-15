import tkinter as tk

class Library:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")

        self.frame1 = tk.Frame(self.root)
        self.frame1.pack(side=tk.TOP)

        self.frame2 = tk.Frame(self.root)
        self.frame2.pack(side=tk.BOTTOM)
    
        self.book = tk.Label(self.frame1, text="BOOK NAME")
        self.book.grid(row=0, column=0)
        self.bookin = tk.Entry(self.frame1)
        self.bookin.grid(row=0, column=1)

        self.stu = tk.Label(self.frame1, text="STUDENT NAME")
        self.stu.grid(row=0, column=2)
        self.stuin = tk.Entry(self.frame1)
        self.stuin.grid(row=0, column=3)

        self.button = tk.Button(self.frame1, text="Search Book")
        self.button.grid(row=1, column=0)

root = tk.Tk()
obj = Library(root)
root.mainloop()

