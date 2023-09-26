import sys
import PyQt5.QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

print(PyQt5.QtCore.qVersion())


app = QApplication(sys.argv)

window = QWidget()
window.resize(289, 170)
window.setWindowTitle("FIrst Qt Program")

label = QLabel('Hello Qt', window)
label.move(110, 80)

window.show()
app.exec_()
