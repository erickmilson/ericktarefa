from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from moduloinserir import inserir
from moduloinserirdata import converterData

class TelaPrincipal(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        carregador = QUiLoader()
        self.tela = carregador.load("Tela.ui")
        self.componentes()
    
    def componentes(self):
        self.caixamovimentacao = self.tela.findChild(QtWidgets.QLineEdit, "caixa_movimentacao")
        self.caixaentrada = self.tela.findChild(QtWidgets.QDateEdit, "caixa_entrada")
        self.caixasaida = self.tela.findChild(QtWidgets.QDateEdit, "caixa_saida")
        self.caixadescricao = self.tela.findChild(QtWidgets.QLineEdit, "caixa_descricao")
        self.caixavalor = self.tela.findChild(QtWidgets.QSpinBox, "caixa_valor")
        self.caixacategoria = self.tela.findChild(QtWidgets.QComboBox, "caixa_categoria")
        self.caixadatamovimentacao = self.tela.findChild(QtWidgets.QDateEdit, "caixa_datamovimentacao")
        self.caixa_botao = self.tela.findChild(QtWidgets.QPushButton, "caixa_botao")
        self.caixa_botao.clicked.connect(self.cadastrarProducao)

    def cadastrarProducao(self):
        tipo_mov = self.caixamovimentacao.text()
        entra_da = self.caixaentrada.text()
        sai_da = self.caixasaida.text()
        descri = self.caixadescricao.text()
        vlr = self.caixavalor.text()
        cat = self.caixacategoria.currentText()
        dt_mov = self.caixadatamovimentacao.text()
        inserir(tipo_mov,converterData(entra_da),converterData(sai_da),descri,vlr,cat, converterData(dt_mov),)

    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    interface = TelaPrincipal()
    interface.tela.showMaximized()
    app.exec()