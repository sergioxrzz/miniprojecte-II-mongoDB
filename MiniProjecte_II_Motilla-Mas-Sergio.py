import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient

# Connecta a MongoDB
client = MongoClient('localhost', 27017) # Valors per defecte, canviar amb la IP que es necessite (si fora el cas) i el port si fora necessàri
db = client['alumnesSergio']

def guardar_inscripcio():

    # dades alumne
    dni = introduir_dni.get()
    nom = introduir_nom.get()
    edat = int(introduir_edat.get())

    # adreça alumne
    localitat = introduir_localitat.get()
    cp = int(introduir_cp.get())  # codi postal
    carrer = introduir_carrer.get()
    vivenda = int(introduir_vivenda.get())  # numero de la vivenda

    # dades cicle a inscriure
    cicle = introduir_cicle.get()
    curs = int(introduir_curs.get())

    # Validació de camps
    if (not nom or not edat or not dni) or (not localitat or not cp or not carrer or not vivenda) or (not cicle or not curs):
        messagebox.showerror("Error", "Per favor completa tots el camps.")
        return

    # Insertar informació a la base de dades
    alumnes_collection = db['alumnes']
    adreçes_collection = db['adreces']
    cicles_collection = db['cicles']

    # Inserta en "MongoDB collections"
    alumnes_collection.insert_one({"_id": dni, "nom": nom, "edat": edat})
    adreçes_collection.insert_one({"_id": cp, "localitat": localitat, "carrer": carrer, "vivenda": vivenda, "propietari": dni})
    cicles_collection.insert_one({"_id": cicle, "curs": curs, "alumne": dni})

    messagebox.showinfo("Inscripció correcta", f"¡{nom} ha sigut inscrit correctament!")


# Finestra principal
finestra = tk.Tk()
finestra.title("Inscripció d'Alumnes")

# Crear i posicionar elements en la app
dades_personals = tk.Label(finestra, text="DADES PERSONALS")
dades_personals.grid(row=0, column=0, columnspan=2)

dades_personals = tk.Label(finestra, text="VIVENDA")
dades_personals.grid(row=0, column=2, columnspan=2)

dades_personals = tk.Label(finestra, text="CICLE A INSCRIURE")
dades_personals.grid(row=0, column=4, columnspan=2)

etiqueta_dni = tk.Label(finestra, text="NIF/NIE:")
etiqueta_dni.grid(row=1, column=0)
introduir_dni = tk.Entry(finestra)
introduir_dni.grid(row=1, column=1)

etiqueta_nom = tk.Label(finestra, text="Nom:")
etiqueta_nom.grid(row=2, column=0)
introduir_nom = tk.Entry(finestra)
introduir_nom.grid(row=2, column=1)

etiqueta_edat = tk.Label(finestra, text="Edat:")
etiqueta_edat.grid(row=3, column=0)
introduir_edat = tk.Entry(finestra)
introduir_edat.grid(row=3, column=1)

# --------------------------------------------------------- ADREÇES

etiqueta_cp = tk.Label(finestra, text="Codi Postal:")
etiqueta_cp.grid(row=1, column=2)
introduir_cp = tk.Entry(finestra)
introduir_cp.grid(row=1, column=3)

etiqueta_localitat = tk.Label(finestra, text="Localitat:")
etiqueta_localitat.grid(row=2, column=2)
introduir_localitat = tk.Entry(finestra)
introduir_localitat.grid(row=2, column=3)

etiqueta_carrer = tk.Label(finestra, text="Carrer:")
etiqueta_carrer.grid(row=3, column=2)
introduir_carrer = tk.Entry(finestra)
introduir_carrer.grid(row=3, column=3)

etiqueta_vivenda = tk.Label(finestra, text="Nº Vivenda:")
etiqueta_vivenda.grid(row=4, column=2)
introduir_vivenda = tk.Entry(finestra)
introduir_vivenda.grid(row=4, column=3)

# --------------------------------------------------------- CICLES

etiqueta_cicle = tk.Label(finestra, text="Cicle:")
etiqueta_cicle.grid(row=1, column=4)
introduir_cicle = tk.Entry(finestra)
introduir_cicle.grid(row=1, column=5)

etiqueta_curs = tk.Label(finestra, text="Curs:")
etiqueta_curs.grid(row=2, column=4)
introduir_curs = tk.Entry(finestra)
introduir_curs.grid(row=2, column=5)

# --------------------------------------------------------- ALTRES ELEMENTS

boto_inscriure = tk.Button(finestra, text = "Inscriure", command = guardar_inscripcio)
boto_inscriure.grid(row=5, columnspan=6)

# Execució
finestra.mainloop()