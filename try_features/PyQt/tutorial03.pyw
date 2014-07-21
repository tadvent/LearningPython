import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QtGui.QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('ToolTips')
        self.show()

def main():
    a = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(a.exec_())

if __name__ == '__main__':
    main()
