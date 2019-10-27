from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
import re

class Find(QtWidgets.QDialog):
    def __init__(self, parent = None):        
        QtWidgets.QDialog.__init__(self, parent)
        self.parent = parent
        self.lastStart = 0
        self.initUI()
 
    def initUI(self):
        # Boton de Buisqueda
        findButton = QtWidgets.QPushButton("Find",self)
        findButton.clicked.connect(self.find)
        # BBoton de Reemplazar
        replaceButton = QtWidgets.QPushButton("Replace",self)
        replaceButton.clicked.connect(self.replace)
        # Eliminar lo encontrad0
        allButton = QtWidgets.QPushButton("Replace all",self)
        allButton.clicked.connect(self.replaceAll)
        # Busqueda Normal
        self.normalRadio = QtWidgets.QRadioButton("Normal",self)
        # Busqueda de expreciones regulares
        regexRadio = QtWidgets.QRadioButton("RegEx",self)
        # Barra a Buscar
        self.findField = QtWidgets.QTextEdit(self)
        self.findField.resize(250,50)
        # Barra con lo que se desea cambiar
        self.replaceField = QtWidgets.QTextEdit(self)
        self.replaceField.resize(250,50)
        
        layout = QtWidgets.QGridLayout()

        layout.addWidget(self.findField,1,0,1,4)
        
        layout.addWidget(self.normalRadio,2,2)
        layout.addWidget(regexRadio,2,3)
        layout.addWidget(findButton,2,0,1,2)
        
        layout.addWidget(self.replaceField,3,0,1,4)
        layout.addWidget(replaceButton,4,0,1,2)
        layout.addWidget(allButton,4,2,1,2)

        self.setGeometry(300,300,360,250)
        self.setWindowTitle("Find and Replace")
        self.setLayout(layout)

        # Modo Normal por default
        self.normalRadio.setChecked(True)

    def find(self):
        # Establecer el texto padre(lo que esta en el QTextEdit)
        text = self.parent.text.toPlainText()
        # Establecer el texto a Encontrar
        query = self.findField.toPlainText()
        if self.normalRadio.isChecked():
            # Busqueda para encontrar a partir de la ultima posicion del cursor
            self.lastStart = text.find(query,self.lastStart + 1)
            if self.lastStart >= 0:
                end = self.lastStart + len(query)           
                self.moveCursor(self.lastStart,end)
            else:
                # Reiniciar la siguiente busqueda desde el inicio
                self.lastStart = 0                
                self.parent.text.moveCursor(QtGui.QTextCursor.End)
        else:
            # Compilar el patron
            pattern = re.compile(query)
            # La Busqueda
            match = pattern.search(text,self.lastStart + 1)
            if match:
                self.lastStart = match.start()              
                self.moveCursor(self.lastStart,match.end())
            else:
                self.lastStart = 0                
                # COlocar el cursor al final en caso de una busqueda insatrisfactoria
                self.parent.text.moveCursor(QtGui.QTextCursor.End)

    def replace(self):
        # Establecer el cursor en el Texto
        cursor = self.parent.text.textCursor()
        # Asegurar posicion
        if cursor.hasSelection():
            # Insertatr el nuevo texto en el lugar del texto original
            cursor.insertText(self.replaceField.toPlainText())
            # Ajustar la posicion del Cursor
            self.parent.text.setTextCursor(cursor)

    def replaceAll(self):
        self.lastStart = 0
        self.find()
        # Reemplazar hasta que el cursor regrese al inicio del archivo
        while self.lastStart:
            self.replace()
            self.find()

    def moveCursor(self,start,end):
        # Obtenrt el cursor de el QTextEdit padre
        cursor = self.parent.text.textCursor()
        # Colocar el cursor al inicio de lo encontrado
        cursor.setPosition(start)
        # Hacer que el cursor seleccione toda la palabra o texto que se busca
        cursor.movePosition(QtGui.QTextCursor.Right,QtGui.QTextCursor.KeepAnchor,end - start)
        self.parent.text.setTextCursor(cursor)
