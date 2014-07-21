#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tadvent
#
# Created:     10/03/2013
# Copyright:   (c) tadvent 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from PyQt4 import QtGui
import sys

def main():
    app = QtGui.QApplication(sys.argv)

    w = QtGui.QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
