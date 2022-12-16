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
max_agregar = 7
#############################################################################

#############################################################################
# Definiciones
#############################################################################
master = tk.Tk()
master.geometry("1366x800")
master.title("Ficha Clínica")

menubar = tk.Menu(master)
master.config(menu=menubar)

#############################################################################

#############################################################################
# Botones
#############################################################################

amedicos_1 = tk.Entry(master, bg=default_bg)
amedicos_2 = tk.Entry(master, bg=default_bg)
amedicos_3 = tk.Entry(master, bg=default_bg)
amedicos_4 = tk.Entry(master, bg=default_bg)
amedicos_5 = tk.Entry(master, bg=default_bg)
amedicos_6 = tk.Entry(master, bg=default_bg)
amedicos_7 = tk.Entry(master, bg=default_bg)

medicamentos_1 = tk.Entry(master, bg=default_bg)
medicamentos_2 = tk.Entry(master, bg=default_bg)
medicamentos_3 = tk.Entry(master, bg=default_bg)
medicamentos_4 = tk.Entry(master, bg=default_bg)
medicamentos_5 = tk.Entry(master, bg=default_bg)
medicamentos_6 = tk.Entry(master, bg=default_bg)
medicamentos_7 = tk.Entry(master, bg=default_bg)

afamiliares_1 = tk.Entry(master, bg=default_bg)
afamiliares_2 = tk.Entry(master, bg=default_bg)
afamiliares_3 = tk.Entry(master, bg=default_bg)
afamiliares_4 = tk.Entry(master, bg=default_bg)
afamiliares_5 = tk.Entry(master, bg=default_bg)
afamiliares_6 = tk.Entry(master, bg=default_bg)
afamiliares_7 = tk.Entry(master, bg=default_bg)

hospital_1 = tk.Entry(master, bg=default_bg)
hospital_2 = tk.Entry(master, bg=default_bg)
hospital_3 = tk.Entry(master, bg=default_bg)
hospital_4 = tk.Entry(master, bg=default_bg)
hospital_5 = tk.Entry(master, bg=default_bg)
hospital_6 = tk.Entry(master, bg=default_bg)
hospital_7 = tk.Entry(master, bg=default_bg)

quirurgico_1 = tk.Entry(master, bg=default_bg)
quirurgico_2 = tk.Entry(master, bg=default_bg)
quirurgico_3 = tk.Entry(master, bg=default_bg)
quirurgico_4 = tk.Entry(master, bg=default_bg)
quirurgico_5 = tk.Entry(master, bg=default_bg)
quirurgico_6 = tk.Entry(master, bg=default_bg)
quirurgico_7 = tk.Entry(master, bg=default_bg)


diagnostico_1 = tk.Entry(master, bg=default_bg)
diagnostico_2 = tk.Entry(master, bg=default_bg)
diagnostico_3 = tk.Entry(master, bg=default_bg)
diagnostico_4 = tk.Entry(master, bg=default_bg)
diagnostico_5 = tk.Entry(master, bg=default_bg)
diagnostico_6 = tk.Entry(master, bg=default_bg)
diagnostico_7 = tk.Entry(master, bg=default_bg)

tratamiento_1 = tk.Entry(master, bg=default_bg)
tratamiento_2 = tk.Entry(master, bg=default_bg)
tratamiento_3 = tk.Entry(master, bg=default_bg)
tratamiento_4 = tk.Entry(master, bg=default_bg)
tratamiento_5 = tk.Entry(master, bg=default_bg)
tratamiento_6 = tk.Entry(master, bg=default_bg)
tratamiento_7 = tk.Entry(master, bg=default_bg)


