from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import sys

class CadastroCliente(QWidget):
    def __init__(self):
        super().__init__()

        # vamos configurar a geometria da tela, setando os valores de posição X e Y, além de largura e altura.
        self.setGeometry(450,250,600,400)

        # texto para a barra de título
        self.setWindowTitle("Cadastro de Patrimônio")

        # gerenciador de layout vertical
        self.layout_v = QVBoxLayout()

        # labels para os dados
        self.label_id = QLabel("ID")
        self.label_id.setStyleSheet("QLabel{font-size:16pt}")

        self.label_serie = QLabel("Número de Série")
        self.label_serie.setStyleSheet("QLabel{font-size:16pt}")

        self.label_patrimonio = QLabel("Nome do Patrimônio")
        self.label_patrimonio.setStyleSheet("QLabel{font-size:16pt}")

        self.label_tipo = QLabel("Tipo")
        self.label_tipo.setStyleSheet("QLabel{font-size:16pt}")

        self.label_descricao = QLabel("Descrição")
        self.label_descricao.setStyleSheet("QLabel{font-size:16pt}")

        self.label_localizacao = QLabel("Localização")
        self.label_localizacao.setStyleSheet("QLabel{font-size:16pt}")

        self.label_dtfabricacao = QLabel("Data de Fabricação")
        self.label_dtfabricacao.setStyleSheet("QLabel{font-size:16pt}")

        self.label_dtaquisicao = QLabel("Data de Aquisição")
        self.label_dtaquisicao.setStyleSheet("QLabel{font-size:16pt}")

        # LineEdit para estilos
        self.edit_id = QLineEdit()
        self.edit_id.setStyleSheet("QLineEdit{font-size:16pt}")

        self.edit_serie = QLineEdit()
        self.edit_serie.setStyleSheet("QLineEdit{font-size:16pt}")

        self.edit_patrimonio = QLineEdit()
        self.edit_patrimonio.setStyleSheet("QLineEdit{font-size:16pt}")

        self.edit_tipo = QLineEdit()
        self.edit_tipo.setStyleSheet("QLineEdit{font-size:16pt}")

        self.edit_descricao = QLineEdit()
        self.edit_descricao.setStyleSheet("QLineEdit{font-size:20pt}")

        self.edit_localizacao = QLineEdit()
        self.edit_localizacao.setStyleSheet("QLineEdit{font-size:16pt}")

        self.edit_dtfabricacao = QLineEdit()
        self.edit_dtfabricacao.setStyleSheet("QLineEdit{font-size:16pt}")

        self.edit_dtaquisicao = QLineEdit()
        self.edit_dtaquisicao.setStyleSheet("QLineEdit{font-size:16pt}")

        # estilo botão
        self.button = QPushButton("Atualizar Patrimônio")
        self.button.setStyleSheet("QPushButton{background-color:blue;color:white;font-size:16pt;font-weight:bold}")

        # chamar a função de cadastro ao clicar
        self.button.clicked.connect(self.cadastrar)

        # adicionar a label nome e o lineedit ao layout vertical
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)

        self.layout_v.addWidget(self.label_serie)
        self.layout_v.addWidget(self.edit_serie)

        self.layout_v.addWidget(self.label_patrimonio)
        self.layout_v.addWidget(self.edit_patrimonio)

        self.layout_v.addWidget(self.label_tipo)
        self.layout_v.addWidget(self.edit_tipo)

        self.layout_v.addWidget(self.label_descricao)
        self.layout_v.addWidget(self.edit_descricao)

        self.layout_v.addWidget(self.label_localizacao)
        self.layout_v.addWidget(self.edit_localizacao)

        self.layout_v.addWidget(self.label_dtfabricacao)
        self.layout_v.addWidget(self.edit_dtfabricacao)

        self.layout_v.addWidget(self.label_dtaquisicao)
        self.layout_v.addWidget(self.edit_dtaquisicao)

        self.layout_v.addWidget(self.button)

        # adicionar o layout_v na tela
        self.setLayout(self.layout_v)

    def cadastrar(self):
        # Variável de referência ao arquivo de texto
        arquivo = open("patrimonio.txt","+a")
        arquivo.write(f"ID: {self.edit_id.text()}\n")
        arquivo.write(f"Nº de Série: {self.edit_serie.text()}\n")
        arquivo.write(f"Nome do Produto: {self.edit_patrimonio.text()}\n")
        arquivo.write(f"Tipo do Produto: {self.edit_tipo.text()}\n")
        arquivo.write(f"Descrição do Produto: {self.edit_descricao.text()}\n")
        arquivo.write(f"Localização do Produto: {self.edit_localizacao.text()}\n")
        arquivo.write(f"Data de Fabricação do Produto: {self.edit_dtfabricacao.text()}\n")
        arquivo.write(f"Data de Aquisição do Produto: {self.edit_dtaquisicao.text()}\n")
        arquivo.write("----------------------------------------\n")
        arquivo.close()

app = QApplication(sys.argv)
# Instância da classe CadastroCliente
tela = CadastroCliente()
# exibir a tela durante a execução
tela.show ()
# ao clicar no botão fechar a tela deve fechar e sair da memória
app.exec_()