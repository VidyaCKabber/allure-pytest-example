import pytest
import allure


def test_a():
    assert True


def test_b():
    assert False


def test_c():
    assert True


def test_d():
    assert False


def test_e():
    assert True

@pytest.mark.skip
def test_f():
    assert True


def test_with_trivial_severity():
    assert True


def test_with_normal_severity_1():
    assert False


def test_with_trivial_severity_1():
    assert True


def test_with_normal_severity():
    assert False

@pytest.mark.skip
def test_with_trivial_severity():
    assert True