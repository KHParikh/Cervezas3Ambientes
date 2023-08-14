import tkinter as tk
from PIL import Image, ImageTk
import sqlite3
from urllib.request import urlopen
import json
import time
import threading
from tkinter import messagebox
from datetime import datetime

start_time = 0
vasito1_datos = 0
vasito1_datos2 = 0
vasito2_datos = 0
vasito2_datos2 = 0
vasito3_datos = 0
vasito3_datos2 = 0
vasito4_datos = 0
vasito4_datos2 = 0
vasito5_datos = 0
vasito5_datos2 = 0
vasito6_datos = 0
vasito6_datos2 = 0
ambiente = ""
state = 0
font_size = 10
pulse = []
gsr = []
today_date = ""
today_time = ""

def collect_data():
    url = "http://localhost:22004/NeuLogAPI?GetSensorValue:[Pulse],[1],[GSR],[1]"
    global pulse
    global gsr

    while state != 1:
        response = urlopen(url)
        data_json = json.loads(response.read())
        pulse.append(data_json["GetSensorValue"][0])
        gsr.append(data_json["GetSensorValue"][1])
        print([pulse, gsr])
    
def emp():
    global ambiente
    global start_time
    global today_date
    global today_time
    today_date = str(datetime.date(datetime.now()))
    today_time = str(datetime.time(datetime.now()))
    start_time = time.time()
    threading.Thread(target = collect_data).start()
    print(start_time)
    id_number = int(id.get())
    conn = sqlite3.connect("Cervezas3Ambientes.db")
    cursor = conn.cursor()
    if varc.get()+varf.get()+varn.get() > 1:
        messagebox.showerror("Hay mas de 1 ambiente seleccionado", "Por favor selecciona SOLO UN ambiente")
    elif varc.get()+varf.get()+varn.get() == 0:
        messagebox.showerror("No hay amb#f7b962iente seleccionado", "Por favor selecciona un ambiente")
    elif varc.get() == 1:
        empezar.configure(bg = "#F77F4A")
        ambiente = "calido"
        cursor.execute("select * from Calido where ID=:id", {"id": id_number})
        results = cursor.fetchall()
        vasito1.configure(text = str(results[0][1]))
        vasito2.configure(text = str(results[0][2]))
        vasito3.configure(text = str(results[0][3]))
        vasito4.configure(text = str(results[0][4]))
        vasito5.configure(text = str(results[0][5]))
        vasito6.configure(text = str(results[0][6]))
    elif varf.get() == 1:
        empezar.configure(bg = "#52B2B0") 
        ambiente = "frio"
        cursor.execute("select * from Frio where ID=:id", {"id": id_number})
        results = cursor.fetchall()
        vasito1.configure(text = str(results[0][1]))
        vasito2.configure(text = str(results[0][2]))
        vasito3.configure(text = str(results[0][3]))
        vasito4.configure(text = str(results[0][4]))
        vasito5.configure(text = str(results[0][5]))
        vasito6.configure(text = str(results[0][6]))
    elif varn.get() == 1:
        empezar.configure(bg = "#F7B962")
        ambiente = "neutral"
        cursor.execute("select * from Neutral where ID=:id", {"id": id_number})
        results = cursor.fetchall()
        vasito1.configure(text = str(results[0][1]))
        vasito2.configure(text = str(results[0][2]))
        vasito3.configure(text = str(results[0][3]))
        vasito4.configure(text = str(results[0][4]))
        vasito5.configure(text = str(results[0][5]))
        vasito6.configure(text = str(results[0][6]))

def d1():
    global vasito1_datos
    vasito1_datos = int(time.time()-start_time)
    datos1.configure(bg = "#ACCF69")

def d12():
    global vasito1_datos2
    vasito1_datos2 = int(time.time()-start_time)
    datos12.configure(bg = "#ACCF69")

