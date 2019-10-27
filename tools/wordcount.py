from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt

class WordCount(QtWidgets.QDialog):
    def __init__(self,parent = None):
        QtWidgets.QDialog.__init__(self, parent)
        self.parent = parent         
        self.initUI()
 
    def initUI(self):
        # Contador de palabras en lo seleccionado
        currentLabel = QtWidgets.QLabel("Current selection",self)
        currentLabel.setStyleSheet("font-weight:bold; font-size: 15px;")
        currentWordsLabel = QtWidgets.QLabel("Words: ", self)
        currentSymbolsLabel = QtWidgets.QLabel("Symbols: ",self)        
        self.currentWords = QtWidgets.QLabel(self)
        self.currentSymbols = QtWidgets.QLabel(self)
        # Numero total de Caracteres o simbolos
        totalLabel = QtWidgets.QLabel("Total",self)
        totalLabel.setStyleSheet("font-weight:bold; font-size: 15px;")
        totalWordsLabel = QtWidgets.QLabel("Words: ", self)
        totalSymbolsLabel = QtWidgets.QLabel("Symbols: ",self)
        self.totalWords = QtWidgets.QLabel(self)
        self.totalSymbols = QtWidgets.QLabel(self)
        # Layout        
        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(currentLabel,0,0)        
        layout.addWidget(currentWordsLabel,1,0)
        layout.addWidget(self.currentWords,1,1)
        layout.addWidget(currentSymbolsLabel,2,0)
        layout.addWidget(self.currentSymbols,2,1)
        spacer = QtWidgets.QWidget()
        spacer.setFixedSize(0,5)
        layout.addWidget(spacer,3,0)
        layout.addWidget(totalLabel,4,0)
        layout.addWidget(totalWordsLabel,5,0)
        layout.addWidget(self.totalWords,5,1)
        layout.addWidget(totalSymbolsLabel,6,0)
        layout.addWidget(self.totalSymbols,6,1)
        self.setWindowTitle("Word count")
        self.setGeometry(300,300,200,200)
        self.setLayout(layout)

    def getText(self):
        # Establecer lo seleccionado
        text = self.parent.text.textCursor().selectedText()
        # Separar el texto para contar
        words = str(len(text.split()))
        # COntar el numero de Caracteres que contiene el nuevo String
        symbols = str(len(text))
        self.currentWords.setText(words)
        self.currentSymbols.setText(symbols)
        # Contar caracteres pero en el esctiro completo
        text = self.parent.text.toPlainText()
        words = str(len(text.split()))
        symbols = str(len(text))
        self.totalWords.setText(words)
        self.totalSymbols.setText(symbols)
