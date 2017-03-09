from tkinter import *
from tkinter import ttk


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
    mylist = Listbox(keyPanel, yscrollcommand=scrollbar.set)
    for line in range(100):
        mylist.insert(END, "This is line number " + str(line))
    mylist.pack(side=LEFT, fill=BOTH, expand=YES)
    panelContainer.add(keyPanel)

    lang1Panel = ttk.Frame(panelContainer)
    lang1Combobox = ttk.Combobox(lang1Panel,values=list(range(100)))
    lang1Combobox.pack(side=TOP, fill=X, expand=NO)
    panelContainer.add(lang1Panel)

    lang2Panel = ttk.Frame(panelContainer)
    lang2Combobox = ttk.Combobox(lang2Panel,values=list(range(100)))
    lang2Combobox.pack(side=TOP, fill=X, expand=NO)
    panelContainer.add(lang2Panel)

    def scrollSet(*L):
        mylist.yview(*L)
        # mylist.yview(L)
        # mylist.yview(L)

    scrollbar.config( command = scrollSet )

    root.mainloop()

if __name__ == "__main__":
    main()
