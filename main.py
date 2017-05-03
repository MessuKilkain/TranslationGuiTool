import tkinter as tk
from tkinter import *
from tkinter import ttk
from ScrollableViewWithContainer import ScrollableViewWithContainer

def main():
    root = Tk()
    mainframe = ttk.Frame(root, width=850, height=400)
    mainframe.pack(fill=BOTH, expand=YES)

    panelContainer = ttk.PanedWindow(mainframe, orient=HORIZONTAL)
    panelContainer.pack(fill=BOTH, expand=YES)

    keyPanel = ttk.Frame(panelContainer)
    openLangFolderButton = ttk.Button(keyPanel, text="Open")
    openLangFolderButton.pack(side=TOP, fill=X, expand=NO)
    scrollbar = Scrollbar(keyPanel)
    scrollbar.pack(side=LEFT, fill=Y, expand=NO)
    keysScrollView = ScrollableViewWithContainer(keyPanel)
    keysScrollView.pack(side=LEFT, fill=BOTH, expand=YES)
    panelContainer.add(keyPanel)
    '''Put in some fake data'''
    for row in range(100):
        t="This is line number " + str(row)
        tk.Label(keysScrollView.frame, text=t, borderwidth="1", relief="solid").grid(row=row, column=0)

    lang1Panel = ttk.Frame(panelContainer)
    lang1Combobox = ttk.Combobox(lang1Panel,values=list(range(100)))
    lang1Combobox.pack(side=TOP, fill=X, expand=NO)
    lang1ScrollView = ScrollableViewWithContainer(lang1Panel)
    lang1ScrollView.pack(side="top", fill="both", expand=True)
    panelContainer.add(lang1Panel)
    '''Put in some fake data'''
    for row in range(100):
        t="this is the first column for row %s" %row
        tk.Label(lang1ScrollView.frame, text=t, borderwidth="1", relief="solid").grid(row=row, column=0)

    lang2Panel = ttk.Frame(panelContainer)
    lang2Combobox = ttk.Combobox(lang2Panel,values=list(range(100)))
    lang2Combobox.pack(side=TOP, fill=X, expand=NO)
    lang2ScrollView = ScrollableViewWithContainer(lang2Panel)
    lang2ScrollView.pack(side="top", fill="both", expand=True)
    panelContainer.add(lang2Panel)
    '''Put in some fake data'''
    for row in range(100):
        t="this is the second column for row %s" %row
        tk.Label(lang2ScrollView.frame, text=t, borderwidth="1", relief="solid").grid(row=row, column=0, sticky="nsew", padx=1, pady=1)

    def yScrollSet(first, last):
        print("yScrollSet", first, last)
        first = float(first)
        last = float(last)
        scrollbar.set(first, last)
        # scrollSet("moveto",first/(1.0-last+first))
        scrollSet("moveto",first)
        return

    def scrollSet(op, howMany, units=''):
        print("scrollSet", op, howMany, units)
        scrollArguments = ''
        if op == 'scroll':
            scrollArguments = (op, howMany, units)
        elif op == 'moveto':
            scrollArguments = (op, howMany)
        print(scrollArguments)
        if scrollArguments:
            keysScrollView.yview(*scrollArguments)
            lang1ScrollView.yview(*scrollArguments)
            lang2ScrollView.yview(*scrollArguments)
        return

    keysScrollView.config( yscrollcommand = yScrollSet )
    lang1ScrollView.config( yscrollcommand = yScrollSet )
    lang2ScrollView.config( yscrollcommand = yScrollSet )
    scrollbar.config( command = scrollSet )

    # self._widgets = []
    # for row in range(rows):
    #     current_row = []
    #     for column in range(columns):
    #         label = tk.Label(self.text_area, text="",
    #                          borderwidth=0, width=width)
    #         label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
    #         current_row.append(label)
    #     self._widgets.append(current_row)

    root.mainloop()

if __name__ == "__main__":
    main()
