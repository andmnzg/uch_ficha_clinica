import tkinter as tk
import pandas as pd
from utils import *
from pathlib import Path

#############################################################################
# Variables Globales
#############################################################################
posicion_antecedentes = 1
posicion_medicamentos = 1
posicion_afamiliares = 1
posicion_hospitalizaciones = 1
posicion_cirugia = 1
posicion_diagnostico = 1
posicion_tratamiento = 1
default_bg = "light gray"
default_title_bg = "white"
default_title_font_size = "14"
#############################################################################

#############################################################################
# Definiciones
#############################################################################
master = tk.Tk()
master.geometry("1366x800")
master.title("Ficha Clínica")

menubar = tk.Menu(master)
master.config(menu=menubar)
menu_tab_1 = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Menu 1", menu=menu_tab_1)
#############################################################################

#############################################################################
# Botones
#############################################################################


def agregar_antecedentes():
    global posicion_antecedentes
    posicion_antecedentes += 1
    a1 = tk.Entry(master, bg=default_bg)
    a1.grid(row=6, column=posicion_antecedentes)


def agregar_medicamentos():
    global posicion_medicamentos
    posicion_medicamentos += 1
    a1 = tk.Entry(master, bg=default_bg)
    a1.grid(row=7, column=posicion_medicamentos)


def agregar_afamiliares():
    global posicion_afamiliares
    posicion_afamiliares += 1
    a1 = tk.Entry(master, bg=default_bg)
    a1.grid(row=12, column=posicion_afamiliares)


def agregar_hospitalizaciones():
    global posicion_hospitalizaciones
    posicion_hospitalizaciones += 1
    a1 = tk.Entry(master, bg=default_bg)
    a1.grid(row=13, column=posicion_hospitalizaciones)


def agregar_cirugia():
    global posicion_cirugia
    posicion_cirugia += 1
    a1 = tk.Entry(master, bg=default_bg)
    a1.grid(row=14, column=posicion_cirugia)


def agregar_diagnostico():
    global posicion_diagnostico
    posicion_diagnostico += 1
    a1 = tk.Entry(master, bg=default_bg)
    a1.grid(row=25, column=posicion_diagnostico)


def agregar_tratamiento():
    global posicion_tratamiento
    posicion_tratamiento += 1
    a1 = tk.Entry(master, bg=default_bg)
    a1.grid(row=26, column=posicion_tratamiento)


#############################################################################

#############################################################################
# Antecedentes
#############################################################################
antecedentes = tk.Label(
    master, text="Antecedentes", font=default_title_font_size, bg=default_title_bg
)
antecedentes.grid(row=0, columnspan=2)

tk.Label(master, text="Nombre").grid(row=1, column=0)
nombre = tk.Entry(master, bg=default_bg)
nombre.grid(row=1, column=1)

tk.Label(master, text="Edad").grid(row=2, column=0)
edad = tk.Entry(master, bg=default_bg)
edad.grid(row=2, column=1)

tk.Label(master, text="Previsión").grid(row=3, column=0)
prevision = tk.Entry(master, bg=default_bg)
prevision.grid(row=3, column=1)

tk.Label(master, text="Educación").grid(row=4, column=0)
educacion = tk.Entry(master, bg=default_bg)
educacion.grid(row=4, column=1)

tk.Label(master, text="Ocupación").grid(row=5, column=0)
ocupacion = tk.Entry(master, bg=default_bg)
ocupacion.grid(row=5, column=1)

tk.Button(
    master,
    text="Antecedentes médicos",
    bg=default_bg,
    command=agregar_antecedentes,
).grid(row=6, column=0)
amedicos = tk.Entry(master, bg=default_bg)
amedicos.grid(row=6, column=1)

tk.Button(
    master,
    text="Medicamentos",
    bg=default_bg,
    command=agregar_medicamentos,
).grid(row=7, column=0)
medicamentos = tk.Entry(master, bg=default_bg)
medicamentos.grid(row=7, column=1)
#############################################################################

#############################################################################
# Anamnesis Próxima
#############################################################################
anamnesis_proxima = tk.Label(
    master, text="Anamnesis próxima", font=default_title_font_size, bg=default_title_bg
)
anamnesis_proxima.grid(row=8, columnspan=2)

tk.Label(master, text="Motivo consulta").grid(row=9, column=0)
motivo = tk.Text(master, width=20, height=3)
motivo.grid(row=9, column=1)


tk.Label(master, text="Anamnesis").grid(row=10, column=0)
anamnesis = tk.Text(master, width=20, height=3)
anamnesis.grid(row=10, column=1)
#############################################################################
# motivo = tk.Label(master, text="motivo de consulta")
# motivo.grid(row=9, column=0)
# anamnesis = tk.Label(master, text="anamnesis")
# anamnesis.grid(row=10, column=0)
# e8 = tk.Entry(master, bg="light gray")
# e8.grid(row=9, column=1)
# e9 = tk.Entry(master, bg="light gray", width=180)
# e9.place(x=135, y=225)

#############################################################################
# Anamnesis Remota
#############################################################################
anamnesis_remota = tk.Label(
    master, text="Anamnesis Remota", font=default_title_font_size, bg=default_title_bg
)
anamnesis_remota.grid(row=11, columnspan=2)

tk.Button(
    master,
    text="Antecedentes familiares",
    bg=default_bg,
    command=agregar_afamiliares,
).grid(row=12, column=0)
afamiliares = tk.Entry(master, bg=default_bg)
afamiliares.grid(row=12, column=1)

tk.Button(
    master,
    text="Hospitalizaciones",
    bg=default_bg,
    command=agregar_hospitalizaciones,
).grid(row=13, column=0)
hospital = tk.Entry(master, bg=default_bg)
hospital.grid(row=13, column=1)


tk.Button(
    master,
    text="Cirugías",
    bg=default_bg,
    command=agregar_cirugia,
).grid(row=14, column=0)
quirurgico = tk.Entry(master, bg=default_bg)
quirurgico.grid(row=14, column=1)

tk.Label(master, text="Tabaco").grid(row=15, column=0)
tabaco = tk.Entry(master, bg=default_bg)
tabaco.grid(row=15, column=1)

tk.Label(master, text="IPA").grid(row=15, column=3)
ipa = tk.Entry(master, bg=default_bg)
ipa.grid(row=15, column=4)

tk.Label(master, text="Tabaco").grid(row=16, column=0)
alcohol = tk.Entry(master, bg=default_bg)
alcohol.grid(row=16, column=1)

tk.Label(master, text="Tabaco").grid(row=17, column=0)
drogas = tk.Entry(master, bg=default_bg)
drogas.grid(row=17, column=1)


tk.Label(master, text="Alimentación").grid(row=18, column=0)
alimentacion = tk.Entry(master, bg=default_bg)
alimentacion.grid(row=18, column=1)

tk.Label(master, text="Actividad física").grid(row=19, column=0)
afisica = tk.Entry(master, bg=default_bg)
afisica.grid(row=19, column=1)

tk.Label(master, text="Defecatorio").grid(row=20, column=0)
defecacion = tk.Entry(master, bg=default_bg)
defecacion.grid(row=20, column=1)

tk.Label(master, text="Urinario").grid(row=21, column=0)
orina = tk.Entry(master, bg=default_bg)
orina.grid(row=21, column=1)

tk.Label(master, text="Sueño").grid(row=22, column=0)
dormir = tk.Entry(master, bg=default_bg)
dormir.grid(row=22, column=1)


tk.Label(master, text="Sexual").grid(row=23, column=0)
sexual = tk.Entry(master, bg=default_bg)
sexual.grid(row=23, column=1)
#############################################################################

#############################################################################
# Examen Físico
#############################################################################
examen_fisico = tk.Label(master, text="Exámen Físico")
examen_fisico.grid(row=24, column=0)
examenfisico= tk.Text(master, width=20, height=3)
examenfisico.grid(row=24, column=1)


tk.Button(
    master,
    text="Diagnóstico",
    bg=default_bg,
    command=agregar_diagnostico,
).grid(row=25, column=0)
diagnostico = tk.Entry(master, bg=default_bg)
diagnostico.grid(row=25, column=1)

tk.Button(
    master,
    text="Tratamiento",
    bg=default_bg,
    command=agregar_tratamiento,
).grid(row=26, column=0)
tratamiento = tk.Entry(master, bg=default_bg)
tratamiento.grid(row=26, column=1)


def read_data() -> pd.DataFrame:
    if Path("data.xlsx").exists():
        return pd.read_excel("data.xlsx")
    else:
        return pd.DataFrame(
            {
                "nombre": [],
                "edad": [],
                "prevision": [],
                "educacion": [],
                "ocupacion": [],
                # "Sexo": [],
                # "Fecha": [],
                # "Motivo": [],
                # "Anamnesis": [],
                # "Antecedentes familiares": [],
                # "Hospitalizaciones": [],
                # "Cirugías": [],
                # "Tabaco": [],
                # "IPA": [],
                # "Alcohol": [],
                # "Drogas": [],
                # "Alimentación": [],
                # "Actividad física": [],
                # "Defecatorio": [],
                # "Urinario": [],
                # "Sueño": [],
                # "Sexual": [],
                # "examenfisico": [],
                # "Diagnóstico": [],
                # "Tratamiento": [],
            }
        )


def get_input():
    df = read_data()

    data = [
        {
            "nombre": nombre.get(),
            "edad": edad.get(),
            "prevision": prevision.get(),
            "educacion": educacion.get(),
            "ocupacion": ocupacion.get(),
        }
    ]
    data = pd.DataFrame.from_records(data)

    df = pd.concat([df, data], axis=0)

    df.to_excel("data.xlsx", index=False)
    print(df)


guardar = tk.Button(master, text="Guardar", bg="light gray", command=get_input)
guardar.grid(row=27, columnspan=4)

master.mainloop()
