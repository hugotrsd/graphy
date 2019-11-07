import logging
from PyQt5 import QtCore, QtWidgets, QtGui
from gui.mainwindow.action_panel.editgraph import EditGraph
from gui.mainwindow.action_panel.editunit import EditUnit

class Action(QtWidgets.QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._translate = lambda msg: QtCore.QCoreApplication.translate("Action", msg)

        self.currentChanged.connect(self.tabChanged)

        self._editTabIndex = -1
        self._searchTabIndex = -1

        self.__initUI()

    def tabChanged(self, index):
        logging.debug("TODO: action when tab changed")

    def __initUI(self):
        def editTab() -> QtWidgets.QWidget:
            tab = QtWidgets.QWidget()
            tabLayout = QtWidgets.QVBoxLayout()
            tabLayout.setAlignment(QtCore.Qt.AlignTop)

            tabLayout.addWidget(EditGraph())
            tabLayout.addStretch()
            tabLayout.addWidget(EditUnit())

            tab.setLayout(tabLayout)
            return tab

        def searchTab() -> QtWidgets.QWidget:
            tab = QtWidgets.QWidget()
            tabLayout = QtWidgets.QVBoxLayout()
            tabLayout.setAlignment(QtCore.Qt.AlignVCenter)

            tabLayout.addWidget(QtWidgets.QPushButton("TestSearch"))

            tab.setLayout(tabLayout)
            return tab

        self._editTabIndex = self.addTab(editTab(), self._translate("Edit"))
        self._searchTabIndex = self.addTab(searchTab(), self._translate("Search"))
