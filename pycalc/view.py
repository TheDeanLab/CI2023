# view.py

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

# Main view class for calculator GUI
class PyCalcUi(QMainWindow):
    """
    Main calculator GUI.

    This class represents the main graphical user interface (GUI) of a simple calculator application.

    Attributes:
        display (QLineEdit): The calculator's display for showing input and results.
        buttons (dict): A dictionary of calculator buttons with their respective text labels.

    Methods:
        __init__(self):
            Initializes a PyCalcUi instance, setting up the calculator's GUI components.

        _createDisplay(self):
            Creates and configures the calculator's display area.

        _createButtons(self):
            Creates and configures the calculator's buttons.

        setDisplayText(self, text):
            Sets the text/content in the calculator display.

        displayText(self):
            Gets the current text/content from the calculator display.

        clearDisplay(self):
            Clears the calculator display.
    """

    def __init__(self):
        """
        Initialize a PyCalcUi instance, setting up the calculator's GUI components.

        Args:
            None

        Returns:
            None
        """
        super().__init__()
        self.setWindowTitle("PyCalc")
        self.setFixedSize(235, 235)
        
        # Define general layout main widget for the calculator GUI
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        
        # Create the calculator display and buttons
        self._createDisplay()
        self._createButtons()
    
    def _createDisplay(self):
        """
        Create and configure the calculator's display area.

        Args:
            None

        Returns:
            None
        """
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        
        self.generalLayout.addWidget(self.display)
        
    def _createButtons(self):
        """
        Create and configure the calculator's buttons.

        Args:
            None

        Returns:
            None
        """
        self.buttons = {}
        buttonsLayout = QGridLayout()
        # Button text: position on QGridLayout
        buttons = {"7": (0, 0),
                   "8": (0, 1),
                   "9": (0, 2),
                   "/": (0, 3),
                   "C": (0, 4),
                   "4": (1, 0),
                   "5": (1, 1),
                   "6": (1, 2),
                   "*": (1, 3),
                   "(": (1, 4),
                   "1": (2, 0),
                   "2": (2, 1),
                   "3": (2, 2),
                   "-": (2, 3),
                   ")": (2, 4),
                   "0": (3, 0),
                   "00": (3, 1),
                   ".": (3, 2),
                   "+": (3, 3),
                   "=": (3, 4),
                  }
        # Create buttons and add to grid layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        # Add buttonsLayout to general layout
        self.generalLayout.addLayout(buttonsLayout)
        
    def setDisplayText(self, text):
        """
        Set the text/content in the calculator display.

        Args:
            text (str): The text/content to set in the calculator display.

        Returns:
            None
        """
        self.display.setText(text)
        self.display.setFocus()
        
    def displayText(self):
        """
        Get the current text/content from the calculator display.

        Args:
            None

        Returns:
            str: The current text/content from the calculator display.
        """
        return self.display.text()
        
    def clearDisplay(self):
        """
        Clear the calculator display.

        Args:
            None

        Returns:
            None
        """
        self.setDisplayText("")