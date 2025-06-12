from gui import ShutdownAppGUI
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = ShutdownAppGUI(root)
    root.mainloop()