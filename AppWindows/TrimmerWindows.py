from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from customtkinter import *

class MainWindow(CTk):
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

    def setElements(self, body_elements=None):
            self.body_elements = body_elements if body_elements else self.body_elements

    def getElements(self):
        for element in self.body_elements.values():
            if element and element['type']:
                object = globals()[element['type']]
                object(master=self,**element['attrs']).grid(**element['grid'])

    def __init__(self):
        """Class initializer"""
        super().__init__()
        self.setElements()
        # self.setClickables()
        self.getElements()
        # self.getClickables()
        set_appearance_mode("system")
        set_default_color_theme("../TrimmerGraphics/TrimmerTheme.json")
        self.font = Font(font='Constantia',size=18)
        self.geometry(self.window_geometry if self.window_geometry else "300x300")
        self.title(self.window_title)
        if self.icon_location:
            self.iconbitmap(self.icon_location)

