import turtle as t #importa la funzione turtle
import random
t.bgcolor('#FFFFFF') #imposta un colore
t.title("Tic Tac Toe") #imposta un titolo
#definiscono le 9 celle della tabella di gioco
char1 = t.Turtle()
char2 = t.Turtle()
char3 = t.Turtle()
char4 = t.Turtle()
char5 = t.Turtle()
char6 = t.Turtle()
char7 = t.Turtle()
char8 = t.Turtle()
char9 = t.Turtle()
#si implementa una funzione per ogni quadretto della tabella

#funzione per la cella 1
def show1():
    #dichiarazione variabili starter e enimy
    global starter, enimy
    if starter == "player":
        #viene stabilito che O è il giocatore e X è il nemico
        char1.hideturtle()
        #viene scritto O nella cella
        char1.write("O", font=("CHALKDUSTER", 128))
        box1 = 'o'
        #viene rimossa la possibilità al "nemico" di far 
        #apparire X se la cella 1 è già occupata da O
        starter = "enemy"
        enimy.remove(char1)
        enem()

#funzione per la cella 2
def show2():
    #dichiarazione variabili starter e enimy
    global starter, enimy
    if starter == "player":
        #viene stabilito che O è il giocatore e X è il nemico
        char2.hideturtle()
        #viene scritto O nella cella
        char2.write("O", font=("CHALKDUSTER", 128))
        box2 = 'o'
        #viene rimossa la possibilità al "nemico" di far 
        #apparire X se la cella 2 è già occupata da O
        starter = "enemy"
        enem()
        enimy.remove(char2)

#funzione per la cella 3
def show3():
    #dichiarazione variabili starter e enimy
    global starter, enimy
    if starter == "player":
        #viene stabilito che O è il giocatore e X è il nemico
        char3.hideturtle()
        #viene scritto O nella cella
        char3.write("O", font=("CHALKDUSTER", 128))
        box3 = 'o'
        #viene rimossa la possibilità al "nemico" di far 
        #apparire X se la cella 3 è già occupata da O
        starter = "enemy"
        enimy.remove(char3)
        enem()

#funzione per la cella 4
def show4():
    #dichiarazione variabili starter e enimy
    global starter, enimy
    if starter == "player":
        #viene stabilito che O è il giocatore e X è il nemico
        char4.hideturtle()
        #viene scritto O nella cella
        char4.write("O", font=("CHALKDUSTER", 128))
        box4 = 'o'
        #viene rimossa la possibilità al "nemico" di far 
        #apparire X se la cella 4 è già occupata da O
        starter = "enemy"
        enimy.remove(char4)
        enem()

#funzione per la cella 5
def show5():
    #dichiarazione variabili starter e enimy
    global starter, enimy
    if starter == "player":
        #viene stabilito che O è il giocatore e X è il nemico
        char5.hideturtle()
        #viene scritto O nella cella
        char5.write("O", font=("CHALKDUSTER", 128))
        box5 = 'o'
        #viene rimossa la possibilità al "nemico" di far 
        #apparire X se la cella 5 è già occupata da O
        starter = "enemy"
        enimy.remove(char5)
        enem()

#funzione per la cella 6
def show6():
    #dichiarazione variabili starter e enimy
    global starter, enimy
    if starter == "player":
        #viene stabilito che O è il giocatore e X è il nemico
        char6.hideturtle()
        #viene scritto O nella cella
        char6.write("O", font=("CHALKDUSTER", 128))
        box6 = 'o'
        #viene rimossa la possibilità al "nemico" di far 
        #apparire X se la cella 6 è già occupata da O
        starter = "enemy"
        enimy.remove(char6)
        enem()

#funzione per la cella 7
def show7():
    #dichiarazione variabili starter e enimy
    global starter, enimy
    if starter == "player":
        #viene stabilito che O è il giocatore e X è il nemico
        char7.hideturtle()
        #viene scritto O nella cella
        char7.write("O", font=("CHALKDUSTER", 128))
        box7 = 'o'
        #viene rimossa la possibilità al "nemico" di far 
        #apparire X se la cella 7 è già occupata da O
        starter = "enemy"
        enimy.remove(char7)
        enem()

