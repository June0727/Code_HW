import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel,QMessageBox
from PySide6.QtGui import QPixmap, QKeyEvent
from PySide6.QtCore import Qt

class NumberViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_number = 0
        self.label = QLabel(self)
        self.setCentralWidget(self.label)
        self.show_number()

    def show_number(self):
        # 이미지 경로 설정
        image_path = f"D:/visualstudio/QDialog/image/{self.current_number}.png"  # 이미지 파일명은 0.png부터 9.png까지 숫자에 해당

        # 현재 이미지 출력
        pixmap = QPixmap(image_path)
        self.label.setPixmap(pixmap)
        self.label.setAlignment(Qt.AlignCenter)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Plus:
            if self.current_number == 9:
                QMessageBox.information(self, "최댓값", "최댓값입니다!")
            else:
                self.current_number = min(9, self.current_number + 1)  # 9를 넘어가지 않도록
                self.show_number()
        elif event.key() == Qt.Key_Minus:
            if self.current_number == 0:
                QMessageBox.information(self, "최솟값", "최솟값입니다!")
            else:
                self.current_number = max(0, self.current_number - 1)  # 0 미만으로 내려가지 않도록
                self.show_number()
        elif event.key() == Qt.Key_P:
            if self.current_number == 9:
                QMessageBox.information(self, "최댓값", "최댓값입니다!")
            else:
                self.current_number = min(9, self.current_number + 2)  # 9를 넘어가지 않도록
                self.show_number()
        elif event.key() == Qt.Key_M:
            if self.current_number == 0:
                QMessageBox.information(self, "최솟값", "최솟값입니다!")
            else:
                self.current_number = max(0, self.current_number - 2)  # 0 미만으로 내려가지 않도록
                self.show_number()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = NumberViewer()
    viewer.show()
    sys.exit(app.exec())