def d2():
    global vasito2_datos
    vasito2_datos = int(time.time()-start_time)
    datos2.configure(bg = "#ACCF69")

def d22():
    global vasito2_datos2
    vasito2_datos2 = int(time.time()-start_time)
    datos22.configure(bg = "#ACCF69")

def d3():
    global vasito3_datos
    vasito3_datos = int(time.time()-start_time)
    datos3.configure(bg = "#ACCF69")

def d32():
    global vasito3_datos2
    vasito3_datos2 = int(time.time()-start_time)
    datos32.configure(bg = "#ACCF69")

def d4():
    global vasito4_datos
    vasito4_datos = int(time.time()-start_time)
    datos4.configure(bg = "#ACCF69")

def d42():
    global vasito4_datos2
    vasito4_datos2 = int(time.time()-start_time)
    datos42.configure(bg = "#ACCF69")

def d5():
    global vasito5_datos
    vasito5_datos = int(time.time()-start_time)
    datos5.configure(bg = "#ACCF69")

def d52():
    global vasito5_datos2
    vasito5_datos2 = int(time.time()-start_time)
    datos52.configure(bg = "#ACCF69")

def d6():
    global vasito6_datos
    vasito6_datos = int(time.time()-start_time)
    datos6.configure(bg = "#ACCF69")

def d62():
    global vasito6_datos2
    vasito6_datos2 = int(time.time()-start_time)
    datos62.configure(bg = "#ACCF69")

