from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd  
import os
import cv2
imgList = [
  "bmp",
  "jpg",
  "png",
  "ppm",
  "tiff",
  "webp"
]
root = Tk()
root['padx'] = 20
root['pady'] = 10
root.resizable(False,False)
root.title("conversor imagem")

class Window:
  def __init__(self):
    self.img = None
    self.name = None
    self.LabelFile = Label(root,text="arquivo: ")
    self.buttonFile = Button(root,text="Selecionar Imagem",command=self.selectFile) 
    self.buttonConvert = Button(root,text="Converter Imagem",command=self.convert) 
    self.Combobox = ttk.Combobox(root,values=imgList,state="readonly")
    self.Combobox.set("formato Imagem")
    self.buttonFile.pack(pady=3)
    self.LabelFile.pack(pady=3)
    self.Combobox.pack(pady=3)
    self.buttonConvert.pack(pady=3)
    Button(root,text="Sair",command=root.destroy).pack(pady=5)
  def selectFile(self):
    filename = fd.askopenfilename()
    if filename:
      self.name = os.path.splitext(os.path.basename(filename))[0][0:]
      ext = os.path.splitext(os.path.basename(filename))[1][1:]
      self.isImage = False
      for format in imgList:
        if format.lower() == ext.lower():
          self.isImage = True
      if self.isImage:
        self.img = cv2.imread(filename)
        self.LabelFile.config(text=f'arquivo: {os.path.basename(filename)}')
      else:
        self.img = None
        self.LabelFile.config(text='arquivo: ')
  def convert(self):
    if self.isImage and not self.Combobox.get() == "formato Imagem":
      cv2.imwrite(f'{self.name}.{self.Combobox.get()}',self.img)
      if os.path.exists(f'{self.name}.{self.Combobox.get()}'):
        messagebox.showinfo("Sucesso","Imagem convertida com sucesso.")
      else:
        messagebox.showinfo("Erro","Aconteceu Algum Erro.")

obj = Window()
root.mainloop()