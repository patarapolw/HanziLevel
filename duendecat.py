from shared.ui import MainWindow
from duendecat.ui import Layout

from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.setWindowTitle('Duendecat')
    window.layout = Layout()
    window.setGeometry(0, 0, 500, 200)
    window.showUI()

    sys.exit(app.exec_())
