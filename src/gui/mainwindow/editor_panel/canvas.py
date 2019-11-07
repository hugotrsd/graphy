from PyQt5 import QtCore, QtWidgets, QtGui
from gui.mainwindow.editor_panel.graphicsitems.nodeitem import NodeItem
from gui.mainwindow.editor_panel.graphicsitems.edgeitem import EdgeItem


class Canvas(QtWidgets.QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__()

        self.addItem(NodeItem(QtCore.QPoint(100, 200)))
        self.addItem(NodeItem(QtCore.QPoint(0, 0)))
        self.addItem(EdgeItem(None, None, True))

        self.setBackgroundBrush(QtCore.Qt.lightGray)
        self.setSceneRect(-2000, -2000, 4000, 4000)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if event.isAccepted(): return
        
        if event.button() == QtCore.Qt.RightButton:
            self.addItem(NodeItem(event.scenePos()))

    def wheelEvent(self, event):
        # Disable moving the view with the wheel
        event.accept()