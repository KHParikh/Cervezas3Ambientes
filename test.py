# import sqlite3

# conn = sqlite3.connect("test.db")

# cursor = conn.cursor()

# cursor.execute("select * from IDsyVasitos where ID=:id", {"id": 2})

# # results = cursor.fetchall()

# # print(results[0][2])

# # import tkinter as tk
# # def whenpressed():
# #     print(int(entry.get()))
# # root = tk.Tk()
# # entry = tk.Entry(root)
# # entry.pack()
# # button = tk.Button(root, 
# #                    text = "pressme",
# #                    command = whenpressed)
# # button.pack()
# # root.mainloop()

# import sqlite3

# # conn = sqlite3.connect("Cervezas3Ambientes.db")
# # cur = conn.cursor()
# # cur.execute("""INSERT INTO Datos (Nombre, ID, Ambiente, Datos1, Datos2, Datos3, Datos4, Datos5, Datos6) VALUES ("Hello", 1, "Calido", 2, 3, 4, 5, 6, 7)""")
# # conn.commit()
# # conn.close()


# # try:
# #     sqliteConnection = sqlite3.connect('Cervezas3Ambientes.db')
# #     cursor = sqliteConnection.cursor()
# #     print("Successfully Connected to SQLite")

# #     count = cursor.execute("""INSERT INTO Datos
# #                           (Nombre, ID, Ambiente, Datos1, Datos2, Datos3, Datos4, Datos5, Datos6)
# #                            VALUES 
# #                            (?, ?, ?, ?, ?, ?, ?, ?, ?)""", ("Khushi", 1, "Calido", 2, 3, 4, 5, 6, 7))
# #     sqliteConnection.commit()
# #     print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
# #     cursor.close()

# # except sqlite3.Error as error:
# #     print("Failed to insert data into sqlite table", error)
# # finally:
# #     if sqliteConnection:
# #         sqliteConnection.close()
# #         print("The SQLite connection is closed")
    
# from tkinter import *
# from tkinter import font

# root = Tk()
# root.title('Font Families')
# fonts=list(font.families())
# fonts.sort()

# def populate(frame):
#     '''Put in the fonts'''
#     listnumber = 1
#     for item in fonts:
#         label = "listlabel" + str(listnumber)
#         label = Label(frame,text=item,font=(item, 16)).pack()
#         listnumber += 1

# def onFrameConfigure(canvas):
#     '''Reset the scroll region to encompass the inner frame'''
#     canvas.configure(scrollregion=canvas.bbox("all"))

# canvas = Canvas(root, borderwidth=0, background="#ffffff")
# frame = Frame(canvas, background="#ffffff")
# vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
# canvas.configure(yscrollcommand=vsb.set)

# vsb.pack(side="right", fill="y")
# canvas.pack(side="left", fill="both", expand=True)
# canvas.create_window((4,4), window=frame, anchor="nw")

# frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

# populate(frame)

# root.mainloop()

import json
import time
from urllib.request import urlopen
url = "http://localhost:22004/NeuLogAPI?GetSensorValue:[Pulse],[1],[GSR],[1]" 
pulse = []
gsr = []

print("hello")

start_time = time.time()

while time.time()<(start_time+30):
    response = urlopen(url)
    data_json = json.loads(response.read())
    pulse.append(data_json["GetSensorValue"][0])
    gsr.append(data_json["GetSensorValue"][1])
    print([pulse, gsr])

print(len(pulse), len(gsr))