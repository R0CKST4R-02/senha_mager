import tkinter as tk
import sqlite3

# Caminho para o banco de dados
db_path = "../../bd/gerar_senhas.db"

# Conectar ao banco de dados
def conectar_bd():
    return sqlite3.connect(db_path)

# Criar ID no banco de dados
def criar_id():
    global label_erro

    user_id = input_user.get().strip()

    if not user_id:
        label_erro.config(text="Preencha o campo!", fg="red")
        return  

    try:
        conexao = conectar_bd()
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO usuarios (nome) VALUES (?);
        """, (user_id,))

        conexao.commit()
        conexao.close()

        nova_janela()  # Abrir a nova janela após criar o usuário

    except sqlite3.Error as e:
        label_erro.config(text=f"Erro: {e}", fg="red")

# Função para abrir a nova janela
def nova_janela():
    global user_senha, label_mensagem

    user_id = input_user.get().strip()

    if not user_id:
        label_erro.config(text="Preencha o campo!", fg="red")
        return

    root.withdraw()  # Esconder a janela principal

    nova_janela = tk.Toplevel(root)  
    nova_janela.title("Janela Secundária")
    nova_janela.geometry("600x400")

    tk.Label(nova_janela, text="Digite uma senha:").pack(pady=10)

    user_senha = tk.Entry(nova_janela)
    user_senha.pack(pady=10)

    btn = tk.Button(nova_janela, text="Guardar senha", command=add_senha)
    btn.pack(pady=5)

    label_mensagem = tk.Label(nova_janela, text="", fg="green")  # Para exibir mensagens
    label_mensagem.pack(pady=10)

    nova_janela.protocol("WM_DELETE_WINDOW", lambda: root.deiconify())

# Adicionar senha ao banco e exibir mensagem
def add_senha():
    global user_senha, label_mensagem, usuario_atual  

    senha = user_senha.get().strip()

    if not senha:
        label_mensagem.config(text="Preencha o campo!", fg="red")
        return

    try:
        conexao = conectar_bd()
        cursor = conexao.cursor()

        # Verificar se o usuário existe
        cursor.execute("SELECT nome FROM usuarios WHERE nome = ?;", (usuario_atual,))
        usuario_existente = cursor.fetchone()

        if not usuario_existente:
            label_mensagem.config(text="Usuário não encontrado!", fg="red")
            return

        # Inserir a senha
        cursor.execute("INSERT INTO senhas (user_id, senha) VALUES (?, ?);", (usuario_atual, senha))

        conexao.commit()
        conexao.close()

        label_mensagem.config(text="Nova senha adicionada!", fg="green")

    except sqlite3.Error as e:
        label_mensagem.config(text=f"Erro: {e}", fg="red")

# Criar interface principal
root = tk.Tk()
root.title("Gerenciador de Senhas")
root.geometry("300x400")

# Widgets da interface
label = tk.Label(root, text="Informe o seu ID")
input_user = tk.Entry(root)
botao1 = tk.Button(root, text="Entrar", command=nova_janela)
botao2 = tk.Button(root, text="Criar ID", command=criar_id)
label_erro = tk.Label(root, text="", fg="red")  

# Layout
label.pack()
input_user.pack(pady=10)
botao1.pack(pady=5)
botao2.pack(pady=5)
label_erro.pack(pady=5)

root.mainloop()
