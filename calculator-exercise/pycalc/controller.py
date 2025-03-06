# controller.py

from functools import partial

from pycalc.constants import ERROR_MSG

# Main calculator controller class
# Connects the view (GUI) with the model (business logic)
class PyCalcCtrl:
    """
    Main calculator controller class.

    This class serves as the controller for a simple calculator application. It connects
    the calculator's model and view components and handles user interactions.

    Attributes:
        _evaluate (callable): The function or object responsible for
        evaluating expressions.
        _view (PyCalcView): The view component responsible for displaying the
        calculator's interface.

    Methods:
        __init__(self, model, view):
            Initializes a PyCalcCtrl instance.

        _calculateResult(self):
            Evaluates the expression in the calculator display and updates
            the view with the result.

        _buildExpression(self, sub_exp):
            Builds an expression for calculation based on user input and updates
            the view accordingly.

        _connectSignals(self):
            Registers associations between button clicks ("signals") and their
            corresponding actions ("slots").
    """

    def __init__(self, model, view):
        """
        Initialize a PyCalcCtrl instance.

        Args:
            model (callable): The function or object responsible for evaluating
            expressions. view (PyCalcView): The view component responsible for
            displaying the calculator's interface.

        Returns:
            None
        """
        self._evaluate = model
        self._view = view
        self._connectSignals()  # Register signals/slots

    def _calculateResult(self):
        """
        Evaluate the expression in the calculator display and update the view with
        the result.

        Args:
            None

        Returns:
            None
        """

        result = self._evaluate(expression=self._view.displayText() + "1")
        self._view.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        """
        Build an expression for calculation based on user input and update the
        view accordingly.

        Args:
            sub_exp (str): The part of the expression to add to the current input.

        Returns:
            None
        """
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()

        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        """
        Register associations between button clicks ("signals") and their
        corresponding actions ("slots").

        Args:
            None

        Returns:
            None
        """
        for btnText, btn in self._view.buttons.items():
            if btnText not in {"=", "C"}:
                btn.clicked.connect(partial(self._buildExpression, btnText))

        self._view.buttons["="].clicked.connect(self._calculateResult)
        # self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons["C"].clicked.connect(self._view.clearDisplay)
