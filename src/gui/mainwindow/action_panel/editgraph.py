from PyQt5 import QtCore, QtWidgets, QtGui


class EditGraph(QtWidgets.QGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setTitle("Modify the graph")  # TODO tr

        self._addButton = None
        self._removeButton = None

        self.__initUI()

    def __initUI(self):
        def newButton(title: str) -> QtWidgets.QPushButton():
            b = QtWidgets.QPushButton()
            b.setText(title) # TODO tr
            b.setCheckable(True)
            b.setAutoExclusive(True)
            return b

        layout = QtWidgets.QVBoxLayout()
        self._addButton = newButton("Add mode")
        layout.addWidget(self._addButton)

        self._removeButton = newButton("Remove mode")
        layout.addWidget(self._removeButton)

        self._addButton.setChecked(True)
        self.setLayout(layout)