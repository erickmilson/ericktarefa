from conexaoBD import conectar
import mysql.connector
from tkinter import messagebox

def deletar(id):
    conexao, cursor = conectar()
    try:
        slqDeletar = f"""DELETE FROM tb_prod
                     WHERE id_pro='{id}'   
                    """
        cursor.execute(slqDeletar)
        conexao.commit()
        messagebox.showinfo("Deletado",
            "Apagado com sucesso!")
        return True
    except mysql.connector.Error as falha:
        messagebox.showerror("Falha",
            "Falha ao deletar"+str(falha))
        return False
    finally:
        conexao.close()
        cursor.close()