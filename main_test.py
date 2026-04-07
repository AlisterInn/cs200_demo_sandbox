from main import func1, func2


def test_func1_collects_numbers_until_zero(monkeypatch):
    entries = iter(["5", "10", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(entries))

    result = func1()

    assert result == [5, 10]


def test_func1_returns_empty_list_when_zero_is_first_value(monkeypatch):
    entries = iter(["0"])
    monkeypatch.setattr("builtins.input", lambda _: next(entries))

    result = func1()

    assert result == []


def test_func2_prints_sum_and_goodbye(monkeypatch, capsys):
    entries = iter(["1", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(entries))

    func2([1, 2, 3])

    output = capsys.readouterr().out
    assert "Here is the data:" in output
    assert "[1, 2, 3]" in output
    assert "The sum is 6" in output
    assert "Goodbye" in output


def test_func2_prints_min_and_max(monkeypatch, capsys):
    entries = iter(["2", "3", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(entries))

    func2([7, 2, 9, 2])

    output = capsys.readouterr().out
    assert "Min value: 2 - at index: 1" in output
    assert "Max value: 9 - at index: 2" in output
    assert "Goodbye" in output
