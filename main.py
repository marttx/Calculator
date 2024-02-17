import tkinter as tk
def a(value):
    global otvet
    if value=="=":
        try: 
            analiz=str(eval(otvet))
            okno.delete(0, tk.END)
            okno.insert(tk.END, analiz)
            otvet=analiz
        except Exception as e:
             okno.delete(0, tk.END)
             okno.insert(tk.END, "ERROR")
             otvet=""
    else:
        otvet+=value
        okno.insert(tk.END, value)

def trush():
    global otvet
    global vivod
    otvet=""
    okno.delete(0, tk.END)
    vivod=""
    
win=tk.Tk()
win.geometry("320x690")
win.title("Калькулятор")
win.config(bg="Gainsboro")
vid=tk.Frame(win)
vid.grid(row=0, column=0, columnspan=4, sticky="nsew")
okno=tk.Entry(vid, width=50, bg="DimGrey")
okno.bind("<Key>", lambda e:"break")
okno.pack()
car = (
    ('7', '8', '9', '*', '4'),
    ('4', '5', '6', '-', '4'),
    ('1', '2', '3', '+', '4'),
    ('0', '.', '=', '/', '4')
)
otvet=""
vivod=""
dell=tk.Button(win, text="C", command=trush)
dell.grid(row=1, column=3, sticky="nsew")
for i in range(4):
    for j in  range(5):
        if car[i][j]=="=":
            tk.Button(win, width=10, height=10, text=car[i][j], 
command=lambda value=car[i][j]:a(value)).grid(row=i+2, column=j, 
sticky="nsew", padx=1, pady=1)
        else:
            tk.Button(win, width=10, height=10, text=car[i][j], 
command=lambda value=car[i][j]:a(value)).grid(row=i+2, column=j, 
sticky="nsew", padx=1, pady=1)

win.mainloop()
