import mysql.connector
from tkinter import messagebox

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="bd_prod"
        )
        cursor = conexao.cursor()
        print("Conectado com sucesso ao BD")
        return conexao, cursor
    except mysql.connector.Error as falha:
        messagebox.showerror(
            "Erro", "Falha na conexão com BD"+str(falha))
        return None, None
