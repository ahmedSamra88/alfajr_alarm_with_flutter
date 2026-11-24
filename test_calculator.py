
import calculator


def test_add_numbers():
    assert calculator.add_numbers(2, 3) == 5
    assert calculator.add_numbers(0, 0) == 0
    assert calculator.add_numbers(-5, 5) == 0
    assert calculator.add_numbers(-5, -5) == -10

def test_get_user_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '2')
    assert calculator.get_user_input() == (2.0, 2.0)

    monkeypatch.setattr('builtins.input', lambda _: '-3')
    assert calculator.get_user_input() == (-3.0, -3.0)