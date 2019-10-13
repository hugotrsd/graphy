import logging
import sys
import signal
from PyQt5 import QtCore, QtWidgets, QtGui
import gui.mainwindow.mainwindow


class Application:
    CONFIG = None

    def __init__(self):
        logging.basicConfig(level=logging.NOTSET)

        Application.CONFIG = QtCore.QSettings("config.ini", QtCore.QSettings.IniFormat)

        QtCore.QCoreApplication.setApplicationName("Graphs")
        QtCore.QCoreApplication.setOrganizationName("Graphs")
        QtWidgets.qApp.setDesktopSettingsAware(False)  # TODO remove
        self.qApplication = QtWidgets.QApplication(sys.argv)

        # Install the signal handeler
        # @see https://stackoverflow.com/a/4939113
        signal.signal(signal.SIGINT, Application.sigint_handeler)
        self.interpreterTimer = QtCore.QTimer()
        self.interpreterTimer.start(200)
        self.interpreterTimer.timeout.connect(lambda: None)

        self.mainWindow = gui.mainwindow.mainwindow.MainWindow()
        self.mainWindow.show()

    def __del__(self):
        if Application.CONFIG is not None:
            del Application.CONFIG
        Application.CONFIG = None

    def run(self):
        logging.info("Starting application")
        self.qApplication.exec_()
        logging.info("Closing application")

    @staticmethod
    def sigint_handeler(*args):
        logging.info("Received SIGINT")
        QtCore.QCoreApplication.exit()
