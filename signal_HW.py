import sys
from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLineEdit, QPushButton, QDialogButtonBox

class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Enter 값을 입력하세요")
        layout = QVBoxLayout(self)
        self.input_field = QLineEdit(self)
        layout.addWidget(self.input_field)
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        layout.addWidget(button_box)

        # 버튼에 연결할 슬롯 설정
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

    def get_integer_value(self):
        value = self.input_field.text()
        try:
            return int(value)
        except ValueError:
            return None

class MainWindow(QDialog):
    my_signal = Signal(int) 
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("메인 윈도우")
        layout = QVBoxLayout(self)
        button = QPushButton("모달 다이얼로그 열기", self)
        layout.addWidget(button)

        button.clicked.connect(self.open_dialog)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.emit_custom_signal()

    def emit_custom_signal(self):
        value, ok = self.get_input_value()
        if ok:
            self.my_signal.emit(value)

    def get_input_value(self):
        dialog = CustomDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            return dialog.get_integer_value(), True
        else:
            return None, False

    def open_dialog(self):
        value, ok = self.get_input_value()
        if ok:
            print("입력받은 값:", value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())