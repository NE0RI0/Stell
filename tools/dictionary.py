from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
import nltk
from nltk.corpus import wordnet

class Dictionary(QtWidgets.QDialog):
    def __init__(self, parent = None):
        QtWidgets.QDialog.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        #Boton para iniciar Busqueda se sinonimos
        synButton = QtWidgets.QPushButton("Synonims", self)
        synButton.clicked.connect(self.syn)
        # boton para buscar antoimos
        antButton = QtWidgets.QPushButton("Antonyms", self)
        antButton.clicked.connect(self.ant)
        #Boton para Buscar Definicion
        defButton = QtWidgets.QPushButton("Definition", self)
        defButton.clicked.connect(self.definition)
        # Boton para buscar ejemplos
        exButton = QtWidgets.QPushButton("Examples", self)
        exButton.clicked.connect(self.examples)

        # Barra a Buscar
        self.findField = QtWidgets.QTextEdit(self)
        self.findField.resize(250,50)
        # Barra de Resultados
        self.resultsField = QtWidgets.QTextEdit(self)
        self.resultsField.resize(250,50)

        layout = QtWidgets.QGridLayout()

        layout.addWidget(self.findField,1,0,1,5)

        layout.addWidget(synButton,2,0,1,2)
        layout.addWidget(antButton,2,2)
        layout.addWidget(defButton,2,3)
        layout.addWidget(exButton,2,4)

        layout.addWidget(self.resultsField,3,0,1,5)

        self.setGeometry(300,300,360,250)
        self.setWindowTitle("Dictionary")
        self.setLayout(layout)


    def syn(self):
        word = self.findField.toPlainText()
        synonyms = []
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                synonyms.append(l.name())
        synonyms = list(set(synonyms))
        self.resultsField.setPlainText(', '.join(synonyms))

    def ant(self):
        word = self.findField.toPlainText()
        antonyms = []
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())
        antonyms = list(set(antonyms))    
        self.resultsField.setPlainText(', '.join(antonyms))

    def definition(self):
        word = self.findField.toPlainText()
        syns = wordnet.synsets(word)
        defin = syns[0].definition()
        self.resultsField.setPlainText(defin)

    def examples(self):
        word = self.findField.toPlainText()
        syns = wordnet.synsets(word)
        exemp = syns[0].examples()
        self.resultsField.setPlainText(', '.join(exemp))
