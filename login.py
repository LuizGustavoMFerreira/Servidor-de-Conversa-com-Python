from pickle import FRAME
import tkinter
from tkinter import messagebox

# cores ----------------------------------
co0 = "#f0f3f5" # Preta
co1 = "#feffff" # Branca
co2 = "#3fb5a3" # Verde
co3 = "#38576b" # Valor
co4 = "#403d3d" # Letra
co5 = "#ffff66" 
co6 = "#8080ff"

# Criando Janela -------------------------
janela = tkinter.Tk()
janela.title('Servidor')
janela.geometry("310x300")
janela.configure(background=co1)
janela.resizable(width=False, height=False)

# Dividindo a janela ----------------------
frame_cima = tkinter.Frame(janela, width=310, height=50, bg=co1, relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=tkinter.NSEW)

frame_baixo = tkinter.Frame(janela, width=310, height=250, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=tkinter.NSEW)

# Configurando o frame cima ---------------
l_nome = tkinter.Label(frame_cima, text='LOGIN', anchor=tkinter.NE, font=('Arial 25'),bg=co1, fg=co4)
l_nome.place(x=5, y=5)

l_linha = tkinter.Label(frame_cima, text='', width=275, anchor=tkinter.NW, font=('Arial 1'),bg=co5, fg=co4)
l_linha.place(x=10, y=45)

credenciais = ['Marcos', '20112066', '05252022'] 

# Verificar a senha 
def verifica_senha():
    nome = e_nome.get()
    senha = e_senha.get()

    if nome == 'Marcos' and senha == '20112016':
        messagebox.showinfo('Login', 'Seja bem vindo Srº ' + nome)
        janela.destroy()
    elif nome == '' and senha == '':
         messagebox.showwarning('Erro', 'Nome e a senha não digitado') 
    elif nome == 'marcos' and senha == '':
         messagebox.showwarning('Erro', 'Senha não digitada') 
    elif senha == '20112016' and nome == '':
        messagebox.showwarning('Erro', 'Nome não digitado') 
    else:
        messagebox.showwarning('Erro', 'Verifique o nome e a senha') 

# Configurando o frame baixo ---------------
l_nome = tkinter.Label(frame_baixo, text='Nome *', anchor=tkinter.NW, font=('Arial 10'),bg=co1, fg=co4)
l_nome.place(x=10, y=20)
e_nome = tkinter.Entry(frame_baixo, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
e_nome.place(x=12, y=50)

l_pass = tkinter.Label(frame_baixo, text='Senha *', anchor=tkinter.NW, font=('Arial 10'),bg=co1, fg=co4)
l_pass.place(x=10, y=95)
e_senha = tkinter.Entry(frame_baixo, width=25, justify='left', show='*', font=("", 15), highlightthickness=1, relief='solid')
e_senha.place(x=12, y=130)

b_confirmar = tkinter.Button(frame_baixo, command=verifica_senha, text='Entrar', width=39, height=2, font=('Arial 8 bold'),bg=co6, fg=co1, relief=tkinter.RAISED, overrelief=tkinter.RIDGE)
b_confirmar.place(x=13, y=180)

janela.mainloop()