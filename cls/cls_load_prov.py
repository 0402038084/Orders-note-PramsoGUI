from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QHeaderView, QDialog
from PyQt5 import uic 
from cls.cls_database import comunication_pramso_database

class load_prov(QDialog):
    def __init__(self):
        super(load_prov, self).__init__()
        uic.loadUi("Interface/loadprov.ui", self)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint,False)  # Remueve el signo de pregunta del Qdialog

