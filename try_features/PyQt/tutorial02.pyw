#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tadvent
#
# Created:     11/03/2013
# Copyright:   (c) tadvent 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('tutorial02icon.gif'))
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
