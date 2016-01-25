import sys
from PyQt5.QtCore import QCoreApplication, QThread

class Thread1(QThread):
    def run(self):
        for i in range(5):
            print("Hello {}".format(i))


class Thread2(QThread):
    def run(self):
        t2 = Thread1()
        t2.start()
        for i in range(2):
            print("world {}".format(i))

if __name__ == '__main__':
    app = QCoreApplication(sys.argv)
    p1 = Thread2()
    p1.start()
    p1.wait()
    print('EEEha')
