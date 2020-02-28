import pytest
import allure


def test_g():
    assert True


def test_h():
    assert False

@pytest.mark.skip
def test_i():
    assert True


def test_j():
    assert False


def test_k():
    assert True


def test_l():
    assert True


def test_with_trivial_severity_2():
    assert True


def test_with_normal_severity_2():
    assert False


def test_with_trivial_severity_2():
    assert True