from PyQt5 import QtCore, QtWidgets, QtGui


class Properties(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__initUI()

    def __initUI(self):
        layout = QtWidgets.QVBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignTop)

        # Section title
        titleLabelLayout = QtWidgets.QHBoxLayout()
        titleLabelLayout.setAlignment(QtCore.Qt.AlignCenter)
        titleLabelLayout.addWidget(QtWidgets.QLabel("Graph properties"))  # TODO tr
        layout.addLayout(titleLabelLayout)

        layout.addSpacing(10)

        # Graph title
        titleLayout = QtWidgets.QHBoxLayout()
        titleLayout.setAlignment(QtCore.Qt.AlignLeft)
        titleLayout.addWidget(QtWidgets.QLabel("Title:"))  # TODO tr
        titleLayout.addStretch()
        titleLayout.addWidget(QtWidgets.QLineEdit())
        layout.addLayout(titleLayout)

        # Graph directed property
        directedLayout = QtWidgets.QHBoxLayout()
        directedLayout.setAlignment(QtCore.Qt.AlignLeft)
        directedLayout.addWidget(QtWidgets.QLabel("Directed:"))  # TODO tr
        directedLayout.addStretch()
        directedLayout.addWidget(QtWidgets.QCheckBox())
        layout.addLayout(directedLayout)

        # Graph vertex-weighted property
        vertexWeightedLayout = QtWidgets.QHBoxLayout()
        vertexWeightedLayout.setAlignment(QtCore.Qt.AlignLeft)
        vertexWeightedLayout.addWidget(QtWidgets.QLabel("Vertex-weighted:"))  # TODO tr
        vertexWeightedLayout.addStretch()
        vertexWeightedLayout.addWidget(QtWidgets.QCheckBox())
        layout.addLayout(vertexWeightedLayout)

        # Graph edge-weighted property
        edgeWeightedLayout = QtWidgets.QHBoxLayout()
        edgeWeightedLayout.setAlignment(QtCore.Qt.AlignLeft)
        edgeWeightedLayout.addWidget(QtWidgets.QLabel("Edge-weighted:"))  # TODO tr
        edgeWeightedLayout.addStretch()
        edgeWeightedLayout.addWidget(QtWidgets.QCheckBox())
        layout.addLayout(edgeWeightedLayout)


        self.setLayout(layout)
