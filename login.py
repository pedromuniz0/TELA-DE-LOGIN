import tkinter as tk
from tkinter import messagebox

# Função para verificar login
def verificar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    
    # Aqui, você pode adicionar a lógica para verificar o login, como consultar um banco de dados.
    if usuario == "admin" and senha == "1234":
        messagebox.showinfo("Login bem-sucedido", "Bem-vindo!")
    else:
        messagebox.showerror("Erro de Login", "Nome de usuário ou senha incorretos.")

# Configuração da janela principal
root = tk.Tk()
root.title("Tela de Login")
root.geometry("400x300")
root.configure(bg="#0D1B2A")  # Azul escuro

# Label para o título
titulo = tk.Label(root, text="Login", font=("Arial", 24), bg="#0D1B2A", fg="#FFD700")  # Dourado
titulo.pack(pady=20)

# Campo para nome de usuário
label_usuario = tk.Label(root, text="Usuário", font=("Arial", 14), bg="#0D1B2A", fg="#FFD700")
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(root, font=("Arial", 12))
entry_usuario.pack(pady=5, padx=20, fill="x")

# Campo para senha
label_senha = tk.Label(root, text="Senha", font=("Arial", 14), bg="#0D1B2A", fg="#FFD700")
label_senha.pack(pady=5)
entry_senha = tk.Entry(root, font=("Arial", 12), show="*")
entry_senha.pack(pady=5, padx=20, fill="x")

# Botão de login
botao_login = tk.Button(root, text="Entrar", font=("Arial", 14), bg="#FFD700", fg="#0D1B2A", command=verificar_login)
botao_login.pack(pady=20)

root.mainloop()
