import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton
from googletrans import Translator

class TranslatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Translator")
        self.setGeometry(200, 200, 300, 200)

        self.layout = QVBoxLayout()

        self.text_field = QLineEdit()
        self.translate_button = QPushButton("Translate")
        self.translate_button.clicked.connect(self.translate_text)
        self.output_label = QLabel()

        self.layout.addWidget(self.text_field)
        self.layout.addWidget(self.translate_button)
        self.layout.addWidget(self.output_label)

        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

    def translate_text(self):
        text = self.text_field.text()
        translator = Translator()
        translation = translator.translate(text, dest='ru')
        self.output_label.setText(translation.text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    translator_app = TranslatorApp()
    translator_app.show()
    sys.exit(app.exec_())
