#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
class Application(Frame):
    """docstring for Application"""
    def __init__(self, master = None):
        # super(Application, self).__init__(self.master)
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.helloLabel = Label(self,text = 'Hello World')
        self.helloLabel.pack()
        self.quitButton = Button(self,text = 'Quit',command = self.quit)
        self.quitButton.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self,text = 'Hello',command = self.hello)
        self.alertButton.pack()
    def hello(self):
        name = self.nameInput.get() or 'World'
        messagebox.showinfo('Message','Hello,%s' % name)
        # self.quit()
app = Application()
app.master.title('Hello World')
app.mainloop()