def agregar_antecedentes():
    row_number = 6
    global posicion_antecedentes
    if posicion_antecedentes < max_agregar:
        posicion_antecedentes += 1
    if posicion_antecedentes == 2:
        amedicos_2.grid(row=row_number, column=posicion_antecedentes)
    if posicion_antecedentes == 3:
        amedicos_3.grid(row=row_number, column=posicion_antecedentes)
    if posicion_antecedentes == 4:
        amedicos_4.grid(row=row_number, column=posicion_antecedentes)
    if posicion_antecedentes == 5:
        amedicos_5.grid(row=row_number, column=posicion_antecedentes)
    if posicion_antecedentes == 6:
        amedicos_6.grid(row=row_number, column=posicion_antecedentes)
    if posicion_antecedentes == 7:
        amedicos_7.grid(row=row_number, column=posicion_antecedentes)


def agregar_medicamentos():
    row_number = 7
    global posicion_medicamentos
    if posicion_medicamentos < max_agregar:
        posicion_medicamentos += 1
    if posicion_medicamentos == 2:
        medicamentos_2.grid(row=row_number, column=posicion_medicamentos)
    if posicion_medicamentos == 3:
        medicamentos_3.grid(row=row_number, column=posicion_medicamentos)
    if posicion_medicamentos == 4:
        medicamentos_4.grid(row=row_number, column=posicion_medicamentos)
    if posicion_medicamentos == 5:
        medicamentos_5.grid(row=row_number, column=posicion_medicamentos)
    if posicion_medicamentos == 6:
        medicamentos_6.grid(row=row_number, column=posicion_medicamentos)
    if posicion_medicamentos == 7:
        medicamentos_7.grid(row=row_number, column=posicion_medicamentos)


def agregar_afamiliares():
    row_number = 12
    global posicion_afamiliares
    if posicion_afamiliares < max_agregar:
        posicion_afamiliares += 1
    if posicion_afamiliares == 2:
        afamiliares_2.grid(row=row_number, column=posicion_afamiliares)
    if posicion_afamiliares == 3:
        afamiliares_3.grid(row=row_number, column=posicion_afamiliares)
    if posicion_afamiliares == 4:
        afamiliares_4.grid(row=row_number, column=posicion_afamiliares)
    if posicion_afamiliares == 5:
        afamiliares_5.grid(row=row_number, column=posicion_afamiliares)
    if posicion_afamiliares == 6:
        afamiliares_6.grid(row=row_number, column=posicion_afamiliares)
    if posicion_afamiliares == 7:
        afamiliares_7.grid(row=row_number, column=posicion_afamiliares)


def agregar_hospitalizaciones():
    row_number = 13
    global posicion_hospitalizaciones
    if posicion_hospitalizaciones < max_agregar:
        posicion_hospitalizaciones += 1
    if posicion_hospitalizaciones == 2:
        hospital_2.grid(row=row_number, column=posicion_hospitalizaciones)
    if posicion_hospitalizaciones == 3:
        hospital_3.grid(row=row_number, column=posicion_hospitalizaciones)
    if posicion_hospitalizaciones == 4:
        hospital_4.grid(row=row_number, column=posicion_hospitalizaciones)
    if posicion_hospitalizaciones == 5:
        hospital_5.grid(row=row_number, column=posicion_hospitalizaciones)
    if posicion_hospitalizaciones == 6:
        hospital_6.grid(row=row_number, column=posicion_hospitalizaciones)
    if posicion_hospitalizaciones == 7:
        hospital_7.grid(row=row_number, column=posicion_hospitalizaciones)


def agregar_cirugia():
    row_number = 14
    global posicion_cirugia
    if posicion_cirugia < max_agregar:
        posicion_cirugia += 1
    if posicion_cirugia == 2:
        quirurgico_2.grid(row=row_number, column=posicion_cirugia)
    if posicion_cirugia == 3:
        quirurgico_3.grid(row=row_number, column=posicion_cirugia)
    if posicion_cirugia == 4:
        quirurgico_4.grid(row=row_number, column=posicion_cirugia)
    if posicion_cirugia == 5:
        quirurgico_5.grid(row=row_number, column=posicion_cirugia)
    if posicion_cirugia == 6:
        quirurgico_6.grid(row=row_number, column=posicion_cirugia)
    if posicion_cirugia == 7:
        quirurgico_7.grid(row=row_number, column=posicion_cirugia)