def re():
    global state
    global pulse_repr
    global gsr_repr
    state = 1
    print("hello")
    print(repr(pulse), repr(gsr))
    print("goodbye")
    conn = sqlite3.connect("Cervezas3Ambientes.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO Datos (Fecha, Hora, Nombre, ID, Ambiente, Datos1, Datos12, Datos2, Datos22, Datos3, Datos32, Datos4, Datos42, Datos5, Datos52, Datos6, Datos62, Pulse, GSR) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                (today_date, today_time, str(nombre.get()), int(id.get()), ambiente, vasito1_datos, vasito1_datos2, vasito2_datos, vasito2_datos2, vasito3_datos, vasito3_datos2, vasito4_datos, vasito4_datos2, vasito5_datos, vasito5_datos2, vasito6_datos, vasito6_datos2, repr(pulse), repr(gsr)))
    conn.commit()
    cur.close()
    vasito1.configure(text = "")
    vasito2.configure(text = "")
    vasito3.configure(text = "")
    vasito4.configure(text = "")
    vasito5.configure(text = "")
    vasito6.configure(text = "")
    datos1.configure(bg = "#F3443F")
    datos2.configure(bg = "#F3443F")
    datos3.configure(bg = "#F3443F")
    datos4.configure(bg = "#F3443F")
    datos5.configure(bg = "#F3443F")
    datos6.configure(bg = "#F3443F")
    datos12.configure(bg = "#F3443F")
    datos22.configure(bg = "#F3443F")
    datos32.configure(bg = "#F3443F")
    datos42.configure(bg = "#F3443F")
    datos52.configure(bg = "#F3443F")
    datos62.configure(bg = "#F3443F")
    empezar.configure(bg = "#ACCF69")
    nombre.delete(0, len(str(nombre.get())))
    id.delete(0, len(str(id.get())))

root = tk.Tk()
root.title("Cerveza 3 Ambientes")

frame1 = tk.Frame(root, width=600)
frame1.pack()

tk.Label(frame1, 
         text = "Ingrese el nombre del particpante:", 
         font = ('Segoe UI', font_size)).grid(row = 0, column = 0, sticky="W")

tk.Label(frame1,
         text = "Ingrese la ID del participante:",
         font = ('Segoe UI', font_size)).grid(row = 1, column = 0, sticky="W")

tk.Label(frame1,
         text = "Selecciona el ambiente:",
         font = ('Segoe UI', font_size)).grid(row = 2, column = 0, sticky="W")

nombre = tk.Entry(frame1,
                  font = ('Segoe UI', font_size), 
                  relief= 'sunken',
                  bg = "#D9D9D9",
                  fg = 'black')
nombre.grid(row = 0, column = 1, sticky="W")

id = tk.Entry(frame1,
              font = ('Segoe UI', font_size), 
              relief= 'sunken',
              width = 3,
              bg = "#D9D9D9",
              fg = 'black')
id.grid(row = 1, column = 1, sticky="W")

frame2 = tk.Frame(root, width=600)
frame2.pack()

calido = ImageTk.PhotoImage(Image.open("Calido.png"))
varc = tk.IntVar()
tk.Checkbutton(frame2, 
               image = calido,
               variable = varc).grid(row = 0, column = 1)

frio = ImageTk.PhotoImage(Image.open("Frio.png"))
varf = tk.IntVar()
tk.Checkbutton(frame2, 
               image = frio,
               variable = varf).grid(row = 0, column = 2)

neutral = ImageTk.PhotoImage(Image.open("Neutral.png"))
varn = tk.IntVar()
tk.Checkbutton(frame2, 
               image = neutral,
               variable = varn).grid(row = 0, column = 0)

tk.Label(frame2,
         text = "Calido",
         font = ('Segoe UI', font_size)).grid(row = 1, column = 1)

tk.Label(frame2,
         text = "Frio",
         font = ('Segoe UI', font_size)).grid(row = 1, column = 2)

tk.Label(frame2,
         text = "Neutral",
         font = ('Segoe UI', font_size)).grid(row = 1, column = 0)

empezar = tk.Button(frame2,
                    text = "Empezar",
                    font = ('Segoe UI', font_size),
                    relief = "raised",
                    bg = "#ACCF69",
                    command = emp)
empezar.grid(row = 2, column = 1)

n = 3

tk.Label(frame2,
         text = "Muestra 1",
         font = ('Segoe UI', font_size)).grid(row = n+0, column = 0)

tk.Label(frame2,
         text = "Muestra 2",
         font = ('Segoe UI', font_size)).grid(row = n+2, column = 0)

tk.Label(frame2,
         text = "Muestra 3",
         font = ('Segoe UI', font_size)).grid(row = n+4, column = 0)

tk.Label(frame2,
         text = "Muestra 4",
         font = ('Segoe UI', font_size)).grid(row = n+6, column = 0)

tk.Label(frame2,
         text = "Muestra 5",
         font = ('Segoe UI', font_size)).grid(row = n+8, column = 0)

tk.Label(frame2,
         text = "Muestra 6",
         font = ('Segoe UI', font_size)).grid(row = n+10, column = 0)

tk.Label(frame2,
         text = "Numero del vasito:",
         font = ('Segoe UI', font_size)).grid(row = n+0, column = 1)

tk.Label(frame2,
         text = "Numero del vasito:",
         font = ('Segoe UI', font_size)).grid(row = n+2, column = 1)

tk.Label(frame2,
         text = "Numero del vasito:",
         font = ('Segoe UI', font_size)).grid(row = n+4, column = 1)

tk.Label(frame2,
         text = "Numero del vasito:",
         font = ('Segoe UI', font_size)).grid(row = n+6, column = 1)

tk.Label(frame2,
         text = "Numero del vasito:",
         font = ('Segoe UI', font_size)).grid(row = n+8, column = 1)

tk.Label(frame2,
         text = "Numero del vasito:",
         font = ('Segoe UI', font_size)).grid(row = n+10, column = 1)

vasito1 = tk.Label(frame2,
                  font = ('Segoe UI', font_size), 
                  relief = 'sunken',
                  width = 3)
vasito1.grid(row = n+1, column = 1)

vasito2 = tk.Label(frame2,
                  font = ('Segoe UI', font_size), 
                  relief = 'sunken',
                  width = 3)
vasito2.grid(row = n+3, column = 1)

vasito3 = tk.Label(frame2,
                  font = ('Segoe UI', font_size), 
                  relief = 'sunken',
                  width = 3)
vasito3.grid(row = n+5, column = 1)

vasito4 = tk.Label(frame2,
                  font = ('Segoe UI', font_size), 
                  relief = 'sunken',
                  width = 3)
vasito4.grid(row = n+7, column = 1)

vasito5 = tk.Label(frame2,
                  font = ('Segoe UI', font_size), 
                  relief = 'sunken',
                  width = 3)
vasito5.grid(row = n+9, column = 1)

vasito6 = tk.Label(frame2,
                  font = ('Segoe UI', font_size), 
                  relief = 'sunken',
                  width = 3)
vasito6.grid(row = n+11, column = 1)

datos1 = tk.Button(frame2,
           text = "Coleccionar Datos",
           font = ('Segoe UI', font_size),
           relief = "raised",
           bg = "#F3443F",
           command = d1)
datos1.grid(row = n+0, column = 2)

datos12 = tk.Button(frame2,
           text = "Acabar",
           font = ('Segoe UI', font_size),
           relief = "raised",
           bg = "#F3443F",
           command = d12)
datos12.grid(row = n+1, column = 2)

datos2 = tk.Button(frame2,
           text = "Coleccionar Datos",
           font = ('Segoe UI', font_size),
           relief = "raised",
           bg = "#F3443F",
           command = d2)
datos2.grid(row = n+2, column = 2)

datos22 = tk.Button(frame2,
           text = "Acabar",
           font = ('Segoe UI', font_size),
           relief = "raised",
           bg = "#F3443F",
           command = d22)
datos22.grid(row = n+3, column = 2)

datos3 = tk.Button(frame2,
           text = "Coleccionar Datos",
           font = ('Segoe UI', font_size),
           relief = "raised",
           bg = "#F3443F",
           command = d3)
datos3.grid(row = n+4, column = 2)

datos32 = tk.Button(frame2,
           text = "Acabar",
           font = ('Segoe UI', font_size),
           relief = "raised",
           bg = "#F3443F",
           command = d32)
datos32.grid(row = n+5, column = 2)

datos4 = tk.Button(frame2,
           text = "Coleccionar Datos",
           font = ('Segoe UI', font_size),
           relief = "raised",
           bg = "#F3443F",
           command = d4)
datos4.grid(row = n+6, column = 2)

datos42 = tk.Button(frame2,
           text = "Acabar",
           font = ('Segoe UI', font_size),
           relief = "raised",
           bg = "#F3443F",
           command = d42)
datos42.grid(row = n+7, column = 2)

datos5 = tk.Button(frame2,
           text = "Coleccionar Datos",
           font = ('Segoe UI', font_size),
           relief = "raised",
           bg = "#F3443F",
           command = d5)
datos5.grid(row = n+8, column = 2)

datos52 = tk.Button(frame2,
           text = "Acabar",
           font = ('Segoe UI', font_size),
           relief = "raised",
           bg = "#F3443F",
           command = d52)
datos52.grid(row = n+9, column = 2)

datos6 = tk.Button(frame2,
           text = "Coleccionar Datos",
           font = ('Segoe UI', font_size),
           relief = "raised",
           bg = "#F3443F",
           command = d6)
datos6.grid(row = n+10, column = 2)

datos62 = tk.Button(frame2,
           text = "Acabar",
           font = ('Segoe UI', font_size),
           relief = "raised",
           bg = "#F3443F",
           command = d62)
datos62.grid(row = n+11, column = 2)

reiniciar = tk.Button(frame2,
                     text = "Reiniciar",
                     font = ('Segoe UI', font_size),
                     relief = "raised",
                     bg = "#ACCF69",
                     command = re)
reiniciar.grid(row = n+12, column = 1)

root.mainloop()