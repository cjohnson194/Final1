from controller import *
import sys


def main():
    app = QApplication([])
    window = Controller()
    window.setWindowTitle('Test 10')
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
