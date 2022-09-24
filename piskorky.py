import tkinter,random
platno = tkinter.Canvas(bg="white",width = 250,height = 250)
platno.pack()

tab = []
def tabulka():
    global tab
    platno.delete("all")
    tab.clear()
    x,y = 0,0
    for i in range(3):
        tab.append([])
        for j in range(3):
            tab[i].append(0)
            platno.create_rectangle(x,y,x+50,y+50)
            x+=50
        x = 0
        y+= 50
tabulka()
def osetrenie(n):
    ide = False
    vyhral = False
    for i in range(len(tab)):
        ide = True
        for j in range(len(tab[i])):
            if tab[i][j] !=n:
                ide = False
        if ide:  
            return ide
        ide = True
        for j in range(len(tab[i])):
            if tab[j][i] !=n:
                ide = False
        if ide:  
            return ide
        ide = True
        for j in range(len(tab[i])):
            if tab[j][j] !=n:
                ide = False
        if ide:  
            return ide
        ide = True
        pocet = len(tab[i])-1
        for j in range(len(tab[i])):
            if tab[j][pocet] != n:
                ide = False
            pocet -=1
        if ide:  
            return ide
        
                    
                
def krizik(sur):
    global tab
    if tab[sur.y//50][sur.x//50]==2:
        print("Miesto je zabraté")
    else:
        tab[sur.y//50][sur.x//50]=1
        x,y = (sur.x//50)*50, (sur.y//50)*50
        platno.create_line(x,y,x+50,y+50)
        platno.create_line(x,y+50,x+50,y)
    print(osetrenie(1))

def kruh(sur):
    global tab
    if tab[sur.y//50][sur.x//50]==1:
        print("Miesto je zabraté")
    else:
        tab[sur.y//50][sur.x//50]=2
        x,y = (sur.x//50)*50,(sur.y//50)*50
        platno.create_oval(x,y,x+50,y+50)
        

b1 = tkinter.Button(text ="nova",command = tabulka)
b1.pack()

platno.bind("<Button-1>",krizik)
platno.bind("<Button-3>",kruh)
