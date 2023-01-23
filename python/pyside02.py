import sys
import PySide2
from PySide2.QtWidgets import QApplication, QWidget, QLabel
#from PySide2.QtCore import QCoreApplication

print(PySide2.__version__)
print(PySide2.QtCore.__version__)
print(PySide2.QtCore.qVersion())

# QCoreApplication.setLibraryPaths(['/usr/local/anaconda3/envs/tflow/lib/python3.7/site-packages/PySide2/'])

app = QApplication(sys.argv)

window = QWidget()
window.resize(289, 170)
window.setWindowTitle("FIrst Qt Program")

label = QLabel('Hello Qt', window)
label.move(110, 80)

window.show()
app.exec_()
