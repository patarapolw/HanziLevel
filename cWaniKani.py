import sys
from PyQt5.QtGui import *
from PyQt5.QtQml import *
from PyQt5.QtCore import *

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load(QUrl('cWaniKani/qml/main.qml'))
    win = engine.rootObjects()[0]
    win.show()
    sys.exit(app.exec_())
