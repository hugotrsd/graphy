from PyQt5 import QtCore, QtWidgets, QtGui
import core.app
from gui.mainwindow.leftpanel.leftpanel import LeftPanel
from gui.mainwindow.middlepanel.middlepanel import MiddlePanel
from gui.mainwindow.rightpanel.rightpanel import RightPanel


class Container(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.splitterRef = None
        self.leftPanel = None
        self.middlePanel = None
        self.rightPanel = None

        self.__initUI()

        # Use a timer to prevent lag due to constant writing to disk
        self._saveToConfigTimer = QtCore.QTimer()
        self._saveToConfigTimer.setSingleShot(True)
        self._saveToConfigTimer.setInterval(100)
        self._saveToConfigTimer.timeout.connect(self.__saveToConfig)

    def __saveToConfig(self):
        core.app.Application.CONFIG.setValue("mainwindow/container_splitter", self.splitterRef.saveState())

    def __initUI(self):
        layout = QtWidgets.QHBoxLayout()
        splitter = QtWidgets.QSplitter()
        splitter.splitterMoved.connect(lambda: self._saveToConfigTimer.start())
        self.splitterRef = splitter

        self.leftPanel = LeftPanel()
        splitter.addWidget(self.leftPanel)

        self.middlePanel = MiddlePanel()
        splitter.addWidget(self.middlePanel)
        splitter.setCollapsible(1, False)

        self.rightPanel = RightPanel()
        splitter.addWidget(self.rightPanel)

        splitterPreviousState = core.app.Application.CONFIG.value("mainwindow/container_splitter")
        if splitterPreviousState:
            splitter.restoreState(splitterPreviousState)

        layout.addWidget(splitter)
        self.setLayout(layout)
