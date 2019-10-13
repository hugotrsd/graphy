from PyQt5 import QtCore, QtWidgets, QtGui
import core.app
from gui.mainwindow.leftpanel.leftpanel import LeftPanel
from gui.mainwindow.canvas.canvas import Canvas
from gui.mainwindow.rightpanel.rightpanel import RightPanel


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
        core.app.Application.CONFIG.setValue("mainwindow/container_splitter", self.splitterRef.saveState())

    def __initUI(self):
        layout = QtWidgets.QHBoxLayout()
        splitter = QtWidgets.QSplitter()
        splitter.splitterMoved.connect(lambda: self._saveToConfigTimer.start())
        self.splitterRef = splitter

        splitter.addWidget(LeftPanel())

        splitter.addWidget(Canvas())

        splitter.addWidget(RightPanel())

        splitterPreviousState = core.app.Application.CONFIG.value("mainwindow/container_splitter")
        if splitterPreviousState:
            splitter.restoreState(splitterPreviousState)

        layout.addWidget(splitter)
        self.setLayout(layout)
