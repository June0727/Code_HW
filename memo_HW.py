import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, 
                                QTextEdit, QFileDialog)
from PySide6.QtGui import QAction


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        # 메뉴바 생성
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        # 파일을 열기 위한 액션 추가
        openAction = QAction('Open', self)
        openAction.triggered.connect(self.openFile)
        fileMenu.addAction(openAction)

        # 종료 액션 추가
        exitAction = QAction('Exit', self)
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Text Editor')
        self.show()

    def openFile(self):
    # 사용자가 선택한 파일 경로를 반환하는 메소드 / 매개변수 2-대화상자제목, 3-대화상자 초기디렉토리(대화상자의 시작위치를 설정함), 4-파일 필터
    # 해당 메소드는 두개의 반환값을 가짐 [파일 경로,필터 이름] 필터 이름 반환값을 _로 무시함
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Text File", "", "Text Files (*.txt);;All Files (*)")
    
        if fileName:
        # 파일 열기 및 내용 표시
            try:
                with open(fileName, 'r', encoding='utf-8') as file:
                    self.textEdit.setText(file.read())
            except UnicodeDecodeError:
                print("파일을 읽는 중 오류가 발생했습니다. 파일 인코딩을 확인해주세요.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = TextEditor()
    sys.exit(app.exec())
