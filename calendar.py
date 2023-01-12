import sys
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import (QApplication, QCalendarWidget,
                             QGridLayout, QLabel, QWidget)

class Calendar(QWidget):

    def __init__(self):
        super().__init__()

        # Create a calendar widget and set its start and end dates
        self.calendar = QCalendarWidget(self)
        self.calendar.setMinimumDate(QDate(1900, 1, 1))
        self.calendar.setMaximumDate(QDate(3000, 1, 1))

        # Create a label to display the selected date
        self.label = QLabel(self)
        self.label.setText('No date selected')

        # Set up the layout
        layout = QGridLayout(self)
        layout.addWidget(self.calendar, 0, 0)
        layout.addWidget(self.label, 1, 0)

        # Connect the calendar's selectionChanged signal to a slot
        self.calendar.selectionChanged.connect(self.on_date_selected)

    def on_date_selected(self):
        # Get the selected date from the calendar
        date = self.calendar.selectedDate()
        # Format the date and display it in the label
        self.label.setText(date.toString())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calendar = Calendar()
    calendar.show()
    sys.exit(app.exec_())