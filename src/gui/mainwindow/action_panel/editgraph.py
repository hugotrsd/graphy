from PyQt5 import QtCore, QtWidgets, QtGui


import logging

class EditGraph(QtWidgets.QGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setTitle("Modify the graph")  # TODO tr

        self._addButton = None
        self._removeButton = None

        self.__initUI()

    def restoreState(self):
        logging.debug("TODO: restore tab state")

    def __initUI(self):
        def newButton(title: str) -> QtWidgets.QPushButton():
            b = QtWidgets.QPushButton()
            b.setText(title) # TODO tr
            b.setCheckable(True)
            b.setAutoExclusive(True)
            return b

        layout = QtWidgets.QVBoxLayout()
        self._addButton = newButton("Add mode")
        self._addButton.clicked.connect(self._addButtonClicked)
        layout.addWidget(self._addButton)

        self._removeButton = newButton("Remove mode")
        self._removeButton.clicked.connect(self._removeButtonClicked)
        layout.addWidget(self._removeButton)

        self._addButton.click()
        self.setLayout(layout)

    def _addButtonClicked(self):
        logging.debug("TODO: add mode selected")

    def _removeButtonClicked(self):
        logging.debug("TODO: remove mode selected")