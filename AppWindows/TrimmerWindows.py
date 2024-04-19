from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from customtkinter import *

class TrimmerWindow(CTk):
    color_theme=''
    window_geometry=''
    window_title=''
    icon_location=''
    body_elements={
        'null_element': {
            'type' : None,
            'attrs': {},
            'grid': {},
        }
    }

    # def setTheme(self):
    #     ctk.set_default_color_theme("../TrimmerGraphics/TrimmerTheme.json")

    def setElements(self, body_elements=None):
            self.body_elements = body_elements if body_elements else self.body_elements

    def getElements(self):
        for element in self.body_elements.values():
            if element and element['type']:
                object = globals()[element['type']]
                object(master=self,**element['attrs']).grid(**element['grid'])

    def CloseApp(self):
        self.destroy()

    def setClickables(self):
        CTkButton(master=self,text="Exit",command=self.CloseApp).grid(row=0,column=3)

    def getClickables(self):
         pass

    def __init__(self):
        """Class initializer"""
        super().__init__()
        self.setElements()
        self.setClickables()
        self.getElements()
        self.getClickables()
        self.font = Font(font='Constantia',size=18)
        self.geometry(self.window_geometry if self.window_geometry else "300x300")
        self.title(self.window_title)
        if self.icon_location:
            self.iconbitmap(self.icon_location)

class MainWindow(TrimmerWindow):
    window_geometry=''
    window_title='HTML Trimmer'
    icon_location=''
    body_elements={
        'null_element': {
            'type' : None,
            'attrs': {},
            'grid': {},
        }
    }

    def toggleColor(self):
        if not self.color_theme or self.color_theme == "../TrimmerGraphics/TrimmerTheme.json":
            self.color_theme = 'green'
        elif self.color_theme == 'green':
            self.color_theme = 'blue'
        elif self.color_theme == 'blue':
            self.color_theme = 'dark-blue'
        elif self.color_theme == 'dark-blue':
            self.color_theme = "../TrimmerGraphics/TrimmerTheme.json"
        set_default_color_theme(self.color_theme)
        print(self.color_theme)

    def setClickables(self):
        super().setClickables()
        CTkButton(master=self,text="Hello There",command=self.toggleColor).grid(column=0,row=0)
