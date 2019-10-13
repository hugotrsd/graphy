from PyQt5 import QtCore, QtWidgets, QtGui


class EditUnit(QtWidgets.QFrame):
    LINE_EDIT_WIDTH = 60

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFrameStyle(QtWidgets.QFrame.Box)

        self.__initUI()

    def __initUI(self):
        layout = QtWidgets.QVBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignTop)

        # Title label
        titleLabelLayout = QtWidgets.QHBoxLayout()
        titleLabelLayout.setAlignment(QtCore.Qt.AlignCenter)
        titleLabelLayout.addWidget(QtWidgets.QLabel("Unit properties"))  # TODO tr
        layout.addLayout(titleLabelLayout)

        layout.addSpacing(10)

        # Edit unit name
        unitNameLayout = QtWidgets.QHBoxLayout()
        unitNameLayout.addWidget(QtWidgets.QLabel("Name: "))  # TODO tr
        unitNameLineEdit = QtWidgets.QLineEdit()
        unitNameLineEdit.setMaximumWidth(EditUnit.LINE_EDIT_WIDTH)
        unitNameLineEdit.setText("Oui")
        unitNameLineEdit.setEnabled(False)
        unitNameLayout.addWidget(unitNameLineEdit)
        layout.addLayout(unitNameLayout)

        # Unit weight
        unitWeightLayout = QtWidgets.QHBoxLayout()
        unitWeightLayout.addWidget(QtWidgets.QLabel("Weight: "))  # TODO tr
        unitWeightLineEdit = QtWidgets.QLineEdit()
        unitWeightLineEdit.setMaximumWidth(EditUnit.LINE_EDIT_WIDTH)
        unitWeightLayout.addWidget(unitWeightLineEdit)
        layout.addLayout(unitWeightLayout)

        self.setLayout(layout)
