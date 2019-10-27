from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt

class Notes(QtWidgets.QDialog):
    def __init__(self, parent = None):
        QtWidgets.QDialog.__init__(self,parent)
        self.parent = parent
        self.lastStart = 0
        self.filename = ""
        self.changesSaved = True
        self.initUI()


    def initUI(self):
        self.text = QtWidgets.QTextEdit(self)
        # self.text.setTabStopWidth(33)
        self.text.textChanged.connect(self.changed)
        self.setGeometry(100,100,1030,800)
        self.setWindowTitle("Notes")
        self.setWindowIcon(QtGui.QIcon("icons/icon.png"))

        saveButton = QtWidgets.QPushButton("Save", self)
        saveButton.clicked.connect(self.save)

        cancelButton = QtWidgets.QPushButton("Cancel", self)
        cancelButton.clicked.connect(self.can)

        layout = QtWidgets.QGridLayout()

        layout.addWidget(saveButton,19,7,1,1)
        layout.addWidget(cancelButton,19,8,1,1)


    def open(self):
        # Obtener el nombre y mostrar solo archivos .bio
        self.filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File',".","(*.bio)")[0]
        if self.filename:
            with open(self.filename,"rt") as file:
                self.text.setText(file.read())

    def save(self):
        # Solo abrir la ventana si no tiene nombre actualmente
        if not self.filename:
          self.filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')[0]
        if self.filename:            
            # Agregar la extension si no la contiene actualmente
            if not self.filename.endswith(".bio"):
              self.filename += ".bio"
            # Guardar el texto en un .txt y el formato en HTML (Por que Qt lo hace facil punto 
            with open(self.filename,"wt") as file:
                file.write(self.text.toHtml())
            self.changesSaved = True
    
    def can(self):
        self.close()

    def changed(self):
        self.changesSaved = False

    def closeEvent(self,event):
        if self.changesSaved:
            event.accept()
        else:        
            popup = QtWidgets.QMessageBox(self)
            popup.setIcon(QtWidgets.QMessageBox.Warning)    
            popup.setText("The document has been modified") 
            popup.setInformativeText("Do you want to save your changes?")            
            popup.setStandardButtons(QtWidgets.QMessageBox.Save   |
                                      QtWidgets.QMessageBox.Cancel |
                                      QtWidgets.QMessageBox.Discard)            
            popup.setDefaultButton(QtWidgets.QMessageBox.Save)
            answer = popup.exec_()
            if answer == QtWidgets.QMessageBox.Save:
                self.save()
            elif answer == QtWidgets.QMessageBox.Discard:
                event.accept()
            else:
                event.ignore()

    def context(self,pos):
        # Ubicar el Cursor
        cursor = self.text.textCursor()
        # Pendiente
        table = cursor.currentTable()
        if table:
            menu = QtGui.QMenu(self)
            appendRowAction = QtWidgets.QAction("Append row",self)
            appendRowAction.triggered.connect(lambda: table.appendRows(1))
            appendColAction = QtWidgets.QAction("Append column",self)
            appendColAction.triggered.connect(lambda: table.appendColumns(1))
            removeRowAction = QtWidgets.QAction("Remove row",self)
            removeRowAction.triggered.connect(self.removeRow)
            removeColAction = QtWidgets.QAction("Remove column",self)
            removeColAction.triggered.connect(self.removeCol)
            insertRowAction = QtWidgets.QAction("Insert row",self)
            insertRowAction.triggered.connect(self.insertRow)
            insertColAction = QtWidgets.QAction("Insert column",self)
            insertColAction.triggered.connect(self.insertCol)
            mergeAction = QtWidgets.QAction("Merge cells",self)
            mergeAction.triggered.connect(lambda: table.mergeCells(cursor))
            # Solo permite que se unan si hay una seleccion
            if not cursor.hasSelection():
                mergeAction.setEnabled(False)
            splitAction = QtWidgets.QAction("Split cells",self)
            cell = table.cellAt(cursor)
            # Solo permite separarlas si la celda actual es mas grande de lo normal
            if cell.rowSpan() > 1 or cell.columnSpan() > 1:
                splitAction.triggered.connect(lambda: table.splitCell(cell.row(),cell.column(),1,1))
            else:
                splitAction.setEnabled(False)

            menu.addAction(appendRowAction)
            menu.addAction(appendColAction)
            menu.addSeparator()
            menu.addAction(removeRowAction)
            menu.addAction(removeColAction)
            menu.addSeparator()
            menu.addAction(insertRowAction)
            menu.addAction(insertColAction)
            menu.addSeparator()
            menu.addAction(mergeAction)
            menu.addAction(splitAction)
            # Convierte las cordenadas de la wid en cordenadas Globales
            pos = self.mapToGlobal(pos)
            if self.toolbar.isVisible():
                pos.setY(pos.y() + 45)
            if self.formatbar.isVisible():
                pos.setY(pos.y() + 45)                
            # Mueve el menu a la nueva posicion
            menu.move(pos)
            menu.show()
        else:
            event = QtGui.QContextMenuEvent(QtGui.QContextMenuEvent.Mouse,QtCore.QPoint())
            self.text.contextMenuEvent(event)

    def removeRow(self):
        # Ubicar cursor
        cursor = self.text.textCursor()
        # Ubicarse en la tabla actual
        table = cursor.currentTable()
        # Ubicarse en la celda
        cell = table.cellAt(cursor)
        # Eliminar la (row) de la celda
        table.removeRows(cell.row(),1)

    def removeCol(self):
        # Ubicar el cursor
        cursor = self.text.textCursor()
        # Ubicarse en la table actual
        table = cursor.currentTable()
        # Ubicarse en la celda
        cell = table.cellAt(cursor)
        # Eliminar la columna de la celda
        table.removeColumns(cell.column(),1)

    def insertRow(self):
        cursor = self.text.textCursor()
        table = cursor.currentTable()
        cell = table.cellAt(cursor)
        # Insert Insertar la nueva (row)
        table.insertRows(cell.row(),1)

    def insertCol(self):
        cursor = self.text.textCursor()
        table = cursor.currentTable()
        cell = table.cellAt(cursor)
        # Insertar la Columna
        table.insertColumns(cell.column(),1)