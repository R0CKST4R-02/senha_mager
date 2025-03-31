import tkinter as tk
 
 #criar janela
root = tk.Tk()
root.title("Gerenciador de Senhss")
root.geometry("300x400")

def nova_janela():

    #fechar a janela principal
    root.destroy()

    nova_janela = tk.Tk()
    nova_janela.title("Janela segundaria")
    nova_janela.geometry("600x400")

    input = tk.Entry(nova_janela)
    btn = tk.Button(nova_janela, text="Guardar senha")
    input.pack(pady=20)
    btn.pack(pady=2)
    

    tk.Label(nova_janela, text="Senhas!").pack(pady=20)
    lista = {'ezequiel', 'pedro', 'antonio', 'francisco'}
    for nomes in lista:
        label = tk.Label(nova_janela, text=f"{nomes}")
        label.pack()

    #manter a nova janela aberta
    nova_janela.mainloop()

label = tk.Label(root, text="Informe o seu ID")
input = tk.Entry(root)
botao1 = tk.Button(root, text="Entrar", command=nova_janela)
botao2 = tk.Button(root, text="Criar ID")

input.place(x=70, y=80)
botao1.place(x=70, y=120)
botao2.place(x=150, y=120)

root.mainloop()