import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, QTextEdit

class DictionaryApp(QWidget):
    def __init__(self, dictionary_data):
        super().__init__()

        self.dictionary_data = dictionary_data

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('My Offline Dictionary')
        self.setGeometry(100, 100, 600, 460)  

        self.word_label = QLabel('Enter a word:')
        self.word_entry = QLineEdit()
        # self.definition_label = QLabel('')
        self.definition_text = QTextEdit()

        self.setStyleSheet("QWidget { background-color: #001233; }"
                           "QLabel { font-size: 60px; color: white; font-family: Acme; }"
                           "QLineEdit { font-size: 80px; color: white; }"
                           "QTextEdit { font-size: 45px; padding: 4px; color: white; font-family: Acme }"
                           "QPushButton { font-size: 16px; padding: 4px; }")

        layout = QVBoxLayout()
        layout.addWidget(self.word_label)
        layout.addWidget(self.word_entry)
        # layout.addWidget(self.definition_label)
        layout.addWidget(self.definition_text)

        self.word_entry.textChanged.connect(self.show_definition)

        self.setLayout(layout)

    def show_definition(self):
        word = self.word_entry.text()
        print(f'Entered Word: {word}')
        definition = self.dictionary_data.get(word, 'Word not found')
        self.definition_text.setPlainText(f'Definition: {definition}')

def load_dictionary_from_json(file_path):
    try:
        import json
        with open(file_path, 'r') as file:
            dictionary_data = json.load(file)
        return dictionary_data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return {}

if __name__ == '__main__':
    dictionary_path = 'dictionary.json'
    dictionary_data = load_dictionary_from_json(dictionary_path)

    app = QApplication(sys.argv)
    window = DictionaryApp(dictionary_data)
    window.show()
    sys.exit(app.exec_())
