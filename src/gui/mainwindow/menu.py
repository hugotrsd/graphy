from PyQt5 import QtCore, QtWidgets, QtGui

import logging


class Menu(QtWidgets.QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._translate = lambda msg: QtCore.QCoreApplication.translate("Menu", msg)

        self.currentChanged.connect(self.tabChanged)

        self.editGraphTabIndex = -1
        self.searchGraphTabIndex = -1

        self.__initUI()

    def tabChanged(self, index):
        logging.debug("TODO: action when tab changed")

    def __initUI(self):
        # Modify graph tab
        mGraph = QtWidgets.QWidget()

        mGraphLayout = QtWidgets.QVBoxLayout()
        mGraphLayout.setAlignment(QtCore.Qt.AlignTop)
        mGraphLayout.addWidget(QtWidgets.QPushButton("Yesy"))

        mGraph.setLayout(mGraphLayout)
        self.editGraphTabIndex = self.addTab(mGraph, self._translate("Modify"))

        # Traversing the graph
        search = QtWidgets.QWidget()

        searchLayout = QtWidgets.QVBoxLayout()
        searchLayout.setAlignment(QtCore.Qt.AlignTop)
        searchLayout.addWidget(QtWidgets.QPushButton("juytfy"))

        search.setLayout(searchLayout)
        self.searchGraphTabIndex = self.addTab(search, self._translate("Search"))
