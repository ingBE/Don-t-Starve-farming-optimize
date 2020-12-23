import tkinter as tk
import tkinter.font as tkFont
#import numpy as np
from DontStarveFarming import *

NAMES = ["당근", "옥수수", "감자", "토마토", "아스파라거스", "가지", "호박", "수박", "용과", "두리안", "마늘", "양파", "고추", "석류"]

toggle = False

def calCompost():
    x = [0 for x in range(N)]
    for i in range(N):
        x[i] = int(spinbox[i].get())

    #x = np.array(x)
    z = np.matmul(A,x)
    z1.config(text=int(z[0]))
    z2.config(text=int(z[1]))
    z3.config(text=int(z[2]))
    
    global toggle
    toggle = False

def optimize():
    x = [0 for x in range(N)]
    for i in range(N):
        x[i] = int(spinbox[i].get())

    xopt = seedCombination(x)

    for i in range(N):
        seedLabel[i].config(text=int(xopt[i]))

    z = np.matmul(A,xopt)
    z1.config(text=int(z[0]))
    z2.config(text=int(z[1]))
    z3.config(text=int(z[2]))

    global toggle
    toggle = True

def spinboxCommand():
    if toggle == False:
        calCompost()
    else:
        optimize()

if __name__ == "__main__":
    N = len(NAMES)

    root = tk.Tk()
    root.title("Don't Starve seed combination calculator   by ingBE")
    root.geometry("500x480")
    root.resizable(False, False)

    # set default font family and size
    default_font = tkFont.nametofont("TkDefaultFont")
    default_font.configure(family="맑은 고딕", size=12)

    spinbox_font = tkFont.Font(family="맑은 고딕", size=13)
    button_font = tkFont.Font(family="맑은 고딕", size=10)

    # FRAME 0
    frame0 = tk.Frame(root)
    frame0.pack(side="left")

    a0 = tk.Label(frame0, text="", width=3)
    a0.pack()

    # FRAME 1
    frame1 = tk.Frame(root)
    frame1.pack(side="left")

    label1 = tk.Label(frame1, text="작물 종류", width = 11, bg="snow4")
    label1.pack(side="top")

    nameLabel = ["" for x in range(N)]
    for i in range(N):
        nameLabel[i] = tk.Label(frame1, text=NAMES[i], width=11, bg="snow3")
        nameLabel[i].pack(side="top")

    # FRAME 2
    frame2 = tk.Frame(root, bg="snow2")
    frame2.pack(side="left")

    label2 = tk.Label(frame2, text="씨앗 갯수", width=9, bg="snow4")
    label2.pack(side="top")

    spinbox = [0 for x in range(N)]
    for i in range(N):
        spinbox[i] = tk.Spinbox(frame2, from_ = 0, to = 99, width=3, bg="snow2", font=spinbox_font, command=spinboxCommand)
        spinbox[i].pack(side="top")

    # FRAME 3
    frame3 = tk.Frame(root, bg="snow2")
    frame3.pack(side="left")

    label3 = tk.Label(frame3, text="추천 갯수", width=9, bg="snow4")
    label3.pack(side="top")

    seeds = [0 for x in range(N)]
    seedLabel = [0 for x in range(N)]
    for i in range(N):
        seedLabel[i] = tk.Label(frame3, text=seeds[i], width=5, bg="snow2")
        seedLabel[i].pack(side="top")

    # FRAME 4
    frame4 = tk.Frame(root)
    frame4.pack(side="top")

    empty0 = tk.Label(frame4, text="", height=1)
    empty0.pack()

    # image
    from small import *
    img = tk.PhotoImage(data=imageString)
    image = tk.Label(frame4, image=img)
    image.pack()

    empty1 = tk.Label(frame4, text="", height=1)
    empty1.pack()

    button1 = tk.Button(frame4, text="영양 계산", font=button_font, width=11, command=calCompost)
    button1.pack()

    button2 = tk.Button(frame4, text="씨앗 수 계산", font=button_font, width=11, command=optimize)
    button2.pack()
    
    # FRAME 5
    frame5 = tk.Frame(root)
    frame5.pack()

    empty2 = tk.Label(frame5, text="", height=1)
    empty2.pack()

    label4 = tk.Label(frame5, text="영양소", width=16, bg="snow4")
    label4.pack()

    # FRAME 6
    frame6 = tk.Frame(frame5, bg="snow2")
    frame6.pack(side="left")

    label5 = tk.Label(frame6, text="생장식", width=5, bg="snow3")
    label5.pack()

    z1 = tk.Label(frame6, text=0, bg="snow2")
    z1.pack()

    # FRAME 7
    frame7 = tk.Frame(frame5, bg="snow2")
    frame7.pack(side="left")

    label6 = tk.Label(frame7, text="퇴비", width=5, bg="snow3")
    label6.pack()

    z2 = tk.Label(frame7, text=0, bg="snow2")
    z2.pack()

    # FRAME 8
    frame8 = tk.Frame(frame5, bg="snow2")
    frame8.pack(side="left")

    label7 = tk.Label(frame8, text="비료", width=5, bg="snow3")
    label7.pack()

    z3 = tk.Label(frame8, text=0, bg="snow2")
    z3.pack()

    root.mainloop()