#funzione per la cella 8
def show8():
    #dichiarazione variabili starter e enimy
    global starter, enimy
    if starter == "player":
        #viene stabilito che O è il giocatore e X è il nemico
        char8.hideturtle()
        #viene scritto O nella cella
        char8.write("O", font=("CHALKDUSTER", 128))
        box8 = 'o'
        #viene rimossa la possibilità al "nemico" di far 
        #apparire X se la cella 8 è già occupata da O
        starter = "enemy"
        enimy.remove(char8)
        enem()

#funzione per la cella 9
def show9():
    #dichiarazione variabili starter e enimy
    global starter, enimy
    if starter == "player":
        #viene stabilito che O è il giocatore e X è il nemico
        char9.hideturtle()
        #viene scritto O nella cella
        char9.write("O", font=("CHALKDUSTER", 128))
        box9 = 'o'
        #viene rimossa la possibilità al "nemico" di far 
        #apparire X se la cella 9 è già occupata da O
        starter = "enemy"
        enimy.remove(char9)
        enem()
def enem():
    #dichiarazione variabile enimy
    global enimy
    #viene stabilito che X deve apparire in una casella scelta a caso
    enemy = random.choice(enimy)
    
    #funzione per scrivere nella cella 1
    if enemy == char1:
        char1.hideturtle()
        #viene scritto X nella cella 1
        char1.write("X", font=("CHALKDUSTER", 128))
        box1 = 'x'
        #viene rimossa la possibilità di far 
        #apparire X o O perchè questa cella è già occupata
        enimy.remove(char1)
        #tocca all'altro giocatore
        starter = "player"
        loopy()

    #funzione per scrivere nella cella 2
    if enemy == char2:
        char2.hideturtle()
        #viene scritto X nella cella 2
        char2.write("X", font=("CHALKDUSTER", 128))
        box2 = 'x'
        #viene rimossa la possibilità di far 
        #apparire X o O perchè questa cella è già occupata
        enimy.remove(char2)
        #tocca all'altro giocatore
        starter = "player"
        loopy()

    #funzione per scrivere nella cella 3
    if enemy == char3:
        char3.hideturtle()
        #viene scritto X nella cella 3
        char3.write("X", font=("CHALKDUSTER", 128))
        box3 = 'x'
        #viene rimossa la possibilità di far 
        #apparire X o O perchè questa cella è già occupata
        enimy.remove(char3)
        #tocca all'altro giocatore
        starter = "player"
        loopy()

    #funzione per scrivere nella cella 4
    if enemy == char4:
        char4.hideturtle()
        #viene scritto X nella cella 4
        char4.write("X", font=("CHALKDUSTER", 128))
        box4 = 'x'
        #viene rimossa la possibilità di far 
        #apparire X o O perchè questa cella è già occupata
        enimy.remove(char4)
        #tocca all'altro giocatore
        starter = "player"
        loopy()

    #funzione per scrivere nella cella 5
    if enemy == char5:
        char5.hideturtle()
        #viene scritto X nella cella 5
        char5.write("X", font=("CHALKDUSTER", 128))
        box5 = 'x'
        #viene rimossa la possibilità di far 
        #apparire X o O perchè questa cella è già occupata
        enimy.remove(char5)
        #tocca all'altro giocatore
        starter = "player"
        loopy()

    #funzione per scrivere nella cella 6
    if enemy == char6:
        char6.hideturtle()
        #viene scritto X nella cella 6
        char6.write("X", font=("CHALKDUSTER", 128))
        box6 = 'x'
        #viene rimossa la possibilità di far 
        #apparire X o O perchè questa cella è già occupata
        enimy.remove(char6)
        #tocca all'altro giocatore
        starter = "player"
        loopy()

    #funzione per scrivere nella cella 7
    if enemy == char7:
        char7.hideturtle()
        #viene scritto X nella cella 7
        char7.write("X", font=("CHALKDUSTER", 128))
        box7 = 'x'
        #viene rimossa la possibilità di far 
        #apparire X o O perchè questa cella è già occupata
        enimy.remove(char7)
        #tocca all'altro giocatore
        starter = "player"
        loopy()

    #funzione per scrivere nella cella 8
    if enemy == char8:
        char8.hideturtle()
        #viene scritto X nella cella 8
        char8.write("X", font=("CHALKDUSTER", 128))
        box8 = 'x'
        #viene rimossa la possibilità di far 
        #apparire X o O perchè questa cella è già occupata
        enimy.remove(char8)
        #tocca all'altro giocatore
        starter = "player"
        loopy()

    #funzione per scrivere nella cella 9
    if enemy == char9:
        char9.hideturtle()
        #viene scritto X nella cella 9
        char9.write("X", font=("CHALKDUSTER", 128))
        box9 = 'x'
        #viene rimossa la possibilità di far 
        #apparire X o O perchè questa cella è già occupata
        enimy.remove(char9)
        #tocca all'altro giocatore
        starter = "player"
        loopy()
