import tkinter as tk

vypocet = ""


def handle_click(value):
    global vypocet
    vypocet += value

    print(vypocet)


def main():
    okno = tk.Tk()
    okno.title("Kalkulačka")
    canvas = tk.Canvas(okno, height=300, width=600)
    canvas.grid(columnspan=3, rowspan=3)

    input = tk.Entry()
    input.grid(row=0, column=1, sticky="nswe")

    btn_frame = tk.Frame(okno)
    btn_frame.grid(row=1, column=1)

    # 1 row
    one = tk.Button(btn_frame, text="1", font="Arial 20", border=0, padx=15, command=lambda: handle_click("1"), bg="#4ECDC4", activebackground="#1B8A83")
    one.grid(row=3, column=0, sticky="nswe")

    two = tk.Button(btn_frame, text="2", font="Arial 20", border=0, padx=15, command=lambda: handle_click("2"), bg="#4ECDC4", activebackground="#1B8A83")
    two.grid(row=3, column=1, sticky="nswe")

    three = tk.Button(btn_frame, text="3", font="Arial 20", border=0, padx=15, command=lambda: handle_click("3"), bg="#4ECDC4", activebackground="#1B8A83")
    three.grid(row=3, column=2, sticky="nswe")

    # 2 row
    four = tk.Button(btn_frame, text="4", font="Arial 20", border=0, padx=15, command=lambda: handle_click("4"), bg="#4ECDC4", activebackground="#1B8A83")
    four.grid(row=2, column=0, sticky="nswe")

    five = tk.Button(btn_frame, text="5", font="Arial 20", border=0, padx=15, command=lambda: handle_click("5"), bg="#4ECDC4", activebackground="#1B8A83")
    five.grid(row=2, column=1, sticky="nswe")

    six = tk.Button(btn_frame, text="6", font="Arial 20", border=0, padx=15, command=lambda: handle_click("6"), bg="#4ECDC4", activebackground="#1B8A83")
    six.grid(row=2, column=2, sticky="nswe")

    # 3 row
    seven = tk.Button(btn_frame, text="7", font="Arial 20", border=0, padx=15, command=lambda: handle_click("7"), bg="#4ECDC4", activebackground="#1B8A83")
    seven.grid(row=1, column=0, sticky="nswe")

    eight = tk.Button(btn_frame, text="8", font="Arial 20", border=0, padx=15, command=lambda: handle_click("8"), bg="#4ECDC4", activebackground="#1B8A83")
    eight.grid(row=1, column=1, sticky="nswe")

    nine = tk.Button(btn_frame, text="9", font="Arial 20", border=0, padx=15, command=lambda: handle_click("9"), bg="#4ECDC4", activebackground="#1B8A83")
    nine.grid(row=1, column=2, sticky="nswe")

    #zero
    zero = tk.Button(btn_frame, text="0", font="Arial 20", border=0, padx=15, command=lambda: handle_click("0"), bg="#4ECDC4", activebackground="#1B8A83")
    zero.grid(row=4, columnspan=2, sticky="nswe")

    dot = tk.Button(btn_frame, text=".", font="Arial 20", border=0, padx=15, command=lambda: handle_click("."), bg="#4ECDC4", activebackground="#1B8A83")
    dot.grid(row=4, column=2, sticky="nswe")

    equals = tk.Button(btn_frame, text="=", font="Arial 20", border=0, padx=15, bg="#4ECDC4", activebackground="#1B8A83")
    equals.grid(row=3, rowspan=2, column=3, sticky="nswe")

    plus = tk.Button(btn_frame, text="+", font="Arial 20", border=0, padx=15, command=lambda: handle_click("+"), bg="#4ECDC4", activebackground="#1B8A83")
    plus.grid(row=1, rowspan=2, column=3, sticky="nswe")

    minus = tk.Button(btn_frame, text="-", font="Arial 20", border=0, padx=15, command=lambda: handle_click("-"), bg="#4ECDC4", activebackground="#1B8A83")
    minus.grid(row=0, column=3, sticky="nswe")

    mupltiply = tk.Button(btn_frame, text="*", font="Arial 20", border=0, padx=15, command=lambda: handle_click("*"), bg="#4ECDC4", activebackground="#1B8A83")
    mupltiply.grid(row=0, column=2, sticky="nswe")

    divide = tk.Button(btn_frame, text="/", font="Arial 20", border=0, padx=15, command=lambda: handle_click("/"), bg="#4ECDC4", activebackground="#1B8A83")
    divide.grid(row=0, column=1, sticky="nswe")

    clear = tk.Button(btn_frame, text="C", font="Arial 20", border=0, padx=15, bg="#4ECDC4", activebackground="#1B8A83")
    clear.grid(row=0, column=0)

    okno.mainloop()


if __name__ == "__main__":
    main()
