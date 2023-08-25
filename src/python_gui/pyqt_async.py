import sys
import asyncio
import time

import aiohttp
from qasync import QEventLoop, asyncSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("AsyncUIExample")

        layout = QVBoxLayout()

        self.result_label = QLabel("Click 'Fetch' to start.")
        layout.addWidget(self.result_label)

        fetch_button = QPushButton("Fetch")
        fetch_button.clicked.connect(self.fetch_data)
        layout.addWidget(fetch_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    @asyncSlot()
    async def fetch_data(self):
        url = "https://jsonplaceholder.typicode.com/todos/1"
        data = await fetch(url)
        self.result_label.setText(data)


def main():
    app = QApplication(sys.argv)

    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    window = MainWindow()
    window.show()

    with loop:
        sys.exit(loop.run_forever())


if __name__ == '__main__':
    main()
