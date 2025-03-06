import pytest


@pytest.fixture(scope="session")
def qt():
    from PyQt5.QtWidgets import QApplication

    calc = QApplication([])

    yield calc

    calc.exit()


@pytest.fixture(scope="session")
def view(qt):
    from pycalc.view import PyCalcUi

    yield PyCalcUi()


@pytest.fixture(scope="session")
def model():
    from pycalc.model import evaluateExpression

    yield evaluateExpression


@pytest.fixture(scope="session")
def controller(model, view):
    from pycalc.controller import PyCalcCtrl

    yield PyCalcCtrl(model, view)
