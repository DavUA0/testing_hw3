import pytest
from barista import Barista

@pytest.fixture
def setup_object():
    barista = Barista()

    return barista


def test_coffee(setup_object):
    barista = setup_object

    assert barista.make_coffee(withmilk=True) == "Here is your coffee with milk"
    assert barista.make_coffee() == "Here is your regular coffee"


def test_tea(setup_object):
    barista = setup_object

    assert barista.make_tea() == "Your tea is ready"
    assert barista.make_tea(withsugar=True) == "Your sweet tea is ready"


def test_payment(setup_object):
    barista = setup_object

    assert barista.get_payment(cash=False) == "Let me get the POS terminal"
    assert barista.get_payment() == "Thank you for the tip!"
    

def test_menu(setup_object):
    barista = setup_object

    assert barista.present_menu() == "Would you like coffee or tea?"
    assert barista.present_menu(regular=True) == "Would you like the usual?"
