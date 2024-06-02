import sys 
import subprocess
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QWidget, 
                               QVBoxLayout, QLabel, 
                               QLineEdit, QPushButton, 
                               QMessageBox,
                               )

class MW(QWidget):
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        
        self.username_label = QLabel('User_ID:')
        layout.addWidget(self.username_label)
        
        self.username_input = QLineEdit()
        layout.addWidget(self.username_input)
        self.username_input.returnPressed.connect(self.login)
        
        self.password_label = QLabel('Password:')
        layout.addWidget(self.password_label)
        
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)
        self.password_input.returnPressed.connect(self.login)
        
        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)
        
        self.message_label = QLabel()
        layout.addWidget(self.message_label)
        
        self.setLayout(layout)
        self.setWindowTitle('Login_GuiProgram')
        
    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        
        cmd = f"python D:/visualstudio/oop_matplotlib/login_script.py {username} {password}"
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        
        if stderr:
            QMessageBox.critical(self, 'Error', stderr.decode())
        else:
            QMessageBox.information(self, 'Result', stdout.decode())
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Login_Window = MW()
    Login_Window.show()
    sys.exit(app.exec())