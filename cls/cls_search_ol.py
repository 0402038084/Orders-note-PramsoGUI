from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QHeaderView, QDialog
from PyQt5 import uic 

class buscarorderlist(QDialog):
    def __init__(self):
        super(buscarorderlist, self).__init__()
        uic.loadUi("Interface/Searchorderlist.ui", self)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint,False)  # Remueve el signo de pregunta del Qdialog

        self.buscar.clicked.connect(lambda: self.busqueda())

    def busqueda(self):
        self.cliente = str(self.cliente_edit.text().upper())
        self.tractor = str(self.tractor_edit.text().upper())
        self.cosechadora = str(self.cosechadora_edit.text().upper())
        self.plataforma_sojero = str(self.plataforma_sojera.text().upper())
        self.plataforma_maicero = str(self.plataforma_maicera.text().upper())
        self.chasisembocador_ = str(self.chasisembocador.text().upper())
        self.observaciones_ = str(self.observaciones.text().upper())
        self.rodado_ = str(self.rodado.text().upper())
        self.localidad_ = str(self.localidad.text().upper())
        self.provincia_ = str(self.provincia.text().upper())
        self.estado_ = str(self.estado.currentText().upper())

        self.close()        
