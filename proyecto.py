import tkinter as tk
import pandas as pd

# Definiciones
master = tk.Tk()
master.geometry("1366x800")
master.title("Ficha Clínica")


# Menu
menubar = tk.Menu(master)
master.config(menu=menubar)
menu_tab_1 = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Menu 1", menu=menu_tab_1)

# Botones para agregar

posicion_antecedentes=1
def agregar_antecedentes():
 global posicion_antecedentes
 posicion_antecedentes+=1
 a1=tk.Entry(master, bg="light gray")
 a1.grid(row=6,column=posicion_antecedentes)
 
posicion_medicamentos=1
def agregar_medicamentos():
 global posicion_medicamentos
 posicion_medicamentos+=1
 a1=tk.Entry(master, bg="light gray")
 a1.grid(row=7,column=posicion_medicamentos)
 
posicion_afamiliares=1
def agregar_afamiliares():
 global posicion_afamiliares
 posicion_afamiliares+=1
 a1=tk.Entry(master, bg="light gray")
 a1.grid(row=12,column=posicion_afamiliares)

posicion_hospitalizaciones=1
def agregar_hospitalizaciones():
 global posicion_hospitalizaciones
 posicion_hospitalizaciones+=1
 a1=tk.Entry(master, bg="light gray")
 a1.grid(row=13,column=posicion_hospitalizaciones)

posicion_cirugia=1
def agregar_cirugia():
 global posicion_cirugia
 posicion_cirugia+=1
 a1=tk.Entry(master, bg="light gray")
 a1.grid(row=14,column=posicion_cirugia)
 
posicion_diagnostico=1
def agregar_diagnostico():
 global posicion_diagnostico
 posicion_diagnostico+=1
 a1=tk.Entry(master, bg="light gray")
 a1.grid(row=25,column=posicion_diagnostico)

posicion_tratamiento=1
def agregar_tratamiento():
 global posicion_tratamiento
 posicion_tratamiento+=1
 a1=tk.Entry(master, bg="light gray")
 a1.grid(row=26,column=posicion_tratamiento) 
    
# Antecedentes
antecedentes = tk.Label(master, text="Antecedentes", font="15", bg="white")
antecedentes.grid(row=0, columnspan=2)

tk.Label(master, text="Nombre").grid(row=1, column=0)
nombre = tk.Entry(master, bg="light gray")
nombre.grid(row=1, column=1)

tk.Label(master, text="edad").grid(row=2, column=0)
edad = tk.Entry(master, bg="light gray")
edad.grid(row=2, column=1)

tk.Label(master, text="prevision").grid(row=3, column=0)
prevision = tk.Entry(master, bg="light gray")
prevision.grid(row=3, column=1)

tk.Label(master, text="educacion").grid(row=4, column=0)
educacion = tk.Entry(master, bg="light gray")
educacion.grid(row=4, column=1)

tk.Label(master, text="ocupacion").grid(row=5, column=0)
ocupacion = tk.Entry(master, bg="light gray")
ocupacion.grid(row=5, column=1)


### TODO
amedicos = tk.Button(master, text="antecedentes medicos", bg="light gray", command=agregar_antecedentes)
amedicos.grid(row=6, column=0)
medicamentos = tk.Button(master, text="medicamentos", bg="light gray", command=agregar_medicamentos)
medicamentos.grid(row=7, column=0)

e6 = tk.Entry(master, bg="light gray")
e7 = tk.Entry(master, bg="light gray")

