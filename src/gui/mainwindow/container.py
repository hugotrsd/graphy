from PyQt5 import QtCore, QtWidgets, QtGui
from gui.mainwindow.menu import Menu
from gui.mainwindow.canvas import Canvas
from core.config import settingsInst


class Container(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Use a timer to prevent lag due to constant writing to disk
        self._saveToConfigTimer = QtCore.QTimer()
        self._saveToConfigTimer.setSingleShot(True)
        self._saveToConfigTimer.setInterval(100)
        self._saveToConfigTimer.timeout.connect(self.__saveToConfig)

        self.__initUI()

    def __saveToConfig(self):
        settingsInst.setValue("mainwindow/container_splitter", self.splitterRef.saveState())

    def __initUI(self):
        layout = QtWidgets.QHBoxLayout()
        splitter = QtWidgets.QSplitter()
        splitter.splitterMoved.connect(lambda: self._saveToConfigTimer.start())
        self.splitterRef = splitter

        splitter.addWidget(Menu())
        splitter.addWidget(Canvas())
        splitter.addWidget(QtWidgets.QPushButton("Graph infos"))
        splitterPreviousState = settingsInst.value("mainwindow/container_splitter")
        if splitterPreviousState:
            splitter.restoreState(splitterPreviousState)

        layout.addWidget(splitter)
        self.setLayout(layout)
