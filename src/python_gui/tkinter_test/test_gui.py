import tkinter as tk
import cv2

def root_win():
    root= tk.Tk()
    label_hello = tk.Label(root,  text="hello world")
    label_hello.pack()

def sub_setp_up(root):
    pass


if __name__ == '__main__':
    root = root_win()
    sub_setp_up(root)
    root.mainloop()