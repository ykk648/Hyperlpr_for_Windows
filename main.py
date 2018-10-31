import sys
import mainframe_ui
# from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from mainframe import MainWindow
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     MainWindow = QMainWindow()
#     ui = mainframe.Ui_Form()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # widget = QtWidgets.QWidget()
    # ui = mainframe_ui.Ui_Form()
    # ui.setupUi(widget)
    # widget.show()
    # sys.exit(app.exec_())
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())