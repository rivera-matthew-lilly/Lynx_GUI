import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
   app = QApplication(sys.argv)
   w = QWidget()
   b = QLabel(w)
   cb_1 = QComboBox()

   w.setGeometry(500,500,700,250)
   w.setWindowTitle("E.L.I. | Enhanced Lynx Interface")

   b.settext("How many octet files need parsed (Max 3 files)?")
   b.move(10,10)
   cb_1.addItems(["1","2","3"])
   layout = QHBoxLayout()
   layout.addWidget(cb_1)
   w.setLayout(layout)
   


   w.show()
   sys.exit(app.exec_())
if __name__ == '__main__':
   window()



#gui_test.py






# class window(QWidget):
#    def __init__(self, parent = None):
#       super(window, self).__init__(parent)
#       font = QFont()
#       font.setFamily("Arial")
#       font.setPointSize(14)
#       self.label = QLabel(self)

#       self.resize(700,250)
#       self.setWindowTitle("E.L.I. | Enhanced Lynx Interface")

      
      
#       self.label.setText("Hello World")
#       self.label.setFont(font)
#       self.label.move(10,10)

#       layout = QHBoxLayout()
#       self.cb_1 = QComboBox()
#       self.cb_1.addItems(["1","2","3"])
#       layout.addWidget(self.cb_1)
#       self.setLayout(layout)




# def main():
#    app = QApplication(sys.argv)
#    ex = window()
#    ex.show()
#    sys.exit(app.exec_())
# if __name__ == '__main__':
#    main()



#gui_test.py