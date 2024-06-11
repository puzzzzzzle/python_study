import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal
import time

from consts import get_logger

logger = get_logger(__name__)
from python_gui_test.pyqt_test.test1_window import Ui_TestMainWindow


class WorkThread(QThread):
    # 自定义信号对象。参数str就代表这个信号可以传一个字符串
    trigger = pyqtSignal(str)
    index = 0

    def __int__(self):
        # 初始化函数
        super().__init__()

    def run(self):
        checkNum = 0
        while True:
            time.sleep(1)
            checkNum += 1
            self.trigger.emit(f"index:{self.index} now at :{checkNum}")


class MyMainForm(QMainWindow, Ui_TestMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.close_btn.clicked.connect(self.close)
        self.show_info.clicked.connect(self.show_dia)
        # 实例化线程对象
        self.workers = []
        self.run_btn.clicked.connect(self.execute)

    def close(self):
        logger.info(f"start close")
        super().close()

    def show_dia(self):
        QMessageBox.information(self, "标题", "消息正文", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def execute(self):
        # 启动线程
        worker = WorkThread()
        # 线程自定义信号连接的槽函数
        worker.trigger.connect(self.display)
        worker.index = len(self.workers)
        worker.start()
        logger.info(f"start worker {worker.index}")
        self.workers.append(worker)

    def display(self, str):
        # 由于自定义信号时自动传递一个字符串参数，所以在这个槽函数中要接受一个参数
        logger.info(str)


def main_func():
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main_func()
