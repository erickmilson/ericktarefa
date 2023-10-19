from conexaoBD import conectar
import mysql.connector
from tkinter import messagebox

def atualizarCadastro(id, tipomov, entra_da, sai_da, descri, vlr, cat,dt_mov):
    conexao, cursor = conectar()
    try:
        sql = f"""UPDATE tb_prod
            SET tipo_mov='{tipomov}', entrada='{entra_da}',
            saida='{sai_da}', descricao='{descri}', valor ='{vlr}',categoria = '{cat}',data_mov= '{dt_mov}', WHERE id_pro='{id}'
              """
        cursor.execute(sql)
        conexao.commit()
        messagebox.showinfo("Atualizar",
            "Cadastro atualizado!")
        return True
    except mysql.connector.Error as falha:
        messagebox.showerror("Falha",
            "Falha ao atualizar"+str(falha))
        return False
    finally:
        conexao.close()
        cursor.close()