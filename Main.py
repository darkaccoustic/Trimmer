from AppWindows.TrimmerWindows import MainWindow
import customtkinter as ctk

def run():
    # set_appearance_mode("system")
    ctk.set_default_color_theme("../TrimmerGraphics/TrimmerTheme.json")
    main = MainWindow()
    # main.setTheme()
    # main.update_idletasks()
    # main.overrideredirect(True)
    main.mainloop()

if __name__ == '__main__':
    run()