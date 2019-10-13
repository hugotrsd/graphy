import logging
from PyQt5 import QtCore, QtWidgets, QtGui
from gui.mainwindow.container import Container


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._translate = lambda msg: QtCore.QCoreApplication.translate("MainWindow", msg)

        self.setWindowIcon(QtGui.QIcon("res/icon.svg"))

        self.__initUI()

    def toggleFullscreen(self, forceMode: bool = False, forceValue: bool = False):
        """ Toggle between fullscreen and normal display (set forceMode to True to use this as a setter) """
        isFullScreen = forceValue if forceMode else self.isFullScreen()

        if isFullScreen:
            self.showNormal()
            self.menuBar().setVisible(True)
        else:
            self.menuBar().setVisible(False)
            self.showFullScreen()

    def closeEvent(self, event):
        # TODO remove following lines
        logging.debug("TODO check for unsaved work")
        event.accept()
        return

        reply = QtWidgets.QMessageBox.question(
            self,
            self._translate("Warning"),
            self._translate("You have unsaved work. Are you sure you want to quit without saving?"),
            QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Close | QtWidgets.QMessageBox.Cancel,
            QtWidgets.QMessageBox.Save
        )

        event.setAccepted(reply == QtWidgets.QMessageBox.Close)

        if reply == QtWidgets.QMessageBox.Save:
            logging.debug("TODO Trigger saving")
            pass

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            if self.isFullScreen():
                self.toggleFullscreen()

    def __initUI(self):
        menuBar = self.menuBar()

        # File menu
        fileMenu = menuBar.addMenu(self._translate("&File"))

        # Fullscreen
        fileMenu.addAction(QtWidgets.QAction(
            self._translate("&Fullscreen"),
            parent=fileMenu,
            shortcut=QtCore.Qt.Key_F5,
            triggered=self.toggleFullscreen
        ))

        # Quit the app
        fileMenu.addAction(QtWidgets.QAction(
            self._translate("&Quit"),
            parent=fileMenu,
            shortcut=QtGui.QKeySequence.Quit,
            triggered=self.close
        ))

        # Help
        helpMenu = menuBar.addMenu(self._translate("&Help"))
        helpMenu.addAction(QtWidgets.QAction(
            self._translate("&About"),
            parent=helpMenu,
            triggered=lambda: logging.debug("TODO")
        ))

        self.setCentralWidget(Container())
