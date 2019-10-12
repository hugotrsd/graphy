from PyQt5 import QtCore, QtWidgets, QtGui


class Menu(QtWidgets.QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._translate = lambda msg: QtCore.QCoreApplication.translate("Menu", msg)

        self.__initUI()

    def __initUI(self):
        graph = QtWidgets.QWidget()
        
        graphLayout = QtWidgets.QVBoxLayout()
        graphLayout.setAlignment(QtCore.Qt.AlignTop)
        graphLayout.addWidget(QtWidgets.QPushButton("Yesy"))

        graph.setLayout(graphLayout)
        self.addTab(graph, self._translate("Graph"))