from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QStackedWidget

import sqlite3


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self, cursor):
        super().__init__()

        self.cursor = cursor
        self.stack = QStackedWidget()

        self.setFixedSize(QSize(700, 640))
        self.setWindowTitle("Mei's Reading Files")

        self.entry_screen = EntryScreen()
        self.stack.addWidget(self.entry_screen.screen)
        self.entry_screen.button.clicked.connect(self.show_preview)

        self.preview_screen = PreviewScreen()
        self.preview_screen.back_button.clicked.connect(self.back)
        self.stack.addWidget(self.preview_screen.screen)

        self.setCentralWidget(self.stack)

    def show_preview(self):
        self.preview_screen.refresh(self.cursor)
        self.stack.setCurrentIndex(1)

    def back(self):
        self.stack.setCurrentIndex(0)


class EntryScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel(alignment=Qt.AlignmentFlag.AlignCenter)
        self.label.setText("Mei's Reading Files")
        self.button = QPushButton("Enter")

        self.entry_layout = QVBoxLayout()
        self.entry_layout.addWidget(self.label)
        self.entry_layout.addWidget(self.button)

        self.screen = QWidget()
        self.screen.setLayout(self.entry_layout)


class PreviewScreen(QWidget):
    def __init__(self):
        super().__init__()
        preview_label = QLabel(alignment=Qt.AlignmentFlag.AlignCenter)
        preview_label.setText("Preview")
        self.back_button = QPushButton("Back")

        self.most_recent_label = QLabel()
        self.most_recent_label.setText("Most recent read:")
        self.most_recent_list = [QLabel() for _ in range(3)]
        preview_layout = QVBoxLayout()
        preview_layout.addWidget(self.back_button, alignment=Qt.AlignmentFlag.AlignRight)
        preview_layout.addWidget(preview_label)
        preview_layout.addWidget(self.most_recent_label)
        for i in range(3):
            preview_layout.addWidget(self.most_recent_list[i])
        self.screen = QWidget()
        self.screen.setLayout(preview_layout)

    def refresh(self, cursor):
        result = cursor.execute("SELECT Name FROM books, read WHERE books.ISBN = read.ISBN ORDER BY end DESC")
        for i in range(3):
            self.most_recent_list[i].setText(str(i+1) + ". " + result.fetchone()[0])


connection = sqlite3.connect("test.db")

# cursor
cursor = connection.cursor()
app = QApplication([])

window = MainWindow(cursor)
window.show()
app.exec()
connection.close()
