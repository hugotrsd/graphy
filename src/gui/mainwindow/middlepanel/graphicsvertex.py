from PyQt5 import QtCore, QtWidgets, QtGui

class GraphicsVertex(QtWidgets.QGraphicsEllipseItem):
    def __init__(self, pos: QtCore.QPoint, parent=None):
        super().__init__()

        self.setCursor(QtCore.Qt.ArrowCursor)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)

        pen = QtGui.QPen()
        pen.setWidth(4)
        pen.setCapStyle(QtCore.Qt.FlatCap)
        pen.setJoinStyle(QtCore.Qt.RoundJoin)
        pen.setStyle(QtCore.Qt.SolidLine)
        pen.setColor(QtCore.Qt.red)

        brush = QtGui.QBrush()
        brush.setStyle(QtCore.Qt.SolidPattern)
        brush.setColor(QtCore.Qt.green)

        self.setPos(pos)
        self.setRect(QtCore.QRectF(0, 0, 50, 50))
        self.setPen(pen)
        self.setBrush(brush)

        text = "120"
        self.label = QtWidgets.QGraphicsTextItem(self)
        self.label.setPlainText(text)
        
        # Disable mouse events for the label
        self.label.setEnabled(False)
        self.label.setAcceptedMouseButtons(QtCore.Qt.NoButton)

        # See: https://stackoverflow.com/a/2204501/9178828
        # I don't fully understand how it works, but it works..
        factorWidth = (self.rect().width() - pen.width()) / QtWidgets.qApp.fontMetrics().width(text)
        factorHeight = (self.rect().height() - pen.width()) / QtWidgets.qApp.fontMetrics().height()
        factor = min(factorWidth, factorHeight)
        if factor < 1 or factor > 1.25:
            font = QtWidgets.qApp.font()
            font.setPointSizeF(font.pointSizeF() * factor)
            self.label.setFont(font)

        self.label.setDefaultTextColor(QtCore.Qt.black)  # Otherwise the font color is set by the theme
        self.label.setPos(
            self.rect().width() / 2 - self.label.boundingRect().width() / 2,
            self.rect().height() / 2 - self.label.boundingRect().height() / 2
        )