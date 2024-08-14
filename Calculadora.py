import sys
from PySide6.QtWidgets import (QApplication, QWidget, QTextEdit, QPushButton, QGridLayout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()

    def inicializar_ui(self):
        self.setFixedSize(300, 250)
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('Calculadora')
        self.generar_interfaz()
        self.show()

    def generar_interfaz(self):
        self.pantalla = QTextEdit()
        self.pantalla.setDisabled(True)
        boton_1 = QPushButton("1")
        boton_2 = QPushButton("2")
        boton_3 = QPushButton("3")
        boton_4 = QPushButton("4")
        boton_5 = QPushButton("5")
        boton_6 = QPushButton("6")
        boton_7 = QPushButton("7")
        boton_8 = QPushButton("8")
        boton_9 = QPushButton("9")
        boton_0 = QPushButton("0")
        boton_coma = QPushButton(",")

        boton_suma = QPushButton("+")
        boton_resta = QPushButton("-")
        boton_multiplicacion = QPushButton("*")
        boton_division = QPushButton("/")

        boton_AC = QPushButton("AC")
        boton_mas_menos = QPushButton("+/-")
        boton_porciento = QPushButton("%")
        boton_resultado = QPushButton("=")

        botones = [boton_1, boton_2, boton_3, boton_4, boton_5, boton_6,
                   boton_7, boton_8, boton_9, boton_0, boton_coma, boton_suma, boton_resta,
                   boton_multiplicacion, boton_division, boton_AC, boton_mas_menos, boton_porciento, boton_resultado]

        # for boton in botones:
        #     boton.setFixedSize(50, 50)

        self.main_grid = QGridLayout()
        self.main_grid.setHorizontalSpacing(5)  # Espaciado horizontal
        self.main_grid.setVerticalSpacing(500)    # Espaciado vertical

        operaciones = [boton_suma, boton_resta, boton_division, boton_resultado, boton_multiplicacion]
        for boton in operaciones:
            boton.setStyleSheet("background-color: #e89127")

        funciones = [boton_AC, boton_mas_menos, boton_porciento]
        for boton in funciones:
            boton.setStyleSheet("background-color: #9b8a8a")

        self.main_grid = QGridLayout()
        self.main_grid.addWidget(self.pantalla, 0, 0, 2, 4)
        self.main_grid.addWidget(boton_AC, 2, 0, 1, 1)
        self.main_grid.addWidget(boton_mas_menos, 2, 1, 1, 1)
        self.main_grid.addWidget(boton_porciento, 2, 2)
        self.main_grid.addWidget(boton_division, 2, 3)

        self.main_grid.addWidget(boton_7, 3, 0)
        self.main_grid.addWidget(boton_8, 3, 1)
        self.main_grid.addWidget(boton_9, 3, 2)
        self.main_grid.addWidget(boton_multiplicacion, 3, 3)

        self.main_grid.addWidget(boton_4, 4, 0)
        self.main_grid.addWidget(boton_5, 4, 1,)
        self.main_grid.addWidget(boton_6, 4, 2,)
        self.main_grid.addWidget(boton_resta, 4, 3,)

        self.main_grid.addWidget(boton_1, 5, 0,)
        self.main_grid.addWidget(boton_2, 5, 1,)
        self.main_grid.addWidget(boton_3, 5, 2,)
        self.main_grid.addWidget(boton_suma, 5, 3,)

        self.main_grid.addWidget(boton_0, 6, 0, 1, 2)
        self.main_grid.addWidget(boton_coma, 6, 2,)
        self.main_grid.addWidget(boton_resultado, 6, 3,)

        self.setLayout(self.main_grid)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())