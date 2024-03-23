from PyQt6.QtWidgets import QWidget, QApplication, QGridLayout, \
        QLineEdit, QLabel, QPushButton
import sys
from datetime import datetime


class AgeCalculator(QWidget):
    def __init__(self):
        # Call init function in parent class, without this program won't work
        super().__init__()
        # Creating a grid
        grid = QGridLayout()

        # Creating label and edit box
        name_label = QLabel("Name: ")
        self.name_line_edit = QLineEdit()

        date_birth_label = QLabel("Date of birth (MM/DD/YYYY): ")
        self.date_birth_line_edit = QLineEdit()

        calc_age_button = QPushButton("Calculate Age")
        calc_age_button.clicked.connect(self.calculate_age)
        self.disp_age_label = QLabel("")

        # Add labels and edit box to grid
        # Row 0, Column 0
        grid.addWidget(name_label, 0, 0)
        # Row 0, Column 1
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(date_birth_label, 1, 0)
        grid.addWidget(self.date_birth_line_edit, 1, 1)
        # Row 2 Column 0 Expand the button to 1 Row, 2 columns
        grid.addWidget(calc_age_button, 2, 0, 1, 2)
        grid.addWidget(self.disp_age_label, 3, 0, 1, 2)

        # Set up the grid in layout
        self.setLayout(grid)

    def calculate_age(self):
        current_year = datetime.now().year
        date_of_birth = self.date_birth_line_edit.text()
        year_of_birth = datetime.strptime(date_of_birth, "%m/%d/%Y").date().year
        print(year_of_birth)
        age = current_year - 1986
        self.disp_age_label.setText(f"{self.name_line_edit.text()} is {age} years old")


app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())