def loopy():
    #dichiarazione variabile starter
    global starter
    #se inizia enemy poi toccherà a player (il giocatore)
    if starter == "enemy":
        starter = "player"
#qui viene implementata la "grafica" del videogioco, 
#l'apparizione del linee della tabella, i colori e la loro posizione

#impostazioni linea 1
line1 = t.Turtle()
line1.hideturtle()
#viene deciso il colore della linea
line1.color("#AAAAAA")
line1.penup()
#punto di origine della linea (x e y)
line1.setx(-100)
line1.sety(200)
#movimento della riga
line1.pendown()
line1.right(90)
line1.forward(400)

#impostazioni linea 2
line2 = t.Turtle()
line2.hideturtle()
#viene deciso il colore della linea
line2.color("#AAAAAA")
line2.penup()
#punto di origine della linea (x e y)
line2.setx(100)
line2.sety(200)
#movimento della riga
line2.pendown()
line2.right(90)
line2.forward(400)

#impostazioni linea 3
line3 = t.Turtle()
line3.hideturtle()
#viene deciso il colore della linea
line3.color("#AAAAAA")
line3.penup()
#punto di origine della linea (x e y)
line3.setx(-200)
line3.sety(100)
#movimento della riga
line3.pendown()
line3.forward(400)

#impostazioni linea 4
line4 = t.Turtle()
line4.hideturtle()
#viene deciso il colore della linea
line4.color("#AAAAAA")
line4.penup()
#punto di origine della linea (x e y)
line4.setx(-200)
line4.sety(-100)
#movimento della riga
line4.pendown()
line4.forward(400)
#qui viene deciso dove far apparire X o O sullo schermo
#coordinate x e y per ogni cella (9)
char1.penup()
#coordinate x e y della cella 1
char1.sety(120)
char1.setx(120)

char2.penup()
#coordinate x e y della cella 2
char2.sety(120)
char2.setx(-25)

char3.penup()
#coordinate x e y della cella 3
char3.sety(120)
char3.setx(-200)

char4.penup()
#coordinate x e y della cella 4
char4.sety(-50)
char4.setx(-200)

char5.penup()
#coordinate x e y della cella 5
char5.sety(-50)
char5.setx(-25)

char6.penup()
#coordinate x e y della cella 6
char6.sety(-50)
char6.setx(120)

char7.penup()
#coordinate x e y della cella 7
char7.sety(-250)
char7.setx(-200)

char8.penup()
#coordinate x e y della cella 8
char8.sety(-250)
char8.setx(-25)

char9.penup()
#coordinate x e y della cella 9
char9.sety(-250)
char9.setx(150)

#viene creata la casella per inserire il carattere 
#una per ogni cella
box1 = ''
box2 = ''
box3 = ''
box4 = ''
box5 = ''
box6 = ''
box7 = ''
box8 = ''
box9 = ''

#per stabilire chi è il primo a giocare 
#viene utilizzata la funzione random
first = ['player', 'enemy']
#permette al "nemico" di inserire una X in una delle caselle
enimy = [char1,char2,char3,char4,char5,char6,char7,char8,char9]
starter = random.choice(first)
#Stampa sul terminale le istruzioni per giocare
print("COME GIOCARE:")
print("")
print("")
print("Per Inserire X : ")
print("in alto a sinistra premi q, in alto al centro w, in alto a destra e")
print("a sinistra premi a, al centro s, a destra d")
print("in basso a sinistra premi z, in basso al centro x, in basso a destra c")
#funzione in loop
loopy()
#per l'input di ogni casella 
#viene abbinato un tasto
t.onkey(show1, "e")
t.onkey(show2, "w")
t.onkey(show3, "q")
t.onkey(show4, "a")
t.onkey(show5, "s")
t.onkey(show6, "d")
t.onkey(show7, "z")
t.onkey(show8, "x")
t.onkey(show9, "c")
t.listen()
t.mainloop()