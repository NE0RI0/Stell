from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt

class Creat(QtWidgets.QDialog):
    def __init__(self,parent = None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setFixedSize(640, 480)
        self.parent = parent
        self.filename = ""
        self.initUI()

    def initUI(self):
        #Barra de Nombre
        self.nameField = QtWidgets.QTextEdit(self)
        #self.nameField.rezie(250,50)
        nameLabel = QtWidgets.QLabel("Name", self)
        nameLabel.setStyleSheet("font-weight:bold; font-size: 15px;")
        
        # Barra de Lugar de origen
        self.originField = QtWidgets.QTextEdit(self)
        #self.nameField.rezie(250,50)
        originLabel = QtWidgets.QLabel("Origin", self)
        originLabel.setStyleSheet("font-weight:bold; font-size: 15px;")

        # Barra de nacimiento
        birthdayLabel = QtWidgets.QLabel("Birthdate", self)
        birthdayLabel.setStyleSheet("font-weight:bold; font-size: 15px;")
        self.birthdayField = QtWidgets.QTextEdit(self)
        #self.nameField.rezie(250,50)

        # Barra de Raza/Especie
        raceLabel = QtWidgets.QLabel("Race", self)
        raceLabel.setStyleSheet("font-weight:bold; font-size: 15px;")
        self.raceField = QtWidgets.QTextEdit(self)
        #self.nameField.rezie(250,50)

        genderLabel = QtWidgets.QLabel("Gender", self)
        genderLabel.setStyleSheet("font-weight:bold; font-size: 15px;")
        self.genderField = QtWidgets.QTextEdit(self)
        #self.nameField.rezie(250,50)
        
        roleLabel = QtWidgets.QLabel("Role", self)
        roleLabel.setStyleSheet("font-weight:bold; font-size: 15px;")
        self.roleField = QtWidgets.QTextEdit(self)
        #self.nameField.rezie(250,50)
        
        descriptionLabel = QtWidgets.QLabel("Description", self)
        descriptionLabel.setStyleSheet("font-weight:bold; font-size: 15px;")
        self.descriptionField = QtWidgets.QTextEdit(self)
        # self.descriptionField.rezise(250,50)

        bioLabel = QtWidgets.QLabel("Biography", self)
        bioLabel.setStyleSheet("font-weight:bold; font-size: 15px;")
        self.bioField = QtWidgets.QTextEdit(self)
        # self.bioField.rezise(250,50)

        relationsLabel = QtWidgets.QLabel("Relations", self)
        relationsLabel.setStyleSheet("font-weight:bold; font-size: 15px;")
        self.relationsField = QtWidgets.QTextEdit(self)
        # self.relationsField.rezise(250,50)

        afiliationsLabel = QtWidgets.QLabel("Afiliations", self)
        afiliationsLabel.setStyleSheet("font-weight:bold; font-size: 15px;")
        self.afiliationsField = QtWidgets.QTextEdit(self)
        # self.afiliationsField.rezise(250,50)

        featsLabel = QtWidgets.QLabel("Feats", self)
        featsLabel.setStyleSheet("font-weight:bold; font-size: 15px;")
        self.featsField = QtWidgets.QTextEdit(self)
        # self.featsField.rezise(250,50)

        #pictureLabel = QtWidgets.QLabel("Picture", self)
        #pictureLabel.setStyleSheet("font-weight:bold; font-size: 15px;")
        #self.pictureField = QtWidgets.QTextEdit(self)

        saveButton = QtWidgets.QPushButton("Save", self)
        saveButton.clicked.connect(self.sav)

        cancelButton = QtWidgets.QPushButton("Cancel", self)
        cancelButton.clicked.connect(self.can)

        openButton = QtWidgets.QPushButton("Open",self)
        openButton.clicked.connect(self.opn)

        newButton = QtWidgets.QPushButton("New",self)
        newButton.clicked.connect(self.new)

        layout = QtWidgets.QGridLayout()

        layout.addWidget(nameLabel,1,3,1,1)
        layout.addWidget(nameLabel,1,3,1,1)
        layout.addWidget(self.nameField,2,3,1,1)
        layout.addWidget(originLabel,1,5,1,1)
        layout.addWidget(self.originField,2,5,1,1)
        layout.addWidget(birthdayLabel,1,7,1,1)
        layout.addWidget(self.birthdayField,2,7,1,1)

        layout.addWidget(descriptionLabel,3,3,1,1)
        layout.addWidget(self.descriptionField,4,3,1,1)
        layout.addWidget(raceLabel,3,5,1,1)
        layout.addWidget(self.raceField,4,5,1,1)
        layout.addWidget(genderLabel, 3,7,1,1 )
        layout.addWidget(self.genderField, 4,7,1,1)
                
        layout.addWidget(roleLabel,1,8,1,1)
        layout.addWidget(self.roleField,2,8,3,1)

        layout.addWidget(bioLabel,9,1,1,1)
        layout.addWidget(self.bioField,10,1,2,8)

        layout.addWidget(relationsLabel,12,1,1,1)
        layout.addWidget(self.relationsField,13,1,1,4)
        layout.addWidget(afiliationsLabel,12,5,1,1)
        layout.addWidget(self.afiliationsField,13,5,1,4)

        layout.addWidget(featsLabel,16,1,1,1)
        layout.addWidget(self.featsField,17,1,1,8)

        layout.addWidget(newButton,20,1,1,1)
        layout.addWidget(openButton,20,2,1,1)
        layout.addWidget(saveButton,20,7,1,1)
        layout.addWidget(cancelButton,20,8,1,1)

        self.setGeometry(100,100,1030,800)
        self.setWindowTitle("Biography")
        self.setLayout(layout)    

    def sav(self):        
        name = self.nameField.toPlainText() 
        origin = self.originField.toPlainText() 
        birthday = self.birthdayField.toPlainText() 
        role = self.roleField.toPlainText() 
        race = self.raceField.toPlainText() 
        gender = self.genderField.toPlainText() 
        description = self.descriptionField.toPlainText() 
        bio = self.bioField.toPlainText() 
        relations = self.relationsField.toPlainText() 
        afiliation = self.afiliationsField.toPlainText() 
        feats = self.featsField.toPlainText()
        
        data = [name, origin, birthday, role, race, gender, description, bio, relations, afiliation, feats]
          
        fileData = '%%'.join(data) #["%%" + i + "%%" for i in data]

        self.filename=QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')[0]
        if not self.filename.endswith(".bio"):
            self.filename += '.bio'

        with open(self.filename,"wt") as file:
            file.write(fileData)
        
    def can(self):
        self.new()
        self.close()

    def new(self):
        self.filename = ""
        self.nameField.setText("") 
        self.originField.setText("")
        self.birthdayField.setText("") 
        self.roleField.setText("") 
        self.raceField.setText("") 
        self.genderField.setText("") 
        self.descriptionField.setText("") 
        self.bioField.setText("") 
        self.relationsField.setText("") 
        self.afiliationsField.setText("") 
        self.featsField.setText("")

    def opn(self):
        self.filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File',".","(*.bio)")[0]
        if self.filename:
            with open(self.filename,"rt") as file:
                data=file.read()
                dataList = data.split('%%')

                self.nameField.setText(dataList[0]) 
                self.originField.setText(dataList[1]) 
                self.birthdayField.setText(dataList[2]) 
                self.roleField.setText(dataList[3]) 
                self.raceField.setText(dataList[4]) 
                self.genderField.setText(dataList[5]) 
                self.descriptionField.setText(dataList[6]) 
                self.bioField.setText(dataList[7]) 
                self.relationsField.setText(dataList[8]) 
                self.afiliationsField.setText(dataList[9]) 
                self.featsField.setText(dataList[10])


