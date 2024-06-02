import sys, os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog     
from notePad_HW import Ui_MainWindow

class MW(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MW, self).__init__()
        self.setupUi(self)
        self.show()
        self.action_open.triggered.connect(self.openFunction)
        # self.action_save.triggered.connect(self.saveFunction)
        
    def openFunction(self):
        
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Text File", "", "Text Files (*.txt);;All Files (*)")
    
        if fileName:
            # 파일 열기 및 내용 표시
            try:
                with open(fileName, 'r', encoding='utf-8') as file:
                    self.textEdit.setPlainText(file.read())
            except UnicodeDecodeError:
                print("파일을 읽는 중 오류가 발생했습니다. 파일 인코딩을 확인해주세요.")
                
    # def savefunction(self):
                     
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MW()
    sys.exit(app.exec()) 