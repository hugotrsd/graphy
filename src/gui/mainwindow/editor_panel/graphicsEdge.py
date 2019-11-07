from PyQt5 import QtCore, QtWidgets, QtGui

class GraphicsEdge(QtWidgets.QGraphicsLineItem):
    def __init__(self, fromVertex=None, toVertex=None):
        super().__init__()

        