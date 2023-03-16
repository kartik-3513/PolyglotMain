import sys
from PyQt5.QtWidgets import *
from screens.intro import MainPage
from utils import shared

app = QApplication(sys.argv)
main_window = MainPage()
shared.stack_w = QStackedWidget()
shared.stack_w.addWidget(main_window)
shared.stack_w.show()
app.exec_()
