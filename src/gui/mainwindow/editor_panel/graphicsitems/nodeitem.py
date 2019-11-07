from PyQt5 import QtCore, QtWidgets, QtGui

pen = QtGui.QPen()
pen.setWidth(4)
pen.setCapStyle(QtCore.Qt.FlatCap)
pen.setJoinStyle(QtCore.Qt.RoundJoin)
pen.setStyle(QtCore.Qt.SolidLine)
pen.setColor(QtCore.Qt.red)

brush = QtGui.QBrush()
brush.setStyle(QtCore.Qt.SolidPattern)
brush.setColor(QtCore.Qt.green)


class NodeItem(QtWidgets.QGraphicsEllipseItem):
    SIZE = 50

    def __init__(self, pos: QtCore.QPoint):
        super().__init__()

        self.name = "1"
        self.setPos(pos)
        self.setCursor(QtCore.Qt.ArrowCursor)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
        self.setRect(
            - NodeItem.SIZE / 2,
            - NodeItem.SIZE / 2,
            NodeItem.SIZE,
            NodeItem.SIZE
        )
        self.setPen(pen)
        self.setBrush(brush)

        # Init label #
        self.label = QtWidgets.QGraphicsTextItem(self)
        self.label.setDefaultTextColor(QtCore.Qt.black)  # Otherwise the font color is set by the theme

        # Disable mouse events for the label
        self.label.setEnabled(False)
        self.label.setAcceptedMouseButtons(QtCore.Qt.NoButton)
        
        self.__updateLabel()

    def __updateLabel(self):
        self.label.setPlainText(self.name)

        # See: https://stackoverflow.com/a/2204501/9178828
        # I don't fully understand how it works, but it works..
        factorWidth = (self.rect().width() - pen.width()) / QtWidgets.qApp.fontMetrics().width(self.name)
        factorHeight = (self.rect().height() - pen.width()) / QtWidgets.qApp.fontMetrics().height()
        factor = min(factorWidth, factorHeight)
        if factor < 1 or factor > 1.25:
            font = QtWidgets.qApp.font()
            font.setPointSizeF(font.pointSizeF() * factor)
            self.label.setFont(font)

        self.label.setPos(
            self.rect().x() + self.rect().width() / 2 - self.label.boundingRect().width() / 2,
            self.rect().y() + self.rect().height() / 2 - self.label.boundingRect().height() / 2
        )

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if event.button() == QtCore.Qt.RightButton:
            event.accept()
