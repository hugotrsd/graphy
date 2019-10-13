from PyQt5 import QtCore, QtWidgets, QtGui

class RightPanel(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setText("RightPanelTest")