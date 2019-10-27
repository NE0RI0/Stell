# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets #PYQT5 QMainWindow, QApplication, QAction, QFontComboBox, QSpinBox, QTextEdit, QMessageBox PYQT5 QFileDialog, QColorDialog, QDialog
from PyQt5 import QtPrintSupport #PYQT5 QPrintPreviewDialog, QPrintDialog
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from tools import *

class Main(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        QtWidgets.QMainWindow.__init__(self,parent)
        self.filename = ""
        self.changesSaved = True
        self.initUI()
    # Barra de Herramientas
    def initToolbar(self):
        self.newAction = QtWidgets.QAction(QtGui.QIcon("icons/new.png"),"New",self)
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.setStatusTip("Create a new document from scratch.")
        self.newAction.triggered.connect(self.new)

        self.openAction = QtWidgets.QAction(QtGui.QIcon("icons/open.png"),"Open file",self)
        self.openAction.setStatusTip("Open existing document")
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.triggered.connect(self.open)

        self.saveAction = QtWidgets.QAction(QtGui.QIcon("icons/save.png"),"Save",self)
        self.saveAction.setStatusTip("Save document")
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.triggered.connect(self.save)

        self.exportAction = QtWidgets.QAction(QtGui.QIcon("icons/export.png"),"Export",self)
        self.exportAction.setStatusTip("Export to .txt")
        #self.exportAction.setShortcut("")
        self.exportAction.triggered.connect(self.export)

        self.printAction = QtWidgets.QAction(QtGui.QIcon("icons/print.png"),"Print document",self)
        self.printAction.setStatusTip("Print document")
        self.printAction.setShortcut("Ctrl+P")
        self.printAction.triggered.connect(self.printHandler)

        self.previewAction = QtWidgets.QAction(QtGui.QIcon("icons/preview.png"),"Page view",self)
        self.previewAction.setStatusTip("Preview page before printing")
        self.previewAction.setShortcut("Ctrl+Shift+P")
        self.previewAction.triggered.connect(self.preview)

        self.findAction = QtWidgets.QAction(QtGui.QIcon("icons/find.png"),"Find and replace",self)
        self.findAction.setStatusTip("Find and replace words in your document")
        self.findAction.setShortcut("Ctrl+F")
        self.findAction.triggered.connect(find.Find(self).show)

        self.dictionaryAction = QtWidgets.QAction(QtGui.QIcon("icons/dictionary.png"),"Dictionary ",self)
        self.dictionaryAction.setStatusTip("A Dictionary with Synonyms, Antonyms, Definitions and some examples of ow to use the words")
        self.dictionaryAction.setShortcut("Ctrl+D")
        self.dictionaryAction.triggered.connect(dictionary.Dictionary(self).show)

        self.biocreateAction = QtWidgets.QAction(QtGui.QIcon("icons/biography.png"),"Biography ",self)
        self.biocreateAction.setStatusTip("Create a new Place or character that will appear in the story")
        self.biocreateAction.setShortcut("Ctrl+D")
        self.biocreateAction.triggered.connect(biography.Creat(self).show)
        
        self.notesAction = QtWidgets.QAction(QtGui.QIcon("note.png"),"Notes",self)
        self.notesAction.setStatusTip("A place to write notes")
        # self.notesAction.setShortcut("Ctrl+D")
        self.notesAction.triggered.connect(notes.Notes(self).show)
        
        self.cutAction = QtWidgets.QAction(QtGui.QIcon("icons/cut.png"),"Cut to clipboard",self)
        self.cutAction.setStatusTip("Delete and copy text to clipboard")
        self.cutAction.setShortcut("Ctrl+X")
        self.cutAction.triggered.connect(self.text.cut)

        self.copyAction = QtWidgets.QAction(QtGui.QIcon("icons/copy.png"),"Copy to clipboard",self)
        self.copyAction.setStatusTip("Copy text to clipboard")
        self.copyAction.setShortcut("Ctrl+C")
        self.copyAction.triggered.connect(self.text.copy)

        self.pasteAction = QtWidgets.QAction(QtGui.QIcon("icons/paste.png"),"Paste from clipboard",self)
        self.pasteAction.setStatusTip("Paste text from clipboard")
        self.pasteAction.setShortcut("Ctrl+V")
        self.pasteAction.triggered.connect(self.text.paste)

        self.undoAction = QtWidgets.QAction(QtGui.QIcon("icons/undo.png"),"Undo last action",self)
        self.undoAction.setStatusTip("Undo last action")
        self.undoAction.setShortcut("Ctrl+Z")
        self.undoAction.triggered.connect(self.text.undo)

        self.redoAction = QtWidgets.QAction(QtGui.QIcon("icons/redo.png"),"Redo last undone thing",self)
        self.redoAction.setStatusTip("Redo last undone thing")
        self.redoAction.setShortcut("Ctrl+Y")
        self.redoAction.triggered.connect(self.text.redo)

        dateTimeAction = QtWidgets.QAction(QtGui.QIcon("icons/calender.png"),"Insert current date/time",self)
        dateTimeAction.setStatusTip("Insert current date/time")
        dateTimeAction.setShortcut("Ctrl+Shift+D")
        dateTimeAction.triggered.connect(datetime.DateTime(self).show)

        wordCountAction = QtWidgets.QAction(QtGui.QIcon("icons/count.png"),"See word/symbol count",self)
        wordCountAction.setStatusTip("See word/symbol count")
        wordCountAction.setShortcut("Ctrl+W")
        wordCountAction.triggered.connect(self.wordCount)

        tableAction = QtWidgets.QAction(QtGui.QIcon("icons/table.png"),"Insert table",self)
        tableAction.setStatusTip("Insert table")
        tableAction.setShortcut("Ctrl+T")
        tableAction.triggered.connect(table.Table(self).show)

        imageAction = QtWidgets.QAction(QtGui.QIcon("icons/image.png"),"Insert image",self)
        imageAction.setStatusTip("Insert image")
        imageAction.setShortcut("Ctrl+Shift+I")
        imageAction.triggered.connect(self.insertImage)

        bulletAction = QtWidgets.QAction(QtGui.QIcon("icons/bullet.png"),"Insert bullet List",self)
        bulletAction.setStatusTip("Insert bullet list")
        bulletAction.setShortcut("Ctrl+Shift+B")
        bulletAction.triggered.connect(self.bulletList)

        numberedAction = QtWidgets.QAction(QtGui.QIcon("icons/number.png"),"Insert numbered List",self)
        numberedAction.setStatusTip("Insert numbered list")
        numberedAction.setShortcut("Ctrl+Shift+L")
        numberedAction.triggered.connect(self.numberList)


        # Acomodo de los Botones
        self.toolbar = self.addToolBar("Options")

        self.toolbar.addAction(self.newAction)
        self.toolbar.addAction(self.openAction)
        self.toolbar.addAction(self.saveAction)
        self.toolbar.addAction(self.exportAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(self.printAction)
        self.toolbar.addAction(self.previewAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(self.cutAction)
        self.toolbar.addAction(self.copyAction)
        self.toolbar.addAction(self.pasteAction)
        self.toolbar.addAction(self.undoAction)
        self.toolbar.addAction(self.redoAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(bulletAction)
        self.toolbar.addAction(numberedAction)

        self.addToolBarBreak()

        self.toolbar.addAction(self.findAction)
        self.toolbar.addAction(self.notesAction)
        self.toolbar.addAction(self.dictionaryAction)
        self.toolbar.addAction(self.biocreateAction)
        self.toolbar.addAction(dateTimeAction)
        self.toolbar.addAction(wordCountAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(tableAction)
        self.toolbar.addAction(imageAction)

        self.toolbar.addSeparator()

    def initFormatbar(self):
        fontBox = QtWidgets.QFontComboBox(self)
        fontBox.currentFontChanged.connect(lambda font: self.text.setCurrentFont(font))
        fontSize = QtWidgets.QSpinBox(self)
        # Agregar "pt" despues de cada valor
        fontSize.setSuffix(" pt")
        fontSize.valueChanged.connect(lambda size: self.text.setFontPointSize(size))
        fontSize.setValue(12)

        # Apariencia
        fontColor = QtWidgets.QAction(QtGui.QIcon("icons/font-color.png"),"Change font color",self)
        fontColor.triggered.connect(self.fontColorChanged)

        boldAction = QtWidgets.QAction(QtGui.QIcon("icons/bold.png"),"Bold",self)
        boldAction.triggered.connect(self.bold)

        italicAction = QtWidgets.QAction(QtGui.QIcon("icons/italic.png"),"Italic",self)
        italicAction.triggered.connect(self.italic)

        underlAction = QtWidgets.QAction(QtGui.QIcon("icons/underline.png"),"Underline",self)
        underlAction.triggered.connect(self.underline)

        strikeAction = QtWidgets.QAction(QtGui.QIcon("icons/strike.png"),"Strike-out",self)
        strikeAction.triggered.connect(self.strike)

        superAction = QtWidgets.QAction(QtGui.QIcon("icons/superscript.png"),"Superscript",self)
        superAction.triggered.connect(self.superScript)

        subAction = QtWidgets.QAction(QtGui.QIcon("icons/subscript.png"),"Subscript",self)
        subAction.triggered.connect(self.subScript)

        alignLeft = QtWidgets.QAction(QtGui.QIcon("icons/align-left.png"),"Align left",self)
        alignLeft.triggered.connect(self.alignLeft)

        alignCenter = QtWidgets.QAction(QtGui.QIcon("icons/align-center.png"),"Align center",self)
        alignCenter.triggered.connect(self.alignCenter)

        alignRight = QtWidgets.QAction(QtGui.QIcon("icons/align-right.png"),"Align right",self)
        alignRight.triggered.connect(self.alignRight)

        alignJustify = QtWidgets.QAction(QtGui.QIcon("icons/align-justify.png"),"Align justify",self)
        alignJustify.triggered.connect(self.alignJustify)

        indentAction = QtWidgets.QAction(QtGui.QIcon("icons/indent.png"),"Indent Area",self)
        indentAction.setShortcut("Ctrl+Tab")
        indentAction.triggered.connect(self.indent)

        dedentAction = QtWidgets.QAction(QtGui.QIcon("icons/dedent.png"),"Dedent Area",self)
        dedentAction.setShortcut("Shift+Tab")
        dedentAction.triggered.connect(self.dedent)

        backColor = QtWidgets.QAction(QtGui.QIcon("icons/highlight.png"),"Change background color",self)
        backColor.triggered.connect(self.highlight)

        self.formatbar = self.addToolBar("Format")

        self.formatbar.addWidget(fontBox)
        self.formatbar.addWidget(fontSize)

        self.formatbar.addSeparator()

        self.formatbar.addAction(fontColor)
        self.formatbar.addAction(backColor)

        self.formatbar.addSeparator()

        self.formatbar.addAction(boldAction)
        self.formatbar.addAction(italicAction)
        self.formatbar.addAction(underlAction)
        self.formatbar.addAction(strikeAction)
        self.formatbar.addAction(superAction)
        self.formatbar.addAction(subAction)

        self.formatbar.addSeparator()

        self.formatbar.addAction(alignLeft)
        self.formatbar.addAction(alignCenter)
        self.formatbar.addAction(alignRight)
        self.formatbar.addAction(alignJustify)

        self.formatbar.addSeparator()

        self.formatbar.addAction(indentAction)
        self.formatbar.addAction(dedentAction)

    def initMenubar(self):
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        view = menubar.addMenu("View")
        # Acciones en la barra de Herramientas
        file.addAction(self.newAction)
        file.addAction(self.openAction)
        file.addAction(self.saveAction)
        file.addAction(self.exportAction)
        file.addAction(self.printAction)
        file.addAction(self.previewAction)

        edit.addAction(self.undoAction)
        edit.addAction(self.redoAction)
        edit.addAction(self.cutAction)
        edit.addAction(self.copyAction)
        edit.addAction(self.pasteAction)
        edit.addAction(self.findAction)

        # Acciones para las Barras
        toolbarAction = QtWidgets.QAction("Toggle Toolbar",self)
        toolbarAction.triggered.connect(self.toggleToolbar)
        formatbarAction = QtWidgets.QAction("Toggle Formatbar",self)
        formatbarAction.triggered.connect(self.toggleFormatbar)
        statusbarAction = QtWidgets.QAction("Toggle Statusbar",self)
        statusbarAction.triggered.connect(self.toggleStatusbar)
        view.addAction(toolbarAction)
        view.addAction(formatbarAction)
        view.addAction(statusbarAction)

    def initUI(self):
        self.text = QtWidgets.QTextEdit(self)
        # Establecer los espacion que saltara "Tab" en pixeles (33 = 8)
        self.text.setTabStopWidth(33)
        self.initToolbar()
        self.initFormatbar()
        self.initMenubar()
        self.setCentralWidget(self.text)
        # Inicia la barra de estado
        self.statusbar = self.statusBar()
        # Actualizar la ubicacion del cursor al moverse
        self.text.cursorPositionChanged.connect(self.cursorPosition)
        # Pendiente
        self.text.setContextMenuPolicy(Qt.CustomContextMenu)
        self.text.customContextMenuRequested.connect(self.context)
        self.text.textChanged.connect(self.changed)
        self.setGeometry(100,100,1030,800)
        self.setWindowTitle("STELL")
        self.setWindowIcon(QtGui.QIcon("icons/icons.png"))

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
            # COnvierte las cordenadas de la wid en cordenadas Globales
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


    def toggleToolbar(self):
        state = self.toolbar.isVisible()
        # Cambiar si es visible o no
        self.toolbar.setVisible(not state)

    def toggleFormatbar(self):
        state = self.formatbar.isVisible()
        # Invertir el parametro de visivilidad
        self.formatbar.setVisible(not state)

    def toggleStatusbar(self):
        state = self.statusbar.isVisible()
        self.statusbar.setVisible(not state)

    def new(self):
        spawn = Main()
        spawn.show()

    def open(self):
        # Obtener el nombre y mostrar solo archivos .stell
        self.filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File',".","(*.stell)")[0]
        if self.filename:
            with open(self.filename,"rt") as file:
                self.text.setText(file.read())

    def save(self):
        # Solo abrir la ventana si no tiene nombre actualmente
        if not self.filename:
          self.filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')[0]
        if self.filename:            
            # Agregar la extension si no la contiene actualmente
            if not self.filename.endswith(".stell"):
              self.filename += ".stell"
            # Guardar el texto en un .txt y el formato en HTML (Por que Qt lo hace facil punto 
            with open(self.filename,"wt") as file:
                file.write(self.text.toHtml())
            self.changesSaved = True

    def export(self):
        # Solo abrir la ventana si no tiene nombre actualmente
        if not self.filename:
          self.filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Export File')[0]
        if self.filename:            
            # Agregar la extension si no la contiene actualmente
            if not self.filename.endswith(".txt"):
              self.filename += ".txt"
            # Guardar el texto en un .txt y el formato en HTML (Por que Qt lo hace facil punto 
            with open(self.filename,"wt") as file:
                file.write(self.text.toPlainText())
            self.changesSaved = True

    def preview(self):
        # Abre la ventana del Preview
        preview = QtPrintSupport.QPrintPreviewDialog()
        # Si se solicita imprimir algo muestra la ventana de impresion
        preview.paintRequested.connect(lambda p: self.text.print_(p))
        preview.exec_()

    def printHandler(self):
        # Abre la ventana de impresion
        dialog = QtPrintSupport.QPrintDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.text.document().print_(dialog.printer())

    def cursorPosition(self):
        cursor = self.text.textCursor()
        line = cursor.blockNumber() + 1
        col = cursor.columnNumber()
        self.statusbar.showMessage("Line: {} | Column: {}".format(line,col))

    def wordCount(self):
        wc = wordcount.WordCount(self)
        wc.getText()
        wc.show()

    def insertImage(self):
        # Obtener el nombre de la imagen
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Insert image',".","Images (*.png *.xpm *.jpg *.bmp *.gif)")[0]
        if filename:            
            # Crear el objeto
            image = QtGui.QImage(filename)
            # Error si no se puede cargar
            if image.isNull():
                popup = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
                                          "Image load error",
                                          "Could not load image file!",
                                          QtWidgets.QMessageBox.Ok,
                                          self)
                popup.show()
            else:
                cursor = self.text.textCursor()
                cursor.insertImage(image,filename)

    def fontColorChanged(self):
        color = QtWidgets.QColorDialog.getColor()
        self.text.setTextColor(color)

    def highlight(self):
        color = QtWidgets.QColorDialog.getColor()
        self.text.setTextBackgroundColor(color)

    def bold(self):
        if self.text.fontWeight() == QtGui.QFont.Bold:
            self.text.setFontWeight(QtGui.QFont.Normal)
        else:
            self.text.setFontWeight(QtGui.QFont.Bold)

    def italic(self):
        state = self.text.fontItalic()
        self.text.setFontItalic(not state)

    def underline(self):
        state = self.text.fontUnderline()
        self.text.setFontUnderline(not state)

    def strike(self):
        # Identifica el formato del texto
        fmt = self.text.currentCharFormat()
        #lo invierte
        fmt.setFontStrikeOut(not fmt.fontStrikeOut())
        # Muestra el siguiente formato
        self.text.setCurrentCharFormat(fmt)

    def superScript(self):
        fmt = self.text.currentCharFormat()
        align = fmt.verticalAlignment()
        if align == QtGui.QTextCharFormat.AlignNormal:
            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSuperScript)
        else:
            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)
        self.text.setCurrentCharFormat(fmt)

    def subScript(self):
        fmt = self.text.currentCharFormat()
        align = fmt.verticalAlignment()
        if align == QtGui.QTextCharFormat.AlignNormal:
            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSubScript)
        else:
            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)
        self.text.setCurrentCharFormat(fmt)

    def alignLeft(self):
        self.text.setAlignment(Qt.AlignLeft)

    def alignRight(self):
        self.text.setAlignment(Qt.AlignRight)

    def alignCenter(self):
        self.text.setAlignment(Qt.AlignCenter)

    def alignJustify(self):
        self.text.setAlignment(Qt.AlignJustify)

    def indent(self):
        cursor = self.text.textCursor()
        if cursor.hasSelection():
            temp = cursor.blockNumber()
            cursor.setPosition(cursor.anchor())
            diff = cursor.blockNumber() - temp
            direction = QtGui.QTextCursor.Up if diff > 0 else QtGui.QTextCursor.Down
            for n in range(abs(diff) + 1):
                cursor.movePosition(QtGui.QTextCursor.StartOfLine)
                cursor.insertText("\t")
                cursor.movePosition(direction)
        else:
            cursor.insertText("\t")

    def handleDedent(self,cursor):
        cursor.movePosition(QtGui.QTextCursor.StartOfLine)
        line = cursor.block().text()
        if line.startswith("\t"):
            cursor.deleteChar()
        else:
            for char in line[:8]:
                if char != " ":
                    break
                cursor.deleteChar()

    def dedent(self):
        cursor = self.text.textCursor()
        if cursor.hasSelection():
            temp = cursor.blockNumber()
            cursor.setPosition(cursor.anchor())
            diff = cursor.blockNumber() - temp
            direction = QtGui.QTextCursor.Up if diff > 0 else QtGui.QTextCursor.Down
            for n in range(abs(diff) + 1):
                self.handleDedent(cursor)
                cursor.movePosition(direction)
        else:
            self.handleDedent(cursor)


    def bulletList(self):
        cursor = self.text.textCursor()
        cursor.insertList(QtGui.QTextListFormat.ListDisc)

    def numberList(self):
        cursor = self.text.textCursor()
        cursor.insertList(QtGui.QTextListFormat.ListDecimal)

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