def agregar_diagnostico():
    row_number = 25
    global posicion_diagnostico
    if posicion_diagnostico < max_agregar:
        posicion_diagnostico += 1
    if posicion_diagnostico == 2:
        diagnostico_2.grid(row=row_number, column=posicion_diagnostico)
    if posicion_diagnostico == 3:
        diagnostico_3.grid(row=row_number, column=posicion_diagnostico)
    if posicion_diagnostico == 4:
        diagnostico_4.grid(row=row_number, column=posicion_diagnostico)
    if posicion_diagnostico == 5:
        diagnostico_5.grid(row=row_number, column=posicion_diagnostico)
    if posicion_diagnostico == 6:
        diagnostico_6.grid(row=row_number, column=posicion_diagnostico)
    if posicion_diagnostico == 7:
        diagnostico_7.grid(row=row_number, column=posicion_diagnostico)


def agregar_tratamiento():
    row_number = 26
    global posicion_tratamiento
    if posicion_tratamiento < max_agregar:
        posicion_tratamiento += 1
    if posicion_tratamiento == 2:
        tratammiento_2.grid(row=row_number, column=posicion_tratamiento)
    if posicion_tratamiento == 3:
        tratammiento_3.grid(row=row_number, column=posicion_tratamiento)
    if posicion_tratamiento == 4:
        tratammiento_4.grid(row=row_number, column=posicion_tratamiento)
    if posicion_tratamiento == 5:
        tratammiento_5.grid(row=row_number, column=posicion_tratamiento)
    if posicion_tratamiento == 6:
        tratammiento_6.grid(row=row_number, column=posicion_tratamiento)
    if posicion_tratamiento == 7:
        tratammiento_7.grid(row=row_number, column=posicion_tratamiento)


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
amedicos_1.grid(row=6, column=1)

tk.Button(
    master,
    text="Medicamentos",
    bg=default_bg,
    command=agregar_medicamentos,
).grid(row=7, column=0)
medicamentos_1.grid(row=7, column=1)
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
afamiliares_1.grid(row=12, column=1)

tk.Button(
    master,
    text="Hospitalizaciones",
    bg=default_bg,
    command=agregar_hospitalizaciones,
).grid(row=13, column=0)
hospital_1.grid(row=13, column=1)


tk.Button(
    master,
    text="Cirugías",
    bg=default_bg,
    command=agregar_cirugia,
).grid(row=14, column=0)
quirurgico_1.grid(row=14, column=1)

tk.Label(master, text="Tabaco").grid(row=15, column=0)
tabaco = tk.Entry(master, bg=default_bg)
tabaco.grid(row=15, column=1)

tk.Label(master, text="IPA").grid(row=15, column=3)
ipa = tk.Entry(master, bg=default_bg)
ipa.grid(row=15, column=4)

tk.Label(master, text="Alcohol").grid(row=16, column=0)
alcohol = tk.Entry(master, bg=default_bg)
alcohol.grid(row=16, column=1)

tk.Label(master, text="Drogas").grid(row=17, column=0)
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
examen_fisico = tk.Label(
    master, text="Exámen Físico", font=default_title_font_size, bg=default_title_bg
)
examen_fisico.grid(row=24, columnspan=2)


tk.Button(
    master,
    text="Diagnóstico",
    bg=default_bg,
    command=agregar_diagnostico,
).grid(row=25, column=0)
diagnostico_1.grid(row=25, column=1)

tk.Button(
    master,
    text="Tratamiento",
    bg=default_bg,
    command=agregar_tratamiento,
).grid(row=26, column=0)
tratamiento_1.grid(row=26, column=1)

