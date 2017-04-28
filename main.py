from tkinter import *
from tkinter import ttk
from Example import Example

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
    # mylist = Listbox(keyPanel, yscrollcommand=scrollbar.set)
    mylist = Listbox(keyPanel)
    for line in range(100):
        mylist.insert(END, "This is line number " + str(line))
    mylist.pack(side=LEFT, fill=BOTH, expand=YES)
    panelContainer.add(keyPanel)

    lang1Panel = ttk.Frame(panelContainer)
    lang1Combobox = ttk.Combobox(lang1Panel,values=list(range(100)))
    lang1Combobox.pack(side=TOP, fill=X, expand=NO)
    example = Example(lang1Panel)
    example.pack(side="top", fill="both", expand=True)
    panelContainer.add(lang1Panel)

    lang2Panel = ttk.Frame(panelContainer)
    lang2Combobox = ttk.Combobox(lang2Panel,values=list(range(100)))
    lang2Combobox.pack(side=TOP, fill=X, expand=NO)
    panelContainer.add(lang2Panel)

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
            mylist.yview(*scrollArguments)
            example.canvas.yview(*scrollArguments)
        return

    example.canvas.config( yscrollcommand = yScrollSet )
    mylist.config( yscrollcommand = yScrollSet )
    scrollbar.config( command = scrollSet )

    root.mainloop()

if __name__ == "__main__":
    main()
