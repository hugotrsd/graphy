from PyQt5 import QtCore, QtWidgets, QtGui
from gui.mainwindow.middlepanel.graphicsvertex import GraphicsVertex


class Canvas(QtWidgets.QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__()

        self.addItem(GraphicsVertex(QtCore.QPoint(100, 200)))
        self.addItem(GraphicsVertex(QtCore.QPoint(0, 0)))

        self.setBackgroundBrush(QtCore.Qt.lightGray)
        self.setSceneRect(-2000, -2000, 4000, 4000)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)

    def wheelEvent(self, event):
        # Disable moving the view with the wheel
        event.accept()