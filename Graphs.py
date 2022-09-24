import tkinter,random
platno = tkinter.Canvas(bg = "white",width = 800,height = 700)
platno.pack()

hodnoty = []
a = 20
b = 20

for i in range(30):
    c = random.randint(90,120)/100
    hodnoty.append(c)
    platno.create_text(a,b,anchor = "nw",text = c)
    b += 15
platno.create_line(75,75,275,275)
platno.create_line(275,275,475,275)

x,y = 75,65
ide = True
n = 0

def Chod():
    global x,y,ide,n
    platno.delete("gulocka")
    platno.create_oval(x,y,x+10,y+10,tag = "gulocka")
    if ide:
        x+= ((hodnoty[n]*1000)/400)*10
        y+= ((hodnoty[n]*1000)/400)*10
    else:
        x+= (hodnoty[n]*1000)/400
    if y >=265:
        ide = False
        y = 263
    if x >= 475:
        ide = True
        n+= 1
        if n == 29:
            n = 0
        x,y = 75,65
    platno.after(10,Chod)

def Evaluation ():
    l = int(edit1.get())
    Chod()
    p = 0
    for i in range(len(hodnoty)):
        if abs((hodnoty[i]/(l/100))-100) > 5:
            p+= 1
    avg = abs((((sum(hodnoty)/len(hodnoty)))/(l/100))-100)
    platno.create_text(100,350,text = f"Nameraná hodnota sa od predpokladanej odchýlila o viac ako 5% {p}-krát.",anchor="nw")
    platno.create_text(100,365,text = "Priemerná hodnota sa od predpokladanej odchýlila o {:.4f}%.".format(avg),anchor = "nw")
    platno.create_text(100,380,text = f"Najväčšia odchýlka predpokladanej hodnoty bola v meraní číslo  {hodnoty.index(max(hodnoty))+1} s hodnotou {max(hodnoty)}.",anchor="nw")

edit1 = tkinter.Entry()
edit1.pack()
b1 = tkinter.Button(text = "Nastav",command = Evaluation)
b1.pack()
        
