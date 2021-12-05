from tkinter import *
import tkinter
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import filedialog as fd
from tkinter import messagebox
import os.path as path
iteratorForFiles = 0

def createFile():
    global txt
    directory = fd.askdirectory()
    fileExists = True
    while fileExists:
        numOfTheFile = str(iterator())
        fileExists = path.isfile(directory + "//" + "NewFile" + numOfTheFile + ".txt")
    directory = directory + "//" + "NewFile" + numOfTheFile + ".txt"
    my_file = open(directory, "w+")
    my_file.write(txt.get("1.0", tkinter.END))
    my_file.close()
    messagebox.showinfo("Файл успешно сохранен!", r"Путь к файлу: " + directory)

def iterator():
    global iteratorForFiles
    iteratorForFiles += 1
    return iteratorForFiles

def fileOpen():
    global txt
    file_name = fd.askopenfilename()
    if file_name == '':
        messagebox.showinfo("Файл не был открыт!", "Файл был не выбран или не открыт")
        return
    f = open(file_name)
    s = f.read()
    txt.insert(1.0, s)
    f.close()

window = Tk()
window.title("Текстовый редактор KEA20211205")
window.geometry('400x250')

menu = Menu(window)

new_item = Menu(menu)

new_item.add_command(label='Новый', command = createFile)
new_item.add_command(label='Открыть', command = fileOpen)

menu.add_cascade(label='Файл', menu=new_item)

window.config(menu=menu)
txt = scrolledtext.ScrolledText(window, width=400, height=250)
txt.grid(column=0, row=0)

window.mainloop()

