import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import datetime
from nltk.stem import WordNetLemmatizer
import ai21
ai21.api_key = "hXpfTagKhVGTbKtUpb2MUJnDCjuchnhs"


class ServerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Server")
        self.setGeometry(100, 100, 800, 800)

        self.label = QLabel("Server:", self)
        self.entry = QLineEdit(self)
        self.button = QPushButton("<", self)
        self.button.clicked.connect(self.print_entry)
        self.result_label = QLabel("", self)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.entry)
        layout.addWidget(self.button)
        layout.addWidget(self.result_label)
        self.result_label.setTextFormat(Qt.RichText)
        self.setLayout(layout)

    def print_entry(self):
        response_grande = ai21.Completion.execute(
            model="j2-grande-instruct",
            prompt="",
            numResults=1,
            maxTokens=2,
            temperature=0.4,
            topKReturn=0,
            topP=1,
            stopSequences=[]
        )

        text = "get out of the text all of the key words:  " + self.entry.text()
        response_grande_instruct = ai21.Completion.execute(
            model="j2-grande-instruct",
            prompt=text,
            numResults=1,
            maxTokens=100,
            temperature=0.7,
            topKReturn=0,
            topP=1,
            stopSequences=["##"]
        )
        result = response_grande_instruct
        a = (result["completions"][0]["data"]["text"])

        self.result_label.setText(a)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    server_app = ServerApp()
    server_app.show()
    sys.exit(app.exec())


