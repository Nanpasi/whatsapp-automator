import os
import tkinter as tk
from tkinter import ttk
import pywhatkit


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# TODO implementar uma checagem de dados usando uma função decoradora
# TODO implementar checagem de horários usando uma função decoradora


# /////////////////////////// FUNÇÕES //////////////////////////////////////////

def get_dados():
    mensagem = text.get('1.0', 'end-1c')
    numero = entry.get()
    check = check1.get()

    return mensagem, numero, check

def get_horario():
    # implementar checagem de horário usando uma função decoradora
    # Pegando a string do campo "entry1" e transformando em duas variáveis int separadas
    h, m = entry1.get().split(':')       # Retorna uma lista
    h, m = int(h), int(m)                # Desempacota a lista

    return h, m

def send_msg(c, num, msg):
    # Se a checkbox não estiver preenchida
    if not c:
        # Pegar horário fornecido (xx:xx)
        hora, minuto = get_horario()

        # Mensagem programada
        pywhatkit.sendwhatmsg(num, msg, hora, minuto, tab_close=True)

        return False
    
    # Mensagem instantânea
    pywhatkit.sendwhatmsg_instantly(num, msg, tab_close=True)

    return True

def submit():
    # Pegando os dados dos campos de input
    msg, n_telefone, mandar_na_hora = get_dados()

    # Vendo se a mensagem é programada ou instantânea
    send_msg(mandar_na_hora, n_telefone, msg)




# /////////////////////////// GUI //////////////////////////////////////////////

# This code is generated using PyUIbuilder: https://pyuibuilder.com

main = tk.Tk()
main.title("WhatsApp Automator")
main.config(bg="#65ab4d")
main.geometry("795x403")
main.update_idletasks()

geometryX = 0
geometryY = 0

main.geometry("+%d+%d"%(geometryX, geometryY))


style = ttk.Style(main)
style.theme_use("clam")


frame = tk.Frame(master=main)
frame.config(bg="#d2ffb4")
frame.place(x=27, y=20, width=488, height=347)

text = tk.Text(master=frame)
text.config(bg="#fff", fg="#000000", bd=1)
text.place(x=35, y=80, width=305, height=229)

style.configure("label.TLabel", background="#4dd256", foreground="#000", anchor="center")
label = ttk.Label(master=frame, text="Digite sua mensagem no espaço abaixo:", style="label.TLabel")
label.configure(anchor="center")
label.place(x=33, y=21, width=307, height=44)

frame1 = tk.Frame(master=main)
frame1.config(bg="#d2ffb4")
frame1.place(x=538, y=20, width=231, height=260)

style.configure("configs.TLabel", background="#4dd256", foreground="#000", anchor="center")
configs = ttk.Label(master=frame1, text="Configurações", style="configs.TLabel")
configs.configure(anchor="center")
configs.place(x=16, y=10, width=204, height=26)

style.configure("entry.TEntry", fieldbackground="#fff", foreground="#000", borderwidth=1)

# CAMPO DE TELEFONE
entry = ttk.Entry(master=frame1, style="entry.TEntry")
entry.place(x=17, y=96, width=200, height=30)

style.configure("telefone.TLabel", background="#4dd256", foreground="#000", anchor="center")
telefone = ttk.Label(master=frame1, text="Telefone", style="telefone.TLabel")
telefone.configure(anchor="center")
telefone.place(x=16, y=66, width=99, height=22)

style.configure("telefone1.TLabel", background="#4dd256", foreground="#000", anchor="center")
telefone1 = ttk.Label(master=frame1, text="Horário", style="telefone1.TLabel")
telefone1.configure(anchor="center")
telefone1.place(x=18, y=139, width=99, height=22)

style.configure("entry1.TEntry", fieldbackground="#fff", foreground="#000", borderwidth=1)

# CAMPO DE HORÁRIO
entry1 = ttk.Entry(master=frame1, style="entry1.TEntry")
entry1.place(x=16, y=170, width=200, height=30)

# Checkbox "Mandar na hora"
check1 = tk.IntVar()
c1 = tk.Checkbutton(master=frame1, offvalue=0, onvalue=1, text='Mandar na hora', background='#4dd256', variable=check1)
c1.place(x=15, y=215)

style.configure("button.TButton", background="#4dd256", foreground="#000", borderwidth=1)
style.map("button.TButton", background=[("active", "#92e49e")], foreground=[("active", "#000")])

button = ttk.Button(master=main, text="ENVIAR", style="button.TButton", command=submit)
button.place(x=688, y=302, width=80, height=40)


main.mainloop()