from PyQt5 import QtCore, QtWidgets, QtGui


class EditGraph(QtWidgets.QGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setTitle("Modify the graph")  # TODO tr

        self.__initUI()

    def __initUI(self):
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(QtWidgets.QPushButton("TestEditUnit"))
        layout.addWidget(QtWidgets.QPushButton("TestEditUnit2"))

        self.setLayout(layout)