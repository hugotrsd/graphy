from PyQt5 import QtCore, QtWidgets, QtGui
import core.app
from gui.mainwindow.action_panel.action import Action
from gui.mainwindow.editor_panel.editor import Editor
from gui.mainwindow.properties_panel.properties import Properties
from core.graphs.graph import Graph


class Viewer(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.graph = Graph() # TODO
        
        self._action = None
        self._editor = None
        self._properties = None

        self._panelsSplitter = None

        self.__initUI()

        # Use a timer to prevent lag due to constant writing to disk
        self._saveToConfigTimer = QtCore.QTimer()
        self._saveToConfigTimer.setSingleShot(True)
        self._saveToConfigTimer.setInterval(100)
        self._saveToConfigTimer.timeout.connect(self.__saveToConfig)

    def __saveToConfig(self):
        core.app.Application.CONFIG.setValue("mainwindow/viewer_splitter", self._panelsSplitter.saveState())

    def __initUI(self):
        layout = QtWidgets.QHBoxLayout()
        self._panelsSplitter = QtWidgets.QSplitter()
        self._panelsSplitter.splitterMoved.connect(lambda: self._saveToConfigTimer.start())

        self._action = Action()
        self._panelsSplitter.addWidget(self._action)

        self._editor = Editor()
        self._panelsSplitter.addWidget(self._editor)
        self._panelsSplitter.setCollapsible(1, False)

        self._properties = Properties()
        self._panelsSplitter.addWidget(self._properties)

        splitterPreviousState = core.app.Application.CONFIG.value("mainwindow/viewer_splitter")
        if splitterPreviousState:
            self._panelsSplitter.restoreState(splitterPreviousState)

        layout.addWidget(self._panelsSplitter)
        self.setLayout(layout)
