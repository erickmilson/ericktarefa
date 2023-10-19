from conexaoBD import conectar
import mysql.connector
from tkinter import messagebox

def inserir(tipo_mov, entra_da, sai_da, descri, vlr , cat , dt_mov):
    conexao, cursor = conectar()
    try:
        sql = f"""INSERT INTO tb_prod
                (tipo_mov, entrada, saida, descricao, valor, categoria, data_mov)
                VALUES
                ('{tipo_mov}','{entra_da}','{sai_da}','{descri}','{vlr}','{cat}','{dt_mov}')
                """
        cursor.execute(sql)
        conexao.commit()
        messagebox.showinfo("Cadastrado","Cadastrado com sucesso!")
        return True
    except mysql.connector.Error as falha:
        messagebox.showerror("Falha", "Falha ao cadastrar: "+str(falha))
        return False
    finally:
        conexao.close()
        cursor.close()
