from PyQt5 import QtCore, QtWidgets, QtGui

pen = QtGui.QPen()
pen.setWidth(6)
pen.setCapStyle(QtCore.Qt.FlatCap)
pen.setJoinStyle(QtCore.Qt.RoundJoin)
pen.setStyle(QtCore.Qt.SolidLine)
pen.setColor(QtCore.Qt.blue)


class EdgeItem(QtWidgets.QGraphicsLineItem):
    def __init__(self, nodeStart, nodeEnd, directed: bool):
        super().__init__()

        self.setPen(pen)

        if directed:
            pointiness = 0.2
            self.arrowShape = QtGui.QPolygonF()
            self.arrowShape << QtCore.QPointF(0, 0) \
                            << QtCore.QPointF(-pointiness, -0.5) \
                            << QtCore.QPointF(1, 0) \
                            << QtCore.QPointF(-pointiness, 0.5) \
                            << QtCore.QPointF(0, 0)
            self.arrow = QtWidgets.QGraphicsPolygonItem(self.arrowShape, self)
            self.arrow.setPen(QtGui.QPen(pen.color(), 1, QtCore.Qt.SolidLine, QtCore.Qt.SquareCap, QtCore.Qt.MiterJoin))
            self.arrow.setBrush(pen.color())
        else:
            self.arrowShape = None
            self.arrow = None

        self.adjustPosition()

    def adjustPosition(self):
        line = QtCore.QLineF(10, 10, 100, 100)

        self.setLine(line)

        if self.arrow is not None:
            transform = QtGui.QTransform()
            transform.translate(line.p2().x(), line.p2().y())

            w = self.pen().width() * 3.5
            transform.scale(w, w)
            transform.rotate(-line.angle())  # Inverted because Y axis goes down

            self.arrow.setPolygon(transform.map(self.arrowShape))
