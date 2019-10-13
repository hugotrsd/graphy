from PyQt5 import QtCore, QtWidgets, QtGui
from gui.mainwindow.canvas.graphicsvertex import GraphicsVertex


class Canvas(QtWidgets.QGraphicsView):
    def __init__(self, parent=None):
        super().__init__()
        self.setMinimumSize(500, 500)

        self.graphicsScene = QtWidgets.QGraphicsScene(self)

        self.graphicsScene.addItem(GraphicsVertex())

        self.graphicsScene.setBackgroundBrush(QtCore.Qt.lightGray)
        self.graphicsScene.setSceneRect(-2000, -2000, 4000, 4000)

        self.setScene(self.graphicsScene)

        # See https://stackoverflow.com/a/35995179/9178828
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.horizontalScrollBar().disconnect()
        self.verticalScrollBar().disconnect()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragStart = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            oldP = self.mapToScene(self.dragStart)
            newP = self.mapToScene(event.pos())
            translation = newP - oldP

            self.translate(translation.x(), translation.y())

            self.dragStart = event.pos()


"""
class Canvas(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.graphicsScene = QtWidgets.QGraphicsScene(self)
        self.graphicsScene.setBackgroundBrush(QtCore.Qt.blue)
        self.graphicsScene.setSceneRect(QtCore.QRectF(0, 0, 5000, 5000))

        self.graphicsView = QtWidgets.QGraphicsView(self)
        self.graphicsView.setScene(self.graphicsScene)
        print(self.graphicsView.size())

    def resizeEvent(self, event):
        self.graphicsView.setSceneRect(QtCore.QRectF(self.geometry()))

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.fillRect(self.geometry(), QtCore.Qt.red)
        print(self.geometry())
"""
