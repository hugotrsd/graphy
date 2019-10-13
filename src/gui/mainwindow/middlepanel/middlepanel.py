from PyQt5 import QtCore, QtWidgets, QtGui
from gui.mainwindow.middlepanel.canvas import Canvas


class MiddlePanel(QtWidgets.QGraphicsView):
    def __init__(self, parent=None):
        super().__init__()
        self.setMinimumSize(500, 500)
        self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.canvas = Canvas()
        self.setScene(self.canvas)
