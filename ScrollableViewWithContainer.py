import tkinter as tk

class ScrollableViewWithContainer(tk.Canvas):
    def __init__(self, root):

        tk.Canvas.__init__(self, root)
        self.frame = tk.Frame(self, background="#ffffff")

        self.create_window((4,4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        # self.populate()

    def populate(self):
        '''Put in some fake data'''
        for row in range(100):
            tk.Label(self.frame, text="%s" % row, width=3, borderwidth="1",
                     relief="solid").grid(row=row, column=0)
            t="this is the second column for row %s" %row
            tk.Label(self.frame, text=t).grid(row=row, column=1)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.configure(scrollregion=self.bbox("all"))

if __name__ == "__main__":
    root=tk.Tk()
    ScrollableViewWithContainer(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