colnames = [
    "nombre",  # 1
    "edad",  # 2
    "prevision",  # 3
    "educacion",  # 4
    "ocupacion",  # 5
    "amedicos",  # 6
    "medicamentos",  # 7
    "motivo",  # 9
    "anamnesis",  # 10
    "afamiliares",  # 12
    "hospital",  # 13
    "quirurgico",  # 14
    "tabaco",  # 15
    "alcohol",  # 16
    "drogas",  # 17
    "alimentacion",  # 18
    "afisica",  # 19
    "defecacion",  # 20
    "orina",  # 21
    "dormir",  # 22
    "sexual",  # 23
    "diagnostico",  # 25
    "tratamiento",  # 26
]


def read_data() -> pd.DataFrame:
    if Path("data.xlsx").exists():
        return pd.read_excel("data.xlsx")
    else:

        return pd.DataFrame({c: [] for c in colnames})


def get_input():
    df = read_data()

    data = [
        {
            "nombre": nombre.get(),  # 1
            "edad": edad.get(),  # 2
            "prevision": prevision.get(),  # 3
            "educacion": educacion.get(),  # 4
            "ocupacion": ocupacion.get(),  # 5
            "amedicos": [
                amedicos_1.get(),
                amedicos_2.get(),
                amedicos_3.get(),
                amedicos_4.get(),
                amedicos_5.get(),
                amedicos_6.get(),
                amedicos_7.get(),
            ],  # 6
            "medicamentos": [
                medicamentos_1.get(),
                medicamentos_2.get(),
                medicamentos_3.get(),
                medicamentos_4.get(),
                medicamentos_5.get(),
                medicamentos_6.get(),
                medicamentos_7.get(),
            ],  # 7
            "motivo": motivo.get("1.0", "end"),  # 9
            "anamnesis": anamnesis.get("1.0", "end"),  # 10
            "afamiliares_1": [
                afamiliares_1.get(),
                afamiliares_2.get(),
                afamiliares_3.get(),
                afamiliares_4.get(),
                afamiliares_5.get(),
                afamiliares_6.get(),
                afamiliares_7.get(),
            ],  # 12
            "hospital": [
                hospital_1.get(),
                hospital_2.get(),
                hospital_3.get(),
                hospital_4.get(),
                hospital_5.get(),
                hospital_6.get(),
                hospital_7.get(),
            ],  # 13
            "quirurgico": [
                quirurgico_1.get(),
                quirurgico_2.get(),
                quirurgico_3.get(),
                quirurgico_4.get(),
                quirurgico_5.get(),
                quirurgico_6.get(),
                quirurgico_7.get(),
            ],  # 14
            "tabaco": tabaco.get(),  # 15
            "alcohol": alcohol.get(),  # 16
            "drogas": drogas.get(),  # 17
            "alimentacion": alimentacion.get(),  # 18
            "afisica": afisica.get(),  # 19
            "defecacion": defecacion.get(),  # 20
            "orina": orina.get(),  # 21
            "dormir": dormir.get(),  # 22
            "sexual": sexual.get(),  # 23
            "diagnostico": [
                diagnostico_1.get(),
                diagnostico_2.get(),
                diagnostico_3.get(),
                diagnostico_4.get(),
                diagnostico_5.get(),
                diagnostico_6.get(),
                diagnostico_7.get(),
            ],  # 25
            "tratamiento": [
                tratamiento_1.get(),
                tratamiento_2.get(),
                tratamiento_3.get(),
                tratamiento_4.get(),
                tratamiento_5.get(),
                tratamiento_6.get(),
                tratamiento_7.get(),
            ],  # 26
        }
    ]
    data = pd.DataFrame.from_records(data)

    df = pd.concat([df, data], axis=0)

    df.to_excel("data.xlsx", index=False)
    print(df)


archivo = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Archivo", menu=archivo, underline=0)
archivo.add_command(
    label="Guardar",
    command=get_input,
)
archivo.add_command(
    label="Salir",
    command=master.destroy,
)
reportes = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Reportes", menu=reportes, underline=0)
reportes.add_command(
    label="Reporte 1",
    # command=get_input,
)
reportes.add_command(
    label="Reporte 2",
    # command=get_input,
)
reportes.add_command(
    label="Reporte 3",
    # command=get_input,
)

master.mainloop()
