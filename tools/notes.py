from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt

class Notes(QtWidgets.QDialog):
    def __init__(self, parent = None):
        QtWidgets.QDialog.__init__(self,parent)
        self.setFixedSize(640, 480)
        self.parent = parent
        self.filename = ""
        self.initUI()

    def initUI(self):
       self.textField = QtWidgets.QTextEdit(self)

       saveButton = QtWidgets.QPushButton("Save", self)
       saveButton.clicked.connect(self.sav)

       cancelButton = QtWidgets.QPushButton("Cancel", self)
       cancelButton.clicked.connect(self.can)

       openButton = QtWidgets.QPushButton("Open",self)
       openButton.clicked.connect(self.opn)

       layout = QtWidgets.QGridLayout()
       
       layout.addWidget(openButton,1,1,1,1)
       layout.addWidget(saveButton,1,2,1,1)
       layout.addWidget(cancelButton,1,3,1,1)
       layout.addWidget(self.textField,2,1,1,3)


    def opn(self):
        self.filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File',".","(*.txt)")[0]
        if self.filename:
            with open(self.filename,"rt") as file:
                self.textField.setText(file.read())

    def sav(self):
        text = self.textField.toPlainText()
        self.filename=QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')[0]
        if not self.filename.endswith(".txt"):
            self.filename += '.txt'

        with open(self.filename,"wt") as file:
            file.write(fileData)


    def can(self):
        self.close()