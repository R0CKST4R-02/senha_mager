import tkinter as tk
import sqlite3

# Conexão com o banco de dados (o banco já existe na pasta "../bd/")
db_path = "../../bd/gerar_senhas.db"

def criar_id():
    conexao = sqlite3.connect(db_path)
    cursor = conexao.cursor()

    user_id = input_user.get().strip()
    if not user_id:
        label_erro.config(text="Prencha o campo!", fg="red")
        return
        
    try:
        # Criar tabela dentro da função
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS "{user_id}" (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            senha TEXT UNIQUE NOT NULL
        );
        """)

        conexao.commit()  # Salvar mudanças
        conexao.close()  # Fechar conexão após a operação
        nova_janela()

    except sqlite3.Error as e:
        label_erro.config(text=f"Erro: {e}", fg="red")   

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
input_user = tk.Entry(root)
botao1 = tk.Button(root, text="Entrar", command=nova_janela)
botao2 = tk.Button(root, text="Criar ID", command=criar_id)
label_erro = tk.Label(root, text="")  # Label global para mensagens de erro

label_erro.pack()
input_user.place(x=70, y=80)
botao1.place(x=70, y=120)
botao2.place(x=150, y=120)

root.mainloop()