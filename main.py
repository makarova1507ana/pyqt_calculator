import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

# Константы для размеров окна и элементов
WINDOW_SIZE = 235
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40


class PyCalcWindow(QMainWindow):
    """Главное окно калькулятора PyCalc (GUI или представление)."""

    def __init__(self):
        # Инициализация основного окна приложения
        super().__init__()
        self.setWindowTitle("PyCalc")  # Установка заголовка окна
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)  # Фиксированный размер окна

        # Основной вертикальный макет
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)  # Создание центрального виджета
        centralWidget.setLayout(self.generalLayout)  # Установка макета для центрального виджета
        self.setCentralWidget(centralWidget)  # Установка центрального виджета

        # Создание элементов интерфейса
        self._createDisplay()  # Создание экрана калькулятора
        self._createButtons()  # Создание кнопок калькулятора

        # Переменная для хранения текущего ввода пользователя
        self.current_input = ""

    def _createDisplay(self):
        """Создание экрана для калькулятора."""
        self.display = QLineEdit()  # Экран калькулятора (строка ввода)
        self.display.setFixedHeight(DISPLAY_HEIGHT)  # Установка высоты экрана
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)  # Выравнивание текста по правому краю
        self.display.setReadOnly(True)  # Экран доступен только для чтения
        self.generalLayout.addWidget(self.display)  # Добавление экрана в макет

    def _createButtons(self):
        """Создание кнопок калькулятора."""
        # Словарь для хранения кнопок
        self.buttonMap = {}
        # Макет для расположения кнопок
        buttonsLayout = QGridLayout()

        # Раскладка кнопок калькулятора (матрица)
        keyBoard = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="],
        ]

        # Создание кнопок и добавление их в макет
        for row, keys in enumerate(keyBoard):
            for col, key in enumerate(keys):
                self.buttonMap[key] = QPushButton(key)  # Создание кнопки с текстом
                self.buttonMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)  # Установка размера кнопки
                self.buttonMap[key].clicked.connect(self.on_click)  # Подключение обработчика клика
                buttonsLayout.addWidget(self.buttonMap[key], row, col)  # Добавление кнопки в макет

        # Добавление макета с кнопками в основной макет
        self.generalLayout.addLayout(buttonsLayout)

    def on_click(self):
        """Обработчик нажатия на кнопку."""
        sender = self.sender()  # Получаем отправителя (кнопку)
        button_text = sender.text()  # Получаем текст на кнопке

        # Если нажата кнопка "C" — очистить экран
        if button_text == 'C':
            self.current_input = ""  # Очистить текущий ввод
            self.display.clear()  # Очистить экран

        # Если нажата кнопка "=", выполнить вычисление
        elif button_text == '=':
            try:
                result = eval(self.current_input)  # Оценить выражение
                self.display.setText(str(result))  # Отобразить результат
                self.current_input = str(result)  # Обновить текущий ввод с результатом
            except Exception as e:
                self.display.setText('Error')  # Если ошибка — вывести "Error"
                self.current_input = ""  # Очистить текущий ввод
        else:
            # Добавить текст нажатой кнопки к текущему вводу и обновить экран
            self.current_input += button_text
            self.display.setText(self.current_input)


def main():
    """Главная функция для запуска калькулятора PyCalc."""
    pycalcApp = QApplication([])  # Создание приложения PyQt
    pycalcWindow = PyCalcWindow()  # Создание основного окна калькулятора
    pycalcWindow.show()  # Отображение окна
    sys.exit(pycalcApp.exec())  # Запуск цикла обработки событий приложения


if __name__ == "__main__":
    main()  # Запуск главной функции
