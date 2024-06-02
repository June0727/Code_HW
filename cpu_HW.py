import sys
import psutil
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCore import Qt, QTimer
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dynamic CPU and RAM Usage Plotting")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.ax_cpu = self.figure.add_subplot(211)
        self.ax_cpu.set_title("CPU Usage (%)")
        self.ax_cpu.set_ylim(0, 100)
        self.ax_cpu.set_xlabel("Time (s)")
        self.ax_cpu.set_ylabel("Usage (%)")
        self.cpu_data = []

        self.ax_ram = self.figure.add_subplot(212)
        self.ax_ram.set_title("RAM Usage (%)")
        self.ax_ram.set_ylim(0, 100)
        self.ax_ram.set_xlabel("Time (s)")
        self.ax_ram.set_ylabel("Usage (%)")
        self.ram_data = []

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000)  # 1초마다 업데이트

    def update_plot(self):
        # CPU 사용량 및 RAM 사용량 가져오기
        cpu_percent = psutil.cpu_percent()
        ram_percent = psutil.virtual_memory().percent

        # 새로운 데이터 포인트 추가
        if self.cpu_data:
            x = self.cpu_data[-1][0] + 1
        else:
            x = 0
        self.cpu_data.append((x, cpu_percent))
        self.ax_cpu.plot([p[0] for p in self.cpu_data], [p[1] for p in self.cpu_data], 'b-')

        if self.ram_data:
            x = self.ram_data[-1][0] + 1
        else:
            x = 0
        self.ram_data.append((x, ram_percent))
        self.ax_ram.plot([p[0] for p in self.ram_data], [p[1] for p in self.ram_data], 'r-')

        # 차트 업데이트
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
