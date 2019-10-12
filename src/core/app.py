from PyQt5 import QtCore, QtWidgets
from gui.mainwindow.mainwindow import MainWindow


import logging
import sys
import signal


class Application:
    def __init__(self):
        logging.basicConfig(level=logging.NOTSET)

        QtCore.QCoreApplication.setApplicationName("Graphs")
        QtCore.QCoreApplication.setOrganizationName("Graphs")
        self.qApplication = QtWidgets.QApplication(sys.argv)

        # Install the signal handeler
        # @see https://stackoverflow.com/a/4939113
        signal.signal(signal.SIGINT, Application.sigint_handeler)
        self.interpreterTimer = QtCore.QTimer()
        self.interpreterTimer.start(200)
        self.interpreterTimer.timeout.connect(lambda: None)

        self.mainWindow = MainWindow()
        self.mainWindow.show()

    def __del__(self):
        pass

    def run(self):
        logging.info("Starting application")
        self.qApplication.exec_()
        logging.info("Closing application")

    @staticmethod
    def sigint_handeler(*args):
        logging.info("Received SIGINT")
        QtCore.QCoreApplication.exit()
