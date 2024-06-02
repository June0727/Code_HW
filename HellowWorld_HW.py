import PySide6.QtCore
from PySide6.QtWidgets import (QMainWindow, 
                               QApplication, QLabel)
import sys
import os

class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialiseUI()
        
    def initialiseUI(self):
        self.setGeometry(200, 100, 400, 200)
        self.setWindowTitle("Main Window in PyQt")
        self.setup_main_wnd()
        self.show()
        
    def setup_main_wnd(self):
        hello_label = QLabel(self)
        hello_label.setText('Hello World')
        hello_label.move(150, 50)

        # 라벨을 생성하고 현재 스크립트의 절대경로를 설정
        script_dir = os.path.dirname(os.path.realpath(__file__)) #realpath를 통해 현재 스크립트 파일의 절대경로를 반환하고, dirname을 통해 디렉토리 부분만 추출하여 script_dir에 저장함
        dir_label = QLabel("현재 스크립트 디렉토리: " +script_dir, self) # '현재 스크립트 디렉토리:'와 script_dir을 하나의 문자열로 합쳐서 QLabel의 텍스트로 받음
        dir_label.adjustSize()  # 라벨의 크기를 자동으로 조절함(디렉토리 경로가 계속 짤려서 추가함)
        dir_label.move(50, 100)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MW()
    
    sys.exit(app.exec())