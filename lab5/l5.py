#/usr/bin/env python3.5

import sys
from PyQt5.QtWidgets import QApplication
from app import L5MainWindow

app = QApplication(sys.argv)
gui = L5MainWindow()

sys.exit(app.exec_())
