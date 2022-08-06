import sys

from PyQt5 import QtWidgets

class PopUp(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.textField = QtWidgets.QLabel("Not yet clicked!")
        self.button = QtWidgets.QPushButton("Click Me!")
        self.num = 0 
        
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.button)
        v_box.addWidget(self.textField)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.button.clicked.connect(self.click)
        self.show()

    def click(self):
        self.num += 1
        self.textField.setText("I've been clicked " + str(self.num) + " times.")

app = QtWidgets.QApplication(sys.argv)

popup = PopUp()

sys.exit(app.exec_())