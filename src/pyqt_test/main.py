import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from test1_window import Ui_TestMainWindow
from consts import get_logger

logger = get_logger(__name__)


class MyMainForm(QMainWindow, Ui_TestMainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.close_btn.clicked.connect(self.close)

    def close(self):
        logger.info(f"start close")
        super(MyMainForm, self).close()
    def log_test(self):
        logger.info(f"start log")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