e6.grid(row=6, column=1)
e7.grid(row=7, column=1)
anamnesis = tk.Label(master, text="anamnesis proxima")
anamnesis.grid(row=8, column=1)
motivo = tk.Label(master, text="motivo de consulta")
motivo.grid(row=9, column=0)
anamnesis = tk.Label(master, text="anamnesis")
anamnesis.grid(row=10, column=0)
e8 = tk.Entry(master, bg="light gray")
e8.grid(row=9, column=1)
e9 = tk.Entry(master, bg="light gray", width=180)
e9.place(x=135, y =225)
habitos = tk.Label(master, text="anamnesis remota")
habitos.grid(row=11, column=1)
familiares = tk.Button(master, text="antecedentes familiares", bg="light gray", command=agregar_afamiliares)
familiares.grid(row=12, column=0)
hospital = tk.Button(master, text="hospitalizaciones", bg="light gray", command=agregar_hospitalizaciones)
hospital.grid(row=13, column=0)
quirurgico = tk.Button(master, text="cirugia", bg="light gray", command=agregar_cirugia)
quirurgico.grid(row=14, column=0)
tabaco = tk.Label(master, text="tabaco")
tabaco.grid(row=15, column=0)
ipa = tk.Label(master, text="IPA")
ipa.grid(row=15, column=3)
oh = tk.Label(master, text="alcohol")
oh.grid(row=16, column=0)
drogas = tk.Label(master, text="drogas")
drogas.grid(row=17, column=0)
alimentacion = tk.Label(master, text="alimentacion")
alimentacion.grid(row=18, column=0)
afisica = tk.Label(master, text="ac.fisica")
afisica.grid(row=19, column=0)
defecacion = tk.Label(master, text="defecatorio")
defecacion.grid(row=20, column=0)
orina = tk.Label(master, text="urinario")
orina.grid(row=21, column=0)
sueño = tk.Label(master, text="sueño")
sueño.grid(row=22, column=0)
sexual = tk.Label(master, text="sexual")
sexual.grid(row=23, column=0)
e10 = tk.Entry(master, bg="light gray")
e10.grid(row=12, column=1)
e11 = tk.Entry(master, bg="light gray")
e11.grid(row=13, column=1)
e12 = tk.Entry(master, bg="light gray")
e12.grid(row=14, column=1)
e13 = tk.Entry(master, bg="light gray")
e13.grid(row=15, column=1)
e14 = tk.Entry(master, bg="light gray")
e14.grid(row=15, column=4)
e15 = tk.Entry(master, bg="light gray")
e15.grid(row=16, column=1)
e16 = tk.Entry(master, bg="light gray")
e16.grid(row=17, column=1)
e17 = tk.Entry(master, bg="light gray")
e17.grid(row=18, column=1)
e18 = tk.Entry(master, bg="light gray")
e18.grid(row=19, column=1)
e19 = tk.Entry(master, bg="light gray")
e19.grid(row=20, column=1)
e20 = tk.Entry(master, bg="light gray")
e20.grid(row=21, column=1)
e21 = tk.Entry(master, bg="light gray")
e21.grid(row=22, column=1)
e22 = tk.Entry(master, bg="light gray")
e22.grid(row=23, column=1)
ef = tk.Label(master, text="examen fisico")
ef.grid(row=24, column=1)
diagnostico = tk.Button(master, text="diagnostico", bg="light gray", command=agregar_diagnostico)
diagnostico.grid(row=25, column=0)
tratamiento = tk.Button(master, text="tratamiento", bg="light gray", command=agregar_tratamiento)
tratamiento.grid(row=26, column=0)
e23 = tk.Entry(master, bg="light gray")
e23.grid(row=25, column=1)
e24 = tk.Entry(master, bg="light gray")
e24.grid(row=26, column=1)
#


def get_input():
    data = [
        {
            "nombre": nombre.get(),
            "edad": edad.get(),
            "prevision": prevision.get(),
            "educacion": educacion.get(),
            "ocupacion": ocupacion.get(),
        }
    ]
    df = pd.DataFrame.from_records(data)
    df.to_excel("data.xlsx", index=False)
    print(df)


guardar = tk.Button(master, text="Guardar", bg="light gray", command=get_input)
guardar.grid(row=27, column=0)

master.mainloop()
