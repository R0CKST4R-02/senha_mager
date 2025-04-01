import tkinter as tk
import sqlite3


# Conexão com o banco de dados (o banco já existe na pasta "../bd/")
db_path = "../../bd/gestor.db"

def conectar_bd():
    return sqlite3.connect(db_path)
def reload():
    pass

def criar_id():
    id = input_user.get().strip()

    if not id:
        label_erro.config(text="Preencha o campo!", fg="red")
        return
    
    try:
        conexao = conectar_bd()
        cursor = conexao.cursor()

        cursor.execute("""INSERT INTO usuarios (nome) VALUES (?);""", (id,))  
        label_erro.config(text="Id criado com sucesso!", fg="green")

        conexao.commit()
        conexao.close()

        root.mainloop()

    except sqlite3.Error as e:
        label_erro.config(text=f"Erro: {e}", fg="red")

def lista(user_id):

    nome = user_id
    try:
        conexao = conectar_bd()
        cursor = conexao.cursor()

        cursor.execute("""SELECT senhas FROM senhas WHERE userid = ?;""", (nome,))  
        nomes = cursor.fetchall()


        conexao.commit()
        conexao.close()


    except sqlite3.Error as e:
        label_erro.config(text=f"Erro: {e}", fg="red")
    
    return nomes

def add_senha(entry_senha, user_id, label_erro):
    senha = entry_senha.get().strip()
    id = user_id

    if not senha:
        label_erro.config(text="Preencha o campo!", fg="red")
        return
    
    try:
        conexao = conectar_bd()
        cursor = conexao.cursor()

        cursor.execute("""INSERT INTO senhas (userid, senhas) VALUES (?, ?);""", (id, senha))  
        label_erro.config(text="Senha salva com sucesso!", fg="green")


        conexao.commit()
        conexao.close()


    except sqlite3.Error as e:
        label_erro.config(text=f"Erro: {e}", fg="red")

def nova_janela(): 

    user_id = input_user.get().strip()

    if not user_id:
        label_erro.config(text="Preencha o campo!", fg="red")
        return
    
    try:
        conexao = conectar_bd()
        cursor = conexao.cursor()

        cursor.execute("SELECT nome FROM usuarios WHERE nome = ?;", (user_id,))
        usuario_existente = cursor.fetchone()

        if not usuario_existente:
            label_erro.config(text="Usuário não encontrado!", fg="red")
            return
        
        root.destroy()  # Fechar a janela principal

        nova_janela = tk.Tk()
        nova_janela.title("Janela secundária")
        nova_janela.geometry("600x400")

        label_erro_nova = tk.Label(nova_janela, text="", fg="red")
        label_erro_nova.pack()

        entry_senha = tk.Entry(nova_janela)
        btn = tk.Button(nova_janela, text="Guardar senha", command=lambda: add_senha(entry_senha, user_id, label_erro_nova))

        entry_senha.pack(pady=20)
        btn.pack(pady=2)

        tk.Label(nova_janela, text="Senhas!").pack(pady=20)
        for x in lista(user_id):
            label_senhas = tk.Label(nova_janela, text= x)
            label_senhas.pack()

        btn2 = tk.Button(text="Actualizar", command=reload).pack()

        nova_janela.mainloop()

    except sqlite3.Error as e:
        label_erro.config(text=f"Erro {e}!", fg="red")
    
root = tk.Tk()
root.title("Gerenciador de Senhss")
root.geometry("300x400")

label = tk.Label(root, text="Informe o seu ID")
input_user = tk.Entry(root)

botao1 = tk.Button(root, text="Entrar", command=nova_janela)
botao2 = tk.Button(root, text="Criar ID", command=criar_id)
label_erro = tk.Label(root, text="")  

label_erro.pack()
input_user.place(x=70, y=80)
botao1.place(x=70, y=120)
botao2.place(x=150, y=120)

root.mainloop()