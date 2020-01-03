from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Hola Bar'))
layout.addWidget(QPushButton('Chay BAr'))
window.setLayout(layout)
window.show()
app.exec_()
