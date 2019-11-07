from PyQt5 import QtCore, QtWidgets, QtGui
from gui.mainwindow.editor_panel.canvas import Canvas


class Editor(QtWidgets.QGraphicsView):
    def __init__(self, parent=None):
        super().__init__()
        self.setMinimumSize(500, 500)
        self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self._canvas = Canvas()
        self.setScene(self._canvas)
