from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app  = QApplication([])

win = QWidget()
win.resize(800,500)
win.setWindowTitle("Генератор переможця")
winner = QLabel("")
result = QLabel("?")
gen_btn = QPushButton("Згенерувати")
v_line = QVBoxLayout()
v_line.addWidget(winner, alignment=Qt.AlignCenter)
v_line.addWidget(result, alignment=Qt.AlignCenter)
v_line.addWidget(gen_btn, alignment=Qt.AlignCenter)
win.setLayout(v_line)

win.show()
app.exec_()

