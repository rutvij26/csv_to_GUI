import csv
from tkinter import *
import tkinter.ttk as ttk
import pandas as pd

# Change the path here for change in file :)
file_path = 'Node06.csv' 

root = Tk()
root.title("Import Numbers from CSV to Python GUI")
width = 500
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(height=None, width=None)

df =  pd.read_csv(file_path,delimiter=",")
columns = tuple(df.columns)


TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=columns, height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)

scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)

for index,x in enumerate(columns):
    tree.heading(x, text=x, anchor=W)

for index,x in enumerate(columns):
    if index != 0 :
        tree.column("#"+str(index), stretch=NO, minwidth=0, width=100)
    else:
        tree.column("#"+str(index), stretch=NO, minwidth=0, width=0)
tree.pack()



with open(file_path) as f:
    reader = csv.DictReader(f, delimiter=',')
    
    for index,row in enumerate(reader):
        column_values = tuple(list(row[x] for x in columns))
        tree.insert("", 2, values=column_values)


if __name__ == '__main__':
    root.mainloop